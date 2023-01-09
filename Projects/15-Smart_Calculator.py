from tkinter import *

screen = Tk() 
screen.geometry('1000x650')
screen.title("SMART CALCULATOR")
screen.configure(background="orange")

def add(x,y):
    return x+y
def sub(x,y):
    return x-y 
def mul(x,y):
    return x*y 
def div(x,y):
    return x/y
def mod(x,y):
    return x%y
def lcm(x,y):
    L = x if x > y else y 
    while L <= x*y:
        if L%x==0 and L%y==0:
            return L
        L=L+1

def hcf(x,y):
    H = x if x<y else y
    while  H>=1 :
        if x % H==0 and x % H==0:
            return H
        H -= 1

operations= {'+':add, 'add':add, 'sum': add, 'plus':add, 'sub': sub, 'difference':sub,'-':sub, 'minus':sub, 'lcm':lcm, 'hcf':hcf,'*':mul, 'product':mul, 'multiply':mul, '/':div, 'div':div, 'mod':mod, '%':mod}

def extract_from_text(text):
    values= []
    for word in text.split(' '):
        try:
            float(word)          #tries to convert into a float
            values.append(float(word))
        except ValueError: 
            pass                #ignores if it cannot convert word to a float
    return values




def calculate():
    text= txt_input.get()
    for word in text.split(' '):
        if word.lower() in operations.keys():
            try:
                num = extract_from_text(text)
                r = operations[word.lower()](num[0],num[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,"Sorry! Please Try Again")
            finally:
                break
        else:
            list.delete(0,END)
            list.insert(END,"Sorry! Please Try Again")


lbl_hi = Label(screen,text="HELLO THERE! Smart calculator Here !!", font="Roberto 12 bold", width=30, padx=4)
#lbl_hi.place(x=150,y=10)
lbl_hi.place(relx=0.5,rely=0.05, anchor=CENTER) # adjust relative to window 

lbl_ask = Label(screen,text="How can i help you? ", font="Roberto 15 bold", width=30, padx=4)
lbl_ask.place(relx=0.5, rely=0.25, anchor=CENTER)

txt_input = StringVar()
txt_box = Entry(screen, width=65, textvariable=txt_input)
txt_box.place(relx=0.5, rely=0.5, anchor=CENTER)


btn_calc = Button(screen, text="Calculate",font="Roberto 15 bold", command=calculate)
btn_calc.place(relx=0.5, rely=0.7, anchor=CENTER)

list = Listbox(screen, width=40, height=5)
list.place(relx=0.5, rely=0.9, anchor=CENTER)



screen.mainloop()