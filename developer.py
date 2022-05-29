from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        
        title_lbl=Label(self.root,text="DEVELOPER", font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_images\dev.png")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
      
      #FRAME

        main_frame = Frame(f_lbl,bd=2,bg="yellow")
        main_frame.place(x=640,y=320,width=450,height=220)

        img_top1=Image.open(r"college_images\ishhh.jpeg")
        img_top1=img_top1.resize((200,220),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=250,y=0,width=200,height=220)


        #Department
        dev_label=Label(main_frame,text="Ishika Raj",font=("times new roman",20,"bold"),bg="yellow")
        dev_label.place(x=0,y=20)

        dev_label=Label(main_frame,text="Btech CSE",font=("times new roman",20,"bold"),bg="yellow")
        dev_label.place(x=0,y=55)

        dev_label=Label(main_frame,text="Software Developer",font=("times new roman",20,"bold"),bg="yellow")
        dev_label.place(x=0,y=90)

        dev_label=Label(main_frame,text="Web Developer",font=("times new roman",20,"bold"),bg="yellow")
        dev_label.place(x=0,y=125)
      
      





if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()        