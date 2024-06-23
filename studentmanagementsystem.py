
def addstudent():
    def submitadd():
        name = nameval.get()
        gender = genderval.get()
        id  = idval.get()
        roll= rollval.get()
        mobile = mobileval.get()
        depertment = depertmentval.get()
        grade = gradeval.get()
        date = time.strftime("%d/%m/%Y")
        try:
           
           strr = "INSERT INTO studentdata (name,gender,id,roll,mobile,depertment,grade,date)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
           mycursor.execute(strr,(name, gender, id , roll, mobile, depertment, grade, date))
           con.commit()
           res = messagebox.askyesnocancel("Notifications","Name {name} Gender {gender} Added sucessfully..And want to clean the from",parent=addroot)
           if (res==True):
                nameval.set('')
                genderval.set('')
                idval.set('')
                rollval.set('')
                mobileval.set('')
                depertmentval.set('')
                gradeval.set('') 
        except:
            messagebox.showerror('Notification','Student data are Already exist try another ', parent=addroot)
        str = 'select * from studentdata'
        mycursor.execute(str)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
            studenttable.insert('',END,values=vv)
            

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title("ADD Student Personal Data")
    addroot.config(bg='grey')
    addroot.iconbitmap('iitp logo.ico')
    addroot.resizable(False,False)
    #-------------------------------------------------Add  data lable--------------------------------------
    namelable = Label(addroot,text='Student Name:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelable.place(x=10,y=10)

    genderlable = Label(addroot,text='Gender:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlable.place(x=10,y=70)

    idlable = Label(addroot,text='Clg Email id:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlable.place(x=10,y=130)

    rolllable = Label(addroot,text='Roll No:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    rolllable.place(x=10,y=190)

    moblable = Label(addroot,text='Mobile No:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    moblable.place(x=10,y=250)

    depertmentlable = Label(addroot,text='Depertment:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    depertmentlable.place(x=10,y=310)

    gradelable = Label(addroot,text='Grade:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    gradelable.place(x=10,y=370)

    ##--------------------------------------------------------- add student entry----------------------------------------------------------------------------
    nameval = StringVar()
    genderval = StringVar()
    idval = StringVar()
    rollval = StringVar()
    mobileval = StringVar()
    depertmentval = StringVar()
    gradeval = StringVar()

    nameentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=10)

    genderentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=70)

    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=130)

    rollentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=rollval)
    rollentry.place(x=250,y=190)

    mobileentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=250)

    depertentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=depertmentval)
    depertentry.place(x=250,y=310)

    gradeentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=gradeval)
    gradeentry.place(x=250,y=370)

    #------------------------------------add button-----------------------------------------------------------------
    submitbtn = Button(addroot,text='Submit',font=('times',15,'bold'),width=20,bd=5,activebackground='white',activeforeground='red',bg='grey',command=submitadd)
    submitbtn.place(x=150,y=420)
    
    addroot.mainloop()

#----------------------------------------------------------------- search --------------------------------------------------------------------------------------------------


