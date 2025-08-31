import requests
from bs4 import BeautifulSoup

def fetch_links(url):
    """Fetches and prints all hyperlinks from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)

        soup = BeautifulSoup(response.text, 'html.parser')

        print(f"Links found on {url}:")
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                print(href)

    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

def main():
    url = ""  # You can change this to any public website
    fetch_links(url)

if __name__ == "__main__":
    main()
