
import threading
import time
import asyncio
import aiohttp
import random


# Part 1: Multithreading 
def thread_task(name, delay):
    for i in range(3):
        print(f"[Thread {name}] Step {i+1}")
        time.sleep(delay)

def run_multithreading():
    print("=== Multithreading Example ===")
    t1 = threading.Thread(target=thread_task, args=("A", 1))
    t2 = threading.Thread(target=thread_task, args=("B", 2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("All threaded tasks completed!\n")


#Asynchronous Fetch Example


async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"[Async Fetch] Fetched {url} with status {response.status}")
        return await response.text()

async def run_async_fetch():
    print("=== Asynchronous Fetch Example ===")
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/todos/1"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)
    print("All async fetches completed!\n")


# Part 3: Async Download 


async def download_file(file_name):
    print(f"[Download] Starting {file_name}")
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    print(f"[Download] Finished {file_name} in {delay}s")
    return file_name

async def run_download_simulation():
    print("=== Async Download Simulation ===")
    files = [f"file{i}.txt" for i in range(1, 6)]
    tasks = [download_file(f) for f in files]
    results = await asyncio.gather(*tasks)
    print("All files downloaded:", results)


# Main
if __name__ == "__main__":
   
    run_multithreading()

  
    asyncio.run(run_async_fetch())
    asyncio.run(run_download_simulation())