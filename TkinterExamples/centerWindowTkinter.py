"""
Mr. Davis
Quick Demo on Centering your UI

"""

import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry('960x540') # defaults the top left corner to 100, 100
#root.geometry('960x540+0+0')
#root.geometry('960x540+960+540')
#root.geometry(f'{int(screen_width/2)}x{int(screen_height/2)}'+ "+0+0")
print(f'{int(screen_width/2)}x{int(screen_height/2)}' + "+100+300")

root.mainloop()