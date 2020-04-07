from tkinter import *
import tkinter

window =Tk()
window.title("Calculator")
window.resizable(0,0)

input = Entry(window , width = 50, borderwidth = 5 )
input.grid(row=0 , column=0 , columnspan = 3)

def Button_Click(num):
   previous = input.get()
   input.delete(0, END)
   input.insert(0 ,(previous+num))

def Button_Clear():
    input.delete(0, END)

def Button_Add():

    global x
    x=0
    global firstadd
    firstadd=float((input.get()))
    input.delete(0,END)

def Button_Subtract():
    global x ,firstsub
    x = 1
    firstsub = float((input.get()))
    input.delete(0, END)

def Button_Multiply():
    global x, firstmult
    x = 2
    firstmult = float((input.get()))
    input.delete(0, END)

def Button_Divide():
    global x, firstdiv
    x = 3
    firstdiv = float((input.get()))
    input.delete(0, END)

def Button_Equals():

    if x==0:
        global secondnum
        secondnum = float(input.get())
        input.delete(0, END)
        input.insert(0, firstadd + secondnum)
    elif x==1 :
        secondnum = float(input.get())
        input.delete(0, END)
        input.insert(0, firstsub - secondnum)
    elif x==2:
        secondnum = float(input.get())
        input.delete(0, END)
        input.insert(0, firstmult * secondnum)
    elif x==3 :
        secondnum = float(input.get())
        input.delete(0, END)
        input.insert(0, float(firstdiv / secondnum))

#Creating the buttons
Button_1 = Button(window , text="1",padx = 40  , pady= 20,  command = lambda :Button_Click("1"))
Button_2 = Button(window , text="2" ,padx = 40  , pady= 20,command= lambda :Button_Click("2"))
Button_3 = Button(window , text="3"  ,padx = 40  , pady= 20,command= lambda :Button_Click("3"))
Button_4 = Button(window , text="4" ,padx = 40  , pady= 20,command= lambda :Button_Click("4"))
Button_5 = Button(window , text="5" ,padx = 40  , pady= 20,command= lambda :Button_Click("5"))
Button_6 = Button(window , text="6" ,padx = 40  , pady= 20,command= lambda :Button_Click("6"))
Button_7 = Button(window , text="7" ,padx = 40  , pady= 20,command= lambda :Button_Click("7"))
Button_8 = Button(window , text="8" ,padx = 40  , pady= 20,command= lambda :Button_Click("8"))
Button_9 = Button(window , text="9" ,padx = 40  , pady= 20,command= lambda :Button_Click("9"))
Button_0 = Button(window , text="0" ,padx = 40  , pady= 20,command= lambda :Button_Click("0"))
Button_Clear = Button(window , text="Clear" ,padx = 79  , pady= 20,command= Button_Clear)
Button_Equal = Button(window , text="=" ,padx = 90  , pady= 20,command= Button_Equals)
Button_Plus = Button(window , text="+" ,padx = 40  , pady= 20,command= Button_Add)
Button_Subtract = Button(window , text="-" ,padx = 40  , pady= 20,command= Button_Subtract)
Button_Multiply = Button(window , text="x" ,padx = 40  , pady= 20,command= Button_Multiply)
Button_Divide=Button(window , text="/" ,padx = 40  , pady= 20,command= Button_Divide)

#Adding the buttons on the screen
Button_1.grid(row= 3, column =0)
Button_2.grid(row= 3, column =1)
Button_3.grid(row= 3, column =2)

Button_4.grid(row=2 , column =0)
Button_5.grid(row= 2, column =1)
Button_6.grid(row= 2, column =2)

Button_7.grid(row=1 , column =0)
Button_8.grid(row= 1, column =1)
Button_9.grid(row= 1, column =2)

Button_0.grid(row=4 , column =0)
Button_Multiply.grid(row=4 , column =1)
Button_Divide.grid(row=4 , column =2)

Button_Equal.grid(row= 6, column =1 , columnspan= 2)
Button_Subtract.grid(row =6 ,column =0)

Button_Plus.grid(row= 5, column =0)

Button_Clear.grid(row=5 ,column = 1, columnspan =2)

window.mainloop()
