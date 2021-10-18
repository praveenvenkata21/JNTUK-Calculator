import tkinter
from tkinter import messagebox
e1=0
e2=0
proent=ens=en1=en2=en3=en4=en5=en6=en7=en8=en9=c1=0
gsum=0
w=0
def clear():
    en1.delete(0)
    en2.delete(0)
    en3.delete(0)
    en4.delete(0)
    en5.delete(0)
    en6.delete(0)
    en7.delete(0)
    en8.delete(0)
    en9.delete(0)
    proent.delete(0)
    ens.delete(0)
    
def cgcal():
            cgsum=0
            if en1.get()=='':#1-1
                g1=0
            else:
                g1=float(en1.get())
                cgsum=24
            if en2.get()=='':#1-2
                g2=0
            else:
                g2=float(en2.get())
                cgsum+=24
            if en3.get()=='':#2-1
                g3=0
            else:
                g3=float(en3.get())
                cgsum+=22
            if en4.get()=='':#2-2
                g4=0
            else:
                g4=float(en4.get())
                cgsum+=22
            if en5.get()=='':#3-1
                g5=0
            else:
                g5=float(en5.get())
                cgsum+=21
            if en6.get()=='':#3-2
                g6=0
            else:
                g6=float(en6.get())
                cgsum+=21
            if en7.get()=='':#4-1
                g7=0
            else:
                g7=float(en7.get())
                cgsum+=22
            if en8.get()=='':#4-2
                g8=0             
            else:
                g8=float(en8.get())
                cgsum+=24
            gsum=((g1*24)+(g2*24)+(g3*22)+(g4*22)+(g5*21)+(g6*21)+(g7*22)+(g8*24))/cgsum
            gsum=round(gsum,2)
            # cgpala=tkinter.Label(w,text=gsum,font='arial 10 bold')
            #cgpla=tkinter.Label(w,text="CGPA RESULT IS:",font='arial 10 bold').grid(row=12,column=0)
            #cgpala.grid(row=12,column=1)
            messagebox.showinfo(title='RESULT', message='YOUR RESULT IS '+str(gsum))
def cal():
    if int(e1.get())==4:
            pr=proent.get()
            s=ens.get()
            g1=en1.get()
            g2=en2.get()
            g3=en3.get()
            g4=en4.get()
            str1=g1+g2+g3+g4+pr+s           
    elif int(e1.get())==5 and int(e2.get())==3:
            g1=en1.get()
            g2=en2.get()
            g3=en3.get()
            g4=en4.get()
            g5=en5.get()
            g6=en6.get()
            g7=en7.get()
            g8=en8.get()
            str1=g1+g2+g3+g4+g5+g6+g7+g8
    elif int(e1.get())==5 and int(e2.get())==2:
            g1=en1.get()
            g2=en2.get()
            g3=en3.get()
            g4=en4.get()
            g5=en5.get()
            g6=en6.get()
            g7=en7.get()
            str1=g1+g2+g3+g4+g5+g6+g7
    elif int(e1.get())==6 and int(e2.get())==3:
            g1=en1.get()
            g2=en2.get()
            g3=en3.get()
            g4=en4.get()
            g5=en5.get()
            g6=en6.get()
            g7=en7.get()
            g8=en8.get()
            g9=en9.get()
            str1=g1+g2+g3+g4+g5+g6+g7+g8+g9
    elif int(e1.get())==6 and int(e2.get())==2:
            g1=en1.get()
            g2=en2.get()
            g3=en3.get()
            g4=en4.get()
            g5=en5.get()
            g6=en6.get()
            g7=en7.get()
            g8=en8.get()
            str1=g1+g2+g3+g4+g5+g6+g7+g8
    grade=[0]*10
    j=0
    for i in str1:
        if i=='O' or i=='o':
            grade[j]=10.0
            j+=1
        elif i=='S' or i=='s':
            grade[j]=9.0
            j+=1
        elif i=='A' or i=='a':
            grade[j]=8.0
            j+=1
        elif i=='B' or i=='b':
            grade[j]=7.0
            j+=1
        elif i=='C' or i=='c':
            grade[j]=6.0
            j+=1
        elif i=='D' or i=='d':
            grade[j]=5.0
            j+=1
        else:
            grade[j]=0.0
            j+=1
    count=0
    psum=0
    csum=0
    for i in range(len(str1)):
      if str1[i]!=0:
        if int(e1.get())==4 and count<int(e1.get()):
            psum+=grade[i]*3
            count+=1
            csum+=3
        elif int(e1.get())==4 and count>=int(e1.get()):
            psum+=grade[4]*10+grade[5]*2
            csum+=12
            break
        elif count < int(e1.get()):
           psum+=grade[i]*3
           count+=1
           csum+=3
        else:
            psum+=grade[i]*2
            csum+=2
    psum=psum/csum
    psum1=round(psum,2)
    #re=tkinter.Label(w,text="SGPA RESULT IS:",font='arial 10 bold')
    #re.grid(row=12,column=0)
    #resu=tkinter.Label(w,text=psum1,font='arial 10 bold')
    #resu.grid(row=12,column=1)
    messagebox.showinfo(title='RESULT', message='YOUR RESULT IS '+str(psum1))
