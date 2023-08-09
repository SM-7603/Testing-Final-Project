import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

"""
Meta Data:
    - website link: https://demo.guru99.com/V4/
    - Manager Info:
        - user_id: mngr520521
        - password: ajAtYhE
"""

# create the "TestWebsite" class


class TestWebsite(unittest.TestCase):

    # define setup class
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()


    # define teardown class
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

# boilerplate for main entry point 
if __name__ == '__main__':
    unittest.main()
