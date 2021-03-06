from tkinter import *
from tkinter import messagebox
import math

window=Tk()

window.geometry('500x700')
window.title("CALCULATOR")
window.configure(bg='#a6a6a6')


input=StringVar()
operator=''
#================================================functions==============================================================

def click_button(numbers):                                                                                      #functions for inputs
    global operator
    operator=operator+str(numbers)
    input.set(operator)

def equal_button():                                                                                           #function for Addition
    global operator
    add=str(eval(operator))
    input.set(add)
    operator=''

def equal_button():                                                                                        #function for substraction
    global operator
    sub=str(eval(operator))
    input.set(sub)
    operator=''

def equal_button():                                                                                       #function for multiplication
    global operator
    mul=str(eval(operator))
    input.set(mul)
    operator=''

def equal_button():                                                                                         #function for division
    global operator
    try:
        div = str(eval(operator))
        input.set(div)
        operator = ''
    except:messagebox.showinfo(title = "Error", message = "ooopsss!!! Please check the input.", )


def clr_button():                                                                                              #function for clear
    global operator
    operator=""
    input.set("")

def delete():                                                                                                 #function for delete
    global operator
    operator = operator[: -1]
    input.set(operator)

#=============================================Scientific mode===========================================================

def sin_Button():                                                                                                #function for sin
    global operator
    try:
        sin = float(operator)
        value = math.sin(math.radians(sin))
        operator = str(value)
        input.set(value)
    except:messagebox.showinfo(title="Error",message="First enter the number you want and then enter sin ")

def cos_Button():                                                                                                 #function for cos
    global operator
    try:
        sin = float(operator)
        value = math.cos(math.radians(sin))
        operator = str(value)
        input.set(value)
    except:
        messagebox.showinfo(title="Error", message="First enter the number you want and then enter cos ")

def tan_Button():                                                                                                #function for tan
    global operator
    try:
        sin = float(operator)
        value = math.tan(math.radians(sin))
        operator = str(value)
        input.set(value)
    except:
        messagebox.showinfo(title="Error", message="First enter the number you want and then enter tan ")

def square():                                                                                                     #function for square
    global operator
    try:
        square = int(operator)
        value = (square ** 2)
        operator = str(value)
        input.set(value)
    except:
        messagebox.showinfo(title="Error", message="First enter the number you want and then enter x^2 ")

def square_root():                                                                                             #function  for square root
    global operator
    try:
        square_root = float(operator)
        value = math.sqrt(square_root)
        operator = str(value)
        input.set(value)
    except:
        messagebox.showinfo(title="Error", message=u"First enter the number you want and then enter \u221A ")

def cube():                                                                                                        #function for cube
    global operator
    try:
        cube = int(operator)
        value = (cube ** 3)
        operator = str(value)
        input.set(value)
    except:
        messagebox.showinfo(title="Error", message="First enter the number you want and then enter x^3 ")

def log_base2():                                                                                            #function for log to base 2
    global operator
    try:
        log_base2 = float(operator)
        value = math.log2(log_base2)
        operator = str(value)
        input.set(value)
    except:
        messagebox.showinfo(title="Error", message="First enter the number you want and then enter log2(a) ")

def log_base10():                                                                                             #function for log to base 10
    global operator
    try:
        log_base10 = float(operator)
        value = math.log10(log_base10)
        operator = str(value)
        input.set(value)
    except:
        messagebox.showinfo(title="Error", message="First enter the number you want and then enter log10(a) ")

def exponential():                                                                                             #function for exponent
    global operator
    try:
        exponential = float(operator)
        value = math.exp(exponential)
        operator = str(value)
        input.set(value)
    except:
        messagebox.showinfo(title="Error", message="First enter the number you want and then enter e ")

def fact():                                                                                                      #function for factorial
    global operator
    try:
        fact = float(operator)
        value = math.factorial(fact)
        operator = str(value)
        input.set(value)
    except:
        messagebox.showinfo(title="Error", message="First enter the number you want and then enter fact")

def radian():                                                                                                    #function for radians
    global operator
    try:
        radian = float(operator)
        value = math.radians(radian)
        operator = str(value)
        input.set(value)
    except:
        messagebox.showinfo(title="Error", message="First enter the number you want and then enter rad ")

def absolute():                                                                                                  #function for absolute
    global operator
    try:
        absolute = float(operator)
        value = math.fabs(absolute)
        operator = str(value)
        input.set(value)
    except:
        messagebox.showinfo(title="Error", message="First enter the number you want and then enter abs")

#======================================output=========================================================================

output=Entry(window,textvariable=input,font=("lucida 40 bold"),bd=30,insertwidth=4,bg='#41f06f',justify='right')
output.pack()

#======================================Buttons==========================================================================

button1=Button(window,text="1",width=7,height=3,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),                  #from 1 -9 buttons
               command=lambda:click_button(1))
button1.place(x=60,y=340,)

button2=Button(window,text="2",width=7,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),
               command=lambda:click_button(2))
button2.place(x=160,y=340)

