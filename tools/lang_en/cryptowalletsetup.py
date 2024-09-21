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
      
 ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ 
██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗
██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║
██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║
╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ 
                                                   
"""

setup = """1. What is a Cryptocurrency Wallet?

A cryptocurrency wallet is a digital tool that allows you to store, send, and receive cryptocurrencies like Bitcoin, Ethereum, and others. It contains private and public keys, allowing you to manage your funds securely. Wallets come in different forms: software, hardware, or even paper.

2. Types of Cryptocurrency Wallets

Software Wallets (Hot Wallets):

Installed on a computer or mobile device.
Accessible via the internet.
Examples: Exodus, Trust Wallet, Electrum.

Hardware Wallets (Cold Wallets):

Physical devices designed to securely store private keys offline.
More secure than software wallets.
Examples: Ledger Nano S, Trezor.

Paper Wallets:

A physical document that contains your public and private keys.
Secure if stored properly but difficult to use for regular transactions.

3. Setting Up a Software Wallet (Example: Exodus)

Step 1: Download the Wallet

Visit the official website of the wallet provider (in this case, Exodus) to avoid phishing sites.
Download the wallet for your operating system (Windows, macOS, Linux, or mobile).

Step 2: Install the Wallet

Open the installer and follow the instructions.
Once installed, launch the wallet application.

Step 3: Create a New Wallet

On the welcome screen, choose Create a New Wallet.
You’ll be presented with your public address, which you’ll use to receive cryptocurrency.

Step 4: Backup Your Wallet

Exodus (and most wallets) will give you a 12-word recovery phrase.
Write down this recovery phrase and store it in a safe place. This phrase is the only way to recover your wallet if you lose access to your device.
NEVER share this recovery phrase with anyone. Treat it like your private key.

Step 5: Enable Security Features

Set a strong password for the wallet.
Enable 2-factor authentication (2FA) if available (not all wallets support this).

4. Setting Up a Hardware Wallet (Example: Ledger Nano S)

Step 1: Purchase from the Official Website

Only buy hardware wallets from the official website to avoid tampered devices. For Ledger, visit Ledger.com.

Step 2: Initialize the Wallet

Plug the Ledger Nano S into your computer using the provided USB cable.
Follow the instructions on the device’s screen and the Ledger Live app to set it up.
Create a PIN code to access your wallet.

Step 3: Backup Your Recovery Phrase

The device will show you a 24-word recovery phrase. Write this down and store it securely.
This recovery phrase will allow you to restore your wallet if the device is lost or damaged.

Step 4: Install Cryptocurrency Apps

Through the Ledger Live app, install apps for each cryptocurrency you want to store (e.g., Bitcoin, Ethereum).

Step 5: Transfer Cryptocurrency

To receive cryptocurrency, select the appropriate app (e.g., Bitcoin app) and generate a receive address.
Use this address to transfer funds to your hardware wallet from an exchange or another wallet.

5. Security Best Practices

Backup Your Recovery Phrase: Store your recovery phrase in multiple secure locations. Never store it online.
Use Strong Passwords: Always set a strong password for accessing your wallet. Avoid reusing passwords from other sites.
Enable 2FA: If your wallet supports 2FA, enable it to add an extra layer of protection.
Beware of Phishing: Only download wallet software or access services through official websites. Always double-check URLs.
Use Cold Storage for Large Amounts: If you plan to hold a significant amount of cryptocurrency, consider using a hardware wallet or cold storage solution.

6. Using Your Wallet

Receiving Funds: Share your public address with the sender to receive cryptocurrency. Make sure it’s the right wallet (e.g., don’t send Ethereum to a Bitcoin address).

Sending Funds: Enter the recipient’s address, specify the amount, and confirm the transaction with your password or PIN.

Transaction Fees: Be aware that sending cryptocurrency may require you to pay a transaction fee. The fee amount depends on the network and the speed of processing you desire.

"""


os.system('cls' if os.name == 'nt' else 'clear')
print_with_delay(Fore.LIGHTBLUE_EX + banner, delay=0.05)
print()
print(Fore.LIGHTRED_EX + "Setup a Cryptocurrency Wallet :")
print("")
print_with_delay(Fore.LIGHTBLACK_EX + setup, delay=0.05)
print()