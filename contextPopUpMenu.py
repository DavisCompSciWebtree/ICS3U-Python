import tkinter as tk

def show_menu(event):
    menu.post(event.x_root, event.y_root)

root = tk.Tk()

menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Option 1")
menu.add_command(label="Option 2")
menu.add_separator()
menu.add_command(label="Quit", command=root.quit)

button = tk.Button(root, text="Right-click for menu")
button.pack()

button.bind("<Button-3>", show_menu)  # bind the right mouse button to show the menu

root.mainloop()
