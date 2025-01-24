import random
import string

# Function to validate user inputs
def validate_inputs(total_length, num_letters, num_digits, num_special):
    if total_length < 8:
        return "Password must be at least 8 characters long."
    if total_length > 20:
        return "Total length cannot exceed 20 characters."
    if num_letters < 0 or num_digits < 0 or num_special < 0:
        return "Numbers must be non-negative."
    if num_letters + num_digits + num_special > total_length:
        return "The sum of specified characters exceeds the total length."
    return None

# Function to generate the password
def generate_password():
    # Ask the user for input
    try:
        total_length = int(input("Enter the total length of the password (minimum of 8 characters, maximum of 20 characters): "))
        if total_length > 20:
            raise ValueError("Total length cannot exceed 20.")
            
        num_letters = int(input("Enter the number of letters (maximum of 20): "))
        if num_letters > 20:
            raise ValueError("Number of letters cannot exceed 20.")
            
        num_digits = int(input("Enter the number of digits (maximum of 20): "))
        if num_digits > 20:
            raise ValueError("Number of digits cannot exceed 20.")
            
        num_special = int(input("Enter the number of special characters (maximum of 20): "))
        if num_special > 20:
            raise ValueError("Number of special characters cannot exceed 20.")
    except ValueError as e:
        print(e)
        return

    # Validate inputs
    validation_error = validate_inputs(total_length, num_letters, num_digits, num_special)
    if validation_error:
        print(validation_error)
        return

    # Password constraints
    num_uppercase = num_letters // 2
    num_lowercase = num_letters - num_uppercase

    # Generate required characters
    password_chars = (
        random.choices(string.ascii_uppercase, k=num_uppercase) +
        random.choices(string.ascii_lowercase, k=num_lowercase) +
        random.choices(string.digits, k=num_digits) +
        random.choices(string.punctuation, k=num_special)
    )

    # Add remaining characters if needed to meet total length
    remaining_length = total_length - len(password_chars)
    if (remaining_length) > 0:
        password_chars += random.choices(string.ascii_letters + string.digits + string.punctuation, k=remaining_length)

    # Shuffle to ensure randomness
    random.shuffle(password_chars)

    # Combine characters into a single string
    password = ''.join(password_chars)
    print(f"Generated password: {password}")

# Run the function to generate password
generate_password()
