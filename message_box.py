import tkinter as tk
from tkinter import messagebox
def info():
    messagebox.showinfo("Saved", "Your file was saved.")
def warning():
    messagebox.showwarning("Carefull", "The file is very large.")
def error():
    messagebox.showerror("Error", "Could not open the file.")
root = tk.Tk()
root.geometry("500x250")
root.title("MESSAGE BOX")
tk.Button(root, text = "Info", width = 12, command = info).pack(pady = 5)
tk.Button(root, text = "Warning", width = 12, command = warning).pack(pady = 5)
tk.Button(root, text = "Error", width = 12, command = error).pack(pady = 5)
root.mainloop()