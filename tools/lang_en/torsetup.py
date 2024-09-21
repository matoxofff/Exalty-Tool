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

setup = """
1. What is TOR?

TOR (The Onion Router) is a free and open-source software that enables anonymous communication by routing your internet traffic through a network of volunteer-operated servers, or "nodes." It hides your IP address and encrypts your data multiple times to ensure privacy.

Key Benefits of Using TOR:

Anonymity: Hides your real IP address and location.
Privacy: Protects your internet activity from surveillance.
Access: Allows access to websites blocked or censored in your region.

2. Downloading and Installing TOR

Step 1: Download TOR Browser

Visit the official TOR website (https://www.torproject.org) to avoid counterfeit versions or malware.
Download the appropriate version for your operating system (Windows, macOS, Linux, or Android).

Step 2: Install TOR

Once downloaded, run the installer file and follow the installation steps.
Windows/Mac: Simply follow the on-screen instructions.
Linux: Extract the tar.xz file and run the ./start-tor-browser script.
On Android, you can also install the TOR Browser from the Google Play Store or download the APK directly from the TOR website.

3. Configuring TOR Browser

Step 1: Launch TOR Browser

Open the TOR Browser after installation. You will be prompted with two options: Connect or Configure.
Connect: For most users, clicking "Connect" will be sufficient to start using TOR.
Configure: If you live in a country where TOR is blocked or restricted, you may need to configure a bridge or use a proxy. TOR will guide you through the process if this is necessary.

Step 2: Testing Your Connection

Once connected, TOR will open a browser window.
Visit https://check.torproject.org to confirm that you are connected through TOR. The page should tell you, "Congratulations. This browser is configured to use TOR."

4. Using TOR Safely

1. Avoid Full-Screen Mode

Full-screen mode may reveal details about your system, such as your screen size, which could potentially identify your device. Always keep the browser window at its default size.

2. Don’t Use Personal Information

Avoid logging into accounts that contain personal information, like your Google or Facebook account, while using TOR. Doing so could compromise your anonymity.

3. Disable JavaScript

JavaScript can be exploited by hackers or websites to track your identity. By default, TOR is configured to block certain types of JavaScript, but you can enhance security by fully disabling it:
Click on the shield icon in the top right corner of TOR Browser.
Select Advanced Security Settings and choose Safest to disable JavaScript entirely.

4. Use HTTPS Websites

TOR encrypts your traffic within its network, but the exit node (the final server before you reach your destination) decrypts it before delivering it to the destination website. This means using HTTPS websites is crucial to prevent "man-in-the-middle" attacks.

TOR Browser has an integrated tool called HTTPS Everywhere that ensures you’re connecting to secure versions of websites when available. Keep this feature enabled.

5. Be Aware of Browser Fingerprinting

TOR Browser works to reduce browser fingerprinting (collecting data like your browser version, screen resolution, and plugins). However, adding custom extensions or modifying TOR Browser settings can make you more identifiable. Keep TOR Browser as close to its default configuration as possible.

5. Advanced Configuration for Extra Security

1. Using TOR Bridges

In some countries, TOR is blocked by ISPs (Internet Service Providers). TOR bridges are special, unpublished entry points into the TOR network that help bypass such restrictions.
In the TOR Browser startup screen, click on Configure, then select Tor is censored in my country to request bridges or add custom bridges.

2. Avoid Torrenting

Do not use torrent clients over TOR. Torrents can reveal your real IP address, which defeats the purpose of using TOR for privacy. Additionally, torrenting can overwhelm the TOR network, making it slower for other users.

3. Using a VPN with TOR

While TOR alone provides strong anonymity, some users prefer to use a VPN (Virtual Private Network) with TOR for an extra layer of security.
VPN before TOR: This setup hides your TOR usage from your ISP but may slow down your connection.
TOR before VPN: Less common but can route your traffic through a VPN after it exits the TOR network.

6. Accessing the Dark Web with TOR

TOR allows you to access .onion websites, which are hidden services only accessible via TOR. These sites are part of the so-called "Dark Web."

1. Finding .onion Sites

Be cautious when accessing .onion sites. Many of these websites host illegal activities, and visiting them could lead to legal consequences.
Stick to trustworthy sources for finding legitimate .onion services, like the TOR Hidden Wiki.

2. Protect Your Privacy

Always remain cautious when browsing .onion sites, as they can pose higher risks for malware and scams.
Never provide any personal information, and avoid downloading files unless you are sure of their source.
"""

print_with_delay(Fore.LIGHTBLUE_EX + banner, delay=0.05)
print()
print(Fore.LIGHTRED_EX + "How to use TOR :")
print("")
print_with_delay(Fore.LIGHTBLACK_EX + setup, delay=0.01)
print()