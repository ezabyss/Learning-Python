from tkinter import *
from time import strftime
clock = Tk()
clock.title("Digital Clock")




lbl= Label(clock,font="arial 160 bold", bg="black", fg="orange")
lbl.pack(anchor="center", fill="both", expand="yes")

def time():
    string=strftime("%H:%M:%S %p") # %p is for pm or am
    lbl.config(text=string)
    lbl.after(1000,time) # it changes the  value in 1000 milisecond

time() 
mainloop()