import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("Password Generator")

    # Get user input for password length
    length = int(input("Enter the desired length of the password: "))

    # Generate and display password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
