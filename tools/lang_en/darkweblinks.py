import time
import os
from colorama import Fore
from fade import *

def print_with_delay(text, delay=0.05):
    lines = text.splitlines()
    for line in lines:
        print(line)
        time.sleep(delay)

banner = """
      
████████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔═══██╗██╔══██╗
   ██║   ██║   ██║██████╔╝
   ██║   ██║   ██║██╔══██╗
   ██║   ╚██████╔╝██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                          
"""

links = """Illegal Marketplaces:

DeepMart.onion : A marketplace offering everything from drugs, illegal weapons, stolen credit card information, and fake passports.
SilkRoadRevive.onion : Known for selling narcotics, hacked data, and counterfeit goods.
BlackMarketPlace.onion : Offers weapons, drugs, and forged documents.

Hacking Services:

AnonHack.onion : Provides hacking services, including DDoS attacks, personal data retrieval, and website defacement.
HireAHacker.onion : A site where one can hire professional hackers for corporate espionage, revenge hacks, or security testing.
ZeroDayHub.onion : Specializes in selling zero-day exploits, malicious code, and other cyber-weaponry.

Drugs and Pharmaceuticals:

PharmaMarket.onion : Sells prescription drugs without a prescription, including opiates, stimulants, and anxiety meds.
Psychedelica.onion : Focuses on psychedelic drugs like LSD, DMT, and magic mushrooms.
OpioidMaster.onion : A specialized site for heroin, fentanyl, and other opioids.

Stolen Data & Fraud:

CardersWorld.onion : Specializes in selling stolen credit card information, SSNs, and banking credentials.
BankCracker.onion : Offers bank account hacking services, personal identity theft services, and online fraud guides.
SSNMarket.onion : A marketplace for buying and selling stolen social security numbers.

Hitman & Extremist Services:

AssassinMarket.onion : A highly controversial site offering hitmen services for hire.
DarkMercenary.onion : Focuses on paramilitary services, ranging from personal protection to hired assassins.
RevolutionaryForce.onion : A site hosting extremist content, inciting violence, and illegal revolutionary movements."""

os.system('cls' if os.name == 'nt' else 'clear')
print_with_delay(Fore.LIGHTBLUE_EX + banner, delay=0.05)
print()
print(Fore.LIGHTRED_EX + "Darkweb Links :")
print("")
print_with_delay(Fore.LIGHTBLACK_EX + links, delay=0.05)
print()