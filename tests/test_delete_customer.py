# test_delete_customer.py

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from login_module import login


class TestDeleteCustomer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()
        login(cls.browser, "mngr520521", "ajAtYhE")

    def setUp(self):
        # Find new customer field from nav bar:
        delete_customer_field = self.browser.find_element(
            By.PARTIAL_LINK_TEXT, "Delete Customer")
        # Click new customer
        delete_customer_field.click()
        # Wait
        sleep(0.25)

    # ... rest of your test methods ...

    def test_dc01_empty_id(self):
        # # do stuff
        # # I want to have this in setup:
        # # find new customer field from nav bar:
        # delete_customer_field = self.browser.find_element(
        #     By.PARTIAL_LINK_TEXT, "New Customer")
        # # click new customer
        # delete_customer_field.click()
        # # wait
        # sleep(0.25)

        # entering proper values:

        # find customer name field:
        customer_id_field = self.browser.find_element(By.NAME, "cusid")
        # enter values:
        customer_id_field.send_keys(Keys.TAB)
        # wait
        sleep(0.25)

        # find customer error message:
        customer_id_error_field = self.browser.find_element(By.ID, "message14")

        # assert the error message:
        assert (customer_id_error_field.text ==
                "Customer ID is required")

        # wait
        sleep(0.25)

    def test_dc02_num_id(self):
        # entering proper values:

        # find customer name field:
        customer_id_field = self.browser.find_element(By.NAME, "cusid")
        # enter values:
        customer_id_field.send_keys("123a")
        # wait
        sleep(0.25)

        # find customer error message:
        customer_id_error_field = self.browser.find_element(By.ID, "message14")

        # assert the error message:
        assert (customer_id_error_field.text ==
                "Characters are not allowed")
        # wait
        sleep(0.25)

    def test_dc03_special_char_id(self):
        # entering proper values:

        # find customer name field:
        customer_id_field = self.browser.find_element(By.NAME, "cusid")
        # enter values:
        customer_id_field.send_keys("***")
        # wait
        sleep(0.25)

        # find customer error message:
        customer_id_error_field = self.browser.find_element(By.ID, "message14")

        # assert the error message:
        assert (customer_id_error_field.text ==
                "Special characters are not allowed")
        # wait
        sleep(0.25)

    def test_dc04_char_blank(self):
        # entering proper values:

        # find customer name field:
        customer_id_field = self.browser.find_element(By.NAME, "cusid")
        # enter values:
        customer_id_field.send_keys("123 4")
        # wait
        sleep(0.25)

        # find customer error message:
        customer_id_error_field = self.browser.find_element(By.ID, "message14")

        # assert the error message:
        assert (customer_id_error_field.text ==
                "Characters are not allowed")
        # wait
        sleep(0.25)

    def test_dc05_first_char_blank(self):
        # entering proper values:

        # find customer name field:
        customer_id_field = self.browser.find_element(By.NAME, "cusid")
        # enter values:
        customer_id_field.send_keys(" ")
        # wait
        sleep(0.25)

        # find customer error message:
        customer_id_error_field = self.browser.find_element(By.ID, "message14")

        # assert the error message:
        assert (customer_id_error_field.text ==
                "First character can not have space")
        # wait
        sleep(0.25)

    def test_dc06_incorrect_customer_id(self):
        # entering proper values:

        # find customer name field:
        customer_id_field = self.browser.find_element(By.NAME, "cusid")
        # enter values:
        customer_id_field.send_keys("123")
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
        expected_url = "https://demo.guru99.com/V4/manager/deleteCustomer.php"

        self.assertEqual(expected_url, self.browser.current_url)

        # wait
        sleep(0.25)

    def test_dc07_correct_customer_id(self):
        # entering proper values:

        # find customer name field:
        customer_id_field = self.browser.find_element(By.NAME, "cusid")
        # enter values:
        customer_id_field.send_keys("18316")
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
        expected_url = "https://demo.guru99.com/V4/manager/deleteCustomer.php"

        self.assertEqual(expected_url, self.browser.current_url)

        # wait
        sleep(0.25)

    def test_dc08_reset_button(self):
        # entering proper values:

        # find customer name field:
        customer_id_field = self.browser.find_element(By.NAME, "cusid")
        # enter values:
        customer_id_field.send_keys("18316")
        # wait
        sleep(0.25)

        
        # find reset button field:
        reset_btn_field = self.browser.find_element(By.NAME, "res")
        # click reset button
        reset_btn_field.click()

        # wait
        sleep(0.25)

        # field after reset

        customer_id_field_empty = self.browser.find_element(By.NAME, "cusid")

        customer_id_field_cleared = customer_id_field.clear()

        # wait
        sleep(0.25)

        # assert the field
        self.assertEqual(customer_id_field_cleared, customer_id_field_empty)

        # wait
        sleep(0.25)


    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()


if __name__ == '__main__':
    unittest.main()
