import requests
import dotenv
from bs4 import BeautifulSoup

def main():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    #saving raw data to a file
    with open('raw_data.html', 'w', encoding='utf-8') as file:
        file.write(response.text)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
        print(f"Title of the page: {title}")

if __name__ == "__main__":
    main()
