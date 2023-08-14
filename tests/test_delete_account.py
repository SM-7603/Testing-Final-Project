import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from login_module import login

class TestDeleteAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()
        login(cls.browser, "mngr520521", "ajAtYhE")
        
    def navigate_delete_account(self):
        new_account_field = self.browser.find_element(By.LINK_TEXT, "Delete Account")
        new_account_field.click()
        sleep(3)

    def test_da01_verify_account_number(self):
        self.navigate_delete_account()
        self.browser.find_element(By.NAME, 'accountno').send_keys(Keys.TAB)
        sleep(0.5)
        error_da1 = "Account Number must not be blank"
        self.assertEqual(error_da1, self.browser.find_element(By.ID, "message2").text)

    def test_da2_account_numeric(self):
        self.navigate_delete_account()
        self.browser.find_element(By.NAME, 'accountno').send_keys("1234abc")
        error_da2 = "Characters are not allowed"
        self.assertEqual(error_da2, self.browser.find_element(By.ID, "message2").text)
        sleep(0.5)
    
    def test_da3_account_special_character(self):
        self.navigate_delete_account()
        self.browser.find_element(By.NAME, 'accountno').send_keys("123!@#")
        error_da3 = "Special characters are not allowed"
        self.assertEqual(error_da3, self.browser.find_element(By.ID, "message2").text)
        sleep(0.5)

    def test_da4_account_blank_space(self):
        self.navigate_delete_account()
        self.browser.find_element(By.NAME, 'accountno').send_keys("123 12")
        error_da4 = "Characters are not allowed"
        self.assertEqual(error_da4, self.browser.find_element(By.ID, "message2").text)
        sleep(0.5)

    def test_da5_account_first_character_space(self):
        self.navigate_delete_account()
        self.browser.find_element(By.NAME, 'accountno').send_keys(" 123")
        error_da5 = "First character cannot have space"
        self.assertEqual(error_da5, self.browser.find_element(By.ID, "message2").text)
        sleep(0.5)

    def test_da6_valid_account_delete(self):
        self.navigate_delete_account()
        self.browser.find_element(By.NAME, 'accountno').send_keys("125578")
        self.browser.find_element(By.NAME, 'AccSubmit').click()
        alert = self.browser.switch_to.alert
        alert.accept()  # Click OK in the confirmation dialog
        excepted_url = "https://demo.guru99.com/V4/manager/DeleteAccount.php"
        self.assertEqual(excepted_url,self.browser.current_url)


    def test_da7_invalid_account_delete(self):
        self.navigate_delete_account()
        account_number = "12345"  # Use an invalid account number
        self.browser.find_element(By.NAME, 'accountno').send_keys(account_number)
        self.browser.find_element(By.NAME, 'AccSubmit').click()

        try:
            alert = self.browser.switch_to.alert
            alert.accept()
            sleep(1)

            alert_01 = self.browser.switch_to.alert
            alert_01.accept()
            sleep(1)


            expected_error_message = "Account does not exist"
            actual_error_message = self.browser.find_element(By.ID, "message2").text
            self.assertEqual(expected_error_message, actual_error_message)
            sleep(2)

            expected_url = "https://demo.guru99.com/V4/manager/DeleteAccount.php"
            self.assertEqual(expected_url, self.browser.current_url)
        except:
            pass


    def test_da8_reset_button(self):
        self.navigate_delete_account()
        account_number = "12345"
        self.browser.find_element(By.NAME, 'accountno').send_keys(account_number)
        self.browser.find_element(By.NAME, 'res').click()



 	# 2146
    # 125579
    


if __name__ == '__main__':
    unittest.main()
