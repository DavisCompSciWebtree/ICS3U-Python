import tkinter as tk
#from tkinter import *

root = tk.Tk()

root.mainloop()

class MyGUI:

    def __int__(self):

        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your Messages", font=('Arial', 18))
        self.label.pack(padx = 10, pady=10)

