"""
Mr. Davis
All the Different Widgets in Tkinter
https://www.studytonight.com/tkinter/python-tkinter-widgets

Helpful Links for Understanding
https://www.tutorialspoint.com/python/tk_button.htm
https://www.tutorialspoint.com/python/tk_cursors.htm
https://www.tutorialspoint.com/python/tk_relief.htm

Advanced GUI topics
https://stackoverflow.com/questions/44099594/how-to-make-a-tkinter-canvas-rectangle-with-rounded-corners
https://www.geeksforgeeks.org/transparent-window-in-tkinter/
"""
import tkinter as tk
#from tkinter import *
from PIL import Image, ImageTk
rainbow = ["red", "orange", "yellow", "green", "blue", "blueviolet", "indigo"]
root = tk.Tk()
root.geometry("800x600")
#root.geometry("1920x1080")
#root.attributes('-fullscreen', True)
#root.resizable(width=False, height=False)
root.title("This is NOT my First GUI")
root.config(bg="crimson")
root.config(cursor="spider")
#root.config(highlightcolor="skyblue")
myDogImage = ImageTk.PhotoImage(file="dog50x50.png")

#var = tk.StringVar()
#label = tk.Label(root, textvariable=var, font=('Arial', 18), bg="purple")
label = tk.Label(root, text="Basic Way", font=('Arial', 18), bg="purple")
#var.set("Is it me you're looking for?")
label.pack(padx="20", pady="10")

textbox = tk.Text(root, height=3, font=('Comicsans', 14), bg="#a4a4a4", fg="#E817B5")
textbox.pack(padx=20)

myEntry = tk.Entry(root, font=('Helvetica', 18), bg="skyblue", fg="crimson")
myEntry.pack(pady=1)

myButton1 = tk.Button(root, text ="I'm the first Button", bg="blue", fg="white", relief="flat")
#relief is the STYLE of button. Options are raised, sunken,flat, groove, ridge
myButton1.pack()

myButton2 = tk.Button(root, text ="I'm the second BUTTON", activebackground="blue", activeforeground="white", relief="sunken")
myButton2.pack(pady=2)
#myButton2.pack(side="left")

myButton3 = tk.Button(root, text ="Change Me", relief="groove", bg="blue", fg="white",activebackground="white", activeforeground="blue")
myButton3.pack(pady=4)
#myButton3.pack(side="right")

#myButton4 = tk.Button(root, image=myDogImage)
#myButton4 = tk.Button(root, image=smallerDogImage)

#myButton4 = tk.Button(root, image=myDogImage, borderwidth=0)
myButton4 = tk.Button(root, image=myDogImage, borderwidth=0, bg="crimson")

myButton4.pack()

frameForAllMyButtons = tk.Frame(root, bg ="pink")

frameForAllMyButtons.columnconfigure(0, weight=1)
frameForAllMyButtons.columnconfigure(1, weight=1)
frameForAllMyButtons.columnconfigure(2, weight=1)

btn1 = tk.Button(frameForAllMyButtons, text="1")
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(frameForAllMyButtons, text="2")
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(frameForAllMyButtons, text="3")
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(frameForAllMyButtons, text="1")
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(frameForAllMyButtons, text="2")
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(frameForAllMyButtons, text="3")
btn6.grid(row=1, column=2)

lbl7 = tk.Label(frameForAllMyButtons, text="Whatever")
lbl7.grid(row=2, column=2, sticky=tk.W+tk.E)
frameForAllMyButtons.pack(fill='x')

canvas1 = tk.Canvas(root, bg="ghostwhite")
canvas1.pack(padx=5, pady=5)

checkbut1 = tk.Checkbutton(root, text = "Homepage",
                         onvalue = 1,
                         offvalue = 0,
                         height = 2,
                         width = 10)

checkbut2 = tk.Checkbutton(root, text = "Tutorials",
                         onvalue = 1,
                         offvalue = 0,
                         height = 2,
                         width = 10)

checkbut3 = tk.Checkbutton(root, text = "Contactus",
                         onvalue = 1,
                         offvalue = 0,
                         height = 2,
                         width = 10)

checkbut1.pack()
checkbut2.pack()
checkbut3.pack()

root.mainloop()