import random
import string

def get_positive_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 2:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

total_length = get_positive_number("Enter the total length of the password: ")

while True:
    num_letters = get_positive_number("How many letters do you want? ")
    num_digits = get_positive_number("Enter the number of digits: ")
    num_special_characters = get_positive_number("How many special characters do you want? ")

    if num_letters + num_digits + num_special_characters > total_length:
        print("The sum of letters, digits, and special characters exceeds the total length. Try again.")
    else:
        break

password_chars = []

for _ in range(num_letters):
    password_chars.append(random.choice(string.ascii_letters))

for _ in range(num_digits):
    password_chars.append(random.choice(string.digits))

for _ in range(num_special_characters):
    password_chars.append(random.choice(string.punctuation))

random.shuffle(password_chars)

password = ''.join(password_chars)
print(f"Generated password: {password}")
