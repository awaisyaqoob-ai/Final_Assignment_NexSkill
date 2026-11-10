# Project 1: Scrape quotes from a JavaScript website
# Install: python3.12 -m pip install selenium

import csv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

rows = []
driver = webdriver.Chrome()

try:
    driver.get("https://quotes.toscrape.com/js/")

    # Wait for JavaScript to display the quotes
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "quote"))
    )

    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, "text").text
        author = quote.find_element(By.CLASS_NAME, "author").text
        rows.append([text, author])
        print("Author:", author)
        print("Quote:", text)
        print("------------------------")
finally:
    driver.quit()

# Save results as CSV
with open(Path(__file__).resolve().parent / "selenium_js_quotes.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])
    writer.writerows(rows)

print("Total quotes:", len(rows))
print("Saved:", Path(__file__).resolve().parent / "selenium_js_quotes.csv")
