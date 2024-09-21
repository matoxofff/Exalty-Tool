import random
import string
from colorama import Fore

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = int(input(Fore.LIGHTCYAN_EX + "Entre la longueur du mot de passe que tu souhaite génerer :"))
generated_password = generate_password(password_length)

print("Le mot de passe généré est  :", generated_password)