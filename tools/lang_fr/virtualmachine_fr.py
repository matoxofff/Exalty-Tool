import time
from colorama import Fore
from fade import *

def print_with_delay(text, delay=0.05):
    lines = text.splitlines()
    for line in lines:
        print(line)
        time.sleep(delay)

instruction = """
1. Choisissez un logiciel de virtualisation

Vous aurez besoin d'un hyperviseur pour créer et gérer des machines virtuelles (VM). Les deux options les plus populaires sont :

VirtualBox (Gratuit, open-source)
VMware Workstation Player (Gratuit pour une utilisation personnelle)

Téléchargez et installez le logiciel de votre choix :

VirtualBox : https://www.virtualbox.org
VMware : https://www.vmware.com/

2. Téléchargez une image ISO

Un fichier ISO est une copie numérique d'un système d'exploitation. Choisissez l'OS que vous souhaitez installer :

Ubuntu : Télécharger Ubuntu
Windows : Windows ISO
Kali Linux (Pour le test de pénétration) : Télécharger Kali Linux

3. Créez une machine virtuelle

Ouvrez votre logiciel de virtualisation et suivez ces étapes :

Dans VirtualBox :

Cliquez sur "Nouveau" pour créer une nouvelle VM.
Nommez votre VM, sélectionnez le type de système d'exploitation (ex : Linux, Windows) et allouez de la mémoire (RAM). Un minimum de 2 Go est recommandé.
Créez un disque dur virtuel (format VDI, allocation dynamique de préférence).
Sélectionnez la quantité d'espace de stockage (minimum de 20 Go recommandé).

Dans VMware :

Cliquez sur "Créer une nouvelle machine virtuelle".
Choisissez l'image disque d'installation (ISO) et recherchez l'ISO que vous avez téléchargé.
Suivez les instructions à l'écran pour configurer la RAM, l'espace disque et d'autres configurations.

4. Installez le système d'exploitation

Démarrez la VM et elle démarrera à partir du fichier ISO.
Suivez les étapes d'installation standard pour l'OS choisi.
Après l'installation, retirez le fichier ISO des paramètres de la machine virtuelle pour éviter de démarrer à nouveau à partir de celui-ci.

5. Installez les Additions Invités / Outils VMware

Une fois l'OS installé, vous pouvez installer les Additions Invités (pour VirtualBox) ou les Outils VMware (pour VMware). Ces outils améliorent les performances, permettent l'intégration de la souris, activent le partage du presse-papiers et offrent une meilleure résolution d'écran.

Dans VirtualBox : Allez dans "Périphériques" > "Insérer une image CD des Additions Invités", puis suivez les instructions à l'intérieur de la VM.
Dans VMware : Allez dans "Player" > "Gérer" > "Installer VMware Tools".

6. Créez des instantanés (Optionnel mais recommandé)

Les instantanés vous permettent de sauvegarder l'état actuel de votre VM afin de pouvoir y revenir si quelque chose tourne mal.

Dans VirtualBox : Cliquez sur "Instantanés" et créez un nouvel instantané.
Dans VMware : Allez dans "VM" > "Instantané" > "Prendre un instantané".

7. Tester dans l'environnement virtuel

Maintenant que votre VM est configurée, vous pouvez l'utiliser pour :

Tester des logiciels.
Naviguer sur le web de manière anonyme.
Réaliser des tests d'intrusion en toute sécurité (si vous utilisez un OS spécialisé comme Kali Linux).
Expérimenter différentes configurations sans affecter votre machine principale.

8. Conseils de sécurité

Utilisez toujours un adaptateur réseau virtuel pour isoler la VM de votre réseau réel si vous testez des logiciels potentiellement malveillants.
Mettez régulièrement à jour l'OS de la VM et prenez des instantanés avant toute modification importante.
Ne partagez pas de fichiers entre la machine hôte et la VM, sauf si vous êtes certain que les fichiers sont sûrs."""

print(Fore.LIGHTRED_EX + "Voici les instructions pour installer une VM :")
print("")
print_with_delay(Fore.LIGHTBLACK_EX + instruction, delay=0.03)
print()