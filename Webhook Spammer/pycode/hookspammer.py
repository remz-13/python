# start of the hookspammer code made by 0x7ffc13cbbd50
import requests
import time
from colorama import Fore, Style, init
import os

init()

def greeting(): # defines a function called greeting
    os.system('title HookSpammer - made by 0x7ffc13cbbd50') # changes the title of the console window
    os.system("cls") # clears the console for the first time of many
    print(f"""{Fore.BLUE}
                                __             __                                      
                               / /  ___  ___  / /__  ___ ___  ___ ___ _  __ _  ___ ____
                              / _ \/ _ \/ _ \/  '_/ (_-</ _ \/ _ `/  ' \/  ' \/ -_) __/ 
                             /_//_/\___/\___/_/\_\ /___/ .__/\_,_/_/_/_/_/_/_/\__/_/   
                                                      /_/                              
                                                    :)
                                            made by 0x7ffc13cbbd50{Style.RESET_ALL}""") # some cool ascii 
    print("Welcome to HookSpammer! This tool will spam a message to a discord webhook of your choice.\n")
    input(f"{Fore.CYAN}press enter to enter the rabbit hole...{Style.RESET_ALL}")
    os.system("cls") # clears the console
    print("loading...") # little loading animation
    time.sleep(3) # sleeps for 3 secs
    os.system("cls") # clears the console again.

greeting() # calls the greeting function we just defined ^

def send_webhook_message(webhook_url, message, repeat): # sending messages through the webhook url provided by the user
    payload = {"content": message}
    headers = {"Content-Type": "application/json"}
    
    for _ in range(repeat):
        response = requests.post(webhook_url, json=payload, headers=headers)
        
        if response.status_code in [200, 204]:
            print(f"{Fore.GREEN}sent successfully!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Failed to send message. Status code: {response.status_code}, Response: {response.text}{Style.RESET_ALL} Pausing for a second before spamming again due to rate limits.")
            time.sleep(1.5)         

def delete_webhook(webhook_url): # deletes the webhook after spamming - its optional which is quite cool if you are wanting to troll the scammer/webhook user a bit more.
    response = requests.delete(webhook_url)
    
    if response.status_codein [200, 204]:
        print(f"{Fore.GREEN}webhook deleted successfully.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Failed to delete webhook. Status code: {response.status_code}, Response: {response.text}{Style.RESET_ALL}")

webhook_url = input("Input the webhook url you would like to spam -> ") # initialising variables with inputs
message = input("what message would you like to spam? -> ")
repeat = int(input("how many times would you like to send the message? -> ")) # requires an integer input

send_webhook_message(webhook_url, message, repeat)

delete_option = input("would you like to delete the webhook you provided? (y/n): ").strip().lower() # strips whitespace and converts to lowercase letters
if delete_option == "y": # checks the user for the input of yes, they want to delete the webhook
    delete_webhook(webhook_url)
else:
    print(f"{Fore.RED}webhook not deleted.{Style.RESET_ALL}")