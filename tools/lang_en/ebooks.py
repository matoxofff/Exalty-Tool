import time
import os 
from colorama import Fore
from fade import *

def print_with_delay(text, delay=0.05):
    lines = text.splitlines()
    for line in lines:
        print(line)
        time.sleep(delay)

os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.LIGHTRED_EX + "The ebooks are not yet available on the discord server...")