button3=Button(window,text="3",width=7,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),
               command=lambda:click_button(3))
button3.place(x=260,y=340)

button4=Button(window,text="4",width=7,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),
               command=lambda:click_button(4))
button4.place(x=60,y=270)

button5=Button(window,text="5",width=7,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),
               command=lambda:click_button(5))
button5.place(x=160,y=270)

button6=Button(window,text="6",width=7,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),
               command=lambda:click_button(6))
button6.place(x=260,y=270)

button7=Button(window,text="7",width=7,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),
               command=lambda:click_button(7))
button7.place(x=60,y=200)

button8=Button(window,text="8",width=7,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),
               command=lambda:click_button(8))
button8.place(x=160,y=200)

button9=Button(window,text="9",width=7,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),
               command=lambda:click_button(9))
button9.place(x=260,y=200)

button_minus=Button(window,text="-",width=7,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),            #minus button
                    command=lambda:click_button('-'))
button_minus.place(x=360,y=130)

button_multiply=Button(window,text="x",width=7,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),         #multiply button
                       command=lambda:click_button('*'))
button_multiply.place(x=260,y=130)

button_delete=Button(window,text="DEL",width=7,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),         #delete button
                       command=delete)
button_delete.place(x=160,y=130)

button_clear=Button(window,text="C",width=7,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),            #Clear Button
                    command=clr_button)
button_clear.place(x=60,y=130)

button_equals=Button(window,text="=",width=7,height=8,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),            #Equal Button
                     command=equal_button)
button_equals.place(x=360,y=340)

button0=Button(window,text="0",width=22,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),                #zero button
               command=lambda:click_button(0))
button0.place(x=60,y=410)

button_point=Button(window,text=".",width=7,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),            #point button
                    command=lambda:click_button('.'))
button_point.place(x=260,y=410)

button_plus=Button(window,text="+",width=7,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),             #plus button
                   command=lambda:click_button('+'))
button_plus.place(x=360,y=200)

button_division=Button(window,text="/",width=7,height=3 ,bd=8 ,fg='black',bg='#41f06f' ,font=("lucida 9 bold"),         #division button
                   command=lambda:click_button('/'))
button_division.place(x=360,y=270)

#=======================================scientific mode================================================================

button_sin=Button(window,text="Sin",width=7,height=3 ,bd=8 ,fg='black',bg='#32a852' ,font=("lucida 9 bold"),            #sin button
               command=sin_Button)
button_sin.place(x=60,y=480)

button_cos=Button(window,text="Cos",width=7,height=3 ,bd=8 ,fg='black',bg='#32a852' ,font=("lucida 9 bold"),            #cos button
               command=cos_Button)
button_cos.place(x=160,y=480)

button_tan=Button(window,text="Tan",width=7,height=3 ,bd=8 ,fg='black',bg='#32a852' ,font=("lucida 9 bold"),            #tan button
               command=tan_Button)
button_tan.place(x=260,y=480)

button_square=Button(window,text="x^2",width=7,height=3 ,bd=8 ,fg='black',bg='#32a852' ,font=("lucida 9 bold"),         #square button
                   command=square)
button_square.place(x=360,y=480)

button_sqrt=Button(window,text=u"\u221A",width=7,height=3 ,bd=8 ,fg='black',bg='#32a852' ,font=("lucida 9 bold"),       #square root button
               command=square_root)
button_sqrt.place(x=60,y=550)

button_cube=Button(window,text="x^3",width=7,height=3 ,bd=8 ,fg='black',bg='#32a852' ,font=("lucida 9 bold"),           #cube button
               command=cube)
button_cube.place(x=160,y=550)

button_absolute=Button(window,text="abs",width=7,height=3 ,bd=8 ,fg='black',bg='#32a852' ,font=("lucida 9 bold"),       #absolute button
               command=absolute)
button_absolute.place(x=260,y=550)

button_log_base10=Button(window,text="log10(a)",width=7,height=3 ,bd=8 ,fg='black',bg='#32a852' ,font=("lucida 9 bold"),#log base 10 button
                   command=log_base10)
button_log_base10.place(x=360,y=550)

button_exponent=Button(window,text="e",width=7,height=3 ,bd=8 ,fg='black',bg='#32a852' ,font=("lucida 9 bold"),         #exponential button
               command=exponential)
button_exponent.place(x=60,y=620)

button_factorial=Button(window,text="fact",width=7,height=3 ,bd=8 ,fg='black',bg='#32a852' ,font=("lucida 9 bold"),     #factorial button
               command=fact)
button_factorial.place(x=160,y=620)

button_radian=Button(window,text="rad",width=7,height=3 ,bd=8 ,fg='black',bg='#32a852' ,font=("lucida 9 bold"),         #radian button
               command=radian)
button_radian.place(x=260,y=620)

button_log_base2=Button(window,text="log2(a)",width=7,height=3 ,bd=8 ,fg='black',bg='#32a852' ,font=("lucida 9 bold"),  #log base 2 button
                   command=log_base2)
button_log_base2.place(x=360,y=620)

window.mainloop()