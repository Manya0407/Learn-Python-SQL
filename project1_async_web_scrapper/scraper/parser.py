from bs4 import BeautifulSoup

def parse_page(html_content):
    """ Parse HTML and extract data """
    soup = BeautifulSoup(html_content, "html.parser")
    title = soup.title.string if soup.title else "No Title"
    return {"title": title}
