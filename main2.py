import nltk
import re
import string



print("Welcome to the password strenght Checker")
has_upper = False
has_lower = False
has_digit = False
has_special_character = False
password_strong = False
special_char = False

special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
user_password = input("Enter your password")

def is_special_char(char):
    if char in special_chars:
        return char

if len(user_password) >= 8:
    password_strong = True

else:
    print("Your password is not upto 8 characters")


for char in user_password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
    if is_special_char(char):
        special_char = True


    if has_lower and has_upper and has_digit and special_char:
        break

if has_lower and has_upper and password_strong and has_digit and special_char:
    pass
else:
    print("Your password must contain both uppercase, lowercase, number, special characters and about 8 characters.")



