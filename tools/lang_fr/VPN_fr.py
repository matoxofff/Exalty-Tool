import time
from colorama import Fore
from fade import *

def print_with_delay(text, delay=0.05):
    lines = text.splitlines()
    for line in lines:
        print(line)
        time.sleep(delay)

banner = """

██╗   ██╗██████╗ ███╗   ██╗
██║   ██║██╔══██╗████╗  ██║
██║   ██║██████╔╝██╔██╗ ██║
╚██╗ ██╔╝██╔═══╝ ██║╚██╗██║
 ╚████╔╝ ██║     ██║ ╚████║
  ╚═══╝  ╚═╝     ╚═╝  ╚═══╝
                           
"""

vpn = """
1. ExpressVPN – Connu pour ses vitesses rapides, ses solides fonctionnalités de sécurité et son large réseau de serveurs.

2. NordVPN – Offre une sécurité robuste, des fonctionnalités de confidentialité et un grand nombre de serveurs.

3. CyberGhost – Facile à utiliser avec un fort accent sur la confidentialité et la sécurité.

4. Surfshark – Excellent rapport qualité-prix avec un support illimité pour les appareils et des fonctionnalités de confidentialité solides.

5. Private Internet Access (PIA) – Connu pour ses fonctionnalités de sécurité personnalisables et son prix abordable.

6. ProtonVPN – Offre une sécurité et une confidentialité solides avec un accent sur la transparence et une politique de non-conservation des logs.

7. IPVanish – Bon pour la vitesse et le chiffrement fort, avec une large gamme d'options de serveurs.

8. Hotspot Shield – Offre une bonne vitesse et est facile à utiliser, bien que sa version gratuite soit limitée.

9. TunnelBear – Facile à utiliser avec un design amusant, bien que son plan gratuit soit plus limité.

10. Mullvad – Connu pour son fort engagement envers la confidentialité et l'anonymat."""

print_with_delay(Fore.LIGHTBLUE_EX + banner, delay=0.05)
print()
print(Fore.LIGHTRED_EX + "Ce sont les meilleurs VPN pour le hacking :")
print("")
print_with_delay(Fore.LIGHTBLACK_EX + vpn, delay=0.05)
print()