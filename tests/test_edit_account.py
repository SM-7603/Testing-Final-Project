# test_edit_account.py

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# import the login module - to make sure, we login to the website
from login_module import login

# 125578
class TestEditAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()
        login(cls.browser, "mngr520521", "ajAtYhE")

    def setUp(self):
        # Find new account field from nav bar:
        edit_account_field = self.browser.find_element(
            By.PARTIAL_LINK_TEXT, "Edit Account")
        # Click new account
        edit_account_field.click()
        # Wait
        sleep(0.25)

    

    def test_ea01_empty_number(self):
        # # do stuff
        # # I want to have this in setup:
        # # find new account field from nav bar:
        # edit_account_field = self.browser.find_element(
        #     By.PARTIAL_LINK_TEXT, "New account")
        # # click new account
        # edit_account_field.click()
        # # wait
        # sleep(0.25)

        # entering proper values:

        # find account name field:
        account_number_field = self.browser.find_element(By.NAME, "accountno")
        # enter values:
        account_number_field.send_keys(Keys.TAB)
        # wait
        sleep(0.25)

        # find account error message:
        account_number_error_field = self.browser.find_element(By.ID, "message2")

        # assert the error message:
        assert (account_number_error_field.text ==
                "Account Number must not be blank")

        # wait
        sleep(0.25)

    def test_ea02_num_number(self):
        # entering proper values:

        # find account name field:
        account_number_field = self.browser.find_element(By.NAME, "accountno")
        # enter values:
        account_number_field.send_keys("123abc")
        # wait
        sleep(0.25)

        # find account error message:
        account_number_error_field = self.browser.find_element(By.ID, "message2")

        # assert the error message:
        assert (account_number_error_field.text ==
                "Characters are not allowed")
        # wait
        sleep(0.25)

    def test_ea03_special_char_number(self):
        # entering proper values:

        # find account name field:
        account_number_field = self.browser.find_element(By.NAME, "accountno")
        # enter values:
        account_number_field.send_keys("***")
        # wait
        sleep(0.25)

        # find account error message:
        account_number_error_field = self.browser.find_element(By.ID, "message2")

        # assert the error message:
        assert (account_number_error_field.text ==
                "Special characters are not allowed")
        # wait
        sleep(0.25)

    def test_ea04_char_blank(self):
        # entering proper values:

        # find account name field:
        account_number_field = self.browser.find_element(By.NAME, "accountno")
        # enter values:
        account_number_field.send_keys("123 456")
        # press tab
        account_number_field.send_keys(Keys.TAB)
        # wait
        sleep(0.25)

        # find account error message:
        account_number_error_field = self.browser.find_element(By.ID, "message2")

        # assert the error message:
        assert (account_number_error_field.text ==
                "Characters are not allowed")
        # wait
        sleep(0.25)

# this should fail
    def test_ea05_first_char_blank(self):
        # entering proper values:

        # find account name field:
        account_number_field = self.browser.find_element(By.NAME, "accountno")
        # enter values:
        account_number_field.send_keys(" ")
        # press tab
        account_number_field.send_keys(Keys.TAB)
        # wait
        sleep(0.25)

        # find account error message:
        account_number_error_field = self.browser.find_element(By.ID, "message2")

        # assert the error message:
        assert (account_number_error_field.text ==
                "First character can not have space")
        # wait
        sleep(0.25)

    def test_ea06_correct_account_number(self):
        # entering proper values:

        # find account name field:
        account_number_field = self.browser.find_element(By.NAME, "accountno")
        # enter values:
        account_number_field.send_keys("125578")
        # wait
        sleep(0.25)
        
        # find submit button field:
        submit_btn_field = self.browser.find_element(By.NAME, "AccSubmit")
        # click submit button
        submit_btn_field.click()
        # wait
        sleep(0.25)

        alert_message = self.browser.switch_to.alert
        alert_message.accept()  # Click OK in the confirmation dialog

        # expected url after deletion
        expected_url = "https://demo.guru99.com/V4/manager/editAccountPage.php"

        self.assertEqual(expected_url, self.browser.current_url)

        # wait
        sleep(0.25)


    def test_ea07_incorrect_account_number(self):

        account_number_field = self.browser.find_element(By.NAME, "accountno")
        account_number_field.send_keys("123456")

        submit_btn_field = self.browser.find_element(By.NAME, "AccSubmit")
        submit_btn_field.click()

        # Expected URL after the action
        expected_url = "https://demo.guru99.com/V4/manager/editAccountPage.php"
        self.assertEqual(expected_url, self.browser.current_url)


    def test_ea08_reset_button(self):
        # entering proper values:

        # find account name field:
        account_number_field = self.browser.find_element(By.NAME, "accountno")
        # enter values:
        account_number_field.send_keys("12345")
        # wait
        sleep(0.25)
 
        
        # find reset button field:
        reset_btn_field = self.browser.find_element(By.NAME, "res")
        # click reset button
        reset_btn_field.click()


    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

# ... other test modules ...


if __name__ == '__main__':
    unittest.main()
