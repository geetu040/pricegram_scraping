from selenium import webdriver

# Create an instance of Chrome webdriver
browser = webdriver.Chrome()

# Navigate to the webpage to scrape
browser.get('https://www.example.com')

# Extract the data you need using Selenium methods
# For example, you can extract the page title like this:
title = browser.title
print(title)

# When you're done, close the browser window
browser.quit()
