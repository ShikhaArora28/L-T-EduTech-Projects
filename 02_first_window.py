import tkinter as tk

root = tk.Tk()
root.mainloop()
root.title("Test")
print("Window ready")

root.title("My First App")
root.geometry("400x250")
root.config(bg="lightblue")
root.resizable(True, True)
root.mainloop()

def say_hello():
    print("Button Clicked!")
root.title("Button")
root.geometry("300x450")

# root.title("Labels")
# root.geometry("400x250")

title = tk.Label(root, text="Welcome to My Company! ", font=("Arial",18,"bold"), fg="navy")
title.pack(pady=20)
info = tk.Label(root, text="Hello Everyone", bg="lightgreen", padx=10, pady=5)
info.pack()
btn = tk.Button(root, text="Click me",command=say_hello)
btn.pack(pady=40)
root.mainloop()

count = 0

def add_one():
    global count
    count = count + 1
    label.config(text=f"Clicks: {count}")

root = tk.Tk()
root.title("Click Counter")
label = tk.Label(root, text="Clicks: 0", font=("Arial", 20))
label.pack(pady=20)
tk.Button(root, text="Click me", command=add_one).pack()

root.mainloop()