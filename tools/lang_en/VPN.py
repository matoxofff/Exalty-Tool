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
1. ExpressVPN - Known for its fast speeds, strong security features, and wide server network.

2. NordVPN - Offers robust security, privacy features, and a large number of servers.

3. CyberGhost - User-friendly with a strong focus on privacy and security.

4. Surfshark - Great value with unlimited device support and strong privacy features.

5. Private Internet Access (PIA) - Known for its customizable security features and affordability.

6. ProtonVPN - Offers strong security and privacy with a focus on transparency and no-logs policy.

7. IPVanish - Good for speed and strong encryption, with a wide range of server options.

8. Hotspot Shield - Offers good speed and ease of use, though its free version has limitations.

9. TunnelBear - User-friendly with a fun design, though it has a more limited free plan.

10. Mullvad - Known for its strong commitment to privacy and anonymity."""

print_with_delay(Fore.LIGHTBLUE_EX + banner, delay=0.05)
print()
print(Fore.LIGHTRED_EX + "These are the best VPNs for hacking :")
print("")
print_with_delay(Fore.LIGHTBLACK_EX + vpn, delay=0.05)
print()

