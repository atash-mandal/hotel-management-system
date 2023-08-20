from tkinter import*
from PIL import Image,ImageTk
from customer import Customer
from booking import Booking
from details import Details



class hotel:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel")
        self.root.geometry("1550x800+0+0")
        # =============1st image=========
        img1=Image.open(r"images\hotelbg.png")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg1=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=0,width=1550,height=140)
 
        # ==============logo==============
        img2=Image.open(r"images\logo.png")
        img2=img2.resize((140,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=0,width=140,height=140)

        # ==================title=================
        lbl_title=Label(self.root,text="HOUSTON MANAGEMENT",font=("times new roman",40,"bold"),bg="black",fg="gold",relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        # =================main frame==================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        # =================menu======================
        lbl_title=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bd=4,bg="black",fg="gold",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=230,height=50)
        
        # ===================btn frame===================
        btn_frame=Frame(main_frame,bd=0,relief=RIDGE)
        btn_frame.place(x=0,y=50,width=230,height=190)

        # ===================btns=====================
        cust_btn=Button(btn_frame,command=self.cust_details,text="CUSTOMER",bd=2,font=("times new roman",15,"bold"),bg="black",fg="gold",relief=RIDGE)
        cust_btn.place(x=0,y=0,width=230,height=30)

        room_btn=Button(btn_frame,text="ROOM",command=self.book_details,font=("times new roman",15,"bold"),bg="black",fg="gold",relief=RIDGE)
        room_btn.place(x=0,y=30,width=230,height=30)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details,font=("times new roman",15,"bold"),bg="black",fg="gold",relief=RIDGE)
        details_btn.place(x=0,y=60,width=230,height=30)

        report_btn=Button(btn_frame,text="REPORT",font=("times new roman",15,"bold"),bg="black",fg="gold",relief=RIDGE)
        report_btn.place(x=0,y=90,width=230,height=30)

        logout_btn=Button(btn_frame,text="LOG OUT",command=self.logout,font=("times new roman",15,"bold"),bg="black",fg="gold",relief=RIDGE)
        logout_btn.place(x=0,y=120,width=230,height=30)

    def cust_details(self):
        self.new_win=Toplevel(self.root)
        self.app=Customer(self.new_win)

    def book_details(self):
        self.new_win=Toplevel(self.root)
        self.app=Booking(self.new_win)
    
    def details(self):
        self.new_win=Toplevel(self.root)
        self.app=Details(self.new_win)
    
    def logout(self):
        self.root.destroy()

if __name__=="__main__":
    root=Tk()
    obj=hotel(root)
    root.mainloop()