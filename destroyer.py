import shutil
import os
import time
from colorama import Fore, Style, init
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("Win Destroyer")

init()

print(f"""
{Fore.BLUE}
██╗    ██╗██╗███╗   ██╗    ██████╗ ███████╗███████╗████████╗██████╗  ██████╗ ██╗   ██╗███████╗██████╗ 
██║    ██║██║████╗  ██║    ██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║██║██╔██╗ ██║    ██║  ██║█████╗  ███████╗   ██║   ██████╔╝██║   ██║ ╚████╔╝ █████╗  ██████╔╝
██║███╗██║██║██║╚██╗██║    ██║  ██║██╔══╝  ╚════██║   ██║   ██╔══██╗██║   ██║  ╚██╔╝  ██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║ ╚████║    ██████╔╝███████╗███████║   ██║   ██║  ██║╚██████╔╝   ██║   ███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
{Fore.CYAN}
| By H64Ox
| GitHub repository: https://github.com/H64Ox/WinDestroyer
""")

time.sleep(1)

start = input(f"{Fore.RED}Are you sure you want to proceed? (this will destroy your system!) [yes / no] ")

while True:
    if start.lower() == 'no':
        print(f"{Fore.CYAN}OK, cancelling operation.")
        time.sleep(1)
        break
    elif start.lower() == 'yes':
        confirm = input(f"{Fore.RED}Please confirm you want to proceed [yes / no] ")

        while True:
            if confirm.lower() == 'no':
                print(f"{Fore.CYAN}OK, cancelling operation.")
                time.sleep(1)
                break
            elif confirm.lower() == 'yes':
                print(f"{Fore.RED}Removing System32...")
                shutil.rmtree(r"C:\Windows\System32\\", ignore_errors=True)
                print(f"{Fore.CYAN}Done! Restarting PC...")
                os.system("shutdown /r /t 1")
                break
            else:
                confirm = input(f"{Fore.RED}Invalid answer. Please try again [yes / no] ")
        break
    else:
        start = input(f"{Fore.RED}Invalid answer. Please try again [yes / no] ")
