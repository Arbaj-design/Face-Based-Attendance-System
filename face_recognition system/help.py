from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("face Recognition System")


        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=768)

        img_top=Image.open(r"face_recognition system\images\train_page_photo1.jpg")
        img_top=img_top.resize((1366,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1366,height=325) 

        dev_label=Label(f_lbl,text="Email: team3@gmail.com",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=600,y=300)

if __name__ == "__main__":
     root=Tk()
     obj=Help(root)
     root.mainloop()