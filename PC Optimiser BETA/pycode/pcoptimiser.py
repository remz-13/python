import os
import psutil
import shutil
import winsound  # Windows-only
import sys
import cpuinfo
import customtkinter as ctk
from tkinter import messagebox, simpledialog
from threading import Thread
import time
import requests
import hashlib
from colorama import Fore, Style, init
import getpass  # More reliable than os.getlogin()

init()

key_correct = "1"  # Replace with your actual key


def print_username():
    username = getpass.getuser()
    print(f"{username}")


def clear():
    os.system('cls')


def start():
    os.system('mode 68, 10')
    os.system('title cleaner by remz ~ beta')
    print("Hello, ", end=""), print_username(), print("Welcome to remz pc cleaner.")
    input(f"{Fore.CYAN}press enter to get started.{Style.RESET_ALL}")
    time.sleep(2)
    os.system('cls')


def beep():
    frequency = 400
    duration = 800
    winsound.Beep(frequency, duration)


def get_specs():
    try:
        cpu = cpuinfo.get_cpu_info()
        ram = psutil.virtual_memory()
        disk = shutil.disk_usage('/')
        specs = {
            "CPU": cpu.get('brand_raw', 'Unknown CPU'),
            "Cores": psutil.cpu_count(logical=False),
            "Threads": psutil.cpu_count(logical=True),
            "RAM": f"{round(ram.total / (1024 ** 3), 2)} GB",
            "Disk Space": f"Total: {round(disk.total / (1024 ** 3), 2)} GB, Free: {round(disk.free / (1024 ** 3), 2)} GB"
        }
    except Exception:
        specs = {
            "CPU": "Error fetching CPU info",
            "Cores": "N/A",
            "Threads": "N/A",
            "RAM": "Error fetching RAM info",
            "Disk Space": "Error fetching disk info"
        }
    return specs


def clean_temp_files():
    temp_dirs = [os.environ.get('TEMP'), os.environ.get('TMP')]
    total_deleted = 0
    errors = []
    for temp_dir in temp_dirs:
        if temp_dir:
            try:
                for root, dirs, files in os.walk(temp_dir):
                    for name in files:
                        file_path = os.path.join(root, name)
                        try:
                            total_deleted += os.path.getsize(file_path)
                            os.remove(file_path)
                        except Exception as e:
                            errors.append(str(e))
            except Exception as e:
                errors.append(str(e))
    messagebox.showinfo("Clean Up", f"Deleted {round(total_deleted / (1024 ** 2), 2)} MB of temporary files.")


def defrag_disk():
    try:
        os.system('defrag C:')
        messagebox.showinfo("Disk Defragmenter", "Disk defragmentation completed.")
    except Exception as e:
        messagebox.showerror("Disk Defragmenter", f"Error during defragmentation: {str(e)}")


def terminate_unnecessary_processes():
    critical_processes = ["explorer.exe", "svchost.exe", "winlogon.exe"]
    terminated = 0
    try:
        for proc in psutil.process_iter():
            if proc.name().lower() not in critical_processes and proc.name() != "System Idle Process":
                proc.terminate()
                terminated += 1
    except Exception as e:
        messagebox.showerror("Error", f"Error while terminating processes: {str(e)}")
    messagebox.showinfo("Process Manager", f"Terminated {terminated} unnecessary processes.")


def refresh_data(cpu_label, ram_label):
    while True:
        try:
            cpu_usage = psutil.cpu_percent()
            ram = psutil.virtual_memory()
            cpu_label.configure(text=f"CPU Usage: {cpu_usage}%")
            ram_label.configure(text=f"RAM Usage: {ram.percent}%")
        except Exception:
            cpu_label.configure(text="Error fetching CPU usage")
            ram_label.configure(text="Error fetching RAM usage")
        time.sleep(1)


class PCOptimizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PC Cleaner & Optimizer")
        self.geometry("600x600")
        self.init_ui()

    def init_ui(self):
        specs = get_specs()
        specs_text = "\n".join([f"{k}: {v}" for k, v in specs.items()])
        specs_label = ctk.CTkLabel(self, text=f"System Specifications:\n{specs_text}", justify="left")
        specs_label.pack(pady=10)

        self.cpu_label = ctk.CTkLabel(self, text="CPU Usage: --", font=("Arial", 14))
        self.cpu_label.pack(pady=5)

        self.ram_label = ctk.CTkLabel(self, text="RAM Usage: --", font=("Arial", 14))
        self.ram_label.pack(pady=5)

        clean_button = ctk.CTkButton(self, text="Clean Temp Files", command=clean_temp_files)
        clean_button.pack(pady=10)

        defrag_button = ctk.CTkButton(self, text="Defragment Disk", command=defrag_disk)
        defrag_button.pack(pady=10)

        terminate_button = ctk.CTkButton(self, text="Terminate Processes", command=terminate_unnecessary_processes)
        terminate_button.pack(pady=10)

        exit_button = ctk.CTkButton(self, text="Exit", command=self.destroy)
        exit_button.pack(pady=10)

        refresh_thread = Thread(target=refresh_data, args=(self.cpu_label, self.ram_label), daemon=True)
        refresh_thread.start()


if __name__ == "__main__":
    start()
    key = input(f"{Fore.BLUE}Password: {Style.RESET_ALL}")
    if key == key_correct:
        beep()
        clear()
        try:
            app = PCOptimizerApp()
            app.mainloop()
        except Exception as e:
            print(f"{Fore.RED}Failed to launch GUI: {e}{Style.RESET_ALL}")
            sys.exit(1)
    else:
        print(f"{Fore.RED}Invalid Password. Exiting...{Style.RESET_ALL}")
        time.sleep(2)
        sys.exit(1)
