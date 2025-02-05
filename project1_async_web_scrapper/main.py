import asyncio
from scraper.fetcher import fetch_page
from scraper.parser import parse_page
from scraper.saver import save_data

URLS = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

async def main():
    tasks = [fetch_page(url) for url in URLS]
    results = await asyncio.gather(*tasks)

    parsed_data = [parse_page(content) for content in results]
    save_data(parsed_data)

if __name__ == "__main__":
    asyncio.run(main())
