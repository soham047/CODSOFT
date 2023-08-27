from tkinter import *
from tkinter import ttk
import sys
import os 


def abc():
    y=0
    a=ttk.Notebook(width=800, height=560)

    f1=ttk.Frame(a)
    f2=ttk.Frame(a)
    f3=ttk.Frame(a)
    f4=ttk.Frame(a)
    f5=ttk.Frame(a)
    f6=ttk.Frame(a)
    f7=ttk.Frame(a)
    f8=ttk.Frame(a)
    f9=ttk.Frame(a)
    f10=ttk.Frame(a)

    root=ttk.Frame(a)




    def quiz(y):
        q=["Which of the following Himalayan regions is called Shivalik's?","Which of the given cities is located on the bank of river Ganga?","Which of the given is a disease caused by protozoa?","Garampani sanctuary is located at : ","Hitler party which came into power in 1933 is known as","First human heart transplant operation conducted\n by Dr. Christiaan Barnard on Louis Washkansky, was conducted in :","Exposure to sunlight helps a\n person improve his health because","Galileo was an Italian astronomer who","Golf player Vijay Singh belongs to which country?",".Each year World Red Cross and Red Crescent Day is celebrated on"]
        ans=[["Upper Himalayas","Lower Himalayas","Outer Himalayas","Inner Himalayas","3"],["Patna","Gwalior","Bhopal","Mathura","1"],["Cancer","Typhoid","Kala-azar","Chicken Pox","3"],["Junagarh, Gujarat","Diphu, Assam","Kohima, Nagaland","Gangtok, Sikkim","2"],["Labour Party","Nazi Party","Ku-Klux-Klan","Democratic Party","2"],["1967","1968","1958","1922","1"],["the infrared light kills bacteria in the body","resistance power increases","the pigment cells in the skin get stimulated and produce a healthy tan","the ultraviolet rays convert skin oil into Vitamin D","4"],["developed the telescope","discovered four satellites of Jupiter","discovered that the movement of pendulum produces a regular time measurement","All of the above","4"],["USA","Fiji","India","UK","2"],["May 8","May 18","June 8","June 18","1"]]
        
        a.add(f1, text = "Question 1")
        a.add(f2, text = "Question 2")
        a.add(f3, text = "Question 3")
        a.add(f4, text = "Question 4")
        a.add(f5, text = "Question 5")
        a.add(f6, text = "Question 6")
        a.add(f7, text = "Question 7")
        a.add(f8, text = "Question 8")
        a.add(f9, text = "Question 9")
        a.add(f10, text = "Question 10")
        
        Label(f1, text=q[0], font=("Times", 20, "bold italic")).grid(row =2, column =1)
        #v=IntVar()
        Button(f1, text=ans[0][0], command=lambda:chk(ans[0][4], f1, 1,1), font=("Times", 15)).grid(row=3,column=1)
        Button(f1, text=ans[0][1], command=lambda:chk(ans[0][4], f1, 2,1), font=("Times", 15)).grid(row=4,column=1)
        Button(f1, text=ans[0][2], command=lambda:chk(ans[0][4], f1, 3,1), font=("Times", 15)).grid(row=5,column=1)
        Button(f1, text=ans[0][3], command=lambda:chk(ans[0][4], f1, 4,1), font=("Times", 15)).grid(row=6,column=1)
        
        Label(f2, text=q[1], font=("Times", 20, "bold italic")).grid(row =2, column =1)
        #v1=IntVar()
        Button(f2, text=ans[1][0], command=lambda:chk(ans[1][4], f2, 1,2), font=("Times", 15)).grid(row=3,column=1)
        Button(f2, text=ans[1][1], command=lambda:chk(ans[1][4], f2, 2,2), font=("Times", 15)).grid(row=4,column=1)
        Button(f2, text=ans[1][2], command=lambda:chk(ans[1][4], f2, 3,2), font=("Times", 15)).grid(row=5,column=1)
        Button(f2, text=ans[1][3], command=lambda:chk(ans[1][4], f2, 4,2), font=("Times", 15)).grid(row=6,column=1)
        
        Label(f3, text=q[2], font=("Times", 20, "bold italic")).grid(row =2, column =1)
        #v2=IntVar()
        Button(f3, text=ans[2][0], command=lambda:chk(ans[2][4], f3, 1,3), font=("Times", 15)).grid(row=3,column=1)
        Button(f3, text=ans[2][1], command=lambda:chk(ans[2][4], f3, 2,3), font=("Times", 15)).grid(row=4,column=1)
        Button(f3, text=ans[2][2], command=lambda:chk(ans[2][4], f3, 3,3), font=("Times", 15)).grid(row=5,column=1)
        Button(f3, text=ans[2][3], command=lambda:chk(ans[2][4], f3, 4,3), font=("Times", 15)).grid(row=6,column=1)
        
        
        Label(f4, text=q[3], font=("Times", 20, "bold italic")).grid(row =2, column =1)
        #v2=IntVar()
        Button(f4, text=ans[3][0], command=lambda:chk(ans[3][4], f4, 1,4), font=("Times", 15)).grid(row=3,column=1)
        Button(f4, text=ans[3][1], command=lambda:chk(ans[3][4], f4, 2,4), font=("Times", 15)).grid(row=4,column=1)
        Button(f4, text=ans[3][2], command=lambda:chk(ans[3][4], f4, 3,4), font=("Times", 15)).grid(row=5,column=1)
        Button(f4, text=ans[3][3], command=lambda:chk(ans[3][4], f4, 4,4), font=("Times", 15)).grid(row=6,column=1)
        
        Label(f5, text=q[4], font=("Times", 20, "bold italic")).grid(row =2, column =1)
        #v2=IntVar()
        Button(f5, text=ans[4][0], command=lambda:chk(ans[4][4], f5, 1,5), font=("Times", 15)).grid(row=3,column=1)
        Button(f5, text=ans[4][1], command=lambda:chk(ans[4][4], f5, 2,5), font=("Times", 15)).grid(row=4,column=1)
        Button(f5, text=ans[4][2], command=lambda:chk(ans[4][4], f5, 3,5), font=("Times", 15)).grid(row=5,column=1)
        Button(f5, text=ans[4][3], command=lambda:chk(ans[4][4], f5, 4,5), font=("Times", 15)).grid(row=6,column=1)
        
        Label(f6, text=q[5], font=("Times", 20, "bold italic")).grid(row =2, column =1)
        #v2=IntVar()
        Button(f6, text=ans[5][0], command=lambda:chk(ans[5][4], f6, 1,6), font=("Times", 15)).grid(row=3,column=1)
        Button(f6, text=ans[5][1], command=lambda:chk(ans[5][4], f6, 2,6), font=("Times", 15)).grid(row=4,column=1)
        Button(f6, text=ans[5][2], command=lambda:chk(ans[5][4], f6, 3,6), font=("Times", 15)).grid(row=5,column=1)
        Button(f6, text=ans[5][3], command=lambda:chk(ans[5][4], f6, 4,6), font=("Times", 15)).grid(row=6,column=1)

        Label(f7, text=q[6], font=("Times", 20, "bold italic")).grid(row =2, column =1)
        #v2=IntVar()
        Button(f7, text=ans[6][0], command=lambda:chk(ans[6][4], f7, 1,7), font=("Times", 15)).grid(row=3,column=1)
        Button(f7, text=ans[6][1], command=lambda:chk(ans[6][4], f7, 2,7), font=("Times", 15)).grid(row=4,column=1)
        Button(f7, text=ans[6][2], command=lambda:chk(ans[6][4], f7, 3,7), font=("Times", 15)).grid(row=5,column=1)
        Button(f7, text=ans[6][3], command=lambda:chk(ans[6][4], f7, 4,7), font=("Times", 15)).grid(row=6,column=1)

        Label(f8, text=q[7], font=("Times", 20, "bold italic")).grid(row =2, column =1)
        #v2=IntVar()
        Button(f8, text=ans[7][0], command=lambda:chk(ans[7][4], f8, 1,8), font=("Times", 15)).grid(row=3,column=1)
        Button(f8, text=ans[7][1], command=lambda:chk(ans[7][4], f8, 2,8), font=("Times", 15)).grid(row=4,column=1)
        Button(f8, text=ans[7][2], command=lambda:chk(ans[7][4], f8, 3,8), font=("Times", 15)).grid(row=5,column=1)
        Button(f8, text=ans[7][3], command=lambda:chk(ans[7][4], f8, 4,8), font=("Times", 15)).grid(row=6,column=1)
        
        
        Label(f9, text=q[8], font=("Times", 20, "bold italic")).grid(row =2, column =1)
        #v2=IntVar()
        Button(f9, text=ans[8][0], command=lambda:chk(ans[8][4], f9, 1,9), font=("Times", 15)).grid(row=3,column=1)
        Button(f9, text=ans[8][1], command=lambda:chk(ans[8][4], f9, 2,9), font=("Times", 15)).grid(row=4,column=1)
        Button(f9, text=ans[8][2], command=lambda:chk(ans[8][4], f9, 3,9), font=("Times", 15)).grid(row=5,column=1)
        Button(f9, text=ans[8][3], command=lambda:chk(ans[8][4], f9, 4,9), font=("Times", 15)).grid(row=6,column=1)
        
        
        Label(f10, text=q[9], font=("Times", 20, "bold italic")).grid(row =2, column =1)
        #v2=IntVar()
        Button(f10, text=ans[9][0], command=lambda:chk(ans[9][4], f10, 1,10), font=("Times", 15)).grid(row=3,column=1)
        Button(f10, text=ans[9][1], command=lambda:chk(ans[9][4], f10, 2,10), font=("Times", 15)).grid(row=4,column=1)
        Button(f10, text=ans[9][2], command=lambda:chk(ans[9][4], f10, 3,10), font=("Times", 15)).grid(row=5,column=1)
        Button(f10, text=ans[9][3], command=lambda:chk(ans[9][4], f10, 4,10), font=("Times", 15)).grid(row=6,column=1)
        Button(f10, text="Show Result", command= show_result, font=("Agency FB", 20, "bold")).grid(row=7,column=1)

    def show_result():
        top=Toplevel(a)
        top.geometry("250x250")
        top.title("Score")
        
        global m
        p="Points Scored : "+str(m)
        Label(top, text=p, font=("Times", 20, "bold italic"), fg="green").grid(row=2,column=1)
        Label(top, text="Total Points : 10", font=("Times", 20, "bold italic")).grid(row=1,column=1)
        #Button(top, text="Close", command=top.destroy).grid(row=2,column=2)
        Button(top, text="EXIT", command=sys.exit, bg="green", fg="white",font=("Garamond", 20)).grid(row=4,column=1)
        Button(top, text="Restart", command=restart, bg="green", fg="white",font=("Garamond", 20)).grid(row=3,column=1)

    def menu():
        
        top1=Toplevel(a)
        top1.geometry("720x560")
        top1.title("Main Menu\n\n")
        s="Rules :\n1.There are 10 questions about General Knowledge with four options available.\n2. You will have to select the correct option.\n3. Questions can be accessed from the top of your screen.\n4. Each answer carries 1 point.\n5. Total score will be displayed in the end.\n"
        Label(top1, text="Main Menu",font=("Garamond", 20,"bold")).grid(row=1,column=1)
        Label(top1, text="Welcome to Quiz Game",font=("Garamond", 22, "italic")).grid(row=2,column=1)
        Label(top1, text=s,font=("Helvetica", 14), justify="left", anchor="w").grid(row=3,column=1)
        Button(top1, text="START", command=lambda: [top1.destroy(), quiz(y)], bg="green", fg="white",font=("Garamond", 20)).grid(row=4,column=1)
        top1.wm_transient(a)
        
    def restart():
        a.destroy()
        abc()
        
    def chk(a1, f,o,n):
        #o=v.get()
        if int(a1)==o:
            #w1.config(text="your answer is correct.")
            
            #Label(f, text=s1).grid(row=1,column=2)
            s1.set("Yours answer is correct.")
            if n not in l:
            
                global m
                m+=1
            l.append(n)
            
        else:
            #s="your answer is incorrect. the correct answer is option "+a1
            
            s1.set("Wrong, correct answer is option "+ a1)
            l.append(n)
            #w1.config(text=q[0])
        Label(f, textvariable =s1, font=("Agency FB", 14)).grid(row=1,column=1)

    l=[]
    s1 = StringVar()
    global m
    m=0

    menu()


    a.pack()
    a.mainloop()

abc()
