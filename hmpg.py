from tkinter import*
import os
import time
from tkinter import ttk
import mysql.connector
import tkinter.messagebox as tm
from tkinter import messagebox
color='#87918c'
color1='#757d79'
color3='#bf5454'      
color4='#87918c'
color5='#87918c'
color6='#87918c'
top=Tk()
top.geometry("1500x950")
top.title("Bill")
top.config(bg="#87918c")
path = 'C:\\Users\\Ace Training 13\\Desktop'
mydb=mysql.connector.connect(
           host="localhost",
           user="root",
           passwd="",
           database="sms"
           )
           
mycursor = mydb.cursor()
def insert():
    for i in listbox.curselection():
        print (listbox.get(i))
        rdoc1=listbox.get(i)
    for j in listbox1.curselection():
        print (listbox1.get(j))
        study1=listbox1.get(j)
  
    name1=name.get()
    age1=age.get()
    sex1=sex.get()
    place1=place.get()
    phone1=phone.get()
    date1=date.get()
    amount1=amount.get()
    expense1=expense.get()
    print(name1)
    print(age1)
    print(sex1)
    print(place1)
    print(date1)
    print(amount1)
    print(expense1)
    
  
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="sms"
        )
    mycursor=mydb.cursor()
    total1=int(amount1)+int(expense1)
    print(name1)
    print(age1)
    print(sex1)
    print(place1)
    print(date1)
    print(amount1)
    print(expense1)
    
    txttot.insert(0,str(total1))
    
    if name1=='' or age1==''or sex1=='' or place1=='' or phone1==''  or rdoc1=='' or study1=='' or amount1 =='' or expense1== '' or total1=='':

       tm.showerror("Error","Please Enter all fields")
    else:
     
     sql="insert into scan(Name,Age ,Sex ,Place ,PhoneNo,Date,Rdoc,Study ,Amount ,Expense,Total)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
     data=(str(name1),str(age1),str(sex1),str(place1),str(phone1),str(date1),str(rdoc1),str(study1),str(amount1),str(expense1),str(total1))
     mycursor.execute(sql,data)
     mydb.commit()
     tm.showinfo("INFO","Patient Details inserted Sucessfully")
     txttot.delete(0,"end")
def cbill():
    global x
    pno=str(x)
    pbill=pno + ".txt"
    with open(os.path.join(path,pbill),"w")as file1:
        toFile=bill()
        file1.wite(toFile)
        qmsg = messagebox.showinfo("Information", "Bill Generated")
def bill():
    global pno
    global pnoentry
    global tbill
  
    pno=StringVar()
    pnoentry=StringVar()
    blbl=Label(top,text="Patient No",font=('arial', 16, 'bold'),bd=16, bg=color4, justify='left').place(x=10,y=150)
    pnoentry=Entry(top,textvariable=pno,font=('arial', 16, 'bold'),bd=4, insertwidth=2, justify='left').place(x=160,y=160)
    btn=Button(top,text="Generate Bill",bg="#3b3c36",fg="cyan",command=lambda:billdata(pno.get()),padx=4, pady=4, bd=4, font=('arial', 10, 'bold'), width=10).place(x=430,y=160)

    
def billdata(text):
    
    print("checking",text)
    if(text==""):
       tm.showerror("Error","Please enter the patient no")
    else:
     mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="sms"
        )
     
     sql_select_Query ="select * from scan where pno= %s"
     val = (text, )
     cursor = mydb.cursor()
     cursor.execute(sql_select_Query,val)
     records=cursor.fetchall()
     print(records)
     if records :
         for i in records:
           h1=("___________________________________________________________________________________________\n")
           h2=("  \t \t \t JANAKI SCANS  \n")
           h3=("___________________________________________________________________________________________\n")
           h4=(" \n  \t \t  \t Bill Receipt  \n")
           h5=("__________________________________________________________________________________________\n")
           h6=("\t \t \t  \t   Mobile No:9944120042\n\n\n")
           pname="Patient Name:   " +i[1]+  "    \t \t Age:   "+i[2]+"\t   \t     Sex:\t"+i[3]+"\n"   
           pplace="\nPlace:\t"+i[4]+  "\t \t  \t  DATE :  "+i[6]+"\n""\n"
           pphone="PHONE NUMBER:\t"+i[5]+"\t Reference Doctor:  "+i[7]+"\n \n\n"
           line="___________________________________________________________________________________________\n\n"
                
           pstudy="Name of Study\t \t  \t \t Amount" "\n"
           line1="_________________________________________________________________________________________\n"
           pdata=i[8]+"\t\t\t\t\t"+i[9]
           line2="\n\n_________________________________________________________________________________________\n"
           line3="\n \n\t \t\t\t\t                       Signature"
           string=h1+h2+h3+h4+h5+h6+pname+pplace+pphone+line+pstudy+line1+pdata+line2+line3
           
     
         frmt = text + ".txt"
         global path
         with open(os.path.join(path, frmt), "w") as file1:
         
          file1.write(string)
         qmsg = messagebox.showinfo("Information", "Bill Generated Successfully")
     else:
         messagebox.showinfo("Error", "Patient Number is Wrong ")
           

