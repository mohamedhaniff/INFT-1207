import  random
import  string
total_length  = int(input("Enter the total Length of the password  "))
    if total_length < 8:
        print("Password must be at least 8 characters")
        return total_length
num_letters  = int(input("How many letters do you want "))
for x in  range (0, num_letters):
    random_letter = random.choice(string.ascii_letters)
    print(f"Random letter: {random_letter}")


num_digit = int(input("Enter the num of digits: "))

for x in  range (0, num_digit):
    random_digit = random.choice(string.digits)
    print(f"Random digit: {random_digit}")

num_special_characters   = int( input("How many special characters do you want "))

for x in  range (0, num_special_characters ):
    random_special = random.choice(string.punctuation)
    print(f"Random special character: {random_special}")

password_output = (random_letter, random_digit, random_special)
print("Your password is: " + password_output)
