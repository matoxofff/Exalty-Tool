import os
import sys
import time
import fade
from colorama import Fore
from fade import *

try: 
    username_pc = os.getlogin()
except: 
    username_pc = "username"

current_language = "en"

def load_language():
    global banner, menu, second_menu
    if current_language == "en":
        from Language.lang_en import banner, menu, second_menu
    elif current_language == "fr":
        from Language.lang_fr import banner, menu, second_menu

def run_tool(tool_name):
    if current_language == "en":
        os.system(f"python tools/lang_en/{tool_name}.py")
        print(Fore.LIGHTRED_EX + "")
    elif current_language == "fr":
        os.system(f"python tools/lang_fr/{tool_name}_fr.py")
        print(Fore.LIGHTRED_EX + "")
        os.system("pause")
        main()

def print_with_delay(text, delay=0.05):
    lines = text.splitlines()
    for line in lines:
        print(line)
        time.sleep(delay)

def main():
    global current_language
    load_language()
    os.system("cls")
    print_with_delay(fade.greenblue(banner), delay=0.03)
    print()
    print_with_delay(fade.greenblue(menu), delay=0.02)
    print(Fore.LIGHTCYAN_EX + f'\n┌── <{username_pc}@exalty> ─ [~]')
    
    choice = input('└──╼ $ ' + Fore.LIGHTWHITE_EX)
    
    if choice == "1":
        run_tool("darkgpt")
    elif choice == "2":
        run_tool("darkweblinks")
    elif choice == "3":
        run_tool("vpn")
    elif choice == "4":
        run_tool("darkwebsafely")
    elif choice == "5":
        run_tool("ebooks")
    elif choice == "6":
        run_tool("virtualmachine")
    elif choice == "7":
        run_tool("passwordgenerator")
    elif choice == "8":
        run_tool("cryptowalletsetup")
    elif choice == "9":
        run_tool("torsetup")
    elif choice == '10':
        run_tool("web_site_scanner")
    elif choice == '11':
        run_tool("website_vulnerability_scanner")
    elif choice == '20':
        run_tool("token_login")
    elif choice == "D":
        print(Fore.LIGHTBLACK_EX + "https://discord.gg/megjVBEmaG" + Fore.RED)
        print("")
    elif choice == "L":  
        if current_language == "en":
            current_language = "fr"
        else:
            current_language = "en"
        main()  
    elif choice == "N":
        second_menu_function()
    elif choice == "E":
        sys.exit()
    else:
        print(Fore.RED + "[x] | Invalid choice : ")
    
    os.system("pause")
    main()

def second_menu_function():
    global current_language
    os.system("cls")
    print_with_delay(fade.greenblue(banner), delay=0.03)
    print()
    print_with_delay(fade.greenblue(second_menu), delay=0.03)
    print(Fore.LIGHTCYAN_EX + f'\n┌── <{username_pc}@exalty> ─ [Second Menu]')
    
    choice = input('└──╼ $ ' + Fore.LIGHTWHITE_EX)
    
    if choice == '28':
        run_tool("token_checker")
        os.system("pause")
        second_menu_function()
    elif choice == '29':
        run_tool("token_login")
        os.system("pause")
        second_menu_function()
    elif choice == '30':  
        run_tool("token_info")
    elif choice == "B":
        main()
    elif choice == "E":
        sys.exit()
    else:
        print(Fore.RED + "[x] | Invalid choice in second menu.")
        os.system("pause")
        second_menu_function()

main()
