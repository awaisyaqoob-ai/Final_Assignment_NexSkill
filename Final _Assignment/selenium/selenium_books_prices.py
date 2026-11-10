# Project 3: Find books priced below 30 pounds
import csv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

rows = []
driver = webdriver.Chrome()

try:
    driver.get("https://books.toscrape.com/")
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product_pod"))
    )

    books = driver.find_elements(By.CLASS_NAME, "product_pod")
    for book in books:
        title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        price_text = book.find_element(By.CLASS_NAME, "price_color").text
        price = float(price_text.replace("£", "").replace("Â", ""))

        if price < 30:
            rows.append([title, price])
            print(title, "-", price, "GBP")
finally:
    driver.quit()

with open(Path(__file__).resolve().parent / "selenium_books_under_30.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Book", "Price_GBP"])
    writer.writerows(rows)

print("Books under 30 GBP:", len(rows))
print("Saved:", Path(__file__).resolve().parent / "selenium_books_under_30.csv")
