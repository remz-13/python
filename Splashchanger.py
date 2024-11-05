import os
import requests
from PIL import Image
from io import BytesIO
import winsound
import time
import sys
import ctypes
from colorama import Fore, Style, init


def require_admin():
    if not ctypes.windll.shell32.IsUserAnAdmin():

        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
        sys.exit()


require_admin()

init(autoreset=True)

os.system('title splash changer lol')

correct_key = 'eac'

def verify():
    try:
        print(f"""
{Fore.RED}::::::::::     :::      ::::::::  {Style.RESET_ALL}
{Fore.RED}:+:          :+: :+:   :+:    :+: {Style.RESET_ALL}
{Fore.YELLOW}+:+         +:+   +:+  +:+        {Style.RESET_ALL}
{Fore.YELLOW}+#++:++#   +#++:++#++: +#+        {Style.RESET_ALL}
{Fore.GREEN}+#+        +#+     +#+ +#+       {Style.RESET_ALL} 
{Fore.GREEN}#+#        #+#     #+# #+#    #+# {Style.RESET_ALL}
{Fore.BLUE}########## ###     ###  ######## """)
        
        key = input(f"input the key: {Style.RESET_ALL}")

        if key == correct_key:
            print(f"{Fore.GREEN}valid ;^){Style.RESET_ALL}")
            time.sleep(2)
            os.system('cls')
            image_url = input(Fore.BLUE + "Input your EAC (Fortnite) SplashScreen URL: " + Style.RESET_ALL)
            os.system('cls')
            image_url = input(Fore.BLUE + "Input your Fortnite Splash Image URL: " + Style.RESET_ALL)
            os.system('cls')
            frequency = 500
            duration = 650


            splash_dir = r"E:\Fortnite\FortniteGame\Content\Splash"
            save_directory = r"E:/Fortnite/FortniteGame/Binaries/Win64/EasyAntiCheat"
            save_path = os.path.join(splash_dir, "Splash.bmp")
            save_sigma = os.path.join(save_directory, "SplashScreen.png")


            os.makedirs(save_directory, exist_ok=True)


            os.system('cls')


            response = requests.get(image_url)
            if response.status_code == 200:

                image = Image.open(BytesIO(response.content))
                resized_image = image.resize((800, 450))
                grayscale_image = resized_image.convert("L")


                winsound.Beep(frequency, duration)


                grayscale_image.save(save_sigma)


                resized_image = image.resize((640, 738))
                grayscale_image = resized_image.convert("L")
                grayscale_image.save(save_path)

                print(f"""
        [+] 'Splash.bmp' file created!
        [+] 'SplashScreen.png' file created!
        [+] Place 'SplashScreen.png' in {save_sigma}!
        [+] Place 'Splash.bmp' in {save_path}!
                """)
                time.sleep(2)
                os.system('cls')
                print(f"{Fore.GREEN}[+] Photo injection - [success!]{Style.RESET_ALL}")
                time.sleep(2)
                os.system('cls')
                input("Press Enter to exit")
                return True
            else:
                print("Image could not be retrieved. Check the URL and try again.")
                return False

        else:
            print("Wrong key, please try again...")
            return False

    except Exception as e:
        print("Something went wrong, please try again...")
        print(f"Error details: {e}")

# Run the verify function
verify()
