from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from time import strftime
from tkinter import messagebox
import mysql.connector


class Details:
    def __init__(self,root):
        self.root=root
        self.root.title("Details")
        self.root.geometry("1285x550+235+225")

        # ================variables===============
        self.var_floor=StringVar()
        self.var_room=StringVar()
        self.var_type=StringVar()

        # ================title================
        lbl_title=Label(self.root,text="DETAILS",font=("times new roman",20,"bold"),bg="black",bd=4,fg="gold",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1285,height=50)

        # ===============logo===============
        imgl=Image.open(r"images\logo.png")
        imgl=imgl.resize((47,47),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(imgl)

        lblimg=Label(self.root,image=self.photoimg,bd=2,relief=RIDGE)
        lblimg.place(x=0,y=0)

        # ================labelFrame===============
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=25,y=60,width=540,height=350)

        # =================labels and entries===============
        # floor
        floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        floor.grid(row=0,column=0,sticky=W)

        floor=ttk.Combobox(labelframeleft,textvariable=self.var_floor,font=("arial",12),width=27,state="readonly",justify="center")
        floor["values"]=["1","2","3","4","5","6"]
        floor.current(0)
        floor.grid(row=0,column=1,sticky=W,padx=2,pady=6)

        #room
        room=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        room.grid(row=1,column=0,sticky=W)

        room=ttk.Entry(labelframeleft,textvariable=self.var_room,font=("arial",12),width=29,justify="center")
        room.grid(row=1,column=1,sticky=W)

        #room type
        type=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        type.grid(row=2,column=0,sticky=W)

        type=ttk.Combobox(labelframeleft,textvariable=self.var_type,font=("arial",12),width=27,state="readonly",justify="center")
        type["values"]=["Single","Double","Deluxe","Suite"]
        type.current(0)
        type.grid(row=2,column=1,sticky=W)


        # ====================btns====================
        btn_frame=Frame(labelframeleft,padx=5,relief=RIDGE)
        btn_frame.place(x=200,y=150,width=100,height=150)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
        btn_add.grid(row=0,column=0,padx=1,pady=2)

        btn_update=Button(btn_frame,command=self.update_data,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
        btn_update.grid(row=1,column=0,padx=1,pady=2)

        btn_delete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
        btn_delete.grid(row=2,column=0,padx=1,pady=2)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,height=1)
        btn_reset.grid(row=3,column=0,padx=1,pady=2)


        # ====================table_frame==========================
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Details",padx=2,font=("times new roman",12,"bold"))
        tableframe.place(x=650,y=60,width=600,height=350)

        scroll_y=ttk.Scrollbar(tableframe,orient=VERTICAL)
        scroll_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)

        self.details_table=ttk.Treeview(tableframe,column=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.details_table.xview)
        scroll_y.config(command=self.details_table.yview)

        self.details_table.heading("floor",text="Floor")
        self.details_table.heading("roomno",text="Room No")
        self.details_table.heading("roomtype",text="Room Type")

        self.details_table["show"]="headings"

        self.details_table.column("floor",width=100)
        self.details_table.column("roomno",width=100)
        self.details_table.column("roomtype",width=100)

        self.details_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.details_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        if self.var_room.get()=="":
            messagebox.showerror("Error","Missing Fields",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
                cursor=conn.cursor()
                cursor.execute("insert into details values(%s,%s,%s)",(self.var_floor.get(),
                                                                        self.var_room.get(),
                                                                        self.var_type.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Something went wrong :{str(es)}",parent=self.root)

    def update_data(self):
        if self.var_room.get()=="":
            messagebox.showerror("Error","Please enter room number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
            cursor=conn.cursor()
            cursor.execute("update details set floor=%s,roomtype=%s where roomno=%s",(
                                                                                self.var_floor.get(),
                                                                                self.var_type.get(),
                                                                                self.var_room.get()))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Room details updated successfully",parent=self.root)
    
    def delete_data(self):
        del_response=messagebox.askyesno("Hotel Management System","Do you want to delete this room?",parent=self.root)
        if del_response > 0:
            conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
            cursor=conn.cursor()
            cursor.execute("delete from details where roomno=%s",(self.var_room.get(),))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Room deleted successfully",parent=self.root)

    def reset_data(self):
        self.var_floor.set("1")
        self.var_room.set("")
        self.var_type.set("Single")

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="jeet@sql.123",database="management")
        cursor=conn.cursor()
        cursor.execute("Select * from details")
        rows=cursor.fetchall()

        self.details_table.delete(*self.details_table.get_children())
        for i in rows:
            self.details_table.insert("",END,values=i)    

        conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.details_table.focus()
        content=self.details_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0])
        self.var_room.set(row[1])
        self.var_type.set(row[2])


if __name__ == "__main__":
    root=Tk()
    obj=Details(root)
    root.mainloop()