from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar() 
        self.var_check=IntVar()

        # bg image
        self.bg=ImageTk.PhotoImage(file=r"images\reg bg.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # left image
        self.bg1=ImageTk.PhotoImage(file=r"images\reg lft.png")
        bg_lbl1=Label(self.root,image=self.bg1)
        bg_lbl1.place(x=50,y=100,width=470,height=550)

        # Frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        #label
        self.reglbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        self.reglbl.place(x=50,y=20)

        # labels and entries
        # first name
        self.fname=Label(frame,text="First Name",font=("times new roman",15),bg="white")
        self.fname.place(x=50,y=100)

        self.fnameentry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",12))
        self.fnameentry.place(x=50,y=130,width=250,height=30)

        # last name
        self.lname=Label(frame,text="Last Name",font=("times new roman",15),bg="white")
        self.lname.place(x=450,y=100)

        self.lnameentry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",12))
        self.lnameentry.place(x=450,y=130,width=250,height=30)

        # ph number
        self.pno=Label(frame,text="Contact No",font=("times new roman",15),bg="white")
        self.pno.place(x=50,y=175)

        self.pnoentry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",12))
        self.pnoentry.place(x=50,y=205,width=250,height=30)

        # email
        self.email=Label(frame,text="Email Id",font=("times new roman",15),bg="white")
        self.email.place(x=450,y=175)

        self.emailentry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",12))
        self.emailentry.place(x=450,y=205,width=250,height=30)

        # password
        self.pas=Label(frame,text="Password",font=("times new roman",15),bg="white")
        self.pas.place(x=50,y=250)

        self.pasentry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",12))
        self.pasentry.place(x=50,y=280,width=250,height=30)

        # confirm password
        self.cpas=Label(frame,text="Confirm Password",font=("times new roman",15),bg="white")
        self.cpas.place(x=450,y=250)

        self.cpasentry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",12))
        self.cpasentry.place(x=450,y=280,width=250,height=30)

        # security question
        self.sq=Label(frame,text="Select Security Question",font=("times new roman",15),bg="white")
        self.sq.place(x=50,y=325)

        self.sqentry=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",12),state="readonly")
        self.sqentry["values"]=["Select","Your favourite person","Your nick name","Your school name","Your Father's name"]
        self.sqentry.place(x=50,y=355,width=250,height=30)
        self.sqentry.current(0)

        # answer
        self.sqans=Label(frame,text="Security Answer",font=("times new roman",15),bg="white")
        self.sqans.place(x=450,y=325)

        self.sqansentry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",12))
        self.sqansentry.place(x=450,y=355,width=250,height=30)

        # checkbox
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=400)

        # buttons
        imgr=Image.open(r"images\register5.png")
        imgr=imgr.resize((200,50),Image.LANCZOS)
        self.regimg=ImageTk.PhotoImage(imgr)
        b1=Button(frame,command=self.register_data,image=self.regimg,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=75,y=450)

        imgl=Image.open(r"images\login1.png")
        imgl=imgl.resize((200,50),Image.LANCZOS)
        self.logimg=ImageTk.PhotoImage(imgl)
        b2=Button(frame,command=self.des_login,image=self.logimg,borderwidth=0,cursor="hand2",bg="white")
        b2.place(x=475,y=450)


    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & confirm password must be same!",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terma and conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="jeet@sql.123",database="management")
            mycur=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            mycur.execute(query,value)
            row=mycur.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, please try another email!",parent=self.root)
            else:
                mycur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_pass.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully!")

    def des_login(self):
        self.root.destroy()

if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()