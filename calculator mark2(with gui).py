import tkinter as tk
from functools import partial
#____________________________________________________________
def add(label1,n1,n2 ):
    num1=(n1.get())
    num2= (n2.get())
    result=int(num1)+int(num2)
    label.config(text='result is %d'%result)
def sub(label1,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    res=int(num1)-int(num2)
    lebel.config(text='result is %d'%res)
def mul(label1,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    res=int(num1)*int(num2)
    label.config(text='result is %d'%res)
def div(label1,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    res=int(num1)/int(num2)
    label.config(text='result is %d'%res)
def mod(label1,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    res=int(num1)%int(num2)
    label.config(text='result is %d'%res)
#------------------------------------------------------------------
root=tk.Tk()
root.geometry('400x200+100+200')#geometry of dialog box
#The first two parameters are the width and height of the window.
#The last two parameters are x and y screen coordinates.
root.title('calculator mark 2 ')#title of the dialog box
number1=tk.StringVar()# variables to enter values by user
number2 = tk.StringVar()
#------------------------------------------------------------------
labelTitle=tk.Label(root,text='enter your values below').grid(row=0,column=2)
#-------------------------------------------------------------------
labelNum1=tk.Label(root,text='enter a number').grid(row=1,column=0)
labelNum2=tk.Label(root,text='enter another number').grid(row=2,column=0)
#-----------------------------------------------------------------------------
labelResult=tk.Label(root)# for result
labelResult.grid(row=7,column=2)
#----------------------------------------------------------------------------
entryNum1=tk.Entry(root,textvariable=number1).grid(row=1,column=2)# for inputs
entryNum2=tk.Entry(root,textvariable=number2).grid(row=2,column=2)
#------------------------------------------------------------------------------
add= partial(add,labelResult,number1,number2)
mul= partial(mul,labelResult,number1,number2)
sub= partial(sub,labelResult,number1,number2)
div=partial(div,labelResult,number1,number2)
mod=partial(mod,labelResult,number1,number2)
#==============================================
button=tk.Button(root, text="Add", command=add).grid(row=3, column=1)
button=tk.Button(root, text="Multiply", command=mul).grid(row=3, column=2)
button=tk.Button(root,text="Subtract",command=sub).grid(row=3,column=3)
button=tk.Button(root,text="Divide",command=div).grid(row=4,column=1)
button=tk.Button(root,text="Modulas",command=mod).grid(row=4,column=2)
root.mainloop()

































