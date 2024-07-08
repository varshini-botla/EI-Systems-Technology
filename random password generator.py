import string
import random

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the length is at least 4
    if length < 4:
        print("Password length must be at least 4.")
        return
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt user for the desired password length
    try:
        length = int(input("Enter the desired length for the password: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
    
