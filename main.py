import encrypt
import decrypt

# Define function to get user input for encryption or decryption
def get_user_input():
    while True:
        print("Please choose an option:")
        print("1: Encrypt")
        print("2: Decrypt")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            return "encrypt"
        elif choice == "2":
            return "decrypt"
        else:
            print("Invalid choice. Please try again.")

# Define main function to run the program
def main():
    # Get user input for encryption or decryption
    choice = get_user_input()

    # Run the appropriate module based on user choice
    if choice == "encrypt":
        encrypt.main()
    elif choice == "decrypt":
        decrypt.main()

# Call the main function
if __name__ == "__main__":
    main()
