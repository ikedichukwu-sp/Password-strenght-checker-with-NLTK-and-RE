import nltk
from nltk.corpus import words
import re

# Download the words corpus
nltk.download('words')

word_list = set(words.words())  # Load all English words as a set for quick lookup

def contains_english_word(password):
    """
    Checks if the password contains any valid English word.
    Uses regex to extract words (letters only, no digits or special chars).
    """
    # Split password into individual words (considering only letters and not numbers/special chars)
    words_in_password = [word.lower() for word in re.findall(r'\b[a-zA-Z]+\b', password)]
    for word in words_in_password:
        if word in word_list:
            return True
    return False

print("Welcome to the Password Strength Checker")
has_upper = False
has_lower = False
has_digit = False
has_special_character = False
password_strong = False

user_password = input("Enter your password: ")

# Check for minimum length
if len(user_password) >= 8:
    password_strong = True
else:
    print("Your password is not at least 8 characters long.")

# Check for uppercase, lowercase, digit, and special character
for char in user_password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
    if not char.isalnum():  # Special character check
        has_special_character = True

# Check for dictionary word in the password
if contains_english_word(user_password):
    password_strong = False

# Final check
if has_lower and has_upper and password_strong and has_digit and has_special_character and not contains_english_word(user_password):
    print("The password is strong!")
else:
    if contains_english_word(user_password):
        print("Your password contains an English word, which is not allowed.")
    print("Your password must contain:")
    if not has_upper:
        print("- At least one uppercase letter")
    if not has_lower:
        print("- At least one lowercase letter")
    if not has_digit:
        print("- At least one digit")
    if not has_special_character:
        print("- At least one special character")
    if contains_english_word(user_password):
        print("- No common English words (e.g., 'mypass')")
