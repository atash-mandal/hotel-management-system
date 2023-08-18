from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from time import strftime
from tkinter import messagebox
import mysql.connector

class Booking:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Booking")
        self.root.geometry("1285x550+235+225")

        # ==================variables================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_room=StringVar()
        self.var_av_room=StringVar()
        self.var_meals=StringVar()
        self.var_noofdays=StringVar()
        self.var_tax=StringVar()
        self.var_subtotal=StringVar()
        self.var_total=StringVar()

        # ================title================
        lbl_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",20,"bold"),bg="black",bd=4,fg="gold",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1285,height=50)

        #  ==============logo==============
        imgl=Image.open(r"images\logo.png")
        imgl=imgl.resize((47,47),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(imgl)

        lblimg=Label(self.root,image=self.photoimg,bd=2,relief=RIDGE)
        lblimg.place(x=0,y=0)

        # ================labelFrame==============
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Booking Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)

        # =================labels and entries===============
        # Cust_contact
        cust_con=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        cust_con.grid(row=0,column=0,sticky=W)

        cust_con=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13),justify="center")
        cust_con.grid(row=0,column=1,sticky=W)

        btn_fetch=Button(labelframeleft,command=self.fetch_contact,text="Fetch Details",font=("arial",8,"bold"),bg="black",fg="gold",width=9)
        btn_fetch.place(x=340,y=4)

        # Cust checkin
        checkin=Label(labelframeleft,text="Check in",font=("arial",12,"bold"),padx=2,pady=6)
        checkin.grid(row=1,column=0,sticky=W)

        checkin=DateEntry(labelframeleft,textvariable=self.var_checkin,width=27,font=("arial",12),justify="center",selectmode = "day",date_pattern="dd/mm/y")
        checkin.grid(row=1,column=1,sticky=W)

        # Cust checkout
        checkout=Label(labelframeleft,text="Check Out",font=("arial",12,"bold"),padx=2,pady=6)
        checkout.grid(row=2,column=0,sticky=W)

        checkout=DateEntry(labelframeleft,textvariable=self.var_checkout,width=27,font=("arial",12),justify="center",selectmode = "day",date_pattern="dd/mm/y")
        checkout.grid(row=2,column=1,sticky=W)

        # room combo
        room=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        room.grid(row=3,column=0,sticky=W)

        room=ttk.Combobox(labelframeleft,textvariable=self.var_room,font=("arial",12),width=27,state="readonly",justify="center")
        room["values"]=["Single","Double","Deluxe","Suite"]
        room.current(0)
        room.grid(row=3,column=1)

        # available room
        av_room=Label(labelframeleft,text="Available Room",font=("arial",12,"bold"),padx=2,pady=6)
        av_room.grid(row=4,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
        cursor=conn.cursor()
        cursor.execute("select roomno from details where roomtype=%s",(self.var_room.get(),))
        rows=cursor.fetchall()
        print(rows)
        conn.commit()
        conn.close()
        av_room=ttk.Combobox(labelframeleft,textvariable=self.var_av_room,font=("arial",12),width=27,state="readonly",justify="center")
        av_room["values"]=rows
        av_room.current(0)
        av_room.grid(row=4,column=1)

        # meals
        meals=Label(labelframeleft,text="Meals",font=("arial",12,"bold"),padx=2,pady=6)
        meals.grid(row=5,column=0,sticky=W)

        meals=ttk.Combobox(labelframeleft,textvariable=self.var_meals,font=("arial",12),width=27,state="readonly",justify="center")
        meals["values"]=["None","Breakfast","Lunch","Dinner","Breakfast-Lunch","Lunch-Dinner","Breakfast-Dinner","Breakfast-Lunch-Dinner"]
        meals.current(0)
        meals.grid(row=5,column=1)

        # no of days
        days=Label(labelframeleft,text="No of Days",font=("arial",12,"bold"),padx=2,pady=6)
        days.grid(row=6,column=0,sticky=W)
  
        days=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,font=("arial",12),width=29,state="readonly",justify="center")
        days.grid(row=6,column=1)

        # Sub Total
        sub_total=Label(labelframeleft,text="Sub Total",font=("arial",12,"bold"),padx=2,pady=6)
        sub_total.grid(row=7,column=0,sticky=W)

        sub_total=ttk.Entry(labelframeleft,textvariable=self.var_subtotal,width=29,font=("arial",13),state="readonly",justify="center")
        sub_total.grid(row=7,column=1)

        # Tax
        tax=Label(labelframeleft,text="Tax",font=("arial",12,"bold"),padx=2,pady=6)
        tax.grid(row=8,column=0,sticky=W)

        tax=ttk.Entry(labelframeleft,textvariable=self.var_tax,width=29,font=("arial",13),state="readonly",justify="center")
        tax.grid(row=8,column=1)

        # Total
        total=Label(labelframeleft,text="Total Cost",font=("arial",12,"bold"),padx=2,pady=6)
        total.grid(row=9,column=0,sticky=W)

        total=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("arial",13),state="readonly",justify="center")
        total.grid(row=9,column=1)

        # ====================btns====================
        btn_frame=Frame(labelframeleft,padx=5,relief=RIDGE)
        btn_frame.place(x=0,y=350,width=415,height=85)

        btn_bill=Button(btn_frame,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
        btn_bill.grid(row=0,column=0,padx=1,pady=5)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
        btn_add.grid(row=1,column=0,padx=1,pady=10)

        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
        btn_update.grid(row=1,column=1,padx=1,pady=10)

        btn_delete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
        btn_delete.grid(row=1,column=2,padx=1,pady=10)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
        btn_reset.grid(row=1,column=3,padx=1,pady=10)


        # ====================table_frame==========================
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",12,"bold"))
        tableframe.place(x=435,y=280,width=850,height=260)

        search=Label(tableframe,text="Search:",font=("arial",11,"bold"),padx=2,pady=2,bg="red",fg="white")
        search.grid(row=0,column=0,sticky=W,padx=2)

        self.var_search=StringVar()
        search=ttk.Combobox(tableframe,textvariable=self.var_search,font=("arial",11),width=20,state="readonly",justify="center")
        search["values"]=["Contact"]
        search.current(0)
        search.grid(row=0,column=1,padx=2)

        self.var_search_txt=StringVar()
        id=ttk.Entry(tableframe,textvariable=self.var_search_txt,width=25,font=("arial",11),justify="center")
        id.grid(row=0,column=2,padx=2)

        btn_search=Button(tableframe,text="Search",command=self.search,font=("arial",10,"bold"),bg="black",fg="gold",width=21)
        btn_search.grid(row=0,column=3,padx=2)

        btn_show=Button(tableframe,text="Show All",command=self.fetch_data,font=("arial",10,"bold"),bg="black",fg="gold",width=20)
        btn_show.grid(row=0,column=4,padx=2)


        # ==========================Show data table======================
        details_table=Frame(tableframe,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=840,height=190)

        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)

        self.booking_details_table=ttk.Treeview(details_table,column=("Contact","Checkin","Checkout","RoomType","RoomAvailable","Meals","NoofDays"),
                                                                            xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.booking_details_table.xview)
        scroll_y.config(command=self.booking_details_table.yview)

        self.booking_details_table.heading("Contact",text="Contact No")
        self.booking_details_table.heading("Checkin",text="Check in")
        self.booking_details_table.heading("Checkout",text="Check out")
        self.booking_details_table.heading("RoomType",text="Room Type")
        self.booking_details_table.heading("RoomAvailable",text="Room Available")
        self.booking_details_table.heading("Meals",text="Meals")
        self.booking_details_table.heading("NoofDays",text="No of Days")

        self.booking_details_table["show"]="headings"

        self.booking_details_table.column("Contact",width=100)
        self.booking_details_table.column("Checkin",width=100)
        self.booking_details_table.column("Checkout",width=100)
        self.booking_details_table.column("RoomType",width=100)
        self.booking_details_table.column("RoomAvailable",width=100)
        self.booking_details_table.column("Meals",width=100)
        self.booking_details_table.column("NoofDays",width=100)

        self.booking_details_table.pack(fill=BOTH,expand=1)
        self.booking_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter a valid contact number!",parent=self.root)
            return
        conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
        cursor=conn.cursor()
        cursor.execute("select Name from customer where Mobile=%s",(self.var_contact.get(),))
        row=cursor.fetchone()

        if row==None:
            messagebox.showerror("Error","Contact Number not registered",parent=self.root)
        else:
            show_data=Frame(self.root,bd=4,bg="blue",relief=RIDGE,padx=2)
            show_data.place(x=455,y=60,width=300,height=190)

            lbl=Label(show_data,text="Name: ",font=("arial",12,"bold"))
            lbl.grid(row=0,column=0,pady=10,sticky=W)

            lbl=Label(show_data,text=row,font=("courier new",12))
            lbl.grid(row=0,column=1,padx=15,pady=10,sticky=W)

            cursor.execute("select Gender from customer where Mobile=%s",(self.var_contact.get(),))
            row=cursor.fetchone()

            lbl=Label(show_data,text="Gender: ",font=("arial",12,"bold"))
            lbl.grid(row=1,column=0,sticky=W)

            lbl=Label(show_data,text=row,font=("courier new",12))
            lbl.grid(row=1,column=1,padx=15,sticky=W)

            cursor.execute("select Email from customer where Mobile=%s",(self.var_contact.get(),))
            row=cursor.fetchone()

            lbl=Label(show_data,text="Email: ",font=("arial",12,"bold"))
            lbl.grid(row=2,column=0,sticky=W)

            lbl=Label(show_data,text=row,font=("courier new",12))
            lbl.grid(row=2,column=1,padx=15,sticky=W)

            cursor.execute("select Nationality from customer where Mobile=%s",(self.var_contact.get(),))
            row=cursor.fetchone()

            lbl=Label(show_data,text="Nationality: ",font=("arial",12,"bold"))
            lbl.grid(row=3,column=0,sticky=W)

            lbl=Label(show_data,text=row,font=("courier new",12))
            lbl.grid(row=3,column=1,padx=15,sticky=W)

            cursor.execute("select Address from customer where Mobile=%s",(self.var_contact.get(),))
            row=cursor.fetchone()

            lbl=Label(show_data,text="Address: ",font=("arial",12,"bold"))
            lbl.grid(row=4,column=0,sticky=W)

            lbl=Label(show_data,text=row,font=("courier new",12))
            lbl.grid(row=4,column=1,padx=15,sticky=W)

            cursor.execute("select Post from customer where Mobile=%s",(self.var_contact.get(),))
            row=cursor.fetchone()

            lbl=Label(show_data,text="Postal Code: ",font=("arial",12,"bold"))
            lbl.grid(row=5,column=0,sticky=W)

            lbl=Label(show_data,text=row,font=("courier new",12))
            lbl.grid(row=5,column=1,padx=15,sticky=W)

            conn.commit()
            conn.close()
        

    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","Missing Fields",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
                cursor=conn.cursor()
                cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),
                                                                                self.var_checkin.get(),
                                                                                self.var_checkout.get(),
                                                                                self.var_room.get(),
                                                                                self.var_av_room.get(),
                                                                                self.var_meals.get(),
                                                                                self.var_noofdays.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Something went wrong :{str(es)}",parent=self.root)

    def update_data(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
                cursor=conn.cursor()
                cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,room_available=%s,meals=%s,noofdays=%s where contact=%s",(
                                                                                                                            self.var_checkin.get(),
                                                                                                                            self.var_checkout.get(),
                                                                                                                            self.var_room.get(),
                                                                                                                            self.var_av_room.get(),
                                                                                                                            self.var_meals.get(),
                                                                                                                            self.var_noofdays.get(),
                                                                                                                            self.var_contact.get()))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Booking details updated successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Something went wrong :{str(es)}",parent=self.root)

    def delete_data(self):
        del_response=messagebox.askyesno("Hotel Management System","Do you want to delete this booking?",parent=self.root)
        if del_response > 0:
            conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
            cursor=conn.cursor()
            cursor.execute("delete from room where contact=%s",(self.var_contact.get(),))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Booking deleted successfully",parent=self.root)

    def reset_data(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_room.set("")
        self.var_av_room.set("")
        self.var_meals.set("")
        self.var_noofdays.set("")
        self.var_tax.set("")
        self.var_subtotal.set("")
        self.var_total.set("")

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
        cursor=conn.cursor()
        cursor.execute("select * from room where "+str(self.var_search.get())+" LIKE '%"+str(self.var_search_txt.get())+"%'")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.booking_details_table.delete(*self.booking_details_table.get_children())
            for i in rows:
                self.booking_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
        cursor=conn.cursor()
        cursor.execute("Select * from room")
        rows=cursor.fetchall()

        self.booking_details_table.delete(*self.booking_details_table.get_children())
        for i in rows:
            self.booking_details_table.insert("",END,values=i)    

        conn.commit()
        conn.close()
        self.var_search_txt.set("")

    def get_cursor(self,event=""):
        cursor_row=self.booking_details_table.focus()
        content=self.booking_details_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_room.set(row[3])
        self.var_av_room.set(row[4])
        self.var_meals.set(row[5])
        self.var_noofdays.set(row[6])

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
        rate_single=float(800)
        rate_double=float(1350)
        rate_deluxe=float(2150)
        rate_suite=float(3200)
        rate_bf=float(250)
        rate_lh=float(250)
        rate_dn=float(250)
        days=float(self.var_noofdays.get())
        room=self.var_room.get()
        amount=float(0)
        # meals cost
        if self.var_meals.get()=="Breakfast":
            amount+=rate_bf
        elif self.var_meals.get()=="Lunch":
            amount+=rate_lh
        elif self.var_meals.get()=="Dinner":
            amount+=rate_dn
        elif self.var_meals.get()=="Breakfast-Lunch":
            amount+=(rate_bf+rate_lh)
        elif self.var_meals.get()=="Breakfast-Dinner":
            amount+=(rate_bf+rate_dn)
        elif self.var_meals.get()=="Lunch-Dinner":
            amount+=(rate_lh+rate_dn)
        elif self.var_meals.get()=="Breakfast-Lunch-Dinner":
            amount+=(rate_bf+rate_lh+rate_dn)
        
        # room cost
        if room=="Single":
            amount+=(days*rate_single)
        elif room=="Double":
            amount+=(days*rate_double)
        elif room=="Deluxe":
            amount+=(days*rate_deluxe)
        else:
            amount+=(days*rate_suite)

        tax="Rs "+str("%0.2f"%((amount)*0.21))
        sub="Rs "+str("%0.2f"%(amount))
        tot="Rs "+str("%0.2f"%(amount*1.21))
        
        self.var_tax.set(tax)
        self.var_subtotal.set(sub)
        self.var_total.set(tot)






if __name__ == "__main__":
    root=Tk()
    obj=Booking(root)
    root.mainloop()