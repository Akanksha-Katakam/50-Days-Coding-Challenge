# Day - 3 -> Password Generator

import string
import random

# Characters used to generate a password
characters = string.ascii_letters + string.digits + "@#$%&*!"

# Function to generate password
def generate_password(length):
    password =""
    for i in range(length):
        password += random.choice(characters)
        
    return password

length = int(input("Enter Password Length: "))

password = generate_password(length)

print("Generated Password: ", password)
         