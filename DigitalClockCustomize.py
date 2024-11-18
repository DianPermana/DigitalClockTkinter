import tkinter as tk
from tkinter import font
import time

# Function to update the time
def update_time():
    current_time = time.strftime("%H:%M:%S")
    label_clock.config(text=current_time)
    root.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock Using tkinter — Python interface to Tcl/Tk")
root.geometry("400x250")
root.resizable(False, False)
root.configure(bg="#1e1e2f")  # Background color

# Create a custom font
clock_font = font.Font(family="Helvetica", size=60, weight="bold")
date_font = font.Font(family="Helvetica", size=20, weight="normal")

# Digital clock label
label_clock = tk.Label(root, text="", font=clock_font, bg="#1e1e2f", fg="#61dafb")
label_clock.pack(pady=20)

# Date label
label_date = tk.Label(
    root, 
    text=time.strftime("%A, %d %B %Y"), 
    font=date_font, 
    bg="#1e1e2f", 
    fg="#61dafb"
)
label_date.pack()

# Label fot static weather
label_weather = tk.Label(
    root,
    text="Bandung: 25°C, Rain",  # Contoh data cuaca statis
    font=label_clock,
    bg="#1e1e2f",
    fg="#61dafb"
)
label_weather.pack(pady=10)

# Start the clock
update_time()

# Run the application
root.mainloop()
