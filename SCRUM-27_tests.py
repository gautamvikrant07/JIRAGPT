Test Cases for User Story: Implement Basic Authentication System using Flask-Login

1. Test Case: User Registration
   - Input: User provides valid username, email, and password
   - Expected Output: User account is successfully created and added to the database

2. Test Case: User Login
   - Input: User enters valid username and password
   - Expected Output: User is successfully authenticated and logged in

3. Test Case: User Login with Invalid Credentials
   - Input: User enters invalid username or password
   - Expected Output: User receives an error message indicating invalid credentials

4. Test Case: User Logout
   - Input: User clicks on the logout button
   - Expected Output: User is successfully logged out and redirected to the login page

5. Test Case: Session Persistence
   - Input: User logs in and then refreshes the page
   - Expected Output: User session is maintained and the user remains logged in

6. Test Case: User Registration with Existing Username
   - Input: User tries to register with a username that already exists
   - Expected Output: User receives an error message indicating that the username is already taken

7. Test Case: User Registration with Invalid Email Format
   - Input: User provides an invalid email format during registration
   - Expected Output: User receives an error message indicating that the email format is not valid

8. Test Case: User Registration with Weak Password
   - Input: User provides a weak password during registration
   - Expected Output: User receives an error message indicating that the password is too weak

9. Test Case: User Login after Account Deletion
   - Input: User logs in after their account has been deleted
   - Expected Output: User receives an error message indicating that the account does not exist

10. Test Case: User Logout without being Logged in
    - Input: User tries to log out without being logged in
    - Expected Output: User is redirected to the login page without any errors.