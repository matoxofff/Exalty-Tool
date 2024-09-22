import os
import requests

# Définir le chemin du fichier de tokens
input_file = 'Input/Token-List/token_list.txt'

# Fonction pour tester la validité d'un token Discord
def check_token(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    url = "https://discord.com/api/v9/users/@me"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return "Valid"
    elif response.status_code == 401:
        return "Invalid"
    elif response.status_code == 403:
        return "Locked"
    else:
        return f"Error ({response.status_code})"

# Fonction principale pour lire les tokens, les tester et afficher les résultats
def token_checker():
    # Vérifier si le fichier d'entrée existe
    if not os.path.exists(input_file):
        print(f"Le fichier {input_file} n'existe pas.")
        return

    # Lire les tokens depuis le fichier
    with open(input_file, 'r') as file:
        tokens = [line.strip() for line in file if line.strip()]
    
    if not tokens:
        print("Aucun token trouvé dans le fichier.")
        return

    # Tester les tokens et afficher les résultats dans le terminal
    for token in tokens:
        result = check_token(token)
        print(f"Token: {token} -> {result}")

# Exécution du script
if __name__ == "__main__":
    token_checker()
