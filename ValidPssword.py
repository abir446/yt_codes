import re # We'll use the 're' module for checking digits and capitals efficiently

def is_valid_password(password_str):
    """
    Checks if a given password string meets the specified criteria.

    Criteria:
    - Minimum length of 4 characters.
    - Cannot start with a digit.
    - Cannot contain spaces or forward slashes.
    - Must contain at least one uppercase letter.
    - Must contain at least one digit.
    """
    # 1. Minimum length check
    if len(password_str) < 4:
        return False

    # 2. Cannot start with a digit
    if password_str[0].isdigit():
        return False

    # 3. Cannot contain spaces or forward slashes
    if ' ' in password_str or '/' in password_str:
        return False

    # 4. Check for at least one uppercase letter and one digit
    has_capital = False
    has_digit = False

    for char in password_str:
        if char.isupper():
            has_capital = True
        if char.isdigit():
            has_digit = True

    return has_capital and has_digit

# Take user input
user_password = input("Enter a password: ")

# Check the validity of the entered password
if is_valid_password(user_password):
    print("Password is valid.")
else:
    print("Password is not valid.")
