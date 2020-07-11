from tkinter import *

window=Tk()

window.geometry('500x500')
window.title("CALCULATOR")


input=StringVar()
operator=''

def click_button(numbers):#functions for inputs
    global operator
    operator=operator+str(numbers)
    input.set(operator)

def equal_button():#function for Addition
    global operator
    add=str(eval(operator))
    input.set(add)
    operator=''

def equal_button():#function for substraction
    global operator
    sub=str(eval(operator))
    input.set(sub)
    operator=''

def equal_button():#function for multiplication
    global operator
    mul=str(eval(operator))
    input.set(mul)
    operator=''

def equal_button():#function for division
    global operator
    div=str(eval(operator))
    input.set(div)
    operator=''


def clr_button():#function for clear
    global operator
    operator=""
    input.set("")

#output entry
output=Entry(window,textvariable=input,font=("lucida 40 bold"),bd=30,insertwidth=4,bg='powderblue',justify='right')
output.pack()
#Buttons
button1=Button(window,text="1",width=5,height=3 ,command=lambda:click_button(1))
button1.place(x=10,y=310,)
button2=Button(window,text="2",width=5,height=3 ,command=lambda:click_button(2))
button2.place(x=70,y=310)
button3=Button(window,text="3",width=5,height=3 ,command=lambda:click_button(3))
button3.place(x=130,y=310)
button4=Button(window,text="4",width=5,height=3 ,command=lambda:click_button(4))
button4.place(x=10,y=240)
button5=Button(window,text="5",width=5,height=3 ,command=lambda:click_button(5))
button5.place(x=70,y=240)
button6=Button(window,text="6",width=5,height=3 ,command=lambda:click_button(6))
button6.place(x=130,y=240)
button7=Button(window,text="7",width=5,height=3 ,command=lambda:click_button(7))
button7.place(x=10,y=170)
button8=Button(window,text="8",width=5,height=3 ,command=lambda:click_button(8))
button8.place(x=70,y=170)
button9=Button(window,text="9",width=5,height=3 ,command=lambda:click_button(9))
button9.place(x=130,y=170)
button_minus=Button(window,text="-",width=5,height=3 ,command=lambda:click_button('-'))
button_minus.place(x=200,y=100)
button_multiply=Button(window,text="x",width=5,height=3 ,command=lambda:click_button('*'))
button_multiply.place(x=130,y=100)
button_division=Button(window,text="/",width=5,height=3 ,command=lambda:click_button('/'))
button_division.place(x=70,y=100)
button_clear=Button(window,text="clear",width=5,height=3 ,command=clr_button) #Clear Button
button_clear.place(x=10,y=100)
button_equals=Button(window,text="=",width=5,height=8,command=equal_button) # Equal Button
button_equals.place(x=200,y=310)
button0=Button(window,text="0",width=14,height=3 ,command=lambda:click_button(0))
button0.place(x=10,y=380)
button_point=Button(window,text=".",width=5,height=3 ,command=lambda:click_button('.'))
button_point.place(x=130,y=380)
button_plus=Button(window,text="+",width=5,height=8 ,command=lambda:click_button('+'))
button_plus.place(x=200,y=170)


























window.mainloop()