import csv
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url, timeout=20)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
books = []

for card in soup.select("article.product_pod"):
    title = card.select_one("h3 a")["title"]
    price = card.select_one(".price_color").get_text(strip=True)
    availability = card.select_one(".availability").get_text(strip=True)
    books.append([title, price, availability])
    print(title, "|", price, "|", availability)

with open("books_catalog.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Availability"])
    writer.writerows(books)
print("Saved", len(books), "books to books_catalog.csv")
