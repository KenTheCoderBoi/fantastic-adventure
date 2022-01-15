from tkinter import *
import random
root=Tk()
root.geometry("600x600")
root.title("sus")
colors=["red","blue","green","yellow","orange"]
def change():
    root.configure(bg=colors[random.randint(0,4)])
btn= Button(root, text="change",command=change)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()