import time
import requests
from bs4 import BeautifulSoup
import asyncio
import httpx


def sync_get_first_paragraph(page):
    url = f"https://en.wikipedia.org/wiki/{page}"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        first_paragraph = soup.find("p")
        if first_paragraph:
            return first_paragraph.get_text()
        else:
            return f"No content found for '{page}'"
    else:
        return f"Failed to retrieve data for '{page}': {response.status_code}"


async def async_get_first_paragraph(page):
    async with httpx.AsyncClient(verify=False) as client:
        url = f"https://en.wikipedia.org/wiki/{page}"
        response = await client.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            first_paragraph = soup.find("p")
            if first_paragraph:
                return first_paragraph.get_text()
            else:
                return f"No content found for '{page}'"
        else:
            return f"Failed to retrieve data for '{page}': {response.status_code}"


async def main():
    pages_to_fetch = [
        "Python_(programming_language)",
        "Machine_learning",
        "Artificial_intelligence",
        "Object_Exchange_Model",
    ]

    # Measure time for synchronous version
    sync_start_time = time.time()
    sync_results = [sync_get_first_paragraph(page) for page in pages_to_fetch]
    sync_end_time = time.time()
    sync_elapsed_time = sync_end_time - sync_start_time

    # # Optionally print out paragraph content
    # print("Results from synchronous version:")
    # for page, result in zip(pages_to_fetch, sync_results):
    #     print(f"First paragraph of '{page}':\n{result}\n")

    print(f"Sync total time: {sync_elapsed_time:.2f} seconds\n")

    # Measure time for asynchronous version
    async_start_time = time.time()
    async_results = await asyncio.gather(
        *[async_get_first_paragraph(page) for page in pages_to_fetch]
    )
    async_end_time = time.time()
    async_elapsed_time = async_end_time - async_start_time

    # # Optionally print out paragraph content
    # print("Results from asynchronous version:")
    # for page, result in zip(pages_to_fetch, async_results):
    # print(f"First paragraph of '{page}':\n{result}\n")

    print(f"Async total time: {async_elapsed_time:.2f} seconds")


# Run the main coroutine
asyncio.run(main())
