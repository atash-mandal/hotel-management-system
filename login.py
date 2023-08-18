from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from register import Register
from forgotpass import forgotpass
from hotel import hotel

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"images\login bg.webp")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:images\login avatar.webp")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lbl_img1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started", font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)

        # label
        username_lbl=Label(frame,text="Username", font=("times new roman",15),fg="black",bg="white")
        username_lbl.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame, font=("times new roman",15))
        self.txtuser.place(x=40,y=185,width=240,height=30)


        password_lbl=Label(frame,text="Password", font=("times new roman",15),fg="black",bg="white")
        password_lbl.place(x=70,y=235)

        self.txtpass=ttk.Entry(frame,show="*", font=("times new roman",15))
        self.txtpass.place(x=40,y=265,width=240,height=30)


        imgpp=Image.open(r"images\show.png")
        imgpp=imgpp.resize((30,30),Image.LANCZOS)
        self.imgp=ImageTk.PhotoImage(imgpp)
        self.toggle_btn=Button(frame,image=self.imgp,command=self.toggle_password,borderwidth=0,cursor="hand2",bg="white")
        self.toggle_btn.place(x=280,y=265)

        # ====Icon Images======
        img2=Image.open(r"images\user.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(frame,image=self.photoimage2,bg="white",borderwidth=0)
        lbl_img2.place(x=40,y=155,width=25,height=25)

        img3=Image.open(r"images\password.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(frame,image=self.photoimage3,bg="white",borderwidth=0)
        lbl_img3.place(x=40,y=235,width=25,height=25)

        # login button
        lgn_btn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=2,relief=RAISED,fg="white",bg="red",activeforeground="white",activebackground="green")
        lgn_btn.place(x=110,y=320,width=120,height=35)

        regbtn=Button(frame,command=self.register_window,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="blue",activebackground="white")
        regbtn.place(x=40,y=375)

        forgetbtn=Button(frame,text="Forget Password",command=self.forgot_pass,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="blue",activebackground="white")
        forgetbtn.place(x=215,y=375)
    
    def toggle_password(self):
        if self.txtpass.cget('show')=="":
            self.txtpass.config(show="*")
            imgg=Image.open(r"images\show.png")
            imgg=imgg.resize((30,30),Image.LANCZOS)
            self.imggg=ImageTk.PhotoImage(imgg)
            self.toggle_btn.config(image=self.imggg)
        else:
            self.txtpass.config(show="")
            imgg=Image.open(r"images\hide.png")
            imgg=imgg.resize((30,30),Image.LANCZOS)
            self.imggg=ImageTk.PhotoImage(imgg)
            self.toggle_btn.config(image=self.imggg)

    def forgot_pass(self):
        self.new_window=Toplevel(self.root)
        self.app=forgotpass(self.new_window)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error!","All fields required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="jeet@sql.123",database="management")
            mycur=conn.cursor()
            mycur.execute("select * from register where email=%s and password=%s",(
                                                                    self.txtuser.get(),
                                                                    self.txtpass.get()))
            row=mycur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password!")
            else:
                open_main=messagebox.askyesno("Yes/No","Access only admin")
                if open_main > 0:
                    self.new_window=Toplevel(self.root)
                    self.app=hotel(self.new_window)
                else:
                    self.txtpass.delete(0,'end')
                    self.txtuser.delete(0,'end')
                    return

            conn.commit()
            conn.close()



if __name__=="__main__":
    root=Tk()
    app=login_window(root)
    root.mainloop()  