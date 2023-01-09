# tkinter
# tcalendar
from tkinter import *
from tkcalendar import *
import datetime
root = Tk()
root.title("Calendar")
root.geometry("500x300")

cal = Calendar(root, year=2022,month=1,day=5)
cal.pack(pady=30)

root.mainloop()