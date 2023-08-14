# test_new_customer.py


import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# import the login module - to make sure, we login to the website
from login_module import login

class TestEditCustomer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()
        login(cls.browser, "mngr520521", "ajAtYhE")
        
    def navigate_edit_customer(self):
        edit_customer_field = self.browser.find_element(By.LINK_TEXT, "Edit Customer")
        # click the field
        edit_customer_field.click()
        sleep(3)

    def test_EC1_verify_customer_id_empty(self):
        self.navigate_edit_customer()
        self.browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[6]/td[2]/input[1]').send_keys(Keys.TAB)
        sleep(2)  
        error_01 = "Customer ID is required"
        self.assertEqual(error_01, "Customer ID is required")

    def test_EC2_verify_customer_id_numeric(self):
        self.navigate_edit_customer()
        self.browser.find_element(By.NAME, 'cusid').send_keys("1234Acc")
        error_02 = "Characters are not allowed"
        self.assertEqual(error_02, "Characters are not allowed")
        sleep(2)

    def test_EC3_customer_id_special_character(self):
        self.navigate_edit_customer()
        self.browser.find_element(By.NAME, 'cusid').send_keys("123!@#")
        error_02 = "Special characters are not allowed"
        self.assertEqual(error_02, "Special characters are not allowed")
        sleep(2)

    def test_EC4_customer_id_proper(self):
        self.navigate_edit_customer()
        self.browser.find_element(By.NAME, 'cusid').send_keys("68204")
        sleep(2)
        submit_button = self.browser.find_element(By.NAME, 'AccSubmit')
        submit_button.click()

    def test_EC5_verify_address_empty(self):
        # self.browser.find_element(By.NAME, 'addr').clear()
        self.browser.find_element(By.NAME, 'addr').send_keys(Keys.TAB)
        sleep(2)  
        error_message = self.browser.find_element(By.ID, "message3").text
        self.assertEqual(error_message, "Address Field must not be blank")
        

    def test_EC6_verify_city_empty(self):
        # self.navigate_edit_customer()
        # self.browser.find_element(By.NAME, 'city').clear()
        self.browser.find_element(By.NAME, 'city').send_keys(Keys.TAB)
        sleep(2)
        error_message = self.browser.find_element(By.ID, "message4").text
        self.assertEqual(error_message, "City Field must not be blank")

    def test_EC7_city_numeric(self):
        self.browser.find_element(By.NAME, 'city').send_keys("123")
        sleep(2)
        error_message = self.browser.find_element(By.ID, "message4").text
        self.assertEqual(error_message, "Numbers are not allowed")

    def test_EC8_city_special_characters(self):
        # self.browser.find_element(By.NAME, 'city').clear()
        self.browser.find_element(By.NAME, 'city').send_keys("!@#")
        sleep(2)
        error_message = self.browser.find_element(By.ID, "message4").text
        self.assertEqual(error_message, "Special characters are not allowed")


    def test_EC9_verify_state_empty(self):
        # self.browser.find_element(By.NAME, 'state').clear()
        self.browser.find_element(By.NAME, 'state').send_keys(Keys.TAB)
        sleep(3)  
        error_message = self.browser.find_element(By.ID, "message5").text
        self.assertEqual(error_message, "State must not be blank")

    def test_ec10_num_state(self):
        # entering proper values:

        # find customer name field:
        state_field = self.browser.find_element(By.NAME, "state")
        # enter values:
        state_field.send_keys("123")
        # wait
        sleep(1)

        # find customer error message:
        state_error_field = self.browser.find_element(By.ID, "message5")


        # assert the error message:
        assert (state_error_field.text == "Numbers are not allowed")
        # wait
        sleep(1)
    
    
    def test_ec11_num_special_chars(self):
        # entering proper values:

        # find customer name field:
        state_field = self.browser.find_element(By.NAME, "state")
        # enter values:
        state_field.send_keys("***")
        # wait
        sleep(1)

        # find customer error message:
        state_error_field = self.browser.find_element(By.ID, "message5")


        # assert the error message:
        assert (state_error_field.text == "Special characters are not allowed")
        # wait
        sleep(1)


    def test_ec12_pin_numeric(self):
        pin_field = self.browser.find_element(By.NAME,"pinno")

        # enter new provided set of value 
        pin_field.send_keys("PN")
        sleep(1)

        pin_error_field = self.browser.find_element(By.ID, "message6")


        # assert the error message:
        assert (pin_error_field.text == "Characters are not allowed")

    def test_ec13_pin_empty(self):
        pin_field = self.browser.find_element(By.NAME,"pinno")
        # pin_field.clear()
        pin_field.send_keys(Keys.TAB)
        sleep(3)
        pin_error_field = self.browser.find_element(By.ID, "message6")
        assert(pin_error_field.text == "PIN Code must not be blank")

    def test_ec14_pin_length(self):
        pin_field = self.browser.find_element(By.NAME,"pinno")
        pin_field.send_keys("23")
        sleep(1)
        pin_error_field = self.browser.find_element(By.ID, "message6")
        assert(pin_error_field.text == "PIN Code must have 6 Digits")
    
    def test_ec15_pin_special_chars(self):
        pin_field = self.browser.find_element(By.NAME,"pinno")
        # pin_field.clear()
        pin_field.send_keys("##")
        sleep(1)
        pin_error_field = self.browser.find_element(By.ID, "message6")
        assert(pin_error_field.text == "Special characters are not allowed")
    

    def test_ec16_number_empty(self):
        number_field = self.browser.find_element(By.NAME,'telephoneno')
        # number_field.clear()
        number_field.send_keys(Keys.TAB)
        number_error_field = self.browser.find_element(By.ID,'message7')
        assert(number_error_field.text == "Mobile no must not be blank")

    def test_ec17_number_special_character(self):
        number_field = self.browser.find_element(By.NAME,'telephoneno')
        number_field.send_keys("12345!@#45")
        number_error_field = self.browser.find_element(By.ID,'message7')
        assert(number_error_field.text == "Special characters are not allowed")

    def test_ec18_email_empty(self):
        email_field = self.browser.find_element(By.NAME,"emailid")
        # email_field.clear()
        email_field.send_keys(Keys.TAB)
        sleep(3)
        email_error_field = self.browser.find_element(By.ID,'message9')
        assert(email_error_field.text == "Email-ID must not be blank")

    def test_ec19_email_invalid(self):
        email_field = self.browser.find_element(By.NAME,"emailid")
        email_field.send_keys("guru99")
        sleep(3)
        email_error_field = self.browser.find_element(By.ID,'message9')
        assert(email_error_field.text == "Email-ID is not valid")
    

    def test_ec20_submit(self):

        self.browser.find_element(By.NAME,'sub').click()


    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()


if __name__ == '__main__':
    unittest.main()
