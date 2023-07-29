import tkinter as tk
import datetime
import winsound

def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S %p")
    time_label.config(text="Current Time: " + current_time)
    window.after(1000, update_time)

def set_alarm():
    global alarm_time
    alarm_time = entry.get()
    alarm_label.config(text="Alarm Time: " + alarm_time)
    remaining_time()

def remaining_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_diff = datetime.datetime.strptime(alarm_time, "%H:%M") - datetime.datetime.strptime(current_time, "%H:%M:%S")
    remaining_label.config(text="Remaining Time: " + str(time_diff))
    
    if datetime.datetime.now().strftime("%H:%M") >= alarm_time:
        play_alarm()
    else:
        window.after(1000, remaining_time)

def play_alarm():
    # Play a sound when the alarm goes off
    frequency = 2500  # Set frequency (range: 37-32767 Hz)
    duration = 2000  # Set duration in milliseconds
    winsound.Beep(frequency, duration)

# Create the GUI window
window = tk.Tk()
window.title("Alarm Clock")

# Create a label for current time
time_label = tk.Label(window, text="Current Time: ")
time_label.pack()

# Create a label and entry for the alarm time
alarm_label = tk.Label(window, text="Alarm Time: ")
alarm_label.pack()

entry = tk.Entry(window)
entry.pack()

# Create a label to display remaining time for the alarm
remaining_label = tk.Label(window, text="Remaining Time: ")
remaining_label.pack()

# Create a button to set the alarm
button = tk.Button(window, text="Set Alarm", command=set_alarm)
button.pack()

# Update the time every second
update_time()

# Start the GUI event loop
window.mainloop()
