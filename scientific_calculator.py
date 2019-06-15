from tkinter import *
import parser
import math
import os
root = Tk()
root.title("Scientific Calculator")


i=0
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1
def clear_all():
    display.delete(0,END)
def get_operator(operator):
    global i
    length=len(operator)
    display.insert(i,operator)
    i+=length
def calculate():
    entire_string=display.get()
    try:
        a=parser.expr(entire_string).compile()
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")
def factorial():
    entire_string=display.get()
    l=len(entire_string)
    if(l):
        x=int(entire_string[l-1],10)
        fact=math.factorial(x)
        undo()
        display.insert(i,fact)
def trisin():
    entire_string=display.get()
    l=len(entire_string)
    if(l):
        x=int(entire_string[l-1],10)
        fact=math.sin(x)
        fact1 = round(fact, 3)
        undo()
        display.insert(i,fact1)
def tricos():
    entire_string=display.get()
    l=len(entire_string)
    if(l):
        x=int(entire_string[l-1],10)
        fact=math.cos(x)
        undo()
        fact1 = round(fact, 3)
        display.insert(i,fact1)
def tritan():
    entire_string=display.get()
    l=len(entire_string)
    if(l):
        x=int(entire_string[l-1],10)
        fact=math.tan(x)
        undo()
        fact1 = round(fact, 3)
        display.insert(i,fact1)
def mathlog():
    entire_string=display.get()
    l=len(entire_string)
    if(l):
        x=int(entire_string[l-1],10)
        fact=math.log(x,10)
        undo()
        fact1 = round(fact, 3)
        display.insert(i,fact1)
def mathexp():
    entire_string=display.get()
    l=len(entire_string)
    if(l):
        x=int(entire_string[l-1],10)
        fact=math.exp(x)
        undo()
        fact1 = round(fact, 3)
        display.insert(i,fact1)

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W + E)

# 1st column of buttons
Button(root, text="**2  ",command=lambda : get_variables("**2")).grid(row=2, column=0)
Button(root, text="x**y ",command=lambda : get_variables("**")).grid(row=2, column=1)
Button(root, text="sin x",command=lambda : trisin()).grid(row=2, column=2)
Button(root, text="cos x",command=lambda : tricos()).grid(row=2, column=3)
Button(root, text="tan x",command=lambda : tritan()).grid(row=2, column=4)

# 2nd column of buttons
Button(root, text="sqrt()",command=lambda : get_variables("**")).grid(row=3, column=0)
Button(root, text="10**x",command=lambda : get_variables("10**")).grid(row=3, column=1)
Button(root, text="log  ",command=lambda : mathlog()).grid(row=3, column=2)
Button(root, text="exp  ",command=lambda : mathexp()).grid(row=3, column=3)
Button(root, text="mod  ",command=lambda : get_variables("%")).grid(row=3, column=4)

# 3rd column of buttons
Button(root, text="CE   ",command=lambda :clear_all()).grid(row=4, column=0)
Button(root,text="C     ",command=lambda :clear_all()).grid(row=4,column=1)
Button(root,text="<-    ",command=lambda : undo()).grid(row=4,column=2)
Button(root,text="/     ",command=lambda : get_variables("/")).grid(row=4,column=3)

#4th column of buttons
Button(root, text="*3.14").grid(row=5, column=0)
Button(root, text="7    ",command=lambda : get_variables(7)).grid(row=5, column=1)
Button(root, text="8    ",command=lambda : get_variables(8)).grid(row=5, column=2)
Button(root, text="9    ",command=lambda : get_variables(9)).grid(row=5, column=3)
Button(root, text="*    ",command=lambda : get_variables("*")).grid(row=5, column=4)

#5th column of buttons
Button(root, text="!    ",command=lambda : factorial()).grid(row=6, column=0)
Button(root, text="4    ",command=lambda : get_variables(4)).grid(row=6, column=1)
Button(root, text="5    ",command=lambda : get_variables(5)).grid(row=6, column=2)
Button(root, text="6    ",command=lambda : get_variables(6)).grid(row=6, column=3)
Button(root, text="-    ",command=lambda : get_variables("-")).grid(row=6, column=4)

#6th column of buttons
Button(root, text="+-   ").grid(row=7, column=0)
Button(root, text="1    ",command=lambda : get_variables(1)).grid(row=7, column=1)
Button(root, text="2    ",command=lambda : get_variables(2)).grid(row=7, column=2)
Button(root, text="3    ",command=lambda : get_variables(3)).grid(row=7, column=3)
Button(root, text="+    ",command=lambda : get_variables("+")).grid(row=7, column=4)

#7th column of buttons
Button(root, text="(",command=lambda : get_variables("(")).grid(row=8, column=0)
Button(root, text=")",command=lambda : get_variables(")")).grid(row=8, column=1)
Button(root, text="0",command=lambda : get_variables(0)).grid(row=8, column=2)
Button(root, text=".",command=lambda : get_variables(".")).grid(row=8, column=3)
Button(root, text="=",command=lambda : calculate()).grid(row=8, column=4)

root.mainloop()
