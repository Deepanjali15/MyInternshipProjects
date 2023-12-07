import random
import string

def generate_psd(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 to ensure variety of characters.")

    # Choose one character of each type(uppercase, lowercase , digits and symbols
    uppercase_letter = random.choice(string.ascii_uppercase)
    lowercase_letter = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special_char = random.choice(string.punctuation)

    # Ensure the rest of the password meets the desired length
    remaining_length = length - 4
    characters = string.ascii_letters + string.digits + string.punctuation
    rest_of_password = ''.join(random.choice(characters) for _ in range(remaining_length))

    # Shuffling the characters of the password
    password_chars = list(uppercase_letter + lowercase_letter + digit + special_char + rest_of_password)
    random.shuffle(password_chars)

    password = ''.join(password_chars)
    return password

# Generate number of passwords as given by user
def generate_multiple_passwords(num_passwords, length=12):
    passwords = [generate_psd(length) for _ in range(num_passwords)]
    return passwords

def get_valid_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password (must be at least 4): "))
            if length >= 4:
                return length
            else:
                print("\nPassword length must be at least 4. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("\nWelcome to the Password Generator!\n")

    # Get a valid password length
    length = get_valid_length()

    # Get user input for the number of passwords to generate
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Generate passwords
    passwords = generate_multiple_passwords(num_passwords, length)

    # Display generated passwords
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")

if __name__ == "__main__":
    main()
