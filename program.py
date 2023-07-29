import tkinter as tk
import datetime
import winsound

class AlarmClockApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Alarm Clock")
        self.alarm_time = None

        # Create a label for current time
        self.time_label = tk.Label(self.window, text="Current Time: ")
        self.time_label.pack()

        # Create a label and entry for the alarm time
        self.alarm_label = tk.Label(self.window, text="Alarm Time: ")
        self.alarm_label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        # Create a label to display remaining time for the alarm
        self.remaining_label = tk.Label(self.window, text="Remaining Time: ")
        self.remaining_label.pack()

        # Create a button to set the alarm
        self.button = tk.Button(self.window, text="Set Alarm", command=self.set_alarm)
        self.button.pack()

        # Update the time every second
        self.update_time()

        # Start the GUI event loop
        self.window.mainloop()

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S %p")
        self.time_label.config(text="Current Time: " + current_time)
        self.window.after(1000, self.update_time)

    def set_alarm(self):
        self.alarm_time = self.entry.get()
        self.alarm_label.config(text="Alarm Time: " + self.alarm_time)
        self.remaining_time()

    def remaining_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time_diff = datetime.datetime.strptime(self.alarm_time, "%H:%M") - datetime.datetime.strptime(current_time, "%H:%M:%S")
        self.remaining_label.config(text="Remaining Time: " + str(time_diff))
        
        if datetime.datetime.now().strftime("%H:%M") >= self.alarm_time:
            self.play_alarm()
        else:
            self.window.after(1000, self.remaining_time)

    def play_alarm(self):
        # Play a sound when the alarm goes off
        frequency = 2500  # Set frequency (range: 37-32767 Hz)
        duration = 2000  # Set duration in milliseconds
        winsound.Beep(frequency, duration)

if __name__ == "__main__":
    app = AlarmClockApp()
