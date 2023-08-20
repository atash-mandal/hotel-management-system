from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class forgotpass: 
    def __init__(self,root):
        self.root=root
        self.root.title("Reset Password")
        self.root.geometry("960x240+300+250")
        self.root.configure(bg="white")
        self.root.resizable(False,False)
   
        self.bg=ImageTk.PhotoImage(file=r"images\forgot.png")
        lbl_bg=Label(root,image=self.bg)
        lbl_bg.place(x=0,y=0)
    

        # username
        self.user=Label(root,text="Username",font=("times new roman",15),bg="white")
        self.user.place(x=475,y=25,width=100)

        self.userentry=ttk.Entry(root,font=("times new roman",12))
        self.userentry.place(x=575,y=25,width=270,height=30)    

        # security question
        self.sq=Label(root,text="Select Security Question",font=("times new roman",15),bg="white")
        self.sq.place(x=380,y=65)

        self.sqentry=ttk.Combobox(root,font=("times new roman",12),state="readonly")
        self.sqentry["values"]=["Select","Your favourite person","Your nick name","Your school name","Your Father's name"]
        self.sqentry.place(x=380,y=90,width=270,height=30)
        self.sqentry.current(0)

        # answer
        self.sqans=Label(root,text="Security Answer",font=("times new roman",15),bg="white")
        self.sqans.place(x=670,y=65)

        self.sqansentry=ttk.Entry(root,font=("times new roman",12))
        self.sqansentry.place(x=670,y=90,width=270,height=30)

        # New Password
        self.np=Label(root,text="New Password",font=("times new roman",15),bg="white")
        self.np.place(x=380,y=130)

        self.npentry=ttk.Entry(root,font=("times new roman",12))
        self.npentry.place(x=380,y=155,width=270,height=30)

        # Confirm Password
        self.cp=Label(root,text="Confirm Password",font=("times new roman",15),bg="white")
        self.cp.place(x=670,y=130)

        self.cpentry=ttk.Entry(root,font=("times new roman",12))
        self.cpentry.place(x=670,y=155,width=270,height=30)


        # reset button
        reset_btn=Button(root,text="RESET",command=self.reset,font=("times new roman",15,"bold"),cursor="hand2",borderwidth=0,fg="white",bg="purple",activeforeground="black",activebackground="green")
        reset_btn.place(x=610,y=195,width=100)
    
    def reset(self):
        if self.userentry.get()=="":
            messagebox.showerror("Error","Invalid username",parent=self.root)
        elif self.sqentry.get()=="Select":
            messagebox.showerror("Error","Please select a security question!",parent=self.root)
        elif self.cpentry.get()!=self.npentry.get():
            messagebox.showerror("Error","Confirm password must be same as new password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="jeet@sql.123",database="pharma_manage")
            mycur=conn.cursor()
            mycur.execute("select * from register where email=%s and securityQ=%s and securityA=%s",(
                                                                                    self.userentry.get(),
                                                                                    self.sqentry.get(),
                                                                                    self.sqansentry.get()))
            row=mycur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password!",parent=self.root)
            else:
                mycur.execute("update register set password=%s where email=%s",(self.npentry.get(),
                                                                                self.userentry.get()))
                messagebox.showinfo("Success","Password reset successfull",parent=self.root)
                self.root.destroy()

            conn.commit()
            conn.close()


if __name__=="__main__":
    root=Tk()
    app=forgotpass(root)
    root.mainloop()  