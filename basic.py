#imports
import tkinter,screens,math
import tkinter.font as font

##
#Functions for calculation.
#Uses pythons inbuilt eval() function to solve for +,-,*,/ The rest of the functions have their definitions

#string for storing the expression
exp = ""

#Expression cleaner for making readable equations
# code=0: Replacing symbols to be suitable for eval() syntax
# code=1: Convertinging eval() return equation to be readable and in syntax for further computations
def clean(exp, code):
    if(code==0):
        for r in (("π", str(math.pi)), ("e", str(math.e)), ("×", "*"), ("÷", "/"), ("^", "**")):
            exp = exp.replace(*r)
        return exp
    else:
        org_exp = exp
        exp = exp.replace("e","×10^(")
        if(exp!=org_exp):
            exp += ")"
        return exp

#Wrapper for clean function, code = 1
def resclean(exp, val):
    exp = clean(exp, 1)
    val.set(exp)

#Error Function
def err(val, e):
    val.set("42! and "+str(e))



#for general buttons
def inp(num, val):
   global exp
   try:
        exp += str(num)
        resclean(exp, val)
   except Exception as e:
       val.set("Error:")


#for 'C'
def clr(val):
   global exp
   exp = ""
   resclean(exp, val)

#for '⌫'
def bks(val):
   global exp
   exp = str(val.get())
   exp = exp[0:-1]
   resclean(exp, val)

#for '1/x'
def inv(val):
    res(val)
    if(val.get()!=''):
        global exp
        try:
            exp = str(1/(eval(exp)))
            resclean(exp, val)
        except Exception as e:
            exp = ""
            err(val, e)

#for '√','x²','x³'
def pwr(num, val):
    res(val)
    if(val.get()!=''):
        global exp
        try:
            exp = str(math.pow(float(exp), float(num)))
            resclean(exp, val)
        except Exception as e:
            exp = ""
            err(val, e)    

#for '+/-'
def neg(val):
    res(val)
    if(val.get()!=''):
        global exp
        try:
            exp = str(float(exp)*-1)
            resclean(exp, val)
        except Exception as e:
            err(val, e)

#for '='
def res(val):
    if(val.get()!=''):
        global exp
        try:
            exp = val.get()
            exp = clean(exp, 0)
            exp = str(eval(exp))
            resclean(exp, val)
        except Exception as e:
            exp = ""
            err(val, e)

#Bind Enter Key to btn['=']
def ent(event):
    global val
    res(val)

screens.home.bind('<Return>',ent)
##

#gui page for basic calulator

#variable associated with textbox(tkinter's)
val = tkinter.StringVar()
#create a textbox for input
txt =  tkinter.Entry(screens.basic, textvariable=val, cursor="xterm")
#txt.place(height=200)
txt.grid(row=1, columnspan=4, ipadx=47, ipady=8, padx=8, pady=10)

#Button Dictionary
btn= {}

#Default Font for Calculator
fnt = font.Font(size=15, family="Consolas")

#Size of Buttons
h=2
w=5
pdy=5

#Create Buttons
# Numerical Buttons
btn['num0'] = tkinter.Button(screens.basic, text=str(0), command=lambda: inp(0, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num1'] = tkinter.Button(screens.basic, text=str(1), command=lambda: inp(1, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num2'] = tkinter.Button(screens.basic, text=str(2), command=lambda: inp(2, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num3'] = tkinter.Button(screens.basic, text=str(3), command=lambda: inp(3, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num4'] = tkinter.Button(screens.basic, text=str(4), command=lambda: inp(4, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num5'] = tkinter.Button(screens.basic, text=str(5), command=lambda: inp(5, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num6'] = tkinter.Button(screens.basic, text=str(6), command=lambda: inp(6, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num7'] = tkinter.Button(screens.basic, text=str(7), command=lambda: inp(7, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num8'] = tkinter.Button(screens.basic, text=str(8), command=lambda: inp(8, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num9'] = tkinter.Button(screens.basic, text=str(9), command=lambda: inp(9, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)

# Buttons used in equation
btn['+'] = tkinter.Button(screens.basic, text='+', command=lambda: inp('+', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['-'] = tkinter.Button(screens.basic, text='-', command=lambda: inp('-', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['*'] = tkinter.Button(screens.basic, text='×', command=lambda: inp('×', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['/'] = tkinter.Button(screens.basic, text='÷', command=lambda: inp('÷', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['.'] = tkinter.Button(screens.basic, text='.', command=lambda: inp('.', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['('] = tkinter.Button(screens.basic, text='(', command=lambda: inp('(', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn[')'] = tkinter.Button(screens.basic, text=')', command=lambda: inp(')', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)

# Command Buttons(Single Use Buttons)
btn['='] = tkinter.Button(screens.basic, text='=', command=lambda: res(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['±'] = tkinter.Button(screens.basic, text='±', command=lambda: neg(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['√'] = tkinter.Button(screens.basic, text='√', command=lambda: pwr(0.5, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['1/x'] = tkinter.Button(screens.basic, text='1/x', command=lambda: inv(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['x²'] = tkinter.Button(screens.basic, text='x²', command=lambda: pwr(2, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['C'] = tkinter.Button(screens.basic, text='C', command=lambda: clr(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['⌫'] = tkinter.Button(screens.basic, text='⌫', command=lambda: bks(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['Basic'] = tkinter.Button(screens.basic, text='Basic', command=lambda: screens.raise_frame(screens.scientific), fg='white', bg='black', bd=0, height=h, width=w, pady=2)

#Apply font to all buttons
for i in btn:
    btn[i]['font']=fnt

#Apply font to text
txt['font']=fnt

#Arrange Buttons from 1 to 9
i=9 #counter
for row in range(4,7):
    for col in range(2, -1, -1):
        btn["num{}".format(i)].grid(row=row,column=col)
        i-=1

#Manually arranging rest of the buttons
btn['Basic'].grid(row=0,column=1, columnspan=2)
btn['('].grid(row=2,column=0)
btn[')'].grid(row=2,column=1)
btn['C'].grid(row=2,column=2)
btn['⌫'].grid(row=2,column=3)
btn['1/x'].grid(row=3,column=0)
btn['x²'].grid(row=3,column=1)
btn['√'].grid(row=3,column=2)
btn['/'].grid(row=3,column=3)
btn['*'].grid(row=4,column=3)
btn['-'].grid(row=5,column=3)
btn['+'].grid(row=6,column=3)
btn['±'].grid(row=7,column=0)
btn['num0'].grid(row=7,column=1)
btn['.'].grid(row=7,column=2)
btn['='].grid(row=7,column=3)