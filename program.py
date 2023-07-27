import tkinter as tk
import datetime
import time
import winsound




def set_alarm():
    alarm_time = entry.get()
    label=tk.Label(window,text="Alarm is set to "+str(alarm_time))
    label.pack()
    while True:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        
        if current_time == alarm_time:
 
            play_alarm()
            break

def play_alarm():
    # Play a sound when the alarm goes off
    frequency = 2500  # Set frequency (range: 37-32767 Hz)
    duration = 2000  # Set duration in milliseconds
    winsound.Beep(frequency, duration)

# Create the GUI window
window = tk.Tk()
window.title("Alarm Clock")

# Create a label and entry for the alarm time

label = tk.Label(window, text="Enter alarm time (HH:MM):")
label.pack()

entry = tk.Entry(window,)
entry.pack()

# Create a button to set the alarm
button = tk.Button(window, text="Set Alarm", command=set_alarm)
button.pack()

# Start the GUI event loop
window.mainloop()
