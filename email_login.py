import time
import random
import getpass
import json
from typing import List

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import bs4


class EnterEmail(Exception):
    pass


email = input("Enter your email: ")
if not email:
    try:
        with open("email.json") as email_file:
            email = json.load(email_file)["email"]
    except FileNotFoundError:
        raise EnterEmail(
            "Please enter a valid email, or create an emails.json \
            file with the key 'email' as your email!"
        )
password = getpass.getpass("Enter your password: ")

profile = webdriver.FirefoxProfile()

PROXY_HOST = "12.12.12.123"
PROXY_PORT = 1234

profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", PROXY_HOST)
profile.set_preference("network.proxy.http_port", PROXY_PORT)
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.set_preference("javascript.enabled", True)
profile.update_preferences()

desired = webdriver.DesiredCapabilities.FIREFOX

wd = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired)
wd.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

wd.get("https://accounts.google.com")

email_input = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#identifierId')))

for letter in email:
    email_input.send_keys(letter)
    time.sleep(random.randint(5, 10) / 100)

email_input.send_keys(Keys.RETURN)

time.sleep(1)

WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="password"][name="password"]')))
password_input = wd.find_element_by_css_selector('input[name="password"][type="password"]')

for letter in password:
    password_input.send_keys(letter)
    time.sleep(random.randint(5, 10) / 100)

password_input.send_keys(Keys.RETURN)

time.sleep(2)

wd.get("https://gmail.com")
WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div + div.Cp > div > table[aria-readonly=true][cellpadding="0"][role="grid"] > tbody')))
unread_emails = wd.find_element_by_css_selector('div + div.Cp > div > table[aria-readonly=true][cellpadding="0"][role="grid"] > tbody').get_attribute('innerHTML')

parsed_unread_emails = bs4.BeautifulSoup(unread_emails, features="html.parser")
email_text_list: List[str] = [element.get_text().replace("Click to teach Personal Website Mail this conversation is important.unread, ", "").replace("\u200c \u200c ", " ").replace("\u200c \u200c", " ").replace("\xa0", " ").replace("\u200b", "").replace("\u200c", "") for element in parsed_unread_emails]

if not email_text_list:
    print("You have no unread emails!")
else:
    print("You have unread emails!")
    print()
    unread_email: str
    for unread_email in email_text_list:
        print(f"Email From: {unread_email.split(', ')[0]}")
        print(f"Email Title: {unread_email.split(', ')[1]}")
        print(f"Email Send On: {unread_email.split(', ')[2]}")
        print(f"Email Content: {', '.join(unread_email.split(', ')[3:]).split(unread_email.split(', ')[0])[0].rstrip('.')}")
        print()
