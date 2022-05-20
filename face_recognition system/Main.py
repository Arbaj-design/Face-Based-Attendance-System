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

# $$$$$@$$$$$
# after vidoe4
#comment the lines 134,138
#uncomment the lines   7,135,139,165 to


class Face_Recognition_System :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        

        #first image
        # img=Image.open(r"face_recognition system\images\college.jpg") #geca logo should be paste here and at photo 3 as well
        # img=img.resize((455,120),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

        img=Image.open(r"images\final-logo.png") #geca logo should be paste here and at photo 3 as well
        img=img.resize((1366,120),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1366,height=120)
        

        #Second image
        img1=Image.open(r"images\face.jpg")
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
        img3=Image.open(r"images\background_image.jpg")
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
        img4=Image.open(r"images\student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=270,width=220,height=40)

        #Detect face button
        img5 =Image.open(r"images\face detect.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=270,width=220,height=40)

        
        
        #Attendance face button
        img6 =Image.open(r"images\left-label.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=270,width=220,height=40)


         
         
         #Help  desk button
        img7 =Image.open(r"images\help_desk.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk ",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=270,width=220,height=40)


        #Train face button
        img8=Image.open(r"images\train.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=320,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=520,width=220,height=40)
 

         #photos face button
        img9=Image.open(r"images\photo.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        # b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)    
        b1.place(x=400,y=320,width=220,height=220)

        # b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white",command=self.open_img)
        b1_1.place(x=400,y=520,width=220,height=40)


         #Developer face button
        img10=Image.open(r"images\developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=320,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=520,width=220,height=40)
 
        #Exit face button
        img11=Image.open(r"images\Exit.jpg")
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
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

   