import tkinter as tk
root = tk.Tk()
root.title("pack() demo")
root.geometry("360x200")

tk.Label(root, text="TOP", bg="tomato", width=10).pack(side="top", pady=15)
tk.Label(root, text="LEFT", bg="blue", width=10).pack(side="left", padx=15)
tk.Label(root, text="RIGHT", bg="green", width=10).pack(side="right", padx=15)
root.mainloop()