from requests import post,delete
from re import search
import requests
from colorama import Fore
from os import system
import random
from time import sleep
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import threading


System.Title("Buffalo Store - Status : loading")

l = Fore.LIGHTRED_EX
r = Fore.RED
y = Fore.YELLOW
g = Fore.GREEN
cy = Fore.CYAN
b = Fore.BLUE
w = Fore.WHITE

countries = ["TH","US","AU","SG","UK"]

def webhookspamming(webhook,name,message):
    try:
        url = f"http://pubproxy.com/api/proxy?limit=1&format=txt&http=true&country={random.choice(countries)}&type=http&post=true"
        print(f"{b}Getting Proxies From: {r}{url}")
        proxy = requests.get(url).text
        session = requests.Session()
        session.proxies = {
            "http": proxy,
            "https": proxy
        }
        session.post(webhook,json={"username": name,"content": message})
        print(f"{l}Status: {g}Succeed")
    except:
        try:
            post(webhook,json={"username": name,"content": message})
            print(f"{l}Status: {g}Succeed")
        except:
            print(f"{l}Status: {r}Error")

banner = F"""

██████╗░██╗░░░██╗███████╗███████╗░█████╗░██╗░░░░░░█████╗░  ░██████╗████████╗░█████╗░██████╗░███████╗
██╔══██╗██║░░░██║██╔════╝██╔════╝██╔══██╗██║░░░░░██╔══██╗  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
██████╦╝██║░░░██║█████╗░░█████╗░░███████║██║░░░░░██║░░██║  ╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░
██╔══██╗██║░░░██║██╔══╝░░██╔══╝░░██╔══██║██║░░░░░██║░░██║  ░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░
██████╦╝╚██████╔╝██║░░░░░██║░░░░░██║░░██║███████╗╚█████╔╝  ██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗
╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░░╚═╝╚══════╝░╚════╝░  ╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝
                      \_____ https://discord.gg/znSSzHnNQj  Press Enter To Start"""
bannersucceed = F"""
                            Spam Succeeded!

██████╗░██╗░░░██╗███████╗███████╗░█████╗░██╗░░░░░░█████╗░  ░██████╗████████╗░█████╗░██████╗░███████╗
██╔══██╗██║░░░██║██╔════╝██╔════╝██╔══██╗██║░░░░░██╔══██╗  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
██████╦╝██║░░░██║█████╗░░█████╗░░███████║██║░░░░░██║░░██║  ╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░
██╔══██╗██║░░░██║██╔══╝░░██╔══╝░░██╔══██║██║░░░░░██║░░██║  ░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░
██████╦╝╚██████╔╝██║░░░░░██║░░░░░██║░░██║███████╗╚█████╔╝  ██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗
╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░░╚═╝╚══════╝░╚════╝░  ╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝
                     \_____ https://discord.gg/znSSzHnNQj  Press Enter To Use Again"""
rainbowbanner = F"""{Fore.LIGHTRED_EX}
██████╗░██╗░░░██╗███████╗███████╗░█████╗░██╗░░░░░░█████╗░  ░██████╗████████╗░█████╗░██████╗░███████╗
{Fore.RED}██╔══██╗██║░░░██║██╔════╝██╔════╝██╔══██╗██║░░░░░██╔══██╗  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
{Fore.YELLOW}██████╦╝██║░░░██║█████╗░░█████╗░░███████║██║░░░░░██║░░██║  ╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░
{Fore.GREEN}██╔══██╗██║░░░██║██╔══╝░░██╔══╝░░██╔══██║██║░░░░░██║░░██║  ░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░
{Fore.CYAN}██████╦╝╚██████╔╝██║░░░░░██║░░░░░██║░░██║███████╗╚█████╔╝  ██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗
{Fore.BLUE}╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░░╚═╝╚══════╝░╚════╝░  ╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝
"""
Anime.Fade(Center.Center(banner), Colors.red_to_blue, Colorate.Vertical, enter=True)
system("clear||cls")
print(Center.Center(rainbowbanner))
def spam():
    webhook = input(F"{g}WEB{w}HOOK : ")
    message = input(F"{r}MESS{w}AGE : ")
    name = input(F"{r}USER{w}NAME : ")
    amount = int(input(f"{y}AMO{w}UNT : "))
    delay = int(input(f"{b}DE{w}lay : "))
    am = 0
    print(f"{r}Sta{w}tus : {g}Waiting For API..")
    sleep(1)
    System.Title(f"Buffalo Store - Status : Spamming To {webhook}")
    for i in range(amount):
        print("\n")
        sleep(delay)
        threading.Thread(target=webhookspamming(webhook,name,message)).start()
        am = am + 1
        print(f"{b}Spamming {r}Round : ({str(am)}/{str(amount)}){g}")
        print("\n")
        System.Title(f"Buffalo Store - Status : Spamming To {webhook} - Round : ({str(am)}/{str(amount)})")
    sleep(1)
    System.Title(f"Buffalo Store - Status : Succeed Spam To {webhook} - Amount {amount}")
    print(f"Succeed Spam To {webhook} - Amount {amount}")
    system("clear||cls")
    Anime.Fade(Center.Center(bannersucceed), Colors.red_to_blue, Colorate.Vertical, enter=True)
    System.Title(f"Buffalo Store - Status : Loading...")
    sleep(1)
    System.Title("Buffalo Store - Status : Waiting For Spaming")
    system("clear||cls")
    print(Center.Center(rainbowbanner))
    run()

def deletew():
    print(Center.Center(rainbowbanner))
    webhook = input(F"{g}WEB{w}HOOK : ")
    delete(webhook)
    print(f"{b}Deleted {webhook}!!")
    sleep(1)
    Anime.Fade(Center.Center(bannersucceed), Colors.red_to_blue, Colorate.Vertical, enter=True)
    System.Title(f"Buffalo Store - Status : Loading...")
    sleep(1)
    System.Title("Buffalo Store - Status : Waiting For Spaming")
    system("clear||cls")
    print(Center.Center(rainbowbanner))
    run()

def run():
    print(f"""
    
    \_ {cy}1 = Spam Webhook {g}2 = Delete Webhook _/
    """)
    INPUT = input(f"  {r}CHO{w}ICE: ")
    if INPUT == "1":
        system("clear||cls")
        spam()
    elif INPUT == "2":
        system("clear||cls")
        deletew()
    else:
        system("clear||cls")
        print(Center.Center(rainbowbanner))
        run()

run()
