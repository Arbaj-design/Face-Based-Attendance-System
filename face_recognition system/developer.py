from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=50)

        img_top=Image.open(r"face_recognition system\images\train_page_photo1.jpg")
        img_top=img_top.resize((1366,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1366,height=325) 

        # Frame
        main_frame=Frame(f_lbl ,bd=2)
        main_frame.place(x=850,y=0,width=500,height=580)

        img_top1=Image.open(r"face_recognition system\images\face.jpg")
        img_top1=img_top.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=250,y=0,width=200,height=200) 

        #Developer info
        dev_label=Label(main_frame,text="Hello my name is Avaiz",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am CSE student",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        img2=Image.open(r"face_recognition system\images\college.jpg")
        img2=img2.resize((400,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=400,height=200)


if __name__ == "__main__":
     root=Tk()
     obj=Developer(root)
     root.mainloop()