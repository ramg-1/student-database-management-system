
def addstudent():
    addroot=Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='blue')
    addroot.iconbitmap('econ.ico.ico')
    addroot.resizable(width=False, height=False)
    #----------------------------------add student label
    # idlabel = Label(addroot,text='Enter ID : ',bg='gold2',font=('times',22,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='W')
    # idlabel.place(x=10,y=10)
    idlabel=Label(addroot,text='Enter ID : ',bg='gold2',)
    addroot.mainloop()
def searchstudent():
    print('student search')
def deletestudent():
    print('student deleted')
def upadatestudent():
    print('student update')
def showallstudent():
    print('student show')
def exportstudent():
    print('student export')
def exitstudent():
    res = messagebox.askyesnocancel('NOTIFICATION','DO YOU WANT TO EXIT')
    if res==True:
        root.destroy()
########################################################################connection of database
def connectdb():
    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('econ.ico.ico')
    dbroot.resizable(0,0)
    dbroot.configure(background='blue')
    ##-----------------------------------connectdb levels
    hostlabel = Label(dbroot,text='Enter Host :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)
    userlabel = Label(dbroot, text='Enter User :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=13, anchor='w')
    userlabel.place(x=10, y=70)
    passwordlabel = Label(dbroot, text='Enter Password :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='w')
    passwordlabel.place(x=10, y=130)

    ##-----------------------------------connectdb entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry=Entry(dbroot,font=('roman',20,'bold'),bd=5,relief=GROOVE,textvariable=hostval)
    hostentry.place(x=250, y=10)
    userentry = Entry(dbroot, font=('roman', 20, 'bold'), bd=5, relief=GROOVE, textvariable=userval)
    userentry.place(x=250, y=70)
    passwordentry = Entry(dbroot, font=('roman', 20, 'bold'), bd=5, relief=GROOVE, textvariable=passwordval)
    passwordentry.place(x=250, y=130)
    ##----------------------------------------------------connectdb button
    submitbutton=Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='blue',activeforeground='white' )
    submitbutton.place(x=150, y=190)
    dbroot.mainloop()
#################################################################################################clock and date
def tick():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%m/%d/%Y")
    clock.config(text='Date:'+date_string+'\n'+'Time:'+time_string)
    clock.after(100,tick)
########################################################## intro slider
import random
colors=['red','yellow','green','blue','magenta','cyan','white']

def IntroLevelColorTick():
    fg=random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(200,IntroLevelColorTick)

def IntroLevelTick():
    global count,text
    if count >= len(ss):
        count=-1
        text=''
        SliderLabel.config(text=text)
    else:
        text=text+ss[count]
        SliderLabel.config(text=text)
    count+=1
    SliderLabel.after(100,IntroLevelTick)
###########################################################################
from tkinter import *
import time
from tkinter import Toplevel,messagebox
root =Tk()
root.title("Student Database Management System")
root.config(bg='gold2')
root.geometry('1174x700+200+50')
root.iconbitmap("econ.ico.ico")
root.resizable(0,0)
######################################################################frame
##---------------------------------------------------dataentry frame intro

DataEntryFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
frontlabel=Label(DataEntryFrame,text='---------Welcome--------------',width=25,font=('alien',22,'italic bold'),bg='gold2',relief=GROOVE)
frontlabel.pack(side=TOP,expand=True)
addbtn=Button(DataEntryFrame,text=' 1. Add Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)
searchbtn=Button(DataEntryFrame,text=' 2. Search Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)
deletebtn=Button(DataEntryFrame,text=' 3. Delete Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)
updatebtn=Button(DataEntryFrame,text=' 4. Update Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=upadatestudent)
updatebtn.pack(side=TOP,expand=True)
showallbtn=Button(DataEntryFrame,text=' 5. Show All',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=showallstudent)
showallbtn.pack(side=TOP,expand=True)
exportbtn=Button(DataEntryFrame,text=' 6. Export Data',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)
exitbtn=Button(DataEntryFrame,text=' 7. Exit',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)
##---------------------------------------------------showentry frame

ShowDataFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=560,y=80,width=610,height=600)




##########################################################################slider
ss='Welcome To Student  Management System'
count=0
text=''
############################
SliderLabel=Label(root,text=ss,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,width=54, bg='cyan')
SliderLabel.place(x=260,y=0)
IntroLevelTick()
IntroLevelColorTick()
###########################################################################clock
clock=Label(root,font='time,30,bold',relief=RIDGE,borderwidth=4,width=15, bg='lawngreen')
clock.place(x=0,y=0)
tick()
#############################################################################connect database button
connectbutton = Button(root,text='Connect To Database',width=23,font=('chiller',21,'italic bold'),relief=RIDGE,borderwidth=4,bg='green2',activebackground='blue',activeforeground='white',command=connectdb)
connectbutton.place(x=930,y=0)
root.mainloop()