def searchstudent():
    def Search():
         
        name = nameval.get()
        gender = genderval.get()
        id  = idval.get()
        roll= rollval.get()
        mobile = mobileval.get()
        depertment = depertmentval.get()
        grade = gradeval.get()
        date = time.strftime("%d/%m/%Y")
        if(name != ""):
            strr = 'select *from studentdata where  name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
               studenttable.insert('',END,values=vv)

        elif(gender != ""):
            strr = 'select *from studentdata wher gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
               studenttable.insert('',END,values=vv)  

        elif(id != ""):
            strr = 'select *from studentdata wher id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
               studenttable.insert('',END,values=vv)
        
        elif(roll != ""):
            strr = 'select *from studentdata wher roll=%s'
            mycursor.execute(strr,(roll))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
               studenttable.insert('',END,values=vv)

        elif(mobile != ""):
            strr = 'select *from studentdata wher mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
               studenttable.insert('',END,values=vv) 

        elif(depertment != ""):
            strr = 'select *from studentdata wher depertment=%s'
            mycursor.execute(strr,(depertment))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
               studenttable.insert('',END,values=vv)

        elif(grade != ""):
            strr = 'select *from studentdata wher grade=%s'
            mycursor.execute(strr,(grade))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
               studenttable.insert('',END,values=vv)   

        elif (date != ""):
            strr = 'select *from studentdata wher date=%s'
            mycursor.execute(strr,(date))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
               studenttable.insert('',END,values=vv)                        

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title("Search Student detail")
    searchroot.config(bg='grey')
    searchroot.iconbitmap('iitp logo.ico')
    searchroot.resizable(False,False)
    #-------------------------------------------------Add  data lable--------------------------------------
    namelable = Label(searchroot,text='Student Name:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelable.place(x=10,y=10)

    genderlable = Label(searchroot,text='Gender:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlable.place(x=10,y=70)

    idlable = Label(searchroot,text='Clg Email id:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlable.place(x=10,y=130)

    rolllable = Label(searchroot,text='Roll No:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    rolllable.place(x=10,y=190)

    moblable = Label(searchroot,text='Mobile No:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    moblable.place(x=10,y=250)

    depertmentlable = Label(searchroot,text='Depertment:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    depertmentlable.place(x=10,y=310)

    gradelable = Label(searchroot,text='Grade:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    gradelable.place(x=10,y=370)

    Datelable = Label(searchroot,text='Date:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    Datelable.place(x=10,y=430)
 
    ##--------------------------------------------------------- add student entry----------------------------------------------------------------------------
    nameval = StringVar()
    genderval = StringVar()
    idval = StringVar()
    rollval = StringVar()
    mobileval = StringVar()
    depertmentval = StringVar()
    gradeval = StringVar()
    dateval =StringVar()

    nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=10)

    genderentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=70)

    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=130)

    rollentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=rollval)
    rollentry.place(x=250,y=190)

    mobileentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=250)

    depertentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=depertmentval)
    depertentry.place(x=250,y=310)

    gradeentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=gradeval)
    gradeentry.place(x=250,y=370)

    dateentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)


    #------------------------------------add button-----------------------------------------------------------------
    submitbtn = Button(searchroot,text='Search',font=('times',15,'bold'),width=20,bd=5,activebackground='white',activeforeground='red',bg='grey',command=Search)
    submitbtn.place(x=150,y=480)
    
    searchroot.mainloop()


def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata where name=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('notification','name{} delete succesfully..'.format(pp))
    strr = 'select * from studentdata '
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
        studenttable.insert('',END,values=vv)

#-----------------------------------------------------------------------------------update------------------------------------------------------------------------------