def ent():
    z=int(e1.get())
    if z<4 or z>6:
            #re=tkinter.Label(w,text="  INVALID DETAILS  ",fg='red',font='bold')
            #re.grid(row=12,column=1)
            messagebox.showinfo(title='RESULT', message='INVALID DETAILS')
    elif z==4:
        ent2()
    else:
        l2=tkinter.Label(w,text="Enter no.of labs")
        l2.grid(row=2,column=0)
        global e2
        e2=tkinter.Entry(w,width=20)
        e2.grid(row=2,column=1)
        b3=tkinter.Button(w,text="ENTER",command=ent1)
        b3.grid(row=1,column=2)    
def ent2():    
        global proent,ens
        pro=tkinter.Label(w,text="ENTER PROJECT GRADE")
        pro.grid(row=2,column=0)
        proent=tkinter.Entry(w,width=20)
        proent.grid(row=2,column=1)
        sem=tkinter.Label(w,text="ENTER SEMINAR GRADE")
        sem.grid(row=3,column=0)
        ens=tkinter.Entry(w,width=20)
        ens.grid(row=3,column=1)
        n=int(e1.get())
        m=4
        while n>0:
            l3=tkinter.Label(w,text="Enter subject grade")
            l3.grid(row=m,column=0)
            m=m+1
            n-=1
        global en1,en2,en3,en4,en5,en6,en7,en8,en9
        en1=tkinter.Entry(w,width=20)
        en1.grid(row=4,column=1)
        en2=tkinter.Entry(w,width=20)
        en2.grid(row=5,column=1)
        en3=tkinter.Entry(w,width=20)
        en3.grid(row=6,column=1)
        en4=tkinter.Entry(w,width=20)
        en4.grid(row=7,column=1)
        res=tkinter.Button(w,text="GET RESULT",command=cal)
        res.grid(row=7,column=2)
        l=tkinter.Label(w,text="Note:\n Don't Enter Grades in Numerics",fg='red',font='arial 10 bold')
        l.grid(row=20,column=1)
        en5=tkinter.Entry(w,width=0)
        en6=tkinter.Entry(w,width=0)
        en7=tkinter.Entry(w,width=0)
        en8=tkinter.Entry(w,width=0)
        en9=tkinter.Entry(w,width=0)
        cl=tkinter.Button(w,text="CLEAR",command=clear)
        cl.grid(row=8,column=2)
