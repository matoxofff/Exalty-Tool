import time
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

setup = """1. Qu'est-ce qu'un portefeuille de cryptomonnaie ?

Un portefeuille de cryptomonnaie est un outil numérique qui vous permet de stocker, envoyer et recevoir des cryptomonnaies comme Bitcoin, Ethereum, et d'autres. Il contient des clés privées et publiques, vous permettant de gérer vos fonds en toute sécurité. Les portefeuilles existent sous différentes formes : logiciels, matériels, ou même papier.

2. Types de portefeuilles de cryptomonnaie

Portefeuilles logiciels (Hot Wallets) :

Installés sur un ordinateur ou un appareil mobile.
Accessibles via Internet.
Exemples : Exodus, Trust Wallet, Electrum.

Portefeuilles matériels (Cold Wallets) :

Appareils physiques conçus pour stocker les clés privées hors ligne.
Plus sécurisés que les portefeuilles logiciels.
Exemples : Ledger Nano S, Trezor.

Portefeuilles papier :

Un document physique qui contient vos clés publiques et privées.
Sécurisé s'il est bien conservé, mais difficile à utiliser pour des transactions régulières.

3. Configuration d'un portefeuille logiciel (Exemple : Exodus)

Étape 1 : Télécharger le portefeuille

Visitez le site officiel du fournisseur de portefeuille (dans ce cas, Exodus) pour éviter les sites de phishing.
Téléchargez le portefeuille pour votre système d'exploitation (Windows, macOS, Linux ou mobile).

Étape 2 : Installer le portefeuille

Ouvrez le programme d'installation et suivez les instructions.
Une fois installé, lancez l'application du portefeuille.

Étape 3 : Créer un nouveau portefeuille

Sur l'écran de bienvenue, choisissez "Créer un nouveau portefeuille".
Vous verrez votre adresse publique, que vous utiliserez pour recevoir des cryptomonnaies.

Étape 4 : Sauvegarder votre portefeuille

Exodus (et la plupart des portefeuilles) vous donnera une phrase de récupération de 12 mots.
Notez cette phrase de récupération et stockez-la dans un endroit sûr. Cette phrase est le seul moyen de récupérer votre portefeuille en cas de perte d'accès à votre appareil.
NE PARTAGEZ JAMAIS cette phrase de récupération avec qui que ce soit. Traitez-la comme votre clé privée.

Étape 5 : Activer les fonctionnalités de sécurité

Définissez un mot de passe fort pour le portefeuille.
Activez l'authentification à deux facteurs (2FA) si disponible (tous les portefeuilles ne prennent pas en charge cette fonctionnalité).

4. Configuration d'un portefeuille matériel (Exemple : Ledger Nano S)

Étape 1 : Acheter sur le site officiel

Achetez des portefeuilles matériels uniquement sur le site officiel pour éviter les appareils compromis. Pour Ledger, visitez Ledger.com.

Étape 2 : Initialiser le portefeuille

Branchez le Ledger Nano S sur votre ordinateur à l'aide du câble USB fourni.
Suivez les instructions à l'écran de l'appareil et de l'application Ledger Live pour le configurer.
Créez un code PIN pour accéder à votre portefeuille.

Étape 3 : Sauvegarder votre phrase de récupération

L'appareil vous montrera une phrase de récupération de 24 mots. Notez-la et stockez-la en lieu sûr.
Cette phrase vous permettra de restaurer votre portefeuille en cas de perte ou de dommage de l'appareil.

Étape 4 : Installer des applications de cryptomonnaies

Via l'application Ledger Live, installez les applications pour chaque cryptomonnaie que vous souhaitez stocker (par exemple, Bitcoin, Ethereum).

Étape 5 : Transférer des cryptomonnaies

Pour recevoir des cryptomonnaies, sélectionnez l'application appropriée (par exemple, l'application Bitcoin) et générez une adresse de réception.
Utilisez cette adresse pour transférer des fonds vers votre portefeuille matériel depuis une plateforme d'échange ou un autre portefeuille.

5. Meilleures pratiques en matière de sécurité

Sauvegardez votre phrase de récupération : Conservez votre phrase de récupération dans plusieurs endroits sécurisés. Ne la stockez jamais en ligne.
Utilisez des mots de passe forts : Toujours définir un mot de passe fort pour accéder à votre portefeuille. Évitez de réutiliser des mots de passe d'autres sites.
Activez le 2FA : Si votre portefeuille prend en charge le 2FA, activez-le pour ajouter une couche de protection supplémentaire.
Méfiez-vous du phishing : Téléchargez uniquement les logiciels de portefeuille ou accédez aux services via les sites officiels. Vérifiez toujours les URL.
Utilisez le stockage à froid pour de grandes sommes : Si vous envisagez de détenir une quantité importante de cryptomonnaie, envisagez d'utiliser un portefeuille matériel ou une solution de stockage à froid.

6. Utilisation de votre portefeuille

Recevoir des fonds : Partagez votre adresse publique avec l'expéditeur pour recevoir des cryptomonnaies. Assurez-vous que c'est le bon portefeuille (par exemple, ne pas envoyer d'Ethereum à une adresse Bitcoin).

Envoyer des fonds : Entrez l'adresse du destinataire, spécifiez le montant, et confirmez la transaction avec votre mot de passe ou code PIN.

Frais de transaction : Soyez conscient que l'envoi de cryptomonnaies peut nécessiter le paiement de frais de transaction. Le montant des frais dépend du réseau et de la rapidité de traitement que vous souhaitez.

"""

print_with_delay(Fore.LIGHTBLUE_EX + banner, delay=0.05)
print()
print(Fore.LIGHTRED_EX + "Configurer un portefeuille de crypto-monnaies :")
print("")
print_with_delay(Fore.LIGHTBLACK_EX + setup, delay=0.02)
print()