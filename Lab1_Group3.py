import  random
import  string
total_length  = int(input("Enter the total Length of the password  "))
num_letters  = int(input("How many letters do you want "))
for x in  range (0, num_letters):
    random_letter = random.choice(string.ascii_letters)
    print(f"Random letter: {random_letter}")


num_digit = int(input("Enter the num of digits: "))

for x in  range (0, num_digit):
    random_digit = random.choice(string.digits)
    print(f"Random digit: {random_digit}")

num_special_characters   = input("How many special characters do you want ")
random_special = random.choice(string.punctuation)
