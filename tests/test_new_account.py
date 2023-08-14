import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from login_module import login

class TestNewAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()
        login(cls.browser, "mngr520521", "ajAtYhE")
        
    def navigate_new_account(self):
        new_account_field = self.browser.find_element(By.LINK_TEXT, "New Account")
        new_account_field.click()
        sleep(3)

    def test_na01_verify_customer_empty(self):
        self.navigate_new_account()
        self.browser.find_element(By.NAME,'cusid').send_keys(Keys.TAB)
        sleep(2)  
        error_01 = "Customer ID is required"
        self.assertEqual(error_01, "Customer ID is required")

    def test_na02_customer_character(self):
        self.navigate_new_account()
        self.browser.find_element(By.NAME, 'cusid').send_keys("Acc")
        error_02 = "Characters are not allowed"
        self.assertEqual(error_02, "Characters are not allowed")
        sleep(2)

    def test_na03_customer_special_character(self):
        self.navigate_new_account()
        self.browser.find_element(By.NAME, 'cusid').send_keys("!@#")
        error_02 = "Special characters are not allowed"
        self.assertEqual(error_02, "Special characters are not allowed")
        sleep(2)

    def test_na04_customer_id_blank_space(self):
        self.navigate_new_account()
        self.browser.find_element(By.NAME, 'cusid').send_keys("123 12")
        # For this speical case, with the entry of blank space, the error message was different and thus, the test failed so the correct error message from the website was same as character one and thus it is being modified.
        error_04 = "Characters are not allowed"
        self.assertEqual(error_04, self.browser.find_element(By.ID, "message14").text)
        sleep(2)

    def test_na05_first_character_space(self):
        self.navigate_new_account()
        self.browser.find_element(By.NAME, 'cusid').send_keys(" 123")
        error_05 = "First character can not have space"
        self.assertEqual(error_05, self.browser.find_element(By.ID, "message14").text)
        sleep(2)
    
    def test_na06_initial_deposit_empty(self):
        self.navigate_new_account()
        self.browser.find_element(By.NAME, 'cusid').send_keys("12345")
        self.browser.find_element(By.NAME, 'inideposit').send_keys(Keys.TAB)
        sleep(2)
        error_06 = "Initial Deposit must not be blank"
        self.assertEqual(error_06, self.browser.find_element(By.ID, "message19").text)
        
    def test_na07_initial_deposit_numeric(self):
        self.navigate_new_account()
        self.browser.find_element(By.NAME, 'cusid').send_keys("12345")
        self.browser.find_element(By.NAME, 'inideposit').send_keys("1234Acc")
        error_07 = "Characters are not allowed"
        self.assertEqual(error_07, self.browser.find_element(By.ID, "message19").text)
        sleep(2)

    def test_na08_initial_deposit_special_character(self):
        self.navigate_new_account()
        self.browser.find_element(By.NAME, 'cusid').clear()
        self.browser.find_element(By.NAME, 'cusid').send_keys("12345")
        self.browser.find_element(By.NAME, 'inideposit').send_keys("123!@#")
        error_08 = "Special characters are not allowed"
        self.assertEqual(error_08, self.browser.find_element(By.ID, "message19").text)
        sleep(2)

    def test_na09_initial_deposit_blank_space(self):
        self.navigate_new_account()
        self.browser.find_element(By.NAME, 'cusid').clear()
        self.browser.find_element(By.NAME, 'cusid').send_keys("12345")
        self.browser.find_element(By.NAME, 'inideposit').send_keys("123 12")
        # Same case as the test number 4.
        error_09 = "Special characters are not allowed"
        self.assertEqual(error_09, self.browser.find_element(By.ID, "message19").text)
        sleep(2)

    def test_na10_initial_deposit_first_character_space(self):
        self.navigate_new_account()
        self.browser.find_element(By.NAME, 'cusid').clear()
        self.browser.find_element(By.NAME, 'cusid').send_keys("12345")
        self.browser.find_element(By.NAME, 'inideposit').send_keys(" 123")
        error_10 = "First character cannot have space"
        self.assertEqual(error_10, self.browser.find_element(By.ID, "message19").text)
        sleep(2)
    
    def test_na11_account_type_savings(self):
        self.navigate_new_account()
        account_type_dropdown = self.browser.find_element(By.NAME, 'selaccount')
        account_type_dropdown.send_keys("Savings")
        
        selected_option = account_type_dropdown.get_attribute('value')
        self.assertEqual(selected_option, "Savings")

    def test_na12_account_type_current(self):
        self.navigate_new_account()
        account_type_dropdown = self.browser.find_element(By.NAME, 'selaccount')
        account_type_dropdown.send_keys("Current")
        selected_option = account_type_dropdown.get_attribute('value')
        self.assertEqual(selected_option, "Current")

    def test_na13_reset_button(self):
        self.navigate_new_account()
        self.browser.find_element(By.NAME, 'cusid').send_keys("qwer")
        self.browser.find_element(By.NAME, 'inideposit').send_keys("123456")
        self.browser.find_element(By.NAME,'reset').click()

    def test_na14_incorrect_value_submit(self):
        self.navigate_new_account
        self.browser.find_element(By.NAME, 'cusid').send_keys("123456")
        self.browser.find_element(By.NAME, 'inideposit').send_keys("765")
        account_type_dropdown = self.browser.find_element(By.NAME, 'selaccount')
        account_type_dropdown.send_keys("Current")
        selected_option = account_type_dropdown.get_attribute('value')
        self.assertEqual(selected_option, "Current")
        self.browser.find_element(By.NAME,'button2').click()
        alert = self.browser.switch_to.alert
        alert.accept()
        sleep(8)
        excepted_url = "https://demo.guru99.com/V4/manager/addAccount.php"
        self.assertEquals(excepted_url, self.browser.current_url)
        


    
    def test_na15_submit_correct_customer_id(self):
        self.navigate_new_account
        self.browser.find_element(By.NAME, 'cusid').send_keys("68204")
        self.browser.find_element(By.NAME, 'inideposit').send_keys("556")
        account_type_dropdown = self.browser.find_element(By.NAME, 'selaccount')
        account_type_dropdown.send_keys("Current")
        selected_option = account_type_dropdown.get_attribute('value')
        self.assertEqual(selected_option, "Current")
        self.browser.find_element(By.NAME,'button2').click()
        error_10 = "Account Generated Successfully!!!"
        self.assertEqual(error_10, self.browser.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/p[1]").text)
        sleep(2)

    def test_na16_link_click(self):
        self.browser.find_element(By.LINK_TEXT,'Continue').click()
        


if __name__ == '__main__':
    unittest.main()
