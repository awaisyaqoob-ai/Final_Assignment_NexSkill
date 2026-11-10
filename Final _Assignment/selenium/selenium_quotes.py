# Project 2: Click Next and scrape two pages of quotes
import csv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

rows = []
driver = webdriver.Chrome()

try:
    driver.get("https://quotes.toscrape.com/")
    for page_number in range(1, 3):
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "quote"))
        )

        quotes = driver.find_elements(By.CLASS_NAME, "quote")
        print("Page:", page_number)
        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text
            rows.append([text, author])
            print(author, ":", text)

        next_buttons = driver.find_elements(By.CSS_SELECTOR, ".next a")
        if not next_buttons:
            break
        if page_number < 2:
            next_buttons[0].click()
finally:
    driver.quit()

with open(Path(__file__).resolve().parent / "selenium_quotes_pages.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])
    writer.writerows(rows)

print("Total quotes:", len(rows))
print("Saved:", Path(__file__).resolve().parent / "selenium_quotes_pages.csv")