def updatestudent():
    def Update():
        name = nameval.get()
        gender = genderval.get()
        id  = idval.get()
        roll= rollval.get()
        mobile = mobileval.get()
        depertment = depertmentval.get()
        grade = gradeval.get()
        date = time.strftime("%d/%m/%Y")

        strr = 'update studentdata set name=%s,mobile%s,email=%s,address=%s,dob=%s,date=%s where id =%s'
        mycursor.execute(strr,(name,gender,id,roll,mobile,depertment,grade,date))
        con.commit()
        messagebox.showinfo('notifications', 'Id {}modified successfully..'.format(name))
        strr = 'select *from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
            studenttable.insert("",END,values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.geometry('470x540+220+200')
    updateroot.title("Search Student detail")
    updateroot.config(bg='grey')
    updateroot.iconbitmap('iitp logo.ico')
    updateroot.resizable(False,False)
    #-------------------------------------------------Add  data lable--------------------------------------
    namelable = Label(updateroot,text='Student Name:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelable.place(x=10,y=10)

    genderlable = Label(updateroot,text='Gender:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlable.place(x=10,y=70)

    idlable = Label(updateroot,text='Clg Email id:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlable.place(x=10,y=130)

    rolllable = Label(updateroot,text='Roll No:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    rolllable.place(x=10,y=190)

    moblable = Label(updateroot,text='Mobile No:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    moblable.place(x=10,y=250)

    depertmentlable = Label(updateroot,text='Depertment:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    depertmentlable.place(x=10,y=310)

    gradelable = Label(updateroot,text='Grade:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    gradelable.place(x=10,y=370)

    Datelable = Label(updateroot,text='Date:',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    Datelable.place(x=10,y=430)
 
    ##--------------------------------------------------------- add student entry----------------------------------------------------------------------------
    nameval = StringVar()
    genderval = StringVar()
    idval = StringVar()
    rollval = StringVar()
    mobileval = StringVar()
    depertmentval = StringVar()
    gradeval = StringVar()
    dateval =StringVar()

    nameentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=10)

    genderentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=70)

    identry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=130)

    rollentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=rollval)
    rollentry.place(x=250,y=190)

    mobileentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=250)

    depertentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=depertmentval)
    depertentry.place(x=250,y=310)

    gradeentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=gradeval)
    gradeentry.place(x=250,y=370)

    dateentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)


    #------------------------------------add button-----------------------------------------------------------------
    submitbtn = Button(updateroot,text='Update',font=('times',15,'bold'),width=20,bd=5,activebackground='white',activeforeground='red',bg='grey',command=Update)
    submitbtn.place(x=150,y=480)
    cc=studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) !=0):
        nameval.set(pp[0])
        genderval.set(pp[1])
        idval.set(pp[3])
        rollval.set(pp[4])
        mobileval.set(pp[5])
        depertmentval.set(pp[6])
        gradeval.set(pp[7])
               
    
    updateroot.mainloop()

def showstudent():
    strr = 'select *from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
        studenttable.insert('',END, values=vv) 

def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    name,gender,id,roll,mobile,depertment,grade=[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i) 
        pp = content['values']
        name.append(pp[0],gender.append(pp[1]),id.append(pp[2]),roll.append(pp[3]),mobile.append(pp[4]),depertment.append(pp[5]),grade.append(pp[6]))
        
    dd = ['Name','Gender','id','Roll','mobile','depertment','grade']
    df = pandas.DataFrame(list(zip('Name','Gender','id','Roll','mobile','depertment','grade')),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notification','Student data is saved'.format(paths))
    


def exitstudent():
    print('student exit')
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res == True):
      root.destroy()

