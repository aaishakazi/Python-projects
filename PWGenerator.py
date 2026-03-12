import string
import random

characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_password():
    pw_length = int(input("Enter the desired password length: "))
    
    random.shuffle(characters)
    password = []
    
    for i in range(pw_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password) 
    print("Generated password:" , password)

while True:
    option = input("Do you want to generate a password? (yes/no): ")
    if option.lower() == "yes":
        generate_password()
        quit()
    elif option.lower() == "no":
        print("Exiting the password generator. Thnx!")
        quit()
    else:
        print("Invalid input. Please enter 'yes' or 'no'.") 
    
