import tkinter as tk

# Create object
root = tk.Tk()

# Adjust size
root.geometry("800x600")

# Change the label text
def changeLabel(anyLabel):
	anyLabel.config( text = strForOptionMenus1.get() )

# The List for the dropdown
options1 = [
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday"
]

# datatype of menu text
strForOptionMenus1 = tk.StringVar()
strForOptionMenus2 = tk.StringVar()


# initial menu text
strForOptionMenus1.set(options1[0])
strForOptionMenus2.set("42")


# Create Dropdown menu
# regMenu = tk.Menu(root,clicked, *options1 )
# regMenu.pack(anchor="nw")



# Create 2 different drop down menus
opMenu1 = tk.OptionMenu(root, strForOptionMenus1, *options1 )
opMenu1.pack(anchor="nw")
#opMenu1.pack(anchor="nw", side=tk.LEFT)

#opMenu2 = tk.OptionMenu(root,strForOptionMenus2, "this", "is", "the", "basic", "way" )
#opMenu2.pack(anchor="nw")
#opMenu2.pack(anchor="nw", side=tk.LEFT)


# Create button, it will change label text
btn1 = tk.Button(root, text = "click Me", command = lambda:changeLabel(lbl1) )
btn1.pack()

# Create Label
lbl1 = tk.Label(root, text= " " )
lbl1.pack()

# Mouse Events
def high_alpha(e):
    root.attributes('-alpha', 1)

def low_alpha(e):
    root.attributes('-alpha', 0.75)

lbl1.bind("<Button-1>", high_alpha)
lbl1.bind("<Button-3>", low_alpha)


# Execute tkinter
root.mainloop()
