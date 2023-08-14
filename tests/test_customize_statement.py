import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# import the login module - to make sure, we login to the website
from login_module import login


class TestCustomizeStatement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()
        login(cls.browser, "mngr520521", "ajAtYhE")

    def setUp(self):
        customized_statement = self.browser.find_element(
            By.PARTIAL_LINK_TEXT, "Customised Statement")
        customized_statement.click()
        sleep(0.25)

    def test_cs01_account_no_not_empty(self):
        account_no = self.browser.find_element(
            By.NAME, "accountno")

        account_no.send_keys(Keys.TAB)

        sleep(0.25)

        account_no_not_empty = self.browser.find_element(By.ID, "message2")

        assert (account_no_not_empty.text ==
                "Account Number must not be blank")

        sleep(0.25)

    def test_cs02_account_no_numeric(self):
        account_no = self.browser.find_element(
            By.NAME, "accountno")

        account_no.send_keys("asd")

        sleep(0.25)

        account_no_numeric = self.browser.find_element(By.ID, "message2")

        assert (account_no_numeric.text == "Characters are not allowed")

    def test_cs03_account_no_not_special_character(self):
        account_no = self.browser.find_element(
            By.NAME, "accountno")

        account_no.send_keys("@")

        sleep(0.25)

        account_no_not_special_character = self.browser.find_element(
            By.ID, "message2")

        assert (account_no_not_special_character.text ==
                "Special characters are not allowed")

    def test_cs04_account_no_no_space(self):

        account_no_no_space = self.browser.find_element(
            By.NAME, "accountno")

        account_no_no_space.send_keys("123 23")

        sleep(0.25)

        account_no_numeric = self.browser.find_element(By.ID, "message2")

        assert (account_no_numeric.text == "Characters are not allowed")

    def test_cs05_account_no_no_first_space(self):
        account_no = self.browser.find_element(
            By.NAME, "accountno")

        account_no.send_keys(" ")

        sleep(0.25)

        account_no_no_first_space = self.browser.find_element(
            By.ID, "message2")

        assert (account_no_no_first_space.text == "Characters are not allowed")

    def test_cs06_from_date(self):
        from_date = self.browser.find_element(By.NAME, "fdate")

        from_date.click()

        # from_date.send_keys(Keys.TAB)

        sleep(0.25)

        from_date = self.browser.find_element(By.ID, "message26")

        assert (from_date.text == "From Date Field must not be blank")

    def test_cs07_to_date(self):
        to_date = self.browser.find_element(By.NAME, "tdate")

        to_date.click()

        # to_date.send_keys(Keys.TAB)

        sleep(0.25)

        to_date = self.browser.find_element(By.ID, "message27")

        assert (to_date.text == "To Date Field must not be blank")

    def test_cs08_min_transaction_must_numeric(self):
        min_transaction_field = self.browser.find_element(
            By.NAME, "amountlowerlimit")

        min_transaction_field.send_keys("hello")

        # wait
        sleep(0.25)

        # min transaction error message:
        min_transaction_error_field = self.browser.find_element(
            By.ID, "message12")

        # assert the error message:
        assert (min_transaction_error_field.text ==
                "Characters are not allowed")
        # wait
        sleep(0.25)

    def test_cs09_min_transaction_special_char(self):
        min_transaction_field = self.browser.find_element(
            By.NAME, "amountlowerlimit")

        min_transaction_field.send_keys("***")

        # wait
        sleep(0.25)

        # min transaction error message:
        min_transaction_error_field = self.browser.find_element(
            By.ID, "message12")

        # assert the error message:
        assert (min_transaction_error_field.text ==
                "Special characters are not allowed")
        # wait
        sleep(0.25)

    def test_cs10_blank_space_transaction(self):
        min_transaction_field = self.browser.find_element(
            By.NAME, "amountlowerlimit")

        min_transaction_field.send_keys("123 45")

        # wait
        sleep(0.25)

        # min transaction error message:
        min_transaction_error_field = self.browser.find_element(
            By.ID, "message12")

        # assert the error message:
        assert (min_transaction_error_field.text ==
                "Characters are not allowed")
        # wait
        sleep(0.25)

    def test_cs11_blank_first_char_transaction(self):
        min_transaction_field = self.browser.find_element(
            By.NAME, "amountlowerlimit")

        min_transaction_field.send_keys(" ")

        # wait
        sleep(0.25)

        # min transaction error message:
        min_transaction_error_field = self.browser.find_element(
            By.ID, "message12")

        # assert the error message:
        assert (min_transaction_error_field.text ==
                "Characters are not allowed")
        # wait
        sleep(0.25)

    def test_cs12_num_transaction_numberic(self):
        min_transaction_field = self.browser.find_element(
            By.NAME, "numtransaction")

        min_transaction_field.send_keys(" ")

        # wait
        sleep(0.25)

        # min transaction error message:
        min_transaction_error_field = self.browser.find_element(
            By.ID, "message13")

        # assert the error message:
        assert (min_transaction_error_field.text ==
                "Characters are not allowed")
        # wait
        sleep(0.25)

    def test_cs13_num_transaction_special_char(self):
        min_transaction_field = self.browser.find_element(
            By.NAME, "numtransaction")

        min_transaction_field.send_keys("***")

        # wait
        sleep(0.25)

        # min transaction error message:
        min_transaction_error_field = self.browser.find_element(
            By.ID, "message13")

        # assert the error message:
        assert (min_transaction_error_field.text ==
                "Special characters are not allowed")
        # wait
        sleep(0.25)

    def test_cs14_num_transaction_blank_space(self):
        min_transaction_field = self.browser.find_element(
            By.NAME, "numtransaction")

        min_transaction_field.send_keys("123 45")

        # wait
        sleep(0.25)

        # min transaction error message:
        min_transaction_error_field = self.browser.find_element(
            By.ID, "message13")

        # assert the error message:
        assert (min_transaction_error_field.text ==
                "Characters are not allowed")
        # wait
        sleep(0.25)

    def test_cs15_num_transaction_blank_first_char(self):
        min_transaction_field = self.browser.find_element(
            By.NAME, "numtransaction")

        min_transaction_field.send_keys(" ")

        # wait
        sleep(0.25)

        # min transaction error message:
        min_transaction_error_field = self.browser.find_element(
            By.ID, "message13")

        # assert the error message:
        assert (min_transaction_error_field.text ==
                "Characters are not allowed")
        # wait
        sleep(0.25)

    # The issue
    def test_cs16_reset_button(self):
        # account field
        account_num_field = self.browser.find_element(By.NAME, "accountno")
        account_num_field.send_keys("123456")

        # from date
        from_date_field = self.browser.find_element(By.NAME, "fdate")
        from_date_field.send_keys("2012-05-12")

        # to date
        to_date_field = self.browser.find_element(By.NAME, "tdate")
        to_date_field.send_keys("2015-05-12")

        # min transaction field
        min_transaction_field = self.browser.find_element(
            By.NAME, "amountlowerlimit")
        min_transaction_field.send_keys("10")

        # num transaction field
        num_transaction_field = self.browser.find_element(
            By.NAME, "numtransaction")
        num_transaction_field.send_keys("5")

        # reset
        reset_button_field = self.browser.find_element(By.NAME, "res")
        reset_button_field.click()

        # wait
        sleep(1)

# this would fail - as the website isn't complete
    def test_cs16_submit_button(self):
        # account field
        account_num_field = self.browser.find_element(By.NAME, "accountno")
        account_num_field.send_keys("125589")

        # from date
        from_date_field = self.browser.find_element(By.NAME, "fdate")
        from_date_field.send_keys("2012-05-12")

        # to date
        to_date_field = self.browser.find_element(By.NAME, "tdate")
        to_date_field.click()

        # min transaction field
        min_transaction_field = self.browser.find_element(
            By.NAME, "amountlowerlimit")
        min_transaction_field.send_keys("10")

        # num transaction field
        num_transaction_field = self.browser.find_element(
            By.NAME, "numtransaction")
        num_transaction_field.send_keys("5")

        # reset
        submit_button_field = self.browser.find_element(By.NAME, "AccSubmit")
        submit_button_field.click()

        # expected url after deletion - the same page, where the error would be shown
        expected_url = "https://demo.guru99.com/V4/manager/CustomisedStatementInput.php"

        self.assertEqual(expected_url, self.browser.current_url)

        # wait
        sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()


if __name__ == '__main__':
    unittest.main()
