from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")
        
        
        # varibles
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        
        #1st
        img=Image.open(r"D:\Student Management System\college_images\st1.jpg")
        img=img.resize((500, 130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        self.btn_1=Button(self.root,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=500,height=130)
        
         #2nd
        img_2=Image.open(r"D:\Student Management System\college_images\cg.jpg")
        img_2=img_2.resize((500, 130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        self.btn_2=Button(self.root,image=self.photoimg_2,cursor="hand2")
        self.btn_2.place(x=500,y=0,width=450,height=130)
        
         #3rd
        img_3=Image.open(r"D:\Student Management System\college_images\st2.jpg")
        img_3=img_3.resize((500, 130),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)
        self.btn_3=Button(self.root,image=self.photoimg_3,cursor="hand2")
        self.btn_3.place(x=950,y=0,width=500,height=130)
        
         #bg
        img_4=Image.open(r"D:\Student Management System\college_images\st3.jpg")
        img_4=img_4.resize((1366, 780),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)
        
        bg_lbl=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=130,width=1366,height=780)
        
        lbl_title=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",18,"bold"),bg="lightblue",fg="darkred")
        lbl_title.place(x=0,y=0,width=1366,height=30)
        
        main_frame=Frame(bg_lbl,bd=2,bg="white",relief=RIDGE)
        main_frame.place(x=5,y=32,width=1343,height=530)
        
         # left side frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,fg="red",text="Students Information",font=("times new roman",12,"bold"))
        Left_frame.place(x=2,y=0,width=660,height=522)

        img_5=Image.open(r"D:\Student Management System\college_images\st3.jpg")
        img_5=img_5.resize((660, 90),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        my_img=Label(Left_frame,image=self.photoimg_5)
        my_img.place(x=2,y=0,width=660,height=90)

        # current course informatiom
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",fg="red",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=90,width=648,height=108)

        #Department
        dep_label=Label(current_course_frame,text="Department :",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=5)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","IT","CMP","CIVIL"," MBBS")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        # course
        course_label=Label(current_course_frame,text="Course :",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select Course","BE","BSC","MEDICAL","MGMT")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=8,sticky=W)
        # Year
        year_label=Label(current_course_frame,text="Year :",font=("times new roman",12,"bold"),bg="pink")
        year_label.grid(row=1,column=0,padx=2,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","2019-20","2020-21","2021-22","2022-23")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=8,sticky=W)

        # Semester
        semester_label=Label(current_course_frame,text="Semester :",font=("times new roman",12,"bold"),bg="yellow")
        semester_label.grid(row=1,column=2,padx=2,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=17)
        semester_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=8,sticky=W)

        # class student informatiom
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=2,y=200,width=650,height=298)

        # student id
        studentId_label=Label(class_Student_frame,text="StudentID :",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=2,pady=4,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_id,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=8,pady=4,sticky=W)

        # student name
        studentName_label=Label(class_Student_frame,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=2,pady=4,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=8,pady=4,sticky=W)

        # class division
        class_div_label=Label(class_Student_frame,text="Class Division :",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=2,pady=4,sticky=W)

        # class_div_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_div,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=8,pady=4,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,width=18,font=("times new roman",12,"bold"),state="readonly")
        div_combo["values"]=("Select Division","A","B","C","D","E","Other")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=8,pady=4,sticky=W)

        # Roll no
        roll_no_label=Label(class_Student_frame,text="Roll No :",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=2,pady=4,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=8,pady=4,sticky=W)

        # Gender
        gender_label=Label(class_Student_frame,text="Gender :",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=2,pady=4,sticky=W)

        # gender_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_gender,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=8,pady=4,sticky=W)
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=18,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Select gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=8,pady=4,sticky=W)

        # dob
        dob_label=Label(class_Student_frame,text="DOB :",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=2,pady=4,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_dob,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=8,pady=4,sticky=W)

        # Email
        email_label=Label(class_Student_frame,text="Email :",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=2,pady=4,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=8,pady=4,sticky=W)

        # phone no
        phone_label=Label(class_Student_frame,text="Phone No :",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=2,pady=4,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_phone,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=8,pady=4,sticky=W)

        # Address
        address_label=Label(class_Student_frame,text="Address :",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=2,pady=4,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_address,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=8,pady=4,sticky=W)

        # Teacher Name
        teacher_label=Label(class_Student_frame,text="Teacher Name :",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=2,pady=4,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=8,pady=4,sticky=W)

        # # radio buttons
        # self.var_radio1=StringVar()
        # radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        # radiobtn1.grid(row=5,column=0)

        # radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        # radiobtn2.grid(row=5,column=1)

        # button frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=1,y=190,width=642,height=35)

        save_button=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0)

        update_button=Button(btn_frame,text="Update",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=1)
        
        delete_button=Button(btn_frame,text="Delete",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_button.grid(row=0,column=2)

        reset_button=Button(btn_frame,text="Reset",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)

        # btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        # btn_frame1.place(x=1,y=230,width=642,height=35)

        # # take_photo_button=Button(btn_frame1,text="Take Photo Sample",width=35,font=("times new roman",12,"bold"),bg="red",fg="white")
        # take_photo_button.grid(row=0,column=0)

        # update_photo_button=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",12,"bold"),bg="red",fg="white")
        # update_photo_button.grid(row=0,column=1)
        
        # right side frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",fg="red",relief=RIDGE,text="Students Information",font=("times new roman",12,"bold"))
        Right_frame.place(x=670,y=0,width=660,height=522)

        img_right=Image.open(r"D:\Student Management System\college_images\pp.jpg")
        img_right=img_right.resize((660, 90),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=2,y=0,width=660,height=90)
        
        # search system

        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=90,width=648,height=60)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",14,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=2,pady=4,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=12)
        search_combo["values"]=("Select","Student_Id","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        search_entry=ttk.Entry(search_frame,width=14,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=8,pady=4,sticky=W)


        search_button=Button(search_frame,text="Search",width=14,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_button.grid(row=0,column=3,padx=3)
        
        showAll_button=Button(search_frame,text="Show All",width=14,font=("times new roman",10,"bold"),bg="blue",fg="white")
        showAll_button.grid(row=0,column=4,padx=3)
        # table frame and scrollbar
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=155,width=648,height=340)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year") 
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100) 
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=130)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=130)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=130)
        self.student_table.column("teacher",width=130)
   

        self.student_table.pack(fill=BOTH,expand=1)
        # self.student_table.bind("<ButtonRelease>",self.get_cursor)
        # self.fetch_data()
        
    # function decleration
    def add_data(self):
        if self.var_dep.get()== "Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="" :
            messagebox.showerror("Error","All Fields are Required, Smile please.",parent=self.root) 
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Nabin@.1?",database="student_mgmt")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get()
                                                                                                              
                                                                                                                

                                                                                                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student Details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)


    # #  fetch data to table from databasse 
    
    # def fetch_data(self):
    #     conn=mysql.connector.connect(host="localhost",username="root",password="Nabin@.1?",database="face_recognizer")
    #     my_cursor=conn.cursor()
    #     my_cursor.execute("select * from student")
    #     data=my_cursor.fetchall()
        
    #     if len(data)!=0:
    #         self.student_table.delete(*self.student_table.get_children())
    #         for i in data:
    #             self.student_table.insert("",END,values=i)
    #         conn.commit()    
    #     conn.close()        
       
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()        