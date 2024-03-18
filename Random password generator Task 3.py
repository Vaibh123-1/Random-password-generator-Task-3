import secrets
import string
import json

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def save_passwords(passwords, filename='passwords.json'):
    with open(filename, 'w') as file:
        json.dump(passwords, file, indent=2)

def load_passwords(filename='passwords.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def main():
    passwords = load_passwords()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Generate a new password")
        print("2. View saved passwords")
        print("3. Save and exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            website = input("Enter the website or service name: ")
            length = int(input("Enter the password length (default is 12): ") or 12)
            password = generate_password(length)
            passwords[website] = password
            print(f"Generated password for {website}: {password}")

        elif choice == '2':
            print("\nSaved Passwords:")
            for website, password in passwords.items():
                print(f"{website}: {password}")

        elif choice == '3':
            save_passwords(passwords)
            print("Password manager saved. Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
