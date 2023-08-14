# login_module.py

from selenium.webdriver.common.by import By
from time import sleep


def login(browser, user_id, password):
    # open website
    browser.get("https://demo.guru99.com/V4/")
    sleep(1)

    # Website Login Steps:

    # find user ID field:
    user_id_field = browser.find_element(By.NAME, "uid")
    # Enter the values in the id field
    user_id_field.send_keys(user_id)

    # find the password field:
    password_field = browser.find_element(By.NAME, "password")
    # Enter the password:
    password_field.send_keys(password)

    # Find the submit Button:
    submit_button_field = browser.find_element(By.NAME, "btnLogin")
    # Click the submit Button:
    submit_button_field.click()
