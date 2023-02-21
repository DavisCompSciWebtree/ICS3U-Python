"""
Mr. Davis
https://www.tutorialspoint.com/python/tk_button.htm
https://www.tutorialspoint.com/python/tk_cursors.htm
https://www.tutorialspoint.com/python/tk_relief.htm
https://stackoverflow.com/questions/44099594/how-to-make-a-tkinter-canvas-rectangle-with-rounded-corners
https://coderslegacy.com/python/tkinter-config/

"""
import tkinter as tk
#from tkinter import *
#from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("800x500")
#root.resizable(width=False, height=False)
root.title("My First GUI")
root.config(bg="crimson")
#root.config(cursor="spider")
#root.config(highlightcolor="skyblue")
#myDogImage = ImageTk.PhotoImage(file="dog.png")
#smallerDogImage= myDogImage.zoom(20, 20)

var = tk.StringVar()
label = tk.Label(root, textvariable=var, font=('Arial', 18), bg="purple")
#label = tk.Label(root, text="Basic Way", font=('Arial', 18), bg="purple")

var.set("Is it me you're looking for?")
label.pack(padx="20", pady="40")

textbox = tk.Text(root, height=3, font=('Arial', 14), bg="#a4a4a4", fg="#E817B5")
textbox.pack(padx=20)

myEntry = tk.Entry(root)
myEntry.pack(pady=1)

myButton1 = tk.Button(root, text ="I'm the first Button", bg="blue", fg="white", relief="raised")
myButton1.pack()

myButton2 = tk.Button(root, text ="I'm the second BUTTON", activebackground="blue", activeforeground="white")
myButton2.pack(pady=2)
#myButton2.pack(side="left")

myButton3 = tk.Button(root, text ="Change Me")
myButton3.pack(pady=4)
#myButton3.pack(side="right")

#myButton4 = tk.Button(root, image=myDogImage)
#myButton4 = tk.Button(root, image=smallerDogImage)

#myButton4 = tk.Button(root, image=myDogImage, borderwidth=0)
#myButton4.pack()

frameForAllMyButtons = tk.Frame(root)

frameForAllMyButtons.columnconfigure(0, weight=1)
frameForAllMyButtons.columnconfigure(1, weight=1)
frameForAllMyButtons.columnconfigure(2, weight=1)

btn1 = tk.Button(frameForAllMyButtons, text="1")
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

frameForAllMyButtons.pack(fill='x')




root.mainloop()