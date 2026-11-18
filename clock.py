import time
import tkinter as tk
def tick():
    now = time.strftime("%H:%M:%S")
    clock.config(text=now)
    root.after(1000, tick)
root = tk.Tk()
root.title("CLOCK")
clock = tk.Label(root, font = ("Arial", 36, "bold"), fg = "navy")
clock.pack(padx = 30, pady = 20)
tick()
root.mainloop()