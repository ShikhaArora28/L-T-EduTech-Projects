import tkinter as tk
root = tk.Tk()
root.title("LIVE PREVIEW")

name = tk.StringVar()
tk.Entry(root, textvariable=name, width = 25).pack(pady = 10)
tk.Label(root, textvariable=name, font = ("Arial", 18), fg = "blue").pack(pady = 10)
root.mainloop()