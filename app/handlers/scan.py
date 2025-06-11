import os
from io import BytesIO
import asyncio

import aiofiles
import vt
from aiogram import F, Router
from aiogram.types import Message
from dotenv import load_dotenv

router = Router()

load_dotenv()

async def check_file(filepath):
    async with vt.Client(os.getenv("VIRUS_TOTAL_API")) as client:
        async with aiofiles.open(filepath, 'rb') as f:
            content = await f.read()
            file_like = BytesIO(content)
            analysis = await client.scan_file_async(file_like, wait_for_completion=True)

        for _ in range(10):
            analysis_result = await client.get_object_async(f"/analyses/{analysis.id}")
            status = getattr(analysis_result, "status", None)
            if status == "completed":
                return analysis_result
            await asyncio.sleep(3)
        return analysis_result

@router.message(F.text == '🦠 scan')
async def cmd_profile(message: Message):
    await message.answer('📄 Drop the file directly into the chat')

@router.message(F.document)
async def handle_document(message: Message):
    document = message.document
    file_name = document.file_name
    file_path = f"downloads/{file_name}"

    os.makedirs("downloads", exist_ok=True)

    file = await message.bot.get_file(document.file_id)
    await message.bot.download_file(file.file_path, destination=file_path)

    await message.answer("📥 File received. Sending to VirusTotal...")

    try:
        analysis_result = await check_file(file_path)

        stats = getattr(analysis_result, "stats", None)
        if not stats:
            stats = getattr(getattr(analysis_result, "attributes", None), "stats", {})

        if stats:
            verdict = (
                f"Malicious: {stats.get('malicious', 0)}\n"
                f"Undetected: {stats.get('undetected', 0)}\n"
                f"Suspicious: {stats.get('suspicious', 0)}\n"
                f"Timeout: {stats.get('timeout', 0)}\n"
                f"Harmless: {stats.get('harmless', 0)}"
            )
        else:
            verdict = "No stats available."

        await message.answer(f"✅ Analysis completed!\n\nResults:\n{verdict}")
    except Exception as e:
        await message.answer(f"❌ Error: {e}")
