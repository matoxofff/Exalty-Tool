import os
import sys

def install(package):
    """Installe un package Python via pip"""
    try:
        os.system(f"pip install {package}")
    except Exception as e:
        print(f"Failed to install {package}: {e}")

try:
    print("Downloading what you need for ExaltyTool")

    # Liste des modules à installer
    modules = [
        'requests', 
        'colorama', 
        'selenium', 
        'beautifulsoup4', 
        'dnspython', 
        'whois', 
        'rich', 
        'fade', 
        'logging',
        'urllib3'
    ]

    # Installation des modules
    for module in modules:
        print(f"Installing {module}...")
        install(module)

    # Mettre à jour pip et exécuter le fichier Exalty.py en fonction du système d'exploitation
    if sys.platform.startswith("win"):
        os.system("python -m pip install --upgrade pip")
        os.system("python Exalty.py")

    elif sys.platform.startswith("linux"):
        os.system("python3 -m pip install --upgrade pip")
        os.system("python3 Exalty.py")

except Exception as exception:
    print(f"An error occurred: {exception}")