def ent1():
  n1=int(e1.get())
  n2=int(e2.get())
  if n2!=2 and n2!=3:
    #re=tkinter.Label(w,text="  INVALID DETAILS  ",fg='red',font='bold')
    #re.grid(row=12,column=1)
    messagebox.showinfo(title='RESULT', message='INVALID DETAILS')
  else:
    k=(n1)+(n2)
    global k1
    k1=k
    k2=n1
    m=3
    while k>0:
      if k2>0:
        l3=tkinter.Label(w,text="Enter subject grade")
        l3.grid(row=m,column=0)
        m=m+1
        k-=1
        k2-=1
      else:
        l3=tkinter.Label(w,text="Enter lab grade")
        l3.grid(row=m,column=0)
        m=m+1
        k-=1
          
    global en1,en2,en3,en4,en5,en6,en7,en8,en9,proent,ens
    en1=en2=en3=en4=en5=en6=en7=en8=en9=0
    if k1==7:
        en1=tkinter.Entry(w,width=20)
        en1.grid(row=3,column=1)
        en2=tkinter.Entry(w,width=20)
        en2.grid(row=4,column=1)
        en3=tkinter.Entry(w,width=20)
        en3.grid(row=5,column=1)
        en4=tkinter.Entry(w,width=20)
        en4.grid(row=6,column=1)
        en5=tkinter.Entry(w,width=20)
        en5.grid(row=7,column=1)
        en6=tkinter.Entry(w,width=20)
        en6.grid(row=8,column=1)
        en7=tkinter.Entry(w,width=20)
        en7.grid(row=9,column=1)
        res=tkinter.Button(w,text="GET RESULT",command=cal)
        res.grid(row=9,column=2)
        cl=tkinter.Button(w,text="CLEAR",command=clear)
        cl.grid(row=10,column=2)
        en8=tkinter.Entry(w,width=0)
        en9=tkinter.Entry(w,width=0)
        proent=tkinter.Entry(w,width=0)
        ens=tkinter.Entry(w,width=0)
        
    elif k1==8:
        
        en1=tkinter.Entry(w,width=20)
        en1.grid(row=3,column=1)
        en2=tkinter.Entry(w,width=20)
        en2.grid(row=4,column=1)
        en3=tkinter.Entry(w,width=20)
        en3.grid(row=5,column=1)
        en4=tkinter.Entry(w,width=20)
        en4.grid(row=6,column=1)
        en5=tkinter.Entry(w,width=20)
        en5.grid(row=7,column=1)
        en6=tkinter.Entry(w,width=20)
        en6.grid(row=8,column=1)
        en7=tkinter.Entry(w,width=20)
        en7.grid(row=9,column=1)
        en8=tkinter.Entry(w,width=20)
        en8.grid(row=10,column=1)
        en9=tkinter.Entry(w,width=0)
        res=tkinter.Button(w,text="GET RESULT",command=cal)
        res.grid(row=10,column=2)
        cl=tkinter.Button(w,text="CLEAR",command=clear)
        cl.grid(row=11,column=2)
        proent=tkinter.Entry(w,width=0)
        ens=tkinter.Entry(w,width=0)
        
    else:
        en1=tkinter.Entry(w,width=20)
        en1.grid(row=3,column=1)
        en2=tkinter.Entry(w,width=20)
        en2.grid(row=4,column=1)
        en3=tkinter.Entry(w,width=20)
        en3.grid(row=5,column=1)
        en4=tkinter.Entry(w,width=20)
        en4.grid(row=6,column=1)
        en5=tkinter.Entry(w,width=20)
        en5.grid(row=7,column=1)
        en6=tkinter.Entry(w,width=20)
        en6.grid(row=8,column=1)
        en7=tkinter.Entry(w,width=20)
        en7.grid(row=9,column=1)
        en8=tkinter.Entry(w,width=20)
        en8.grid(row=10,column=1)
        en9=tkinter.Entry(w,width=20)
        en9.grid(row=11,column=1)
        proent=tkinter.Entry(w,width=0)
        ens=tkinter.Entry(w,width=0)
        res=tkinter.Button(w,text="GET RESULT",command=cal)
        res.grid(row=11,column=2)
        cl=tkinter.Button(w,text="CLEAR",command=clear)
        cl.grid(row=12,column=2)
    l=tkinter.Label(w,text="Note:\n Don't Enter Grades in Numerics",fg='red',font='arial 10 bold')
    l.grid(row=20,column=1)
    
    
