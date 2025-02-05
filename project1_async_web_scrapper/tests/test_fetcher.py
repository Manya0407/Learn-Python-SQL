import pytest
import asyncio
from scraper.fetcher import fetch_page

@pytest.mark.asyncio
async def test_fetch_page():
    url = "https://example.com"
    response = await fetch_page(url)
    assert "<title>" in response