def clear():
  
    txtname.delete(0,"end")
    txttot.delete(0,"end")
    txtage.delete(0,"end")
    txtsex.delete(0,"end")
    txtplace.delete(0,"end")
    txtphone.delete(0,"end")
    txtamt.delete(0,"end")
    txtic.delete(0,"end")
def consolidate():
    global trv
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="sms"
        )
     
    sql_select_Query ="select * from scan"
    
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
   
    records=cursor.fetchall()
   
    Label(f2ac, font=('arial', 25, 'bold'), text=" CONSOLIDATED PATIENT DETAILS", bg=color,bd=15,padx=12, anchor='w').grid(row=0, column=0)
    trv = ttk.Treeview(f2ac, selectmode ='browse')
    trv.grid(row=1,column=0,padx=20,pady=20)

    # number of columns
    trv["columns"] = ("1", "2", "3","4","5","6","7","8","9")

    # Defining heading
    trv['show'] = 'headings'

    # width of columns and alignment 
    trv.column("1", width = 50, anchor ='c')
    trv.column("2", width = 80, anchor ='c')
    trv.column("3", width = 80, anchor ='c')
    trv.column("4", width = 80, anchor ='c')
    trv.column("5", width = 130, anchor ='c')
    trv.column("6", width = 130, anchor ='c')
    trv.column("7", width = 80, anchor ='c')
    trv.column("8", width = 130, anchor ='c')
    trv.column("9", width = 80, anchor ='c')
    # Headings  
    # respective columns
    trv.heading("1", text ="PNO")
    trv.heading("2", text ="Name")
    trv.heading("3", text ="Age")
    trv.heading("4", text ="Sex")  
    trv.heading("5", text ="Place")
    trv.heading("6", text ="Phone No")
    trv.heading("7", text ="Reference Doctor")  
    trv.heading("8", text ="Study")
    trv.heading("9", text ="Total")
    print(records[0])
    for dt in records: 
        trv.insert("", 'end',iid=dt[0], text=dt[0],
               values =(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[7],dt[8],dt[9]))
def edit():
    
    global name
    global age
    global sex
    global place
    global phone
    #global date
    global rdoc1
    global study1
    global total1
    global trv
    
    print(trv.selection)
    if not trv.selection():
       tm.showerror("Error","Please Select Data")
    else:
        currentitem=trv.focus()
        values=trv.item(currentitem)
        selection=values["values"]
        name.set(selection[1]);
        age.set(selection[2]);
        sex.set(selection[3]);
        place.set(selection[4]);
        phone.set(selection[5]);
        total1.set(selection[8]);
