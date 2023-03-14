from requests import post,delete
from re import search
from colorama import Fore
from os import system
from time import sleep
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

System.Title("JJTxStore - Status : loading")

l = Fore.LIGHTRED_EX
r = Fore.RED
y = Fore.YELLOW
g = Fore.GREEN
cy = Fore.CYAN
b = Fore.BLUE
w = Fore.WHITE

banner = F"""
░░░░░██╗░░░░░██╗████████╗██╗░░██╗░██████╗████████╗░█████╗░██████╗░███████╗
░░░░░██║░░░░░██║╚══██╔══╝╚██╗██╔╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
░░░░░██║░░░░░██║░░░██║░░░░╚███╔╝░╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░
██╗░░██║██╗░░██║░░░██║░░░░██╔██╗░░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░
╚█████╔╝╚█████╔╝░░░██║░░░██╔╝╚██╗██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗
░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝
                        Press Enter To Start"""
bannersucceed = F"""
                            Spam Succeeded!

░░░░░██╗░░░░░██╗████████╗██╗░░██╗░██████╗████████╗░█████╗░██████╗░███████╗
░░░░░██║░░░░░██║╚══██╔══╝╚██╗██╔╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
░░░░░██║░░░░░██║░░░██║░░░░╚███╔╝░╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░
██╗░░██║██╗░░██║░░░██║░░░░██╔██╗░░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░
╚█████╔╝╚█████╔╝░░░██║░░░██╔╝╚██╗██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗
░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝
                        Press Enter To Use Again"""
rainbowbanner = F"""{Fore.LIGHTRED_EX}
░░░░░██╗░░░░░██╗████████╗██╗░░██╗░██████╗████████╗░█████╗░██████╗░███████╗
{Fore.RED}░░░░░██║░░░░░██║╚══██╔══╝╚██╗██╔╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
{Fore.YELLOW}░░░░░██║░░░░░██║░░░██║░░░░╚███╔╝░╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░
{Fore.GREEN}██╗░░██║██╗░░██║░░░██║░░░░██╔██╗░░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░
{Fore.CYAN}╚█████╔╝╚█████╔╝░░░██║░░░██╔╝╚██╗██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗
{Fore.BLUE}░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝
"""
Anime.Fade(Center.Center(banner), Colors.red_to_blue, Colorate.Vertical, enter=True)
system("clear||cls")
print(Center.Center(rainbowbanner))
def spam():
    webhook = input(F"{g}WEB{w}HOOK : ")
    message = input(F"{r}MESS{w}AGE : ")
    name = input(F"{r}USER{w}NAME : ")
    amount = int(input(f"{y}AMO{w}UNT : "))
    am = 0
    print(f"{r}Sta{w}tus : {g}Waiting..")
    sleep(1)
    System.Title(f"JJTxStore - Status : Spamming To {webhook}")
    for i in range(amount):
        post(webhook,json={"username": name,"content": message})
        am = am + 1
        print(f"{b}Spamming to {g}-- {w}{webhook} {g}-- {r}Round : ({str(am)}/{str(amount)}){g}")
        System.Title(f"JJTxStore - Status : Spamming To {webhook} - Round : ({str(am)}/{str(amount)})")
    sleep(1)
    System.Title(f"JJTxStore - Status : Succeed Spam To {webhook} - Amount {amount}")
    print(f"Succeed Spam To {webhook} - Amount {amount}")
    system("clear||cls")
    Anime.Fade(Center.Center(bannersucceed), Colors.red_to_blue, Colorate.Vertical, enter=True)
    System.Title(f"JJTxStore - Status : Loading...")
    sleep(1)
    System.Title("JJTxStore - Status : Waiting For Spaming")
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
    System.Title(f"JJTxStore - Status : Loading...")
    sleep(1)
    System.Title("JJTxStore - Status : Waiting For Spaming")
    system("clear||cls")
    print(Center.Center(rainbowbanner))
    run()

def run():
    print(f"""{cy}1 = Spam Webhook {g}2 = Delete Webhook""")
    INPUT = input("")
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
