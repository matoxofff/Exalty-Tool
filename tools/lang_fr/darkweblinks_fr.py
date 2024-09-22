import time
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

links = """Marchés illégaux :

DeepMart.onion : Un marché proposant tout, des drogues, armes illégales, informations de cartes de crédit volées et passeports falsifiés.
SilkRoadRevive.onion : Connu pour vendre des stupéfiants, des données piratées et des produits contrefaits.
BlackMarketPlace.onion : Offre des armes, drogues et documents falsifiés.

Services de piratage :

AnonHack.onion : Propose des services de piratage, y compris des attaques DDoS, la récupération de données personnelles et la défiguration de sites web.
HireAHacker.onion : Un site où l’on peut engager des hackers professionnels pour de l'espionnage industriel, des piratages par vengeance ou des tests de sécurité.
ZeroDayHub.onion : Spécialisé dans la vente d’exploits de type "zero-day", de code malveillant et d’autres cyber-armes.

Drogues et produits pharmaceutiques :

PharmaMarket.onion : Vend des médicaments sur ordonnance sans prescription, incluant des opiacés, des stimulants et des anxiolytiques.
Psychedelica.onion : Focalisé sur les drogues psychédéliques comme le LSD, le DMT et les champignons hallucinogènes.
OpioidMaster.onion : Un site spécialisé dans l’héroïne, le fentanyl et autres opioïdes.

Données volées et fraude :

CardersWorld.onion : Spécialisé dans la vente d’informations de cartes de crédit volées, de numéros de sécurité sociale et d'identifiants bancaires.
BankCracker.onion : Offre des services de piratage de comptes bancaires, des services de vol d'identité et des guides de fraude en ligne.
SSNMarket.onion : Un marché pour acheter et vendre des numéros de sécurité sociale volés.

Services de tueurs à gages et extrémistes :

AssassinMarket.onion : Un site extrêmement controversé offrant des services de tueurs à gages à la demande.
DarkMercenary.onion : Axé sur des services paramilitaires, allant de la protection personnelle à des assassins à louer.
RevolutionaryForce.onion : Un site hébergeant du contenu extrémiste, incitant à la violence et aux mouvements révolutionnaires illégaux."""

print_with_delay(Fore.LIGHTBLUE_EX + banner, delay=0.05)
print()
print(Fore.LIGHTRED_EX + "Liens du DarkWeb :")
print("")
print_with_delay(Fore.LIGHTBLACK_EX + links, delay=0.05)
print()