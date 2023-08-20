from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from random import randint 
from tkinter import messagebox
import mysql.connector


class Customer:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer Details")
        self.root.geometry("1285x550+235+225")

        # ===================variables================
        self.var_ref=StringVar()
        x=randint(1000,9999)
        self.var_ref.set(str(x))
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id=StringVar()
        self.var_id_no=StringVar()
        self.var_address=StringVar()
        self.var_post=StringVar()

        # ================title============
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="black",bd=4,fg="gold",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1285,height=50)

        #  ==============logo==============
        imgl=Image.open(r"images\logo.png")
        imgl=imgl.resize((47,47),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(imgl)

        lblimg=Label(self.root,image=self.photoimg,bd=2,relief=RIDGE)
        lblimg.place(x=0,y=0)


        # ================labelFrame==============
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)


        # =================labels and entries===============
        # Cust_ref
        cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        cust_ref.grid(row=0,column=0,sticky=W)

        cust_name=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13),justify="center",state="readonly")
        cust_name.grid(row=0,column=1)

        # Cust name
        cust_name=Label(labelframeleft,text="Name",font=("arial",12,"bold"),padx=2,pady=6)
        cust_name.grid(row=1,column=0,sticky=W)

        cust_name=ttk.Entry(labelframeleft,textvariable=self.var_name,width=29,font=("arial",13),justify="center")
        cust_name.grid(row=1,column=1)

        # gender combo
        gen=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
        gen.grid(row=2,column=0,sticky=W)

        gen=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12),width=27,state="readonly",justify="center")
        gen["values"]=["Select","Male","Female","Other"]
        gen.current(0)
        gen.grid(row=2,column=1)

        # mobile
        mobile=Label(labelframeleft,text="Mobile",font=("arial",12,"bold"),padx=2,pady=6)
        mobile.grid(row=3,column=0,sticky=W)

        mobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("arial",13),justify="center")
        mobile.grid(row=3,column=1)

        # email
        email=Label(labelframeleft,text="Email",font=("arial",12,"bold"),padx=2,pady=6)
        email.grid(row=4,column=0,sticky=W)

        email=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("arial",13),justify="center")
        email.grid(row=4,column=1)

        # nationality
        nat=Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        nat.grid(row=5,column=0,sticky=W)

        nat=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12),width=27,state="readonly",justify="center")
        nat["values"]=["Select","Indian","American","Other"]
        nat.current(0)
        nat.grid(row=5,column=1)

        # Id proof type
        proof=Label(labelframeleft,text="Id Proof Type",font=("arial",12,"bold"),padx=2,pady=6)
        proof.grid(row=6,column=0,sticky=W)
  
        proof=ttk.Combobox(labelframeleft,textvariable=self.var_id,font=("arial",12),width=27,state="readonly",justify="center")
        proof["values"]=["Select","Adhaar Card","Pan Card","Driving License","Passport","Other"]
        proof.current(0)
        proof.grid(row=6,column=1)

        # Id Number
        id=Label(labelframeleft,text="Id Number",font=("arial",12,"bold"),padx=2,pady=6)
        id.grid(row=7,column=0,sticky=W)

        id=ttk.Entry(labelframeleft,textvariable=self.var_id_no,width=29,font=("arial",13),justify="center")
        id.grid(row=7,column=1)


        # Address
        add=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        add.grid(row=8,column=0,sticky=W)

        add=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("arial",13),justify="center")
        add.grid(row=8,column=1)

        # post code
        post=Label(labelframeleft,text="Postal Code",font=("arial",12,"bold"),padx=2,pady=6)
        post.grid(row=9,column=0,sticky=W)

        post=ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("arial",13),justify="center")
        post.grid(row=9,column=1)

        # ====================btns====================
        btn_frame=Frame(labelframeleft,padx=5,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=415,height=35)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
        btn_reset.grid(row=0,column=3,padx=1)


        # ====================table_frame==========================
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",12,"bold"))
        tableframe.place(x=435,y=50,width=850,height=490)

        search=Label(tableframe,text="Search:",font=("arial",10,"bold"),padx=2,pady=2,bg="red",fg="white")
        search.grid(row=0,column=0,sticky=W,padx=2)

        self.var_search=StringVar()
        search=ttk.Combobox(tableframe,textvariable=self.var_search,font=("arial",12),width=20,state="readonly",justify="center")
        search["values"]=["Mobile","Ref","email"]
        search.current(0)
        search.grid(row=0,column=1,padx=2)

        self.var_search_txt=StringVar()
        id=ttk.Entry(tableframe,textvariable=self.var_search_txt,width=25,font=("arial",12),justify="center")
        id.grid(row=0,column=2,padx=2)

        btn_search=Button(tableframe,text="Search",command=self.search,font=("arial",10,"bold"),bg="black",fg="gold",width=20)
        btn_search.grid(row=0,column=3,padx=2)

        btn_show=Button(tableframe,text="Show All",command=self.fetch_data,font=("arial",10,"bold"),bg="black",fg="gold",width=19)
        btn_show.grid(row=0,column=4,padx=2)


        # ==========================Show data table======================
        details_table=Frame(tableframe,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=840,height=350)

        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)

        self.cust_details_table=ttk.Treeview(details_table,column=("Ref","Name","Gender","Mobile","Email","Nationality","Id","IdNo","Address","Post"),
                                                                    xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("Ref",text="Refer No")
        self.cust_details_table.heading("Name",text="Name")
        self.cust_details_table.heading("Gender",text="Gender")
        self.cust_details_table.heading("Mobile",text="Mobile")
        self.cust_details_table.heading("Email",text="Email")
        self.cust_details_table.heading("Nationality",text="Nationality")
        self.cust_details_table.heading("Id",text="Id Proof")
        self.cust_details_table.heading("IdNo",text="Id Number")
        self.cust_details_table.heading("Address",text="Address")
        self.cust_details_table.heading("Post",text="Postal Code")

        self.cust_details_table["show"]="headings"

        self.cust_details_table.column("Ref",width=100)
        self.cust_details_table.column("Name",width=100)
        self.cust_details_table.column("Gender",width=100)
        self.cust_details_table.column("Mobile",width=100)
        self.cust_details_table.column("Email",width=100)
        self.cust_details_table.column("Nationality",width=100)
        self.cust_details_table.column("Id",width=100)
        self.cust_details_table.column("IdNo",width=100)
        self.cust_details_table.column("Address",width=100)
        self.cust_details_table.column("Post",width=100)

        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","Missing Fields",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
                cursor=conn.cursor()
                cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_mobile.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_nationality.get(),
                                                                                            self.var_id.get(),
                                                                                            self.var_id_no.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_post.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Something went wrong :{str(es)}",parent=self.root)

    def update_data(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
            cursor=conn.cursor()
            cursor.execute("update customer set Name=%s,Gender=%s,Mobile=%s,Email=%s,Nationality=%s,Id=%s,IdNo=%s,Address=%s,Post=%s where Ref=%s",(
                                                                                                            self.var_name.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_mobile.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_nationality.get(),
                                                                                                            self.var_id.get(),
                                                                                                            self.var_id_no.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_post.get(),
                                                                                                            self.var_ref.get()))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Customer details updated successfully",parent=self.root)


    def delete_data(self):
        del_response=messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent=self.root)
        if del_response > 0:
            conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
            cursor=conn.cursor()
            cursor.execute("delete from customer where Ref=%s",(self.var_ref.get(),))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Customer deleted successfully",parent=self.root)
    
    def reset_data(self):
        x=randint(1000,9999)
        self.var_ref.set(str(x))
        self.var_name.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_id_no.set("")
        self.var_address.set("")
        self.var_post.set("")


    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
        cursor=conn.cursor()
        cursor.execute("select * from customer where "+str(self.var_search.get())+" LIKE '%"+str(self.var_search_txt.get())+"%'")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
        conn.commit()
        conn.close()


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
        cursor=conn.cursor()
        cursor.execute("Select * from customer")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)    
        conn.commit()
        conn.close()
        self.var_search_txt.set("")


    def get_cursor(self,event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_name.set(row[1])
        self.var_gender.set(row[2])
        self.var_mobile.set(row[3])
        self.var_email.set(row[4])
        self.var_nationality.set(row[5])
        self.var_id.set(row[6])
        self.var_id_no.set(row[7])
        self.var_address.set(row[8])
        self.var_post.set(row[9])



if __name__ == "__main__":
    root=Tk()
    obj=Customer(root)
    root.mainloop()