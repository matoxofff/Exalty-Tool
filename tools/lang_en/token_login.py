from selenium import webdriver
import time
from colorama import init, Fore, Style

init()

token_file_path = "Input/Token-List/token_list.txt"

with open(token_file_path, "r") as file:
    tokens = [line.strip() for line in file if line.strip()]

if not tokens:
    print(Fore.RED + "No tokens found in 'token.txt'." + Style.RESET_ALL)
    exit()

print(Fore.CYAN + "Choose a token from the following:" + Style.RESET_ALL)
for i, token in enumerate(tokens, start=1):
    print(Fore.LIGHTGREEN_EX + f"{i}. {token}" + Style.RESET_ALL)
token_choice = int(input(Fore.BLUE + "Enter the number corresponding to the token you want to use: " + Style.RESET_ALL)) - 1

if token_choice < 0 or token_choice >= len(tokens):
    print(Fore.RED + "Invalid choice. Please restart the script and choose a valid token." + Style.RESET_ALL)
    exit()

token = tokens[token_choice]

print(Fore.CYAN + "\nChoose the browser you want to use:" + Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX + "1. Chrome" + Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX + "2. Firefox" + Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX + "3. Edge" + Style.RESET_ALL)
browser_choice = input(Fore.BLUE + "Enter the number corresponding to the browser (1, 2, or 3): " + Style.RESET_ALL)

if browser_choice == '1':
    driver = webdriver.Chrome()  
elif browser_choice == '2':
    driver = webdriver.Firefox()  
elif browser_choice == '3':
    driver = webdriver.Edge()  
else:
    print(Fore.RED + "Invalid choice. Please restart the script and choose a valid browser." + Style.RESET_ALL)
    exit()


driver.get("https://discord.com/login")


time.sleep(5)

script = f'''
    function login(token) {{
        setInterval(() => {{
            document.body.appendChild(document.createElement('iframe')).contentWindow.localStorage.token = `"{token}"`;
        }}, 50);
        setTimeout(() => {{
            location.reload();
        }}, 2500);
    }}
    login("{token}");
'''

driver.execute_script(script)

time.sleep(5)

input(Fore.BLUE + "Press Enter to close the browser..." + Style.RESET_ALL)
driver.quit()
