from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

wd = webdriver.Firefox()
wd.get("https://www.google.com")

search_bar = wd.find_element_by_name("q")

to_search = input("What do you want to search: ")

search_bar.send_keys(to_search)

search_bar.send_keys(Keys.RETURN)

WebDriverWait(wd, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'div#search a'))
)

for link in wd.find_elements_by_css_selector('div#search a'):
    print(link.text)
