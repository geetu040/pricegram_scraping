from selenium import webdriver
from selenium.webdriver.common.by import By
import json

def fetch(driver, category_name, category_url, output_dir):

    # Navigations
    driver.get(category_url)
    driver.find_element(By.CSS_SELECTOR, "#ddlResults").click()
    driver.find_element(By.CSS_SELECTOR, "#ddlResults > option:nth-child(6)").click()
    products = driver.find_elements(By.CSS_SELECTOR, "div > h4 > a")

    links = []
    for product in products:
        link = product.get_attribute("href")
        if link[-5:] == ".aspx":
            links.append(link)

    # Saving the Data
    with open(f"{output_dir}/{category_name}.json", 'w') as f:
        json.dump(links, f)
        pass

    print(f"Collected {len(links)} products in Category: {category_name} (saved in {OUTPUT_DIR})")

CATEGORIES = {
    "laptops": "https://www.czone.com.pk/laptops-pakistan-ppt.74.aspx",
    "laptops_used": "https://www.czone.com.pk/laptops-used-pakistan-ppt.715.aspx",
    "smart_watches": "https://www.czone.com.pk/smart-watches-pakistan-ppt.403.aspx",
    "headsets": "https://www.czone.com.pk/headsets-headphones-mic-pakistan-ppt.175.aspx",
}
OUTPUT_DIR = "links"

# Create an instance of Chrome webdriver
driver = webdriver.Chrome()
driver.maximize_window()

for category_name, category_url in CATEGORIES.items():
    fetch(driver, category_name, category_url, OUTPUT_DIR)

driver.quit()