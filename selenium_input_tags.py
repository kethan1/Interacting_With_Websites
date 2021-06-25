from selenium import webdriver
import os
import time

wd = webdriver.Firefox()
wd.get(f"file:///{os.path.join(os.path.dirname(os.path.abspath(__file__)), 'selenium_input_tags.html')}")

time.sleep(3)
wd.find_element_by_id("text_input").send_keys("Selenium")
wd.find_element_by_id("password_input").send_keys("Selenium")
time.sleep(3)
wd.find_element_by_id("reset_input").click()
time.sleep(3)
wd.find_element_by_id("text_input").send_keys("Selenium")
wd.find_element_by_id("password_input").send_keys("Selenium")
time.sleep(3)
wd.find_element_by_id("submit_input").click()
time.sleep(3)
wd.find_element_by_id("radio1_input").click()
wd.find_element_by_id("checkbox2_input").click()
time.sleep(3)
wd.find_element_by_id("button_input").click()
time.sleep(1)
wd.execute_script("document.querySelector('#color_input').value='#FFFFFF';")
wd.execute_script("document.querySelector('#date_input').value='2020-06-25';")
