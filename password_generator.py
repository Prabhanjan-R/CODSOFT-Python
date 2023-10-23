import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on user choice for complexity
    character_set = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a random password
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            password = generate_password(length)

            if password:
                print("Generated Password: ", password)

            another = input("Generate another password? (yes/no): ").lower()
            if another != 'yes':
                print("Thank you for using the Password Generator!")
                break
        except ValueError:
            print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
