import tkinter as tk
def greet():
    name = name_box.get()
    message.config(text=f"Hello, {name}!")

root = tk.Tk()
root.title("Greeter")
root.geometry("500x500")
root.config(bg="lightgreen")
tk.Label(root, text="Type your name:").pack(pady=5)
name_box = tk.Entry(root, width = 25)
name_box.pack()
btn = tk.Button(root, text="Greet me", command=greet)
btn.pack()
message = tk.Label(root, font = ("Arial", 26), fg = "blue")
message.pack()
root.mainloop()