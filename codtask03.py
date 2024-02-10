import random
import string

def generate_password(length):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choice
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Welcome to Password Generator")

    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))

    # Generate and display the password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
