import asyncio
import random

async def download_file(filename):
    print(f"Starting download: {filename}")
    await asyncio.sleep(random.randint(1, 5))  
    print(f"Finished download: {filename}")

async def main():
    files = [f"file_{i}.txt" for i in range(5)]
    tasks = [download_file(file) for file in files]
    await asyncio.gather(*tasks)

asyncio.run(main())
