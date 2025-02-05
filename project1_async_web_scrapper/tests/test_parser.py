import pytest
from scraper.parser import parse_page

def test_parse_page():
    html = "<html><head><title>Test Page</title></head><body></body></html>"
    data = parse_page(html)
    assert data["title"] == "Test Page"
