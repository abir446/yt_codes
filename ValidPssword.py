import re # We'll use the 're' module for checking digits and capitals efficiently

def is_valid_password(password_str):
    
    if len(password_str) < 4:
        return False

   
    if password_str[0].isdigit():
        return False

    
    if ' ' in password_str or '/' in password_str:
        return False

   
    has_capital = False
    has_digit = False

    for char in password_str:
        if char.isupper():
            has_capital = True
        if char.isdigit():
            has_digit = True

    return has_capital and has_digit


user_password = input("Enter a password: ")


if is_valid_password(user_password):
    print("Password is valid.")
else:
    print("Password is not valid.")
