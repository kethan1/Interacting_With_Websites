from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

wd = webdriver.Firefox()

wd.get("https://www.google.com/search?q=python")

# wd.find_element_by_css_selector("a").click()  # This doesn't work, same error

# The css selector is needed, because not all a tags are clickable
WebDriverWait(wd, 20).until(
    expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'div[id=search] a[href^="http"]'))
).click()

# WebDriverWait(wd, 20).until(
#     expected_conditions.element_to_be_clickable((By.XPATH, "//div[@id='search']//a[contains(@href,'http')]"))
# ).click()

time.sleep(5)

wd.close()
