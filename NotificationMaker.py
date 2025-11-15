import os
from win10toast import ToastNotifier
from Utilities import banner
from colorama import Fore, Style
from pystyle import Colors, Colorate

def create_notification():
    toast = ToastNotifier()
    title = input("    Title of the Notification: ")
    message = input("    Message of the Notification: ")
    icon = input("    Path to the icon of the Notification (leave empty if None): ")
    try:
        if icon == "":
            icon = None
        toast.show_toast(title=title, msg=message, icon_path=icon, duration=5)
        print(f"\n    {Fore.GREEN}[+]{Style.RESET_ALL} Notification Sent!")
    except Exception as e:
        print(f"\n    {Fore.RED}[-]{Style.RESET_ALL} An error occured while sending the notification: {e}")

# Banners
NOTIFICATIONMAKER_BANNER = Colorate.Diagonal(Colors.white_to_red, r"""
     _  _     _   _  __ _         _   _            __  __      _    
    | \| |___| |_(_)/ _(_)__ __ _| |_(_)___ _ _   |  \/  |__ _| |_____ _ _ 
    | .` / _ |  _| |  _| / _/ _` |  _| / _ | ' \  | |\/| / _` | / / -_| '_|
    |_|\_\___/\__|_|_| |_\__\__,_|\__|_\___|_||_| |_|  |_\__,_|_\_\___|_|

    =======================================================================

    [1] Create a Notification
    [B] Back to Main Menu
""", 1)

NOTIFICATIONMAKERSMALL_BANNER = Colorate.Diagonal(Colors.white_to_red, r"""
     _  _     _   _  __ _         _   _            __  __      _    
    | \| |___| |_(_)/ _(_)__ __ _| |_(_)___ _ _   |  \/  |__ _| |_____ _ _ 
    | .` / _ |  _| |  _| / _/ _` |  _| / _ | ' \  | |\/| / _` | / / -_| '_|
    |_|\_\___/\__|_|_| |_\__\__,_|\__|_\___|_||_| |_|  |_\__,_|_\_\___|_|

    =======================================================================
""", 1)

# Menu
def notificationMaker_menu():
    while True:
        os.system("cls")
        os.system("title Notification Maker -- Made by Kiwai")
        banner(NOTIFICATIONMAKER_BANNER)
        choice = input("    > ").strip().lower()
        if choice == "1":
            banner(NOTIFICATIONMAKERSMALL_BANNER)
            create_notification()
        elif choice == "b":
            break
        else:
            banner(NOTIFICATIONMAKER_BANNER)
            print(f"    {Fore.RED}[-]{Style.RESET_ALL} Invalid choice.")
        input("\n    Press Enter to continue...")