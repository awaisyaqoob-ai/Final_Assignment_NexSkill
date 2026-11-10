# Project 4: Scrape countries starting with the letter A
import csv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

rows = []
driver = webdriver.Chrome()

try:
    driver.get("https://www.scrapethissite.com/pages/simple/")
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "country"))
    )

    countries = driver.find_elements(By.CLASS_NAME, "country")
    for country in countries:
        name = country.find_element(By.CLASS_NAME, "country-name").text.strip()
        capital = country.find_element(By.CLASS_NAME, "country-capital").text.strip()
        population = country.find_element(By.CLASS_NAME, "country-population").text.strip()

        if name.startswith("A"):
            rows.append([name, capital, population])
            print(name, "-", capital, "-", population)
finally:
    driver.quit()

with open(Path(__file__).resolve().parent / "selenium_countries_a.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Country", "Capital", "Population"])
    writer.writerows(rows)

print("Countries starting with A:", len(rows))
print("Saved:", Path(__file__).resolve().parent / "selenium_countries_a.csv")
