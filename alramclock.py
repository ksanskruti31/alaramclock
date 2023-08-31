import tkinter as tk
import time
import threading
from tkinter import messagebox

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")

        self.time_label = tk.Label(root, text="Set Alarm Time (HH:MM):")
        self.time_label.pack()

        self.time_entry = tk.Entry(root)
        self.time_entry.pack()

        self.set_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack()

        self.stop_button = tk.Button(root, text="Stop Alarm", command=self.stop_alarm, state=tk.DISABLED)
        self.stop_button.pack()

        self.alarm_thread = None

    def set_alarm(self):
        alarm_time = self.time_entry.get()
        try:
            hours, minutes = map(int, alarm_time.split(":"))
            if 0 <= hours < 24 and 0 <= minutes < 60:
                current_time = time.localtime()
                alarm_seconds = hours * 3600 + minutes * 60
                current_seconds = current_time.tm_hour * 3600 + current_time.tm_min * 60 + current_time.tm_sec
                time_to_alarm = alarm_seconds - current_seconds

                if time_to_alarm > 0:
                    self.set_button.config(state=tk.DISABLED)
                    self.stop_button.config(state=tk.NORMAL)
                    self.alarm_thread = threading.Timer(time_to_alarm, self.trigger_alarm)
                    self.alarm_thread.start()
                else:
                    messagebox.showerror("Error", "Please enter a future time.")

            else:
                messagebox.showerror("Error", "Invalid time format.")

        except ValueError:
            messagebox.showerror("Error", "Invalid time format.")

    def trigger_alarm(self):
        self.set_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.alarm_thread = None
        messagebox.showinfo("Alarm", "Wake up!")

    def stop_alarm(self):
        if self.alarm_thread:
            self.alarm_thread.cancel()
            self.alarm_thread = None
            self.set_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()