def sgpa():
    l1=tkinter.Label(w,text="Enter no.of subjects")
    l1.grid(row=1,column=0)
    global e1,c1
    e1=tkinter.Entry(w,width=20)
    e1.grid(row=1,column=1)
    b3=tkinter.Button(w,text="ENTER",command=ent)
    b3.grid(row=1,column=2)
     
def cgpa():
    cgh=tkinter.Label(w,text="Enter SGPA Score")
    cgh.grid(row=1,column=0)
    cgl=tkinter.Label(w,text="Enter your 1-1 score")
    cgl.grid(row=2,column=0)
    cgl=tkinter.Label(w,text="Enter your 1-2 score")
    cgl.grid(row=3,column=0)
    cgl=tkinter.Label(w,text="Enter your 2-1 score")
    cgl.grid(row=4,column=0)
    cgl=tkinter.Label(w,text="Enter your 2-2 score")
    cgl.grid(row=5,column=0)
    cgl=tkinter.Label(w,text="Enter your 3-1 score")
    cgl.grid(row=6,column=0)
    cgl=tkinter.Label(w,text="Enter your 3-2 score")
    cgl.grid(row=7,column=0)
    cgl=tkinter.Label(w,text="Enter your 4-1 score")
    cgl.grid(row=8,column=0)
    cgl=tkinter.Label(w,text="Enter your 4-2 score")
    cgl.grid(row=9,column=0)
    global en1,en2,en3,en4,en5,en6,en7,en8,c1,en9,proent,ens
    en1=tkinter.Entry(w,width=20)
    en1.grid(row=2,column=1)
    en2=tkinter.Entry(w,width=20)
    en2.grid(row=3,column=1)
    en3=tkinter.Entry(w,width=20)
    en3.grid(row=4,column=1)
    en4=tkinter.Entry(w,width=20)
    en4.grid(row=5,column=1)
    en5=tkinter.Entry(w,width=20)
    en5.grid(row=6,column=1)
    en6=tkinter.Entry(w,width=20)
    en6.grid(row=7,column=1)
    en7=tkinter.Entry(w,width=20)
    en7.grid(row=8,column=1)
    en8=tkinter.Entry(w,width=20)
    en8.grid(row=9,column=1)
    en9=tkinter.Entry(w,width=0)
    proent=tkinter.Entry(w,width=0)
    ens=tkinter.Entry(w,width=0)   
    bn=tkinter.Button(w,text="GET RESULT",command=cgcal)
    bn.grid(row=9,column=2)
    cl=tkinter.Button(w,text="CLEAR",command=clear)
    cl.grid(row=10,column=2)
    #print(bn)
def s_create():
    global w
    w=tkinter.Tk()
    w.title("SGPA")
    w.geometry('450x300')
    sgpa()
def c_create():
    global w
    w=tkinter.Tk()
    w.title("SGPA")
    cgpa()
w1=tkinter.Tk()
w1.title("JNTUK CALCULATOR")
w1.geometry('400x150')
b1=tkinter.Button(w1,text="SGPA",command=s_create)
b2=tkinter.Button(w1,text="CGPA",command=c_create)
lh=tkinter.Label(w1,text="JNTUK R16 SGPA/CGPA CALCULATOR",height='3',fg='green',font='bold')
lh.place(x=20,y=0)
b1.place(x=150,y=75)
b2.place(x=200,y=75)
by=tkinter.Label(w1,text="By RVG & PJ",fg='blue')
#by.grid(row=0,column=1)
by.place(x=160,y=110)
w1.mainloop()
