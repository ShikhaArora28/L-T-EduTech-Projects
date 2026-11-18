import tkinter as tk

def check():
    marks = int(marks_box.get())
    if marks >= 40:
        result.config(text = "PASS", bg = "green")
    else:
        result.config(text = "FAIL", bg = "red")
root = tk.Tk()
root.geometry("400x250")
root.config(bg="lightblue")
root.resizable(True, True)
root.title("RESULT CHECKER")
tk.Label(root, text = "Enter marks:").pack(pady = 5)
marks_box = tk.Entry(root, width = 10)
marks_box.pack()
tk.Button(root, text = "Check", command = check).pack(pady = 8)
result = tk.Label(root, text = "?", fg = "white", bg = "gray",
                   font = ("Arial", 20, "bold"), width = 8)
result.pack(pady = 10)
root.mainloop()