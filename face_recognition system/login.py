from email.headerregistry import HeaderRegistry
from re import M
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import tkinter
import PIL
from PIL import Image
from PIL import ImageTk
from student import Student
import os  
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime 

from student import Student


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        
       self.root=root
       self.root.title("Login")
       #self.root.geometry=("1550x900+0+0")
       self.root.geometry("1366x768+0+0")

       bgimg=Image.open(r"face_recognition system\images\train.jpg")  #line 42 43 44 added by me
       bgimg=bgimg.resize((1366,768),Image.ANTIALIAS)
       self.bg=ImageTk.PhotoImage(bgimg)

    #    self.bg=ImageTk.PhotoImage(file=r"images\train.jpg")  
       lbl_bg=Label(self.root,image=self.bg)
       lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


       frame=Frame(self.root, bg="black")
       frame.place(x=610,y=170,width=340,height=450)

       img1=Image.open(r"face_recognition system\images\photo.jpg")   # change photo
       img1=img1.resize((100,100),Image.ANTIALIAS)
       self.photoimage1=ImageTk.PhotoImage(img1)
       lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
       lblimg1.place(x=730,y=175,width=100,height=100)

       get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
       get_str.place(x=95,y=100)

       #labels
       username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
       username.place(x=70,y=155)

       self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
       self.txtuser.place(x=40,y=180,width=270)

       password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
       password.place(x=70,y=225)

       self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
       self.txtpass.place(x=40,y=250,width=270)

       # =====Icon Images======

       img2=Image.open(r"face_recognition system\images\photo.jpg")   #login photo location
       img2=img2.resize((25,25),Image.ANTIALIAS)
       self.photoimage2=ImageTk.PhotoImage(img2)
       lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
       lblimg1.place(x=650,y=323,width=25,height=25)

       img3=Image.open(r"face_recognition system\images\photo.jpg")  #password photo
       img3=img3.resize((25,25),Image.ANTIALIAS)
       self.photoimage3=ImageTk.PhotoImage(img2)
       lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
       lblimg1.place(x=650,y=397,width=25,height=25)
       
       #loginbutton
       loginbtn=Button(frame,command=self.login,text="Login", font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
       loginbtn.place(x=110,y=300,width=120,height=35)

       #registerButton
       loginbtn=Button(frame,text="New User Register",command=self.register_window, font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
       loginbtn.place(x=15,y=350,width=160)

       #forgetpasswordbtn
       loginbtn=Button(frame,text="ForgetPassword",command=self.forgot_password_window, font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
       loginbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    

    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All field required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success", "Welcome to face regognize system")
        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="Nadeem@786", database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                         self.txtuser.get(),
                                                                                         self.txtpass.get()
                                                                                     ))
            row=my_cursor.fetchone()
            #print(Row)
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo", "Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return 
            conn.commit()
            conn.close()

 #==========================reset window===========================
    def reset_password(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="Nadeem@786", database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your paassword haas been reset, pleaase login new password",parent=self.root2)
                self.root2.destroy()

#============================Forgte password window=====================================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="Nadeem@786", database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your school Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman", 15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)
  
 
   





class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")  #200x150

        #=================variables=================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()


         #========bg image===============
        bgimg=Image.open(r"face_recognition system\images\train.jpg")  
        bgimg=bgimg.resize((1366,768),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bgimg)

        #    self.bg=ImageTk.PhotoImage(file=r"images\train.jpg")  
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        

       #=========left image========
        left_lbl=Image.open(r"face_recognition system\images\train.jpg")  
        left_lbl=left_lbl.resize((1366,768),Image.ANTIALIAS)
        self.bg1=ImageTk.PhotoImage(left_lbl)

        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
        # self.bg1=ImageTk.PhotoImage(file=r"images\left_image_register.jpg")   #change photo
        # left_lbl=Label(self.root,image=self.bg1)
        # left_lbl.place(x=50,y=100,width=470,height=550)
        
        #=======main frame===========
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green")
        register_lbl.place(x=20,y=20)

        #==label and entry===

        #=====row1========
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #-----row2-------

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)


        #-=---row3======
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your school Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #----row4=======

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_security.place(x=50,y=340,width=250)

        
        pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=370,y=310)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_security.place(x=370,y=340,width=250)

        #======checkbutton=======
        checkbtn=Checkbutton(frame, variable=self.var_check,text="I Agree The Term & Conditons", font=("times new roman", 12, "bold"), onvalue=1,offvalue=0)
        checkbtn.place(x=50, y=380)


        #==================button===============
        img=Image.open(r"face_recognition system\images\photo.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=10,y=420,width=200)

        img1=Image.open(r"face_recognition system\images\photo.jpg")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=330,y=420,width=200)


        #===============================function decalaration===================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select": 
                messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
                messagebox.showerror("Error", "Please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="Nadeem@786", database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                         self.var_fname.get(),
                                                                                         self.var_lname.get(),
                                                                                         self.var_contact.get(),
                                                                                         self.var_email.get(),
                                                                                         self.var_securityQ.get(),
                                                                                         self.var_securityA.get(),
                                                                                         self.var_pass.get()

                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register successfull")



class Face_Recognition_System :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        

        #first image
        # img=Image.open(r"face_recognition system\images\college.jpg") #geca logo should be paste here and at photo 3 as well
        # img=img.resize((455,120),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

        img=Image.open(r"face_recognition system\images\final-logo.png") #geca logo should be paste here and at photo 3 as well
        img=img.resize((1366,120),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1366,height=120)
        

        #Second image
        img1=Image.open(r"face_recognition system\images\face.jpg")
        img1=img1.resize((455,120),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=455,y=0,width=455,height=120)

        

        #third image
        # img2=Image.open(r"face_recognition system\images\college.jpg")
        # img2=img2.resize((455,120),Image.ANTIALIAS)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=910,y=0,width=455,height=120)



        #background image 
        img3=Image.open(r"face_recognition system\images\background_image.jpg")
        img3=img1.resize((1366,648),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=120,width=1366,height=648)

        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        # ======== time =============
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl, font = ('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0 ,width=110,height=50)
        time()        
        
        #student button
        img4=Image.open(r"face_recognition system\images\student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=270,width=220,height=40)

        #Detect face button
        img5 =Image.open(r"face_recognition system\images\face detect.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=270,width=220,height=40)

        
        
        #Attendance face button
        img6 =Image.open(r"face_recognition system\images\left-label.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=270,width=220,height=40)


         
         
         #Help  desk button
        img7 =Image.open(r"face_recognition system\images\help_desk.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk ",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=270,width=220,height=40)


        #Train face button
        img8=Image.open(r"face_recognition system\images\train.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=320,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=520,width=220,height=40)
 

         #photos face button
        img9=Image.open(r"face_recognition system\images\photo.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        # b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)    
        b1.place(x=400,y=320,width=220,height=220)

        # b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white",command=self.open_img)
        b1_1.place(x=400,y=520,width=220,height=40)


         #Developer face button
        img10=Image.open(r"face_recognition system\images\developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=320,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=520,width=220,height=40)
 
        #Exit face button
        img11=Image.open(r"face_recognition system\images\Exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=320,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=520,width=220,height=40)

# (((((((())))))))
# # uncomment after video4
    def open_img(self):
        os.startfile("face_recognition system\data")

# # (((((((())))))))
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

    # ============Functions=================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


            
















if __name__ == "__main__":
    main()