# run_tests.py

import unittest
# module 1
from tests.test_new_customer import TestNewCustomer
# module 2
from tests.test_edit_customer import TestEditCustomer
# module 3
from tests.test_delete_customer import TestDeleteCustomer
# module 4
from tests.test_new_account import TestNewAccount
# module 5
from tests.test_edit_account import TestEditAccount
# module 6
from tests.test_delete_account import TestDeleteAccount
# module 7
from tests.test_balance_enquiry import TestBalanceEnquiry
# module 8
from tests.test_mini_statement import TestMiniStatement
# module 9
from tests.test_customize_statement import TestCustomizeStatement

# the test_class is basically the module that we're testing
def run_specific_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Run all tests for all defined test classes
def run_all_tests():
    # a list which contains all the modules
    test_classes = [
        TestNewCustomer,
        TestEditCustomer,
        TestDeleteCustomer,
        TestNewAccount,
        TestEditAccount,
        TestDeleteAccount,
        TestBalanceEnquiry,
        TestMiniStatement,
        TestCustomizeStatement,
    ]
    # creating a loop, to run all the test cases at once...
    for test_class in test_classes:
        run_specific_tests(test_class)

def run_tests_menu():
    while True:
        print("Select a test module to run:")
        print("1. Test New Customer")
        print("2. Test Edit Customer")
        print("3. Test Delete Customer")
        print("4. Test New Account")
        print("5. Test Edit Account")
        print("6. Test Delete Account")
        print("7. Test Balance Enquiry")
        print("8. Test Mini Statement")
        print("9. Test Customize Statement")
        print("10. Run All Tests")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            run_specific_tests(TestNewCustomer)
        elif choice == "2":
            run_specific_tests(TestEditCustomer)
        elif choice == "3":
            run_specific_tests(TestDeleteCustomer)
        elif choice == "4":
            run_specific_tests(TestNewAccount)
        elif choice == "5":
            run_specific_tests(TestEditAccount)
        elif choice == "6":
            run_specific_tests(TestDeleteAccount)
        elif choice == "7":
            run_specific_tests(TestBalanceEnquiry)
        elif choice == "8":
            run_specific_tests(TestMiniStatement)
        elif choice == "9":
            run_specific_tests(TestCustomizeStatement)
        elif choice == "10":
            run_all_tests()  # Run all tests
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def main():
    print("Welcome to the Test Runner!")
    run_tests_menu()

if __name__ == "__main__":
    main()
