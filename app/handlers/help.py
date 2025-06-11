from aiogram import F, Router
from aiogram.types import Message

router = Router()

@router.message(F.text == '❔ help')
async def cmd_help(message: Message):
    await message.answer(
        'The Virus Check bot checks files for viruses using the Virustotal API 🛡️ \n\n'
        'To check a file for viruses, you need to: \n'
        '1) Run the bot with the /start command\n'
        '2) Click on the button "🦠 scan"\n'
        '2) Send the file to the chat\n'
        '3) The bot checks the file and sends the result back using the Virustotal API\n\n'
        'Options:\n'
        '2) ❔ help - Send instructions on how to use the bot\n'
        '3) 🦠 scan - Send the file after this command to check for viruses\n'
    )