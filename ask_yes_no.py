import tkinter as tk
from tkinter import messagebox
def quit_app():
    answer = messagebox.askyesno("Exit", "Do you really want to exit?")
    if answer:
        root.destroy()
root = tk.Tk()
root.title("ASK YES OR NO")
root.geometry("200x150")
root.config(bg = "lightgreen")
tk.Button(root, text = "Exit", bg = "lightblue", command = quit_app).pack(pady = 50)
root.mainloop()