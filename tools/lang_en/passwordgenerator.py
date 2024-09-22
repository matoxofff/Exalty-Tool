import random
import os 
import string
from colorama import Fore

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

os.system('cls' if os.name == 'nt' else 'clear')
password_length = int(input(Fore.LIGHTCYAN_EX + "Enter the desired password length :"))
generated_password = generate_password(password_length)

print("Your generated password is :", generated_password)
