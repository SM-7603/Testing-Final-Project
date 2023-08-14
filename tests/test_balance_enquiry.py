# test_new_customer.py

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import the login module - to make sure, we login to the website
from login_module import login

class TestBalanceEnquiry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()
        login(cls.browser, "mngr520521", "ajAtYhE")


    def navigate_bank_enquiry(self):
        self.browser.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        sleep(3)
      

    # ... rest of your test methods ...
    def test_be1_account_num_empty(self):
        self.navigate_bank_enquiry()

        # # entering proper values:

        # # find customer name field:
        balance_enquiry = self.browser.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/input[1]")
        # # enter values:
        balance_enquiry.send_keys(Keys.TAB)
        # # wait
        sleep(2)

        # Find acc num error field
        account_num_error_field = self.browser.find_element(By.ID, "message2")

        # assert the error message
        assert(account_num_error_field.text == "Account Number must not be blank")

        #wait
        sleep(2)

    def test_be2_account_num_must_numeric(self):
        self.navigate_bank_enquiry()

        
        balance_enquiry = self.browser.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/input[1]")
        
        balance_enquiry.send_keys("dfe")
        # # wait


        account_num_must_numeric = self.browser.find_element(By.ID,"message2")

        assert(account_num_must_numeric.text == "Characters are not allowed")

        sleep(1)

    def test_be3_account_num_not_special_character(self):
        self.navigate_bank_enquiry()

        balance_enquiry = self.browser.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/input[1]")
        
        balance_enquiry.send_keys("@")
        # # wait


        account_num_must_numeric = self.browser.find_element(By.ID,"message2")

        assert(account_num_must_numeric.text == "Special characters are not allowed")

        sleep(1)


    def test_be4_account_num_first_character_not_space(self):
        self.navigate_bank_enquiry()

        balance_enquiry = self.browser.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/input[1]")
        
        balance_enquiry.send_keys(" ")
        # # wait

        account_num_must_numeric = self.browser.find_element(By.ID,"message2")

        assert(account_num_must_numeric.text == "Characters are not allowed")

        sleep(1)


    def test_be5_valid_account_num(self):
        self.navigate_bank_enquiry()

        balance_enquiry = self.browser.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/input[1]")
        
        balance_enquiry.send_keys("125440")
        # # wait

        submit_button = self.browser.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]")
        submit_button.click()

        sleep(2)

    def test_be6_invalid_account_num(self):
        # self.navigate_bank_enquiry()
        self.browser.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        sleep(3)

        balance_enquiry = self.browser.find_element(By.NAME,'accountno')
        
        balance_enquiry.send_keys("232323")
        # # wait

        submit_button = self.browser.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]")
        submit_button.click()

        sleep(2)


    def test_be7_reset_button(self):
        self.browser.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        sleep(3)

        balance_enquiry = self.browser.find_element(By.NAME,'accountno')
        
        balance_enquiry.send_keys("232323")
        # # wait

        balance_enquiry = self.browser.find_element(By.NAME,'res').click()

        sleep(2)




    # @classmethod
    # def tearDownClass(cls):
    #     cls.browser.quit()

# ... other test modules ...

if __name__ == '__main__':
    unittest.main()
