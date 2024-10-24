# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x690+1+1")
        self.root.title("student mangement system")
        self.root.configure(background="silver")
        self.root.resizable(False,False)
        title=Label(self.root,text="نظام ادارة الطلاب",
                    background="#1697E8",
                    font=("Cooper","12","bold"))
        title.pack(fill=X)
        #------------varibls----------------
        self.id_var=StringVar()
        self.name_var=StringVar()
        self.phone_var=StringVar()
        self.email_var=StringVar()
        self.cetri_var=StringVar()
        self.gender_var=StringVar()
        self.address_var=StringVar()
        self.serch_var=StringVar()
        self.delete_var=StringVar()
        self.se_by=StringVar()
        self.se_var=StringVar()


        #------------ادوات البرنامج-------------
        manage_frame=Frame(self.root,bg="white")
        manage_frame.place(x=1137,y=25,width=210,height=430)

        title=Label(manage_frame,text="البيانات اضافة ادوات",
                    font=("Consolas","14","bold"),
                    background="black",fg="#1697E8")
        title.pack(fill=X)
        lbl_id=Label(manage_frame,
                     text="التسلسلي الرقم",bg="white",
                     font=("Consolas","14","bold"))
        lbl_id.pack()
        id_entry=Entry(manage_frame,textvariable=self.id_var,bd="2",justify="center")
        id_entry.pack()
        lbl_name=Label(manage_frame,
                     text=" الطالب اسم",bg="white",
                     font=("Consolas","14","bold"))
        lbl_name.pack()
        name_entry=Entry(manage_frame,textvariable=self.name_var,bd="2",justify="center")
        name_entry.pack()
        lbl_email=Label(manage_frame,
                     text="الايميل",bg="white",
                     font=("Consolas","14","bold"))
        lbl_email.pack()
        email_entry=Entry(manage_frame,textvariable=self.email_var,bd="2",justify="center")
        email_entry.pack()
        lbl_phone=Label(manage_frame,
                     text="الهاتف رقم",bg="white",
                     font=("Consolas","14","bold"))
        lbl_phone.pack()
        phone_entry=Entry(manage_frame,textvariable=self.phone_var,bd="2",justify="center")
        phone_entry.pack()
        lbl_cetri=Label(manage_frame,
                     text="الطالب مؤهلات",bg="white",
                     font=("Consolas","14","bold"))
        lbl_cetri.pack()
        cetri_entry=Entry(manage_frame,textvariable=self.cetri_var,bd="2",justify="center")
        cetri_entry.pack()
        lbl_gender=Label(manage_frame,
                     text="الجنس",bg="white",
                     font=("Consolas","14","bold"))
        lbl_gender.pack()
        compo_gender=ttk.Combobox(manage_frame,textvariable=self.gender_var)
        compo_gender["value"]=("ذكر","انثي")
        compo_gender.pack()
        lbl_address=Label(manage_frame,
                     text=" الطالب عنوان",bg="white",
                     font=("Consolas","14","bold")
                     )
        lbl_address.pack()
        adress_entry=Entry(manage_frame,textvariable=self.address_var,bd="2",justify="center")
        adress_entry.pack()
        lbl_delete=Label(manage_frame,
                     text="طالب بيانات مسح",bg="white",
                     font=("Consolas","14","bold"))
        lbl_delete.pack()
        delete_entry=Entry(manage_frame,textvariable=self.delete_var,bd="2",justify="center")
        delete_entry.pack()
        btn_frame=Frame(self.root,bg="white")
        btn_frame.place(x=1137,y=460,width=235,height=420)
        title1=Label(btn_frame,text=" التحكم ادوات ",
                    font=("Consolas","14","bold"),
                    background="black",fg="#1697E8")
        title1.pack(fill=X)
        add_btn=Button(btn_frame,text="طالب اضاقة",
                       font=("Consolas","14","bold"),
                       bg="#1697E8",command=self.add_student)
        add_btn.pack(fill=X)
        delete_btn=Button(btn_frame,text="طالب حذف",
                       font=("Consolas","14","bold"),
                       bg="#1697E8",command=self.dele)
        delete_btn.pack(fill=X)
        update_btn=Button(btn_frame,text="طالب بيانات تعديل ",
                       font=("Consolas","14","bold"),
                       bg="#1697E8",command=self.update)
        update_btn.pack(fill=X)
        Empty_btn=Button(btn_frame,text="الحقول افراغ ",
                               font=("Consolas","14","bold"),
                       bg="#1697E8",
                       command=self.clear)
        Empty_btn.pack(fill=X)
        exit_btn=Button(btn_frame,text=" البرنامج اغلاق ",
                               font=("Consolas","14","bold"),
                       bg="#1697E8",command=root.quit)
        exit_btn.pack(fill=X)
        #----------serch manage-----------
        serch_frame=Frame(self.root,bg="white")
        serch_frame.place(x=1,y=25,width=1134,height=50)
        lbl_serch=Label(serch_frame,text="البحث عن طالب")
        lbl_serch.place(x=1034,y=12)
        compo_serch=ttk.Combobox(serch_frame,justify="right",textvariable=self.se_by)
        compo_serch["value"]=("id","name","email","phone")
        compo_serch.place(x=880,y=12)
        serch_entry=Entry(serch_frame,textvariable=self.se_var,justify="right",bd="2")
        serch_entry.place(x=750,y=12)
        serch_btn=Button(serch_frame,text="بحث",bg="#1697E8",fg="white",command=self.search)
        serch_btn.place(x=630,y=12,width=100,height=25)
        #--------treview--------------
        details_frame=Frame(self.root,bg="white")
        details_frame.place(x=1,y=77,width=1134,height=610)
        scroll_x=Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(details_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(details_frame,columns=("address","gender","cetri","phone","email","name","id"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        self.student_table.place(x=18,y=1,width=1120,height=587)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table["show"]="headings"
        self.student_table.heading("address",text="عنوان الطالب")
        self.student_table.heading("gender",text="جنس الطالب")
        self.student_table.heading("cetri",text="مؤهلات الطالب")
        self.student_table.heading("phone",text=" رقم الهاتف")
        self.student_table.heading("email",text=" ايميل الطالب")
        self.student_table.heading("name",text=" اسم الطالب")
        self.student_table.heading("id",text=" الرقم التسلسلي")
        self.student_table.column("address",width=125)
        self.student_table.column("gender",width=30)
        self.student_table.column("cetri",width=65)
        self.student_table.column("phone",width=65)
        self.student_table.column("email",width=70)
        self.student_table.column("name",width=100)
        self.student_table.column("id",width=17)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)



        self.fetch_all()
    def add_student(self): 
        con=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="student_mangemint_system"
        ) 
        cur=con.cursor()
        cur.execute("insert into student1 values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                self.address_var.get(),
                                                                self.gender_var.get(),
                                                                self.cetri_var.get(),
                                                                self.phone_var.get(),
                                                                self.email_var.get(),
                                                                self.name_var.get(),
                                                                self.id_var.get()
        )) 
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
        

    def fetch_all(self):
        con=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="student_mangemint_system"
        ) 
        cur=con.cursor()
        cur.execute("select * from student1 ")
        rows=cur.fetchall()
        if len (rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows :
                self.student_table.insert("",END,values=row)
                con.commit()
        con.close        

    def dele(self):
        con=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="student_mangemint_system"
        )
        cur=con.cursor()
        cur.execute("delete from student1 where phone =%s ",self.delete_var.get())
        con.commit()
        self.fetch_all()
        con.close()

    def clear (self):
        self.id_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.cetri_var.set("")
        self.gender_var.set("")
        self.address_var.set("")

    def get_cursor (self,ev):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content["values"]
        self.id_var.set(row[6])
        self.name_var.set(row[5])
        self.email_var.set(row[4])
        self.phone_var.set(row[3])
        self.cetri_var.set(row[2])
        self.gender_var.set(row[1])
        self.address_var.set(row[0])

    def update (self):
        con=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="student_mangemint_system"
        )
        cur=con.cursor()
        cur.execute("update student1 set address=%s , gender = %s , cetri = %s , phone = %s , email = %s , name = %s where id = %s ",(
                                                                self.address_var.get(),
                                                                self.gender_var.get(),
                                                                self.cetri_var.get(),
                                                                self.phone_var.get(),
                                                                self.email_var.get(),
                                                                self.name_var.get(),
                                                                self.id_var.get()
        )) 
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()

    def search(self):
            con=pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="student_mangemint_system"
            ) 
            cur=con.cursor()
            cur.execute("select * from student1 where " +
            str(self.se_by.get()) +" LIKE '%"+str(self.se_var.get())+"%'")
            rows=cur.fetchall()
            if len (rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows :
                    self.student_table.insert("",END,values=row)
                con.commit()
            con.close        
    def about (self):
        messagebox.showinfo("The company designed by creativity code ", "This application was programmed br Engineer Ahmed ibrahim")       

root = Tk()
ob = Student(root)

root.mainloop()
