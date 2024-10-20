from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
# Optional: specify the path to geckodriver if it's not in your PATH
geckodriver_path = '/path/to/geckodriver'

# Setup Firefox options (optional)
options = Options()
  # Optional: run in headless mode if you don't want to open a window

# Setup service object for geckodriver
service = Service()

# Initialize WebDriver for Firefox
driver = webdriver.Firefox(service=service, options=options)

# Open a webpage
driver.get("https://www.google.com")

# Print the page title
time.sleep(500000)

# Close the browser
driver.quit()