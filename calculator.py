from tkinter import *
root=Tk()
global y
y=0
a=0
c=0
a1=1

e=Entry(root, width=50)
e.grid(row=0,column=0, columnspan=4, padx=15,pady=15)

def chn(n,h):
    global a
    a=0
    s=0
    s1=1
    w=""
    if "+" in n:

        y=n.rfind("+")
        s=float(n[0:y]) +float(n[y+1::]) 
    elif "-" in n:
        k=0

        y=n.rfind("-")
        s=float(n[0:y]) -float(n[y+1::])
        
    if "x" in n:

        y=n.rfind("x")
        s=float(n[0:y]) *float(n[y+1::])
                     
    elif "/" in n:
        k=0

        y=n.rfind("/")
        s=float(n[0:y]) /float(n[y+1::])
    e.delete(0,END)
    e.insert(0, str(s)+h)
    return str(s)
          
def btnclk(num):
   
    z=e.get()
    e.delete(0,END)
    e.insert(0,str(z)+str(num))

def cls():
    e.delete(0,END)
    global a
    a=0
    global a1
    a1=1

def dot():
    i=e.get()
    e.delete(0,END)
    e.insert(0, i+".")
    
def sqrt():
    i=e.get()
    global a
    a=float(i)**0.5
    e.delete(0,END)
    e.insert(0,str(a))
    a=0

def addition(n):
    i=e.get()
    if ('-' in n) or ('x' in n) or ('/' in n):
        i=chn(e.get(), "+")
        
    
    global c
    c=2
    
    y=i.rfind('+')+1
    i1=i[y::1]
    
    o=len(i1)
    global a
    a=a+float(i1)
    
    e.delete(0,END)
    e.insert(0,str(n)+"+")

def minus(n):
    i=e.get()

    if ('+' in n) or ('x' in n) or ('/' in n):
        
        i=chn(e.get(), "-")
        
    global c
    c=4
    
    y=i.rfind("-")+1
    global a
    if y==0:
    #o=len(i1)
        
        a=float(i)
    else:
        i1=i[y::1]
        
        a=a-float(i1)
    e.delete(0,END)
    e.insert(0,str(a)+"-")

def multiply(n):
    i=e.get()
    if ('-' in n) or ('+' in n) or ('/' in n):
        i=chn(e.get(), "x")
    global c
    c=6
    
    y=i.rfind('x')+1
    i1=i[y::1]
    #o=len(i1)
    global a1
    a1=a1*float(i1)
    e.delete(0,END)
    e.insert(0,str(n)+"x")
    

def divide(n):
    i=e.get()
    if ('-' in n) or ('x' in n) or ('+' in n):
        i=chn(e.get(), "/")
    global c
    c=8
    #o=len(i1)
    
    y=i.rfind("/")+1
    global a
    if y==0:        
        
        a=float(i)
    else:
        i1=i[y::1]
        
        a=a/float(i1)
    e.delete(0,END)
    e.insert(0,str(a)+"/") 

def eqls():
    i=e.get()
    e.delete(0,END)
    global a
    if c==2:
        y=i.rfind('+')+1
        i1=i[y::1]
        #e.insert(0, i1)
        e.insert(0, str(float(a)+float(i1)))
    elif c==4:
        y=i.find('-')+1
        i1=i[y::1]
        #e.insert(0, i1)
        e.insert(0, str(float(a)-float(i1)))
    elif c==6:
        y=i.rfind('x')+1
        i1=i[y::1]
        #e.insert(0, i1)
        e.insert(0, str(float(a1)*float(i1)))
    elif c==8:
        y=i.find('/')+1
        i1=i[y::1]
        #e.insert(0, i1)
        e.insert(0, str(float(a)/float(i1)))
    
    a=0
    
def back_space():
    i=e.get()
    e.delete(0,END)
    e.insert(0, i[:len(i)-1])

b1=Button(root, text="1", padx=40, pady=20, command=lambda:btnclk(1))
b1.grid(row=2,column=0)
b2=Button(root, text="2", padx=40, pady=20, command=lambda:btnclk(2))
b2.grid(row=2,column=1)
b3=Button(root, text="3", padx=40, pady=20, command=lambda:btnclk(3))
b3.grid(row=2,column=2)
clr=Button(root, text="clear", padx=30, pady=20, command=cls)
clr.grid(row=2,column=3)

b4=Button(root, text="4", padx=40, pady=20, command=lambda:btnclk(4))
b4.grid(row=3,column=0)
b5=Button(root, text="5", padx=40, pady=20, command=lambda:btnclk(5))
b5.grid(row=3,column=1)
b6=Button(root, text="6", padx=40, pady=20, command=lambda:btnclk(6))
b6.grid(row=3,column=2)
add1=Button(root, text="+", padx=40, pady=20, command=lambda:addition(e.get()))
add1.grid(row=3,column=3)

b7=Button(root, text="7", padx=40, pady=20, command=lambda:btnclk(7))
b7.grid(row=4,column=0)
b8=Button(root, text="8", padx=40, pady=20, command=lambda:btnclk(8))
b8.grid(row=4,column=1)
b9=Button(root, text="9", padx=40, pady=20, command=lambda:btnclk(9))
b9.grid(row=4,column=2)
mi1=Button(root, text="-", padx=40, pady=20, command=lambda:minus(e.get()))
mi1.grid(row=4,column=3)

dt=Button(root, text=".", padx=40,pady=20, command=dot)
dt.grid(row=5, column=0)
b0=Button(root, text="0", padx=40, pady=20, command=lambda:btnclk(0))
b0.grid(row=5,column=1)
eq=Button(root, text="=", padx=85, pady=20, justify="center", command=eqls)
eq.grid(row=6,column=0, columnspan=2)
bs=Button(root, text="<=", padx=40, pady=20, command=back_space)
bs.grid(row=6, column=2)
mul1=Button(root, text="x", padx=40, pady=20, command=lambda:multiply(e.get()))
mul1.grid(row=6,column=3)
div1=Button(root, text="/", padx=40, pady=20, command=lambda:divide(e.get()))
div1.grid(row=5,column=3)
sr=Button(root, text="sqrt", padx=35,pady=20, command=sqrt)
sr.grid(row=5, column=2)

root.mainloop()
