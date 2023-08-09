# Guru99 Bank Demo Website Structure

> [!INFO] This is the structure of the website:

## Before Logging in
- HomePage (This is the manager login page)
    - Asks for: 
        - User ID 
        - Password

## After Logging in
- Nav Bar (There's a navbar there)
    - Manager (This is the 1st entry, this basically greets the manager)
    - The actual modules:
        - New Customer
        - Edit Customer
        - Delete Customer
        - New Account
        - Edit Account
        - Delete Account
        - Deposit
        - Withdrawal
        - Fund Transfer
        - Change Password
        - Balance Enquiry
        - Mini Statement
        - Customised Statement
    - Log out

> [!Question] So here's my question:

If we're always going to be logging in right? so instead of writing the code for logging in the website in each different module, could I just create a different file where it just logs in & then the user gets the option to select which test case they want to run & the logging in file runs first?

> [!Answer] Yes!

What could be done is, we create a login_module & import it in each of the different test case modules, thereby making sure that the website is logged in each time.