import time
from colorama import Fore
import os 

def print_with_delay(text, delay=0.05):
    lines = text.splitlines()
    for line in lines:
        print(line)
        time.sleep(delay)

darkwebsafely = """
1. Use Tor Browser: The Tor network provides anonymity by routing your connection through multiple servers. Download and use the Tor Browser from its official site to access .onion sites safely.

2. Enable Security Features: In Tor Browser, adjust security settings to “Safest” mode. This disables JavaScript and other potentially dangerous features.

3. Avoid Personal Information: Don’t share any personal information or use your real identity. Use pseudonyms and disposable email addresses if needed.

4. Use a VPN: While Tor provides anonymity, combining it with a VPN adds an extra layer of privacy by masking your IP address before it reaches the Tor network.

5. Be Cautious with Links: Avoid clicking on unverified or suspicious links. Many links on the dark web can lead to malicious sites or scams.

6. Keep Software Updated: Regularly update your Tor Browser and any other software you use to protect against vulnerabilities.

7. Use Cryptocurrency: For transactions, use cryptocurrencies like Bitcoin or Monero to maintain anonymity. Avoid traditional payment methods.

8. Avoid Downloading Files: Downloading files from the dark web can be risky and may expose you to malware. Avoid downloading anything unless you're confident it's safe.

9. Be Aware of Scams: The dark web has many scams and illegal activities. Be skeptical of offers that seem too good to be true.

10. Know the Law: Familiarize yourself with the legal implications of your activities. Engaging in illegal activities can have serious consequences."""

os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.LIGHTRED_EX + "How to go on the dark web safely :")
print("")
print_with_delay(Fore.LIGHTBLACK_EX + darkwebsafely, delay=0.05)
print()
print(Fore.GREEN + f"I am in no way responsible for what you do")