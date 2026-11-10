import csv
import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/", timeout=20)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
rows = []

for book in soup.select("article.product_pod"):
    title = book.select_one("h3 a")["title"]
    raw_price = book.select_one(".price_color").get_text(strip=True)
    price = float(raw_price.replace("£", "").replace("Â", ""))
    rating = book.select_one("p.star-rating").get("class", [])[-1]
    rows.append([title, price, rating])
    print(title, "|", price, "|", rating)

if rows:
    average = sum(row[1] for row in rows) / len(rows)
    print("Average price: £", round(average, 2))

with open("books_ratings.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price_GBP", "Rating"])
    writer.writerows(rows)
print("Saved", len(rows), "books to books_ratings.csv")
