import csv
import requests
from bs4 import BeautifulSoup

all_quotes = []
for page in range(1, 3):
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    for quote in soup.select("div.quote"):
        text = quote.select_one(".text").get_text(strip=True)
        author = quote.select_one(".author").get_text(strip=True)
        tags = ", ".join(tag.get_text(strip=True) for tag in quote.select(".tag"))
        all_quotes.append([text, author, tags])
        print(author, ":", text)

with open("quotes_authors.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])
    writer.writerows(all_quotes)
print("Saved", len(all_quotes), "quotes to quotes_authors.csv")
