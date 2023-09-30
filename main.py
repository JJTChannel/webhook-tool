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


def webhookspamming(webhook,name,message):
    while True:
        try:
            url = f"https://bfstc.xyz/api/proxy.php"
            proxy = requests.get(url).text
            print(f"{cy}Proxie Granted!: {l}{proxy}")
            session = requests.Session()
            session.proxies = {
                "http": proxy,
                "https": proxy
            }
            session.post(webhook,json={"username": name,"content": message})
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
                      \_____ https://discord.gg/HUhgrny78k  Press Enter To Start"""
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
    name = input(F"{cy}USER{w}NAME : ")
    thread = int(input(f"{g}THR{w}EAD : "))
    am = 0
    print(f"{r}Sta{w}tus : {g}Waiting For API..")
    sleep(1)
    System.Title(f"Buffalo Store - Status : Spamming To {webhook}")
    for i in range(thread):
        print("\n")
        threading.Thread(target=webhookspamming(webhook,name,message)).start()

def deletew():
    print(Center.Center(rainbowbanner))
    webhook = input(F"{g}WEB{w}HOOK : ")
    delete(webhook)
    print(f"{b}Deleted {webhook}!!")
    sleep(1)
    Anime.Fade(Center.Center(rainbowbanner), Colors.red_to_blue, Colorate.Vertical, enter=True)
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
