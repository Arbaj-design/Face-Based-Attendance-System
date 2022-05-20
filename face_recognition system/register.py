from atexit import register
from cProfile import label
import email
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

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



      
      


        












if __name__ =="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
