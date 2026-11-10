import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url, timeout=20)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
countries = []

for card in soup.select("div.country"):
    name = card.select_one(".country-name").get_text(strip=True)
    capital = card.select_one(".country-capital").get_text(strip=True)
    population = card.select_one(".country-population").get_text(strip=True)
    area = card.select_one(".country-area").get_text(strip=True)
    countries.append([name, capital, population, area])
    print(name, "-", capital)

with open("countries.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Country", "Capital", "Population", "Area_km2"])
    writer.writerows(countries)
print("Saved", len(countries), "countries to countries.csv")
