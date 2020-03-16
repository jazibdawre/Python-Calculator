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

##for Scientific

#Degree and radians Setting
# 0:Radians - default
# 1:Degree
deg=0

#radian to degree converter 
# code=0:
#   input:deg/rad   output:rad
# code=1:
#   input:rad   output:deg/rad
def check(exp, code):
    global deg
    if(code==0):
        if(deg==0):
            return exp
        else:
            return str(math.pi*float(exp)/180)
    else:
        if(deg==0):
            return exp
        else:
            return str(180*float(exp)/math.pi)

#for btn['Deg'] and btn ['Rad']
def numsys(dg):
    global deg
    global btn
    deg = dg
    if (dg==0):
        btn['Deg'].grid_forget()
        btn['Rad'].grid(row=0, column=4)
    else:
        btn['Rad'].grid_forget()
        btn['Deg'].grid(row=0, column=4)

#for sin
def sin(val):
    res(val)
    if(val.get()!=''):
        global exp
        try:
            exp = val.get()
            exp = check(exp, 0)
            exp = str(math.sin(float(exp)))
            resclean(exp, val)
        except Exception as e:
            exp = ""
            err(val, e)

#for asin
def asin(val):
    res(val)
    if(val.get()!=''):
        global exp
        try:
            exp = val.get()
            exp = check(exp, 1)
            exp = str(math.asin(float(exp)))
            resclean(exp, val)
        except Exception as e:
            exp = ""
            err(val, e)

#for cos
def cos(val):
    res(val)
    if(val.get()!=''):
        global exp
        try:
            exp = val.get()
            exp = check(exp, 0)
            exp = str(math.cos(float(exp)))
            resclean(exp, val)
        except Exception as e:
            exp = ""
            err(val, e)

#for acos
def acos(val):
    res(val)
    if(val.get()!=''):
        global exp
        try:
            exp = val.get()
            exp = check(exp, 1)
            exp = str(math.acos(float(exp)))
            resclean(exp, val)
        except Exception as e:
            exp = ""
            err(val, e)

#for tan
def tan(val):
    res(val)
    if(val.get()!=''):
        global exp
        try:
            exp = val.get()
            exp = check(exp, 0)
            exp = str(math.tan(float(exp)))
            resclean(exp, val)
        except Exception as e:
            exp = ""
            err(val, e)

#for atan
def atan(val):
    res(val)
    if(val.get()!=''):
        global exp
        try:
            exp = val.get()
            exp = str(math.atan(float(exp)))
            exp = check(exp, 1)
            resclean(exp, val)
        except Exception as e:
            exp = ""
            err(val, e)

#for log
def log(val, base):
    res(val)
    if(val.get()!=''):
        try:
            exp=val.get()
            exp = str(math.log(float(exp), base))
            resclean(exp, val)
        except Exception as e:
            exp = ""
            err(val, e)

#for mod
def mod(val):
    res(val)
    if(val.get()!=''):
        try:
            exp=val.get()
            exp = str(abs(float(exp)))
            resclean(exp, val)
        except Exception as e:
            exp = ""
            err(val, e)

#for x!
def fct(val):
    res(val)
    if(val.get()!=''):
        try:
            exp=val.get()
            exp = str(math.factorial(int(exp)))
            resclean(exp, val)
        except Exception as e:
            exp = ""
            err(val, e)

#Button state
# 0:1st state - default
# 1:2nd state
bt = 0 

#for changing buttons
def shft(val):
    global bt
    global btn
    bt = val
    if(val==0):
        btn['2nd'].grid_remove()
        btn['1st'].grid(row=0, column=3)
        btn['asin'].grid_remove()
        btn['sin'].grid(row=4, column=0)
        btn['acos'].grid_remove()
        btn['cos'].grid(row=5, column=0)
        btn['atan'].grid_remove()
        btn['tan'].grid(row=6, column=0)
        btn['n√'].grid_remove()
        btn['xⁿ'].grid(row=3, column=1)
        btn['∛'].grid_remove()
        btn['x³'].grid(row=4, column=3)
        btn['√'].grid_remove()
        btn['x²'].grid(row=4, column=2)
        btn['exp'].grid_remove()
        btn['ln'].grid(row=8, column=0)
    else:
        btn['1st'].grid_remove()
        btn['2nd'].grid(row=0, column=3)
        btn['sin'].grid_remove()
        btn['asin'].grid(row=4, column=0)
        btn['cos'].grid_remove()
        btn['acos'].grid(row=5, column=0)
        btn['tan'].grid_remove()
        btn['atan'].grid(row=6, column=0)
        btn['xⁿ'].grid_remove()
        btn['n√'].grid(row=3, column=1)
        btn['x³'].grid_remove()
        btn['∛'].grid(row=4, column=3)
        btn['x²'].grid_remove()
        btn['√'].grid(row=4, column=2)
        btn['ln'].grid_remove()
        btn['exp'].grid(row=8, column=0)

