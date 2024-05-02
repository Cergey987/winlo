import tkinter as tk
from tkinter import *
root=Tk()
root = tk.Tk()
root.configure(background="#000000")
label = tk.Label(root, text="Введи ключ и нажми ctrl+c", background="#000000",fg="red",font=("Arial", 15, "bold"))
label.place(relx=0.5, rely=0.4, anchor="center")
text=tk.Entry(root)
text.place(relx=0.5, rely=0.5, anchor="center")

root.withdraw()

root.deiconify()
root.after(1000)
root.attributes('-fullscreen', True)
root.title("Программа")
root.mainloop()
