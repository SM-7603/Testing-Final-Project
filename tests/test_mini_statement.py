import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# import the login module - to make sure, we login to the website
from login_module import login


class TestMiniStatement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()
        login(cls.browser, "mngr520521", "ajAtYhE")

    def setUp(self):
        mini_statement = self.browser.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()
        sleep(2)


    def test_ms1_account_num_empty(self):
        mini_statement = self.browser.find_element(By.XPATH,"//tbody/tr[6]/td[2]/input[1]")
        #enter the value
        mini_statement.send_keys(Keys.TAB)

        sleep(1)

        account_num_empty_field = self.browser.find_element(By.ID, "message2")

        #assert the error message
        assert(account_num_empty_field.text =="Account Number must not be blank")

        sleep(1)


    def test_ms2_account_must_numeric(self):
        mini_statement = self.browser.find_element(By.XPATH,"//tbody/tr[6]/td[2]/input[1]")

        mini_statement.send_keys("add")

        account_account_must_numeric = self.browser.find_element(By.ID, "message2")

        #assert the error message
        assert(account_account_must_numeric.text =="Characters are not allowed")
        
        sleep(2)

    def test_ms3_account_no_must_not_special_character(self):
        mini_statement = self.browser.find_element(By.XPATH,"//tbody/tr[6]/td[2]/input[1]")

        mini_statement.send_keys("@")

        account_no_must_not_special_character =self.browser.find_element(By.ID ,"message2")

        assert(account_no_must_not_special_character.text =="Characters are not allowed")

        sleep(1)

    def test_ms4_account_no_must_not_have_space(self):
        mini_statement = self.browser.find_element(By.XPATH,"//tbody/tr[6]/td[2]/input[1]")

        mini_statement.send_keys("12 3")
        account_no_must_not_have_space =self.browser.find_element(By.ID ,"message2")

        assert(account_no_must_not_have_space.text =="Special characters are not allowed")

        sleep(1)

    def test_ms5_account_no_first_character_not_space(self):
        mini_statement = self.browser.find_element(By.XPATH,"//tbody/tr[6]/td[2]/input[1]")

        mini_statement.send_keys(" ")
        account_no_first_character_not_space =self.browser.find_element(By.ID ,"message2")

        assert(account_no_first_character_not_space.text =="Characters are not allowed")

        sleep(1)

    def test_ms6_valid_account_no(self):
        mini_statement = self.browser.find_element(By.XPATH,"//tbody/tr[6]/td[2]/input[1]")

        mini_statement.send_keys("125578")
        # valid_account_no = self.browser.find_element(By.ID ,"message2")
        expected_url = "https://demo.guru99.com/V4/manager/MiniStatementInput.php"
        self.assertEqual(self.browser.current_url, expected_url)

        sleep(1)

    def test_ms7_invaild_account_no(self):
        mini_statement = self.browser.find_element(By.XPATH,"//tbody/tr[6]/td[2]/input[1]")

        mini_statement.send_keys("132326")


    def test_ms8_reset_button(self):
        self.browser.find_element(By.NAME,'accountno').send_keys('12345')
        self.browser.find_element(By.NAME,'res').click()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

# ... other test modules ...


if __name__ == '__main__':
    unittest.main()
