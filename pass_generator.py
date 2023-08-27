import tkinter
from tkinter import *
from tkinter import ttk
import random
import pyperclip

root=Tk()
root.geometry("540x360")

p1="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
p2=p1+"0123456789"
p3=p2+"!@#$%^&*_"

global pas
pas=""

def clr():
    ot.delete(0,END)
    e.delete(0,END)
    e1.delete(0,END)
    l.delete(0,END)

def gntpd(s,n):
    
    ot.delete(0,END)
    p=""
    
    global pas
    pas=""
    if s=="weak":
        p=p1
        
    elif s=="medium":
        p=p2
    elif s=="strong":
        p=p3
    for i in range(n):
        g=random.randint(0,len(p)-1)
        pas+=p[g]
    ot.insert(0,pas)

def copy():
    if ot.get()!="":
        pyperclip.copy(ot.get())
        t=Toplevel(root)
        t.geometry("310x30")
        Label(t, text="Generated Password has been copied to Clipboard.", font=("Helvetica",10)).pack()
    else:
        t=Toplevel(root)
        t.geometry("310x30")
        Label(t, text="Enter the required information.", font=("Helvetica",10)).pack()
    

Label(root, text="Password Generator", font=("Times", 25), fg="blue").grid(row=0,column=1, sticky="w")
Label(root, text="Enter your name : ",font=("Helvetica", 11), justify="left").grid(row=1,column=0, sticky="w")
e=Entry(root, width=50)
e.grid(row=1,column=1, columnspan=4, pady=20, sticky="e")
Label(root, text="Enter length of password : ",font=("Helvetica", 11)).grid(row=2,column=0, sticky="w")
e1=Entry(root, width=50)
e1.grid(row=2,column=1, columnspan=4, pady=20,sticky="e")
s=StringVar()
Label(root, text="Strength of password : ",font=("Helvetica", 11)).grid(row=3,column=0, sticky="w")
l=ttk.Combobox(root, width=47, textvariable=s)
l['values']=('weak', 'medium','strong')
l.grid(row=3,column=1, columnspan=4, sticky="e")

Label(root, text="Password : ",font=("Helvetica", 11)).grid(row=5,column=0,sticky="w")
ot=Entry(root, width=50)
ot.grid(row=5,column=1, columnspan=4, pady=20, sticky="e")

Button(root, text="Generate",font=("Agency FB", 18),padx=15,pady=10, command=lambda:gntpd(l.get(),int(e1.get()))).grid(row=6,column=0)
Button(root, text="Accept",font=("Agency FB", 18),padx=15,pady=10, command=copy).grid(row=6,column=1)

Button(root, text="Reset",font=("Agency FB", 18),padx=15,pady=10, command=clr).grid(row=6,column=2)


root.mainloop()