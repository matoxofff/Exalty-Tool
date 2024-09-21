import time
from colorama import Fore

def print_with_delay(text, delay=0.05):
    lines = text.splitlines()
    for line in lines:
        print(line)
        time.sleep(delay)

darkwebsafely = """
1. Utilisez le navigateur Tor : Le réseau Tor offre l'anonymat en redirigeant votre connexion à travers plusieurs serveurs. Téléchargez et utilisez le navigateur Tor depuis son site officiel pour accéder aux sites en .onion en toute sécurité.

2. Activez les fonctionnalités de sécurité : Dans le navigateur Tor, ajustez les paramètres de sécurité en mode "Le plus sûr". Cela désactive JavaScript et d'autres fonctionnalités potentiellement dangereuses.

3. Évitez les informations personnelles : Ne partagez aucune information personnelle et n'utilisez pas votre véritable identité. Utilisez des pseudonymes et des adresses e-mail jetables si nécessaire.

4. Utilisez un VPN : Bien que Tor offre l'anonymat, le combiner avec un VPN ajoute une couche supplémentaire de confidentialité en masquant votre adresse IP avant qu'elle n'atteigne le réseau Tor.

5. Soyez prudent avec les liens : Évitez de cliquer sur des liens non vérifiés ou suspects. De nombreux liens sur le dark web peuvent mener à des sites malveillants ou des arnaques.

6. Gardez vos logiciels à jour : Mettez régulièrement à jour votre navigateur Tor et tout autre logiciel que vous utilisez pour vous protéger contre les vulnérabilités.

7. Utilisez des cryptomonnaies : Pour les transactions, utilisez des cryptomonnaies comme le Bitcoin ou le Monero pour maintenir l'anonymat. Évitez les méthodes de paiement traditionnelles.

8. Évitez de télécharger des fichiers : Télécharger des fichiers depuis le dark web peut être risqué et vous exposer à des malwares. Ne téléchargez rien à moins d'être sûr que c'est sécurisé.

9. Méfiez-vous des arnaques : Le dark web contient de nombreuses arnaques et activités illégales. Soyez sceptique face aux offres qui semblent trop belles pour être vraies.

10. Connaissez la loi : Familiarisez-vous avec les implications légales de vos activités. Participer à des activités illégales peut entraîner de graves conséquences."""

print(Fore.LIGHTRED_EX + "Voici comment aller sur le darkweb sans problème :")
print("")
print_with_delay(Fore.LIGHTBLACK_EX + darkwebsafely, delay=0.05)
print()