##
##


#gui page for basic calulator

#variable associated with textbox(tkinter's)
val = tkinter.StringVar()
#create a textbox for input
txt =  tkinter.Entry(screens.scientific, textvariable=val, cursor="xterm")
#txt.place(height=200)
txt.grid(row=1,columnspan=5, ipadx=47, ipady=8, padx=8, pady=10)

#Button Dictionary
btn= {}

#Default Font for Calculator
fnt = font.Font(size=15, family="Consolas")

#Size of Buttons
h=2
w=4
pdy=0

#Create Buttons
# Numerical Buttons
btn['num0'] = tkinter.Button(screens.scientific, text=str(0), command=lambda: inp(0, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num1'] = tkinter.Button(screens.scientific, text=str(1), command=lambda: inp(1, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num2'] = tkinter.Button(screens.scientific, text=str(2), command=lambda: inp(2, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num3'] = tkinter.Button(screens.scientific, text=str(3), command=lambda: inp(3, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num4'] = tkinter.Button(screens.scientific, text=str(4), command=lambda: inp(4, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num5'] = tkinter.Button(screens.scientific, text=str(5), command=lambda: inp(5, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num6'] = tkinter.Button(screens.scientific, text=str(6), command=lambda: inp(6, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num7'] = tkinter.Button(screens.scientific, text=str(7), command=lambda: inp(7, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num8'] = tkinter.Button(screens.scientific, text=str(8), command=lambda: inp(8, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['num9'] = tkinter.Button(screens.scientific, text=str(9), command=lambda: inp(9, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)

# Buttons used in equation
btn['+'] = tkinter.Button(screens.scientific, text='+', command=lambda: inp('+', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['-'] = tkinter.Button(screens.scientific, text='-', command=lambda: inp('-', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['*'] = tkinter.Button(screens.scientific, text='×', command=lambda: inp('×', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['/'] = tkinter.Button(screens.scientific, text='÷', command=lambda: inp('÷', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['.'] = tkinter.Button(screens.scientific, text='.', command=lambda: inp('.', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['('] = tkinter.Button(screens.scientific, text='(', command=lambda: inp('(', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn[')'] = tkinter.Button(screens.scientific, text=')', command=lambda: inp(')', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)

# Command Buttons(Single Use Buttons)
##Basic Buttons
#Buttons in 2nd mode
btn['√'] = tkinter.Button(screens.scientific, text='√', command=lambda: pwr((1/2), val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
#Buttons in 1st mode
btn['='] = tkinter.Button(screens.scientific, text='=', command=lambda: res(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['±'] = tkinter.Button(screens.scientific, text='±', command=lambda: neg(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['√'] = tkinter.Button(screens.scientific, text='√', command=lambda: pwr(0.5, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['1/x'] = tkinter.Button(screens.scientific, text='1/x', command=lambda: inv(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['x²'] = tkinter.Button(screens.scientific, text='x²', command=lambda: pwr(2, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['C'] = tkinter.Button(screens.scientific, text='C', command=lambda: clr(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['⌫'] = tkinter.Button(screens.scientific, text='⌫', command=lambda: bks(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
##Scientific Exclusive Buttons
#Buttons in 2nd mode
btn['asin'] = tkinter.Button(screens.scientific, text='sin⁻¹', command=lambda: asin(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['acos'] = tkinter.Button(screens.scientific, text='cos⁻¹', command=lambda: acos(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['atan'] = tkinter.Button(screens.scientific, text='tan⁻¹', command=lambda: atan(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['exp'] = tkinter.Button(screens.scientific, text='exp', command=lambda: pwr(math.e, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['∛'] = tkinter.Button(screens.scientific, text='∛', command=lambda: pwr((1/3), val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['n√'] = tkinter.Button(screens.scientific, text='n√', command=lambda: inp("^(1÷", val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['Deg'] = tkinter.Button(screens.scientific, text='Deg', command=lambda: numsys(0) , fg='white', bg='black', bd=0, height=h, width=w, pady=2, padx=15)
btn['2nd'] = tkinter.Button(screens.scientific, text='2ⁿᵈ', command=lambda: shft(0), fg='white', bg='black', bd=0, height=h, width=w, pady=2, padx=15)
#Buttons in 1st mode
btn['sin'] = tkinter.Button(screens.scientific, text='sin', command=lambda: sin(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['cos'] = tkinter.Button(screens.scientific, text='cos', command=lambda: cos(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['tan'] = tkinter.Button(screens.scientific, text='tan', command=lambda: tan(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['log'] = tkinter.Button(screens.scientific, text='log', command=lambda: log(val,10), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['ln'] = tkinter.Button(screens.scientific, text='ln', command=lambda: log(val, math.e), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['|x|'] = tkinter.Button(screens.scientific, text='|x|', command=lambda: mod(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['x³'] = tkinter.Button(screens.scientific, text='x³', command=lambda: pwr(3, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['x!'] = tkinter.Button(screens.scientific, text='x!', command=lambda: fct(val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['xⁿ'] = tkinter.Button(screens.scientific, text='xⁿ', command=lambda: inp('^(', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['π'] = tkinter.Button(screens.scientific, text='π', command=lambda: inp('π', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['e'] = tkinter.Button(screens.scientific, text='e', command=lambda: inp('e', val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['10ˣ'] = tkinter.Button(screens.scientific, text='10ˣ', command=lambda: pwr(10, val), fg='white', bg='black', bd=0, height=h, width=w, pady=pdy)
btn['1st'] = tkinter.Button(screens.scientific, text='1ˢᵗ', command=lambda: shft(1), fg='white', bg='black', bd=0, height=h, width=w, pady=2, padx=15)
btn['Rad'] = tkinter.Button(screens.scientific, text='Rad', command=lambda: numsys(1), fg='white', bg='black', bd=0, height=h, width=w, pady=2, padx=15)
btn['Scientific'] = tkinter.Button(screens.scientific, text='Scientific', command=lambda: screens.raise_frame(screens.basic), fg='white', bg='black', bd=0, height=h, width=w, pady=2, padx=15)

#Labels
lbl = tkinter.Label(screens.scientific, text=' Current\n Mode:', fg='white', bg='black', bd=0, height=h, width=w, pady=2, padx=15)

#Apply font to all buttons
for i in btn:
    btn[i]['font']=fnt

#Apply font to text
txt['font']=fnt
lbl['font']=fnt

#Smaller size to compensate for text
lbl['font'] = font.Font(size=10, family="Consolas")
btn['Scientific']['font'] = font.Font(size=8, family="Consolas")

#Arrange Buttons from 1 to 9
i=9 #counter
for row in range(5,8):
    for col in range(3, 0, -1):
        btn["num{}".format(i)].grid(row=row,column=col)
        i-=1

#Manually arranging rest of the buttons and label
#row0
lbl.grid(row=0, column=0)
btn['Scientific'].grid(row=0, column=1, columnspan=2)
btn['1st'].grid(row=0, column=3)
btn['2nd'].grid(row=0, column=3)
btn['Deg'].grid(row=0, column=4)
btn['Rad'].grid(row=0, column=4)
#row1 is text entry
#row2
btn['x!'].grid(row=2, column=0)
btn['('].grid(row=2, column=1)
btn[')'].grid(row=2, column=2)
btn['C'].grid(row=2, column=3)
btn['⌫'].grid(row=2, column=4)
#row3
btn['10ˣ'].grid(row=3, column=0)
btn['n√'].grid(row=3, column=1)
btn['xⁿ'].grid(row=3, column=1)
btn['π'].grid(row=3, column=2)
btn['e'].grid(row=3, column=3)
btn['|x|'].grid(row=3, column=4)
#row4
btn['1/x'].grid(row=4, column=1)
btn['√'].grid(row=4, column=2)
btn['x²'].grid(row=4, column=2)
btn['∛'].grid(row=4, column=3)
btn['x³'].grid(row=4, column=3)
btn['asin'].grid(row=4, column=0)
btn['sin'].grid(row=4, column=0)
btn['/'].grid(row=4, column=4)
#row5
btn['acos'].grid(row=5, column=0)
btn['cos'].grid(row=5, column=0)
btn['*'].grid(row=5, column=4)
#row6
btn['atan'].grid(row=6, column=0)
btn['tan'].grid(row=6, column=0)
btn['-'].grid(row=6, column=4)
#row7
btn['log'].grid(row=7, column=0)
btn['+'].grid(row=7, column=4)
#row8
btn['exp'].grid(row=8, column=0)
btn['ln'].grid(row=8, column=0)
btn['±'].grid(row=8, column=1)
btn['num0'].grid(row=8, column=2)
btn['.'].grid(row=8, column=3)
btn['='].grid(row=8, column=4)