import tkinter as tk
root = tk.Tk()
def login():
    if user_box.get() == "admin" and pass_box.get() == "1234":
        status.config(text = "Welcome!", fg = "lightgreen")
    else:
        status.config(text = "Wrong username or password!", fg = "red")
root.title("Login")
tk.Label(root, text = "Username").grid(row = 0,column = 0,padx = 10,pady = 8)
user_box=tk.Entry(root)
user_box.grid(row = 0,column = 1,padx = 10)
tk.Label(root, text="Password").grid(row = 1,column = 0,padx = 10,pady = 8)
pass_box=tk.Entry(root,show = "*")
pass_box.grid(row = 1,column = 1,padx = 10)
tk.Button(root, text = "Login",command = login).grid(row = 2,column = 1,sticky = "e", padx = 10)
status=tk.Label(root, text = "")
status.grid(row=3, column = 0, columnspan = 2, pady = 8)
root.mainloop()