def save():
    global name
    global age
    global sex
    global place
    global phone
    global date
    global amount
    global expense
    global total1
    global pno
    global trv
    
    
    if not trv.selection():
       tm.showerror("Error","Please Selecet Data to Edit")
    else:
        currentitem=trv.focus()
        values=trv.item(currentitem)
        selection=values["values"]
        """ #name.set(selection[1]);
        #age.set(selection[2]);
        #sex.set(selection[3]);
        place.set(selection[4]);
        phone.set(selection[5]);
        total1.set(selection[8]);"""
        
        pno=selection[0]
        print(pno)
        if name== " "or age== " " or sex== " " or place==" " or phone== " " or  total1==" ":
            tm.showerror("Error","Please Enter all fields")
        else:
           mydb=mysql.connector.connect(
           host="localhost",
           user="root",
           passwd="",
           database="sms"
           )
           
           mycursor = mydb.cursor()
           sql=("update scan set name=%s,age=%s,sex=%s,place=%s,phoneno=%s,total=%s where pno=%s")
           data=(str(name.get()),str(age.get()),str(sex.get()),str(place.get()),str(phone.get()),str(total1.get()),str(pno))
           print(sql)
           print(data)
           mycursor.execute(sql,data)
           mydb.commit()
           tm.showinfo("INFO","Patient Details updated Sucessfully")
def delete():
   global trv
   if not trv.selection():
       tm.showerror('Error!', 'Please select an item from the database')
   else:
       current_item = trv.focus()
       values = trv.item(current_item)
       selection = values["values"]
       trv.delete(current_item)
       
       mycursor.execute('DELETE FROM scan WHERE pno=%d' % selection[0])
       mydb.commit()
       tm.showinfo('Done', 'The record is deleted successfully.')
    
