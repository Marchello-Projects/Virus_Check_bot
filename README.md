![prew](./imgs/prew.png)

Telegram bot that will check files for viruses and display the check result!

# API:
In this project, i used the following API:

![Virustotal](./imgs/virustotal-logo-freelogovectors.net_-400x69-2864668405.png)

VirusTotal provides an API for scanning files, URLs, IP addresses, and domains for malicious content. This bot uses the free version:

    🔑 Requires API key (get it by registering)

    📦 Up to 500 requests per day

    ⏱ Max 4 requests per minute

    📁 Max file size: 650 MB

    🚫 For personal, non-commercial use only

Code from the repository:
```python
sync def check_file(filepath):
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
```