import requests
from bs4 import BeautifulSoup

# Base class
class BookScraper:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        raise NotImplementedError("Subclasses must implement fetch()")


# Subclass for HTML scraping (your current logic)
class HTMLBookScraper(BookScraper):
    def fetch(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception("Failed to retrieve content.")

        soup = BeautifulSoup(response.text, 'html.parser')

        # Customize for the book site structure:
        title = soup.title.string.strip() if soup.title else "Untitled"
        content = soup.get_text(separator="\n").strip()

        return title, content


