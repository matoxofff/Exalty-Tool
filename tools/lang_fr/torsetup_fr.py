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

setup = """1. Qu'est-ce que TOR ?

TOR (The Onion Router) est un logiciel gratuit et open-source qui permet une communication anonyme en redirigeant votre trafic Internet à travers un réseau de serveurs opérés par des bénévoles, appelés "nœuds". Il masque votre adresse IP et crypte vos données plusieurs fois pour assurer votre confidentialité.

Avantages clés de l'utilisation de TOR :

Anonymat : Masque votre véritable adresse IP et localisation.
Confidentialité : Protège vos activités en ligne contre la surveillance.
Accès : Permet d'accéder aux sites bloqués ou censurés dans votre région.

2. Téléchargement et installation de TOR

Étape 1 : Téléchargez le navigateur TOR

Visitez le site officiel de TOR (https://www.torproject.org) pour éviter les versions contrefaites ou malveillantes.
Téléchargez la version appropriée pour votre système d'exploitation (Windows, macOS, Linux ou Android).

Étape 2 : Installez TOR

Une fois téléchargé, lancez le fichier d'installation et suivez les étapes :

Windows/Mac : Suivez simplement les instructions à l'écran.
Linux : Extrayez le fichier tar.xz et exécutez le script ./start-tor-browser.
Sur Android, vous pouvez aussi installer TOR Browser depuis le Google Play Store ou télécharger l'APK directement depuis le site de TOR.

3. Configuration du navigateur TOR

Étape 1 : Lancez TOR Browser

Ouvrez TOR Browser après l'installation. Vous serez invité à choisir entre deux options : Connecter ou Configurer.

Connecter : Pour la plupart des utilisateurs, cliquer sur "Connecter" suffit pour commencer à utiliser TOR.
Configurer : Si vous vivez dans un pays où TOR est bloqué ou restreint, vous devrez peut-être configurer un pont ou utiliser un proxy. TOR vous guidera à travers ce processus si nécessaire.

Étape 2 : Testez votre connexion

Une fois connecté, TOR ouvrira une fenêtre du navigateur.
Visitez https://check.torproject.org pour vérifier que vous êtes bien connecté à TOR. La page devrait vous indiquer : "Félicitations. Ce navigateur est configuré pour utiliser TOR."

4. Utiliser TOR en toute sécurité

1. Évitez le mode plein écran

Le mode plein écran peut révéler des détails sur votre système, comme la taille de votre écran, ce qui pourrait potentiellement identifier votre appareil. Gardez toujours la fenêtre du navigateur à sa taille par défaut.

2. N'utilisez pas d'informations personnelles

Évitez de vous connecter à des comptes contenant des informations personnelles, comme votre compte Google ou Facebook, pendant que vous utilisez TOR. Cela pourrait compromettre votre anonymat.

3. Désactivez JavaScript

JavaScript peut être exploité par des hackers ou des sites web pour suivre votre identité. Par défaut, TOR bloque certains types de JavaScript, mais vous pouvez renforcer la sécurité en le désactivant complètement :

Cliquez sur l'icône de bouclier en haut à droite de TOR Browser.
Sélectionnez Paramètres de sécurité avancés et choisissez Le plus sûr pour désactiver JavaScript entièrement.

4. Utilisez des sites HTTPS

TOR crypte votre trafic au sein de son réseau, mais le nœud de sortie (le dernier serveur avant que vous atteigniez votre destination) le décrypte avant de l'envoyer au site web de destination. Cela signifie qu'il est crucial d'utiliser des sites HTTPS pour prévenir les attaques de type "man-in-the-middle".

TOR Browser intègre un outil appelé HTTPS Everywhere, qui garantit que vous vous connectez à des versions sécurisées des sites lorsque cela est possible. Gardez cette fonctionnalité activée.

5. Attention au "fingerprinting" de votre navigateur

TOR Browser réduit le risque de "fingerprinting" (collecte de données comme la version de votre navigateur, la résolution d'écran et les plugins). Cependant, l'ajout d'extensions personnalisées ou la modification des paramètres de TOR Browser peuvent vous rendre plus identifiable. Gardez TOR Browser aussi proche que possible de sa configuration par défaut.

5. Configuration avancée pour une sécurité accrue

1. Utilisation des ponts TOR

Dans certains pays, TOR est bloqué par les fournisseurs d'accès Internet (FAI). Les ponts TOR sont des points d'entrée spéciaux, non publiés, dans le réseau TOR, qui permettent de contourner ces restrictions.

Sur l'écran de démarrage de TOR Browser, cliquez sur Configurer, puis sélectionnez TOR est censuré dans mon pays pour demander des ponts ou ajouter des ponts personnalisés.

2. Évitez le torrenting

N'utilisez pas de clients torrent via TOR. Les torrents peuvent révéler votre véritable adresse IP, ce qui annule l'objectif d'utiliser TOR pour la confidentialité. En outre, le torrenting peut surcharger le réseau TOR, le rendant plus lent pour les autres utilisateurs.

3. Utilisation d'un VPN avec TOR

Bien que TOR fournisse un anonymat fort à lui seul, certains utilisateurs préfèrent utiliser un VPN (réseau privé virtuel) avec TOR pour une couche de sécurité supplémentaire.

VPN avant TOR : Ce paramètre masque votre utilisation de TOR à votre FAI, mais peut ralentir votre connexion.
TOR avant VPN : Moins courant, mais cela peut acheminer votre trafic via un VPN après qu'il a quitté le réseau TOR.

6. Accéder au Dark Web avec TOR

TOR vous permet d'accéder aux sites .onion, qui sont des services cachés accessibles uniquement via TOR. Ces sites font partie de ce qu'on appelle le "Dark Web".

1. Trouver des sites .onion

Soyez prudent lorsque vous accédez aux sites .onion. De nombreux sites hébergent des activités illégales, et leur visite peut entraîner des conséquences juridiques. Restez fidèle à des sources fiables pour trouver des services légitimes en .onion, comme le TOR Hidden Wiki.

2. Protégez votre vie privée

Soyez toujours vigilant lorsque vous naviguez sur des sites .onion, car ils peuvent poser des risques plus élevés pour les malwares et les arnaques. Ne fournissez jamais d'informations personnelles et évitez de télécharger des fichiers à moins d'être certain de leur source."""

print_with_delay(Fore.LIGHTBLUE_EX + banner, delay=0.05)
print()
print(Fore.LIGHTRED_EX + "Comment utiliser TOR :")
print("")
print_with_delay(Fore.LIGHTBLACK_EX + setup, delay=0.01)
print()