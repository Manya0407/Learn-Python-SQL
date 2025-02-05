import aiohttp
import asyncio

async def fetch_page(url):
    """ Fetch page content asynchronously """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
