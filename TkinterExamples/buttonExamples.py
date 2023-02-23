import tkinter as tk

root = tk.Tk()
root.geometry("1200x900")

#Making a Label Widget
lbl1 = tk.Label(root, text="This will change when you click ANY button", bg="violet")
lbl1.pack(padx=4, pady=4, side=tk.TOP)

#Making a Button Widget the "slow" way
#Learn the difference between side and anchor
btn1 = tk.Button(root, text="This is btn1", font=('Helvetica', 24), command= lambda:changeTheLabel(lbl1))
btn1.pack(padx=4, pady=4, side=tk.LEFT)
#btn1.pack(padx=4, pady=4, anchor="nw")

#Making Buttons the 'fast way'
buttonList =[]
for x in range(0, 10):
    buttonList.append(tk.Button(root, text=f"{x}", width = 10))
    buttonList[x].pack(padx=4, pady=4, side=tk.RIGHT)
    #buttonList[x].pack(padx=4, pady=4, anchor="ne")

#first time seeing a function/method
def changeTheLabel(anyWidgetWithText):
    anyWidgetWithText.configure(text="hi")


root.mainloop()