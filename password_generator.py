import random
import string

def generate_password(length):
    # characters which are going to be used for password generation
    characters = string.ascii_letters + string.digits + string.punctuation

    # it generates the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))

        # valid length or not
        if length <= 0:
            print("Invalid password length. Please enter a positive integer.")
        else:
            # Generation of password is done here
            password = generate_password(length)

            # Display the generated password
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")