##########################################################connection of Database#####################################
def connectdb():
    def submitdb():
        global con,mycursor
        host =hostval.get()
        user = userval.get()
        password =passwordval.get()
        try:
            con = mysql.connector.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification','Data is incorrect please try again')
            return
        try:
            strr = 'create database priyanshudb'
            mycursor.execute(strr)
            strr ='use priyanshudb'  
            mycursor.execute(strr) 
            strr ='create table studentdata(name varchar(20),gender varchar(20),id varchar(300),roll varchar(20), mobile varchar(12), depertment varchar(20),grade varchar(10), date varchar(20))'
            mycursor.execute(strr)
            strr ='alter table studentdata modify column id str not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id str primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Database created,Now You are connected to the database......',parent=dbroot)
           

        except:
            strr='use priyanshudb'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now You are connected to the database......',parent=dbroot)
        dbroot.destroy()    
           


    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('iitp logo.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')

    hostlabel= Label(dbroot,text='Enter Host:',bg='grey',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel= Label(dbroot,text='Enter user id:',bg='grey',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel= Label(dbroot,text='Enter password:',bg='grey',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)

    #__________________________________connectdb label_________________________________________
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()
    
    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

    #-----------------------------connectdb--------------------------------------------------
    submitbuttton = Button(dbroot,text='submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='white',activeforeground='black',command=submitdb)
    submitbuttton.place(x=150,y=190)

    dbroot.mainloop()

def IntroLabelTick():
    global count,text 
    if (count>=len(ss)):
        count = 0
        text =''
        sliderLable.config(text=text)
    else:
        text = text+ss[count]
        sliderLable.config(text=text)
        count += 1
    sliderLable.after(200,IntroLabelTick)
    

#############################################################################
from tkinter import*
from tkinter import Toplevel
from tkinter import messagebox, filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import mysql.connector
import pandas 
import time


root = Tk()
root.title('student management system')
root.config(bg='sky blue')
root.geometry("1174x700+200+50")

root.resizable(False, False)
################################################## Frame###########
DataEntryFrame = Frame(root,bg='grey',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
#-------------------------------------------------------frame intro-------------------------------------------------

addbutton = Button(DataEntryFrame,text='Add Student Information',width=25,font=('times',20,'bold'),bd=6,activebackground='red',relief=RIDGE,activeforeground='white',command=addstudent)
addbutton.pack(side=TOP,expand=True)

searchbutton = Button(DataEntryFrame,text=' Search',width=25,font=('times',20,'bold'),bd=6,activebackground='red',relief=RIDGE,activeforeground='white',command=searchstudent)
searchbutton.pack(side=TOP,expand=True)

delbutton = Button(DataEntryFrame,text='Delete',width=25,font=('times',20,'bold'),bd=6,activebackground='red',relief=RIDGE,activeforeground='white',command=deletestudent)
delbutton.pack(side=TOP,expand=True)

updatebutton = Button(DataEntryFrame,text=' Update',width=25,font=('times',20,'bold'),bd=6,activebackground='red',relief=RIDGE,activeforeground='white',command=updatestudent)
updatebutton.pack(side=TOP,expand=True)

showbutton = Button(DataEntryFrame,text='Show All',width=25,font=('times',20,'bold'),bd=6,activebackground='red',relief=RIDGE,activeforeground='white',command=showstudent)
showbutton.pack(side=TOP,expand=True)

exportbutton = Button(DataEntryFrame,text='Export Data',width=25,font=('times',20,'bold'),bd=6,activebackground='red',relief=RIDGE,activeforeground='white',command=exportstudent)
exportbutton.pack(side=TOP,expand=True)

exitbutton = Button(DataEntryFrame,text='Exit',width=25,font=('times',20,'bold'),bd=6,activebackground='red',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbutton.pack(side=TOP,expand=True)

ShowDataFrame = Frame(root,bg='white',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)

#------------------------------------------------------------------show Dataframe-----------------------------------------------------------------------------------------------------
style= ttk.Style()
style.configure('Treeview.heading',font=('roman',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),foreground='black')
Scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
Scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,columns=('Student name','Gender','id','Roll No','Mob','Depertment','Grade','Date'),
                        yscrollcommand=Scroll_y,xscrollcommand=Scroll_x.set)

Scroll_x.pack(side=BOTTOM,fill=X)
Scroll_y.pack(side=RIGHT,fill=Y)
Scroll_x.config(command=studenttable.xview)
Scroll_y.config(command=studenttable.yview)
studenttable.heading('Student name',text='Student Name')
studenttable.heading('Gender',text='Gender')
studenttable.heading('id',text='College Email Id')
studenttable.heading('Roll No',text='Roll No')
studenttable.heading('Mob',text='Mobile No')
studenttable.heading('Depertment',text='Depertment')
studenttable.heading('Grade',text='Grade')
studenttable.heading('Date',text='Date')
studenttable['show'] = 'headings'

studenttable.column('Student name',width=200)
studenttable.column('Gender',width=100)
studenttable.column('id',width=200)
studenttable.column('Roll No',width=100)
studenttable.column('Mob',width=100)
studenttable.column('Depertment',width=100)
studenttable.column('Grade',width=100)
studenttable.column('Date',width=100)

studenttable.pack(fill=BOTH,expand=1)
###############################################################################################################
ss ='IIT PATNA Student Management System'
count = 0
text = ''
##############################################

sliderLable =Label(root,text=ss,font=('times',25,'bold'),relief=RIDGE,borderwidth=4,width=40,bg="cyan")
sliderLable.place(x=10,y=0)
IntroLabelTick()
##########################################################################################################################
connectionbuttom = Button(root,text='login',width=20,font=('times',16,'bold'),relief=RIDGE,borderwidth=4,bg='grey',
                          activebackground='red',activeforeground='white',command=connectdb)
connectionbuttom.place(x=930,y=0)
root.mainloop()