def input():
    
    global name
    global age
    global sex
    global place
    global phone
    global date
    global rdoc1
    global study1
    global amount
    global expense
    global total1
    global listbox
    global listbox1
    global txttot
    global txtno
    global txtname
    global txtage
    global txtsex
    global txtplace
    global txtphone
    global txtdate
    global txtamt
    global txtic
    global f2ac
    name=StringVar()
    age=StringVar()
    sex=StringVar()
    place=StringVar()
    phone=StringVar()
    date=StringVar()
    rdoc1=StringVar()
    study1=StringVar()
    amount=StringVar()
    expense=StringVar()
    total1=StringVar()
    listbox=StringVar()
    listbox1=StringVar()
    
    date.set(time.strftime("%d/%m/%y"))
    top1 = Frame(top, height=50, bd=8, bg=color, relief="sunken")
    top1.pack(side=TOP)

    phead = Label(top1, font=('arial', 25, 'bold'), text=" Billing System", bg=color,bd=15,padx=12, anchor='w')
    phead.grid(row=0, column=0)

   

    f1 = Frame(top, height=850, bd=3, bg=color, relief="sunken")
    f1.pack(fill = BOTH, expand = True)

    f1a = Frame(f1, width=1500, height=330, bd=8, bg=color, relief="groove")
    f1a.pack(fill = BOTH, expand = True)
    
    f2a = Frame(f1, width=900, height=320, bd=8, bg=color, relief="groove")
    f2a.pack(side=BOTTOM)

    f1aa = Frame(f1a, width=400, height=430, bd=8, bg=color, relief="groove")
    f1aa.pack(side=LEFT)

    f1ab = Frame(f1a, width=1000, height=820, bd=8, bg=color, relief="groove")
    f1ab.pack(side=LEFT)

    f2aa = Frame(f2a, width=700, height=330, bd=8, bg=color, relief="groove")
    f2aa.pack(side=LEFT)

    f2ab = Frame(f2a, width=700, height=330, bd=8, bg=color, relief="groove")
    f2ab.pack(side=LEFT)

    f2ac = Frame(f1a, width=900, height=530, bd=8, bg=color, relief="groove")
    f2ac.pack(side=LEFT)
   

    lblname = Label(f1aa, font=('arial', 16, 'bold'),  text="Patient Name", bd=16, bg=color4, justify='left')
    lblname.grid(row=1, column=0)
    txtname = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=name,bd=10, insertwidth=2, justify='left')
    txtname.grid(row=1, column=1)

    lblage = Label(f1aa, font=('arial', 16, 'bold'), text="Age", bd=16, bg=color4, justify='left')
    lblage.grid(row=2, column=0)
    txtage = Entry(f1aa, font=('arial', 16, 'bold'),textvariable=age, bd=10, insertwidth=2, justify='left')
    txtage.grid(row=2, column=1)

    lblsex = Label(f1aa, font=('arial', 16, 'bold'), text="Sex", bd=16, bg=color4, justify='left')
    lblsex.grid(row=3, column=0)
    txtsex = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=sex, bd=10, insertwidth=2, justify='left')
    txtsex.grid(row=3, column=1)
    
    lblplace = Label(f1aa, font=('arial', 16, 'bold'), text="Place", bd=16, bg=color4, justify='left')
    lblplace.grid(row=4, column=0)
    txtplace = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=place, bd=10, insertwidth=2, justify='left')
    txtplace.grid(row=4, column=1)

    lblphone = Label(f1aa, font=('arial', 16, 'bold'), text="Phone No", bd=16, bg=color4, justify='left')
    lblphone.grid(row=5, column=0)
    txtphone= Entry(f1aa, font=('arial', 16, 'bold'), textvariable=phone, bd=10, insertwidth=2, justify='left')
    txtphone.grid(row=5, column=1)

    lbldate = Label(f1aa, font=('arial', 16, 'bold'), text="Date", bd=16, bg=color4, justify='left')
    lbldate.grid(row=6, column=0)
    txtdate = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=date, bd=10, insertwidth=2, justify='left')
    txtdate.grid(row=6, column=1)
    

    lblrdoc= Label(f1ab, font=('arial', 16, 'bold'), text="Doctor", bd=16, bg=color5, justify='left')
    lblrdoc.grid(row=0, column=0)

    listbox=Listbox(f1ab,exportselection=0,font=('arial', 12))
    listbox.insert(1,"Dr.AnbuSelvi")
    listbox.insert(2,"Dr.Sathyaseelan")
    listbox.insert(3,"Dr.RadhaLakshmi")
    listbox.insert(4,"Dr.Priyan")
    listbox.grid(row=0, column=1)

    lblstudy= Label(f1ab, font=('arial', 16, 'bold'), text=" Study", bd=16, bg=color5, justify='left')
    lblstudy.grid(row=1, column=0)

    listbox1=Listbox(f1ab,exportselection=0,font=('arial', 12))
    listbox1.insert(1,"Ultra Sound")
    listbox1.insert(2,"CT")
    listbox1.insert(3,"MRI")
    listbox1.insert(4,"X-Ray")
    listbox1.insert(5,"HSG")
    listbox1.grid(row=1, column=1)

    
    lblamt = Label(f2aa, font=('arial', 16, 'bold'), text="Amount", bd=16, bg=color6, justify='left')
    lblamt.grid(row=0, column=0)
    txtamt = Entry(f2aa, font=('arial', 16, 'bold'), textvariable=amount, bd=10, insertwidth=2, justify='left')
    txtamt.grid(row=0, column=1)
    lblic = Label(f2aa, font=('arial', 16, 'bold'), text="Expenses", bd=16, bg=color6, justify='left')
    lblic.grid(row=1, column=0)
    txtic = Entry(f2aa, font=('arial', 16, 'bold'), textvariable=expense, bd=10, insertwidth=2, justify='left')
    txtic.grid(row=1, column=1)
    lbltot= Label(f2aa, font=('arial', 16, 'bold'), text="Total", bd=16, bg=color6, justify='left')
    lbltot.grid(row=2, column=0)
    txttot = Entry(f2aa, font=('arial', 16, 'bold'),textvariable=total1,  bd=10, insertwidth=2, justify='left')
    txttot.grid(row=2, column=1)
   
    btnadd = Button(f2ab, padx=8, pady=8, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                  text="Add", bg=color,command=insert).grid(row=1, column=0)
    btnedit = Button(f2ab, padx=8, pady=8, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                  text="Edit", bg=color,command=edit).grid(row=1, column=1)
    btnsave = Button(f2ab, padx=8, pady=8, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                  text="Save", bg=color,command=save).grid(row=1, column=2)
    btnclear = Button(f2ab, padx=8, pady=8, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                  text="Clear", bg=color,command=clear).grid(row=2, column=0)
   
    btndel = Button(f2ab, padx=8, pady=8, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                  text="Delete",command=delete, bg=color).grid(row=2, column=1)
    btncon = Button(f2ab, padx=8, pady=8, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                  text="Consolidate",command=consolidate, bg=color).grid(row=2, column=2)
    btnbil = Button(f2ab, padx=8, pady=8, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                 text="Bill",command=bill, bg=color).grid(row=3, column=1)

    top.mainloop()
input()




    

