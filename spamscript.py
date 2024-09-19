import pyautogui
import time


message = input("Enter the message you want to spam send: ")
repetitions = int(input("Enter the number of repetitions: "))

print("You have 5 seconds to switch to the target application...")
time.sleep(5)


for _ in range(repetitions):
    pyautogui.write(message)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(0.1)

print("Finished sending messages.")