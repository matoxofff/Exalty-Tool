import time
from colorama import Fore
from fade import *

def print_with_delay(text, delay=0.05):
    lines = text.splitlines()
    for line in lines:
        print(line)
        time.sleep(delay)

print(Fore.LIGHTRED_EX + "Les Ebooks ne sont pas encore disponibles sur le serveur discord...")