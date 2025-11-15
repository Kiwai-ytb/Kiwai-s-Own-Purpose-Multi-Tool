import os, requests
from colorama import Fore, Style
from pystyle import Colors, Colorate
from Utilities import banner, resize_and_center_console

# IP Tracker handling
def IpTracker(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}?fields=28533759")
    data = response.json()
    if data["status"] == "success":
        print(f"    {Fore.GREEN}[+]{Style.RESET_ALL} IP {ip} Tracked successfuly, Here's the infos:\n")
        print(f"    IP Address: {data['query']}")
        print(f"    Continent: {data['continent']} [{data['continentCode']}]")
        print(f"    Country: {data['country']} [{data['countryCode']}]")
        print(f"    Region/State: {data['regionName']} [{data['region']}]")
        print(f"    City: {data['city']}")
        print(f"    Zip: {data['zip']}")
        print(f"    Latitude: {data['lat']}")
        print(f"    Longitude: {data['lon']}")
        print(f"    Timezone: {data['timezone']}")
        print(f"    Currency: {data['currency']}")
        print(f"    ISP: {data['isp']}\n")
        print(f"    Mobile?: {(Fore.GREEN if data['mobile'] else Fore.RED)}{data['mobile']}{Style.RESET_ALL}")
        print(f"    Proxy?: {(Fore.GREEN if data['proxy'] else Fore.RED)}{data['proxy']}{Style.RESET_ALL}")
        print(f"    Hosting?: {(Fore.GREEN if data['hosting'] else Fore.RED)}{data['hosting']}{Style.RESET_ALL}\n")
        print(f"    URL: https://www.google.com/maps?q={data['lat']},{data["lon"]}")
    elif data["status"] == "fail":
        print(f"    {Fore.RED}[-]{Style.RESET_ALL} Error: {response.status_code}, text: {response.text}")
    input("\n    Press Enter to go Back...")

# Banners
IPTRACKER_BANNER = Colorate.Diagonal(Colors.green_to_blue, r"""
     ___ ___   _____            _           
    |_ _| _ \ |_   _| _ __ _ __| |_____ _ _ 
     | ||  _/   | || '_/ _` / _| / / -_) '_|
    |___|_|     |_||_| \__,_\__|_\_\___|_|  

    ========================================

    [B] To go Back
    [*] Or Enter the IP Address
""", 1)

IPTRACKERSMALL_BANNER = Colorate.Diagonal(Colors.green_to_blue, r"""
     ___ ___   _____            _           
    |_ _| _ \ |_   _| _ __ _ __| |_____ _ _ 
     | ||  _/   | || '_/ _` / _| / / -_) '_|
    |___|_|     |_||_| \__,_\__|_\_\___|_|  

    ========================================
""", 1)

# Menu
def ipTracker_menu():
    while True:
        resize_and_center_console(150, 32)
        os.system("cls")
        os.system("title IP Tracker -- Made by Kiwai")
        banner(IPTRACKER_BANNER)
        choice = input("    > ").strip()
        if choice.lower() == "b":
            break
        elif choice:
            banner(IPTRACKERSMALL_BANNER)
            IpTracker(choice)
        else:
            banner(IPTRACKER_BANNER)
            print(f"    {Fore.RED}[-]{Style.RESET_ALL} Invalid IP.")
            input("\n    Press Enter to go back...")