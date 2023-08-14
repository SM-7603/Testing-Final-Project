# test_new_customer.py

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# import the login module - to make sure, we login to the website
from login_module import login


class TestNewCustomer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()
        login(cls.browser, "mngr520521", "ajAtYhE")

    def setUp(self):
        # Find new customer field from nav bar:
        new_customer_field = self.browser.find_element(
            By.PARTIAL_LINK_TEXT, "New Customer")
        # Click new customer
        new_customer_field.click()
        # Wait
        sleep(0.25)

    # ... rest of your test methods ...

    def test_nc01_empty_name(self):
        # # do stuff
        # # I want to have this in setup:
        # # find new customer field from nav bar:
        # new_customer_field = self.browser.find_element(
        #     By.PARTIAL_LINK_TEXT, "New Customer")
        # # click new customer
        # new_customer_field.click()
        # # wait
        # sleep(0.25)

        # entering proper values:

        # find customer name field:
        customer_name_field = self.browser.find_element(By.NAME, "name")
        # enter values:
        customer_name_field.send_keys(Keys.TAB)
        # wait
        sleep(0.25)

        # find customer error message:
        customer_name_error_field = self.browser.find_element(By.ID, "message")

        # assert the error message:
        assert (customer_name_error_field.text ==
                "Customer name must not be blank")

        # wait
        sleep(0.25)

    def test_nc02_num_name(self):
        # entering proper values:

        # find customer name field:
        customer_name_field = self.browser.find_element(By.NAME, "name")
        # enter values:
        customer_name_field.send_keys("123")
        # wait
        sleep(0.25)

        # find customer error message:
        customer_name_error_field = self.browser.find_element(By.ID, "message")

        # assert the error message:
        assert (customer_name_error_field.text ==
                "Numbers are not allowed")
        # wait
        sleep(0.25)

    def test_nc03_special_char_name(self):
        # entering proper values:

        # find customer name field:
        customer_name_field = self.browser.find_element(By.NAME, "name")
        # enter values:
        customer_name_field.send_keys("***")
        # wait
        sleep(0.25)

        # find customer error message:
        customer_name_error_field = self.browser.find_element(By.ID, "message")

        # assert the error message:
        assert (customer_name_error_field.text ==
                "Special characters are not allowed")
        # wait
        sleep(0.25)

    def test_nc04_first_char_blank(self):
        # entering proper values:

        # find customer name field:
        customer_name_field = self.browser.find_element(By.NAME, "name")
        # enter values:
        customer_name_field.send_keys(" ")
        # wait
        sleep(0.25)

        # find customer error message:
        customer_name_error_field = self.browser.find_element(By.ID, "message")

        # assert the error message:
        assert (customer_name_error_field.text ==
                "First character can not have space")
        # wait
        sleep(0.25)

    def test_nc05_empty_address(self):
        # entering proper values:

        # find customer name field:
        address_field = self.browser.find_element(By.NAME, "addr")
        # enter values:
        address_field.send_keys(Keys.TAB)
        # wait
        sleep(0.25)

        # find customer error message:
        address_error_field = self.browser.find_element(By.ID, "message3")

        # assert the error message:
        assert (address_error_field.text ==
                "Address Field must not be blank")
        # wait
        sleep(0.25)

    def test_nc06_first_char_blank_address(self):
        # entering proper values:

        # find customer name field:
        address_field = self.browser.find_element(By.NAME, "addr")
        # enter values:
        address_field.send_keys(" ")
        # wait
        sleep(0.25)

        # find customer error message:
        address_error_field = self.browser.find_element(By.ID, "message3")

        # assert the error message:
        assert (address_error_field.text ==
                "First character can not have space")
        # wait
        sleep(0.25)

    def test_nc07_empty_city(self):
        # entering proper values:

        # find customer name field:
        city_field = self.browser.find_element(By.NAME, "city")
        # enter values:
        city_field.send_keys(Keys.TAB)
        # wait
        sleep(0.25)

        # find customer error message:
        city_error_field = self.browser.find_element(By.ID, "message4")

        # assert the error message:
        assert (city_error_field.text ==
                "City Field must not be blank")
        # wait
        sleep(0.25)

    def test_nc08_num_city(self):
        # entering proper values:

        # find customer name field:
        city_field = self.browser.find_element(By.NAME, "city")
        # enter values:
        city_field.send_keys("123")
        # wait
        sleep(0.25)

        # find customer error message:
        city_error_field = self.browser.find_element(By.ID, "message4")

        # assert the error message:
        assert (city_error_field.text ==
                "Numbers are not allowed")
        # wait
        sleep(0.25)

    def test_nc09_special_char_city(self):
        # entering proper values:

        # find customer name field:
        city_field = self.browser.find_element(By.NAME, "city")
        # enter values:
        city_field.send_keys("***")
        # wait
        sleep(0.25)

        # find customer error message:
        city_error_field = self.browser.find_element(By.ID, "message4")

        # assert the error message:
        assert (city_error_field.text ==
                "Special characters are not allowed")
        # wait
        sleep(0.25)

    def test_nc10_first_char_blank_city(self):
        # entering proper values:

        # find customer name field:
        city_field = self.browser.find_element(By.NAME, "city")
        # enter values:
        city_field.send_keys(" ")
        # wait
        sleep(0.25)

        # find customer error message:
        city_error_field = self.browser.find_element(By.ID, "message4")

        # assert the error message:
        assert (city_error_field.text ==
                "First character can not have space")
        # wait
        sleep(0.25)

    def test_nc11_empty_state(self):
        # entering proper values:

        # find customer name field:
        state_field = self.browser.find_element(By.NAME, "state")
        # enter values:
        state_field.send_keys(Keys.TAB)
        # wait
        sleep(0.25)

        # find customer error message:
        state_error_field = self.browser.find_element(By.ID, "message5")

        # assert the error message:
        assert (state_error_field.text ==
                "State must not be blank")
        # wait
        sleep(0.25)

    def test_nc12_num_state(self):
        # entering proper values:

        # find customer name field:
        state_field = self.browser.find_element(By.NAME, "state")
        # enter values:
        state_field.send_keys("123")
        # wait
        sleep(0.25)

        # find customer error message:
        state_error_field = self.browser.find_element(By.ID, "message5")

        # assert the error message:
        assert (state_error_field.text ==
                "Numbers are not allowed")
        # wait
        sleep(0.25)

    def test_nc13_special_char_state(self):
        # entering proper values:

        # find customer name field:
        state_field = self.browser.find_element(By.NAME, "state")
        # enter values:
        state_field.send_keys("***")
        # wait
        sleep(0.25)

        # find customer error message:
        state_error_field = self.browser.find_element(By.ID, "message5")

        # assert the error message:
        assert (state_error_field.text ==
                "Special characters are not allowed")
        # wait
        sleep(0.25)

    def test_nc14_first_char_blank_state(self):
        # entering proper values:

        # find customer name field:
        state_field = self.browser.find_element(By.NAME, "state")
        # enter values:
        state_field.send_keys(" ")
        # wait
        sleep(0.25)

        # find customer error message:
        state_error_field = self.browser.find_element(By.ID, "message5")

        # assert the error message:
        assert (state_error_field.text ==
                "First character can not have space")
        # wait
        sleep(0.25)

    def test_nc15_non_numeric_pin(self):
        # entering proper values:

        # find customer name field:
        pin_num_field = self.browser.find_element(By.NAME, "pinno")
        # enter values:
        pin_num_field.send_keys("hi")
        # wait
        sleep(0.25)

        # find customer error message:
        pin_num_error_field = self.browser.find_element(By.ID, "message6")

        # assert the error message:
        assert (pin_num_error_field.text ==
                "Characters are not allowed")
        # wait
        sleep(0.25)

    def test_nc16_empty_pin(self):
        # entering proper values:

        # find customer name field:
        pin_num_field = self.browser.find_element(By.NAME, "pinno")
        # enter values:
        pin_num_field.send_keys(Keys.TAB)
        # wait
        sleep(0.25)

        # find customer error message:
        pin_num_error_field = self.browser.find_element(By.ID, "message6")

        # assert the error message:
        assert (pin_num_error_field.text ==
                "PIN Code must not be blank")
        # wait
        sleep(0.25)

    def test_nc17_incorrect_length_pin(self):
        # entering proper values:

        # find customer name field:
        pin_num_field = self.browser.find_element(By.NAME, "pinno")
        # enter values:
        pin_num_field.send_keys("12345")
        # wait
        sleep(0.25)

        # find customer error message:
        pin_num_error_field = self.browser.find_element(By.ID, "message6")

        # assert the error message:
        assert (pin_num_error_field.text ==
                "PIN Code must have 6 Digits")
        # wait
        sleep(0.25)

    def test_nc18_special_char_pin(self):
        # entering proper values:

        # find customer name field:
        pin_num_field = self.browser.find_element(By.NAME, "pinno")
        # enter values:
        pin_num_field.send_keys("***")
        # wait
        sleep(0.25)

        # find customer error message:
        pin_num_error_field = self.browser.find_element(By.ID, "message6")

        # assert the error message:
        assert (pin_num_error_field.text ==
                "Special characters are not allowed")
        # wait
        sleep(0.25)

    def test_nc19_first_char_blank_pin(self):
        # entering proper values:

        # find customer name field:
        pin_num_field = self.browser.find_element(By.NAME, "pinno")
        # enter values:
        pin_num_field.send_keys(" ")
        # wait
        sleep(0.25)

        # find customer error message:
        pin_num_error_field = self.browser.find_element(By.ID, "message6")

        # assert the error message:
        assert (pin_num_error_field.text ==
                "First character can not have space")
        # wait
        sleep(0.25)

    # I think, here you meant to insert a space b/w the digits

    def test_nc20_blank_space_pin(self):
        # entering proper values:

        # find customer name field:
        pin_num_field = self.browser.find_element(By.NAME, "pinno")
        # enter values:
        pin_num_field.send_keys("12 34")
        # wait
        sleep(0.25)

        # find customer error message:
        pin_num_error_field = self.browser.find_element(By.ID, "message6")

        # assert the error message:
        assert (pin_num_error_field.text ==
                "Characters are not allowed")
        # wait
        sleep(0.25)

    def test_nc21_empty_mobile_number(self):
        # entering proper values:

        # find customer name field:
        mobile_num_field = self.browser.find_element(By.NAME, "telephoneno")
        # enter values:
        mobile_num_field.send_keys(Keys.TAB)
        # wait
        sleep(0.25)

        # find customer error message:
        mobile_num_error_field = self.browser.find_element(By.ID, "message7")

        # assert the error message:
        assert (mobile_num_error_field.text ==
                "Mobile no must not be blank")
        # wait
        sleep(0.25)

    def test_nc22_first_char_blank_mobile_number(self):
        # entering proper values:

        # find customer name field:
        mobile_num_field = self.browser.find_element(By.NAME, "telephoneno")
        # enter values:
        mobile_num_field.send_keys(" ")
        # wait
        sleep(0.25)

        # find customer error message:
        mobile_num_error_field = self.browser.find_element(By.ID, "message7")

        # assert the error message:
        assert (mobile_num_error_field.text ==
                "First character can not have space")
        # wait
        sleep(0.25)

    def test_nc23_mobile_number_with_spaces(self):
        # entering proper values:

        # find customer name field:
        mobile_num_field = self.browser.find_element(By.NAME, "telephoneno")
        # enter values:
        mobile_num_field.send_keys("123 456")
        # wait
        sleep(0.25)

        # find customer error message:
        mobile_num_error_field = self.browser.find_element(By.ID, "message7")

        # assert the error message:
        assert (mobile_num_error_field.text ==
                "Characters are not allowed")
        # wait
        sleep(0.25)

    def test_nc24_special_char_mobile_number(self):
        # entering proper values:

        # find customer name field:
        mobile_num_field = self.browser.find_element(By.NAME, "telephoneno")
        # enter values:
        mobile_num_field.send_keys("123*456")
        # wait
        sleep(0.25)

        # find customer error message:
        mobile_num_error_field = self.browser.find_element(By.ID, "message7")

        # assert the error message:
        assert (mobile_num_error_field.text ==
                "Special characters are not allowed")
        # wait
        sleep(0.25)

    def test_nc25_empty_email(self):
        # entering proper values:

        # find customer name field:
        email_id_field = self.browser.find_element(By.NAME, "emailid")
        # enter values:
        email_id_field.send_keys(Keys.TAB)
        # wait
        sleep(0.25)

        # find customer error message:
        email_id_error_field = self.browser.find_element(By.ID, "message9")

        # assert the error message:
        assert (email_id_error_field.text ==
                "Email-ID must not be blank")
        # wait
        sleep(0.25)

    def test_nc26_invalid_email_formats(self):
        # entering proper values:

        # find customer name field:
        email_id_field = self.browser.find_element(By.NAME, "emailid")
        # enter values:
        email_id_field.send_keys("hi@")
        # wait
        sleep(0.25)

        # find customer error message:
        email_id_error_field = self.browser.find_element(By.ID, "message9")

        # assert the error message:
        assert (email_id_error_field.text ==
                "Email-ID is not valid")
        # wait
        sleep(0.25)

    # >[!important] - this one fails, fault of the website
    def test_nc27_email_with_spaces(self):
        # entering proper values:

        # find customer name field:
        email_id_field = self.browser.find_element(By.NAME, "emailid")
        # enter values:
        email_id_field.send_keys("h @gmail.com")
        # wait
        sleep(0.25)

        # find customer error message:
        email_id_error_field = self.browser.find_element(By.ID, "message9")

        # assert the error message:
        assert (email_id_error_field.text ==
                "Email-ID is not valid")
        # wait
        sleep(0.25)

    def test_nc28_empty_password(self):
        # entering proper values:

        # find customer name field:
        password_field = self.browser.find_element(By.NAME, "password")
        # enter values:
        password_field.send_keys(Keys.TAB)
        # wait
        sleep(0.25)

        # find customer error message:
        password_error_field = self.browser.find_element(By.ID, "message18")

        # assert the error message:
        assert (password_error_field.text ==
                "Password must not be blank")
        # wait
        sleep(0.25)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()


if __name__ == '__main__':
    unittest.main()
