import tkinter as tk
from tkinter import messagebox
def new_file():
    print("New File clicked")
def about():
    messagebox.showinfo("About", "My first menu app")
root = tk.Tk()
root.title("MENU")
root.config(bg ="lightblue")
root.geometry("400x300")
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)  #tearoff ?
file_menu.add_command(label="New", command = new_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command = root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=about)
#help_menu.add_separator()
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)
root.mainloop()