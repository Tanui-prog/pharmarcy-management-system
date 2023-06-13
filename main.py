from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import tkinter as tk
import sqlite3

##create database##

conn = sqlite3.connect("mypharmacy.db")
curs = conn.cursor()

curs.execute("""CREATE TABLE IF NOT EXISTS Information (
                        Ref_no text,
                        Company_name text,
                        Type_of_med text,
                        Med_name text,
                        Lot_no text,
                        Issue_dt text,
                        Exp_dt text,
                        Uses text,
                        Side_effect text,
                        Precaution text,
                        Dosage text,
                        Price text,
                        Quantity text
                )""")
curs.execute("""CREATE TABLE IF NOT EXISTS pharma(
                        Ref_no integer,
                        Med_name text
                )""")


class Pharmacy:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1370x695")
        self.root.resizable(False, False)

        ################## ADDMED VARIABLE #####################################
        self.ref_variable = StringVar()
        self.addmed_variable = StringVar()

        ########## MEDICINE DEPARTMENT VARIABLE ###############################
        self.refno_var = StringVar()
        self.companyname_var = StringVar()
        self.typemed_var = StringVar()
        self.medicine_var = StringVar()
        self.lotno_var = StringVar()
        self.issuedt_var = StringVar()
        self.expdt_var = StringVar()
        self.uses_var = StringVar()
        self.sideeffect_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.quantity_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        ##############TITLE############################
        label_title = Label(self.root, text="Pharmacy management system", relief=RIDGE, fg="white", bg="black", bd=3,
                            font=('times new roman', 30, 'bold'))
        label_title.place(x=0, y=0, width=1370, height=70)

        #####################topframe###################
        top_frame = Frame(self.root, bg="violet", bd=4, relief=RIDGE, padx=20)
        top_frame.place(x=0, y=75, width=1370, height=370)

        ####################Downframe###################
        down_frame = Frame(self.root, bg='grey', bd=2, relief=RIDGE)
        down_frame.place(x=0, y=492, width=1365, height=200)

        #####################rightframe##########3#######
        medinfo_frame = LabelFrame(top_frame, bg='grey', bd=10, relief=RIDGE, padx=20, text="Medicine Information",
                                   font=("arial", 13, "bold"), fg="white")
        medinfo_frame.place(x=500, y=5, width=820, height=350)

        #####################leftframe##################
        new_medframe = LabelFrame(top_frame, bg='grey', bd=10, relief=RIDGE, text="New Medicine",
                                  font=("arial", 13, "bold"), fg="white")
        new_medframe.place(x=0, y=5, width=452, height=350)

        #######################down button frame#########
        down_buttonframe = Frame(self.root, bg='grey', bd=10, relief=RIDGE, padx=20)
        down_buttonframe.place(x=0, y=432, width=1365, height=60)

        #######################
        newframe_buttons = Frame(new_medframe, bg='grey', bd=5, relief=RIDGE)
        newframe_buttons.place(x=260, y=100, width=170, height=170)

        #######################Images####################
        self.bgg = ImageTk.PhotoImage(file=r"/home/victor/Downloads/Pharmacy_management-system-master/image/medi.jpg")
        lbl_bgg = Label(medinfo_frame, image=self.bgg)
        lbl_bgg.place(x=400, y=165, width=200, height=150)
        self.bg = ImageTk.PhotoImage(file=r"/home/victor/Downloads/Pharmacy_management-system-master/image/med.jpg")
        lbl_bg = Label(medinfo_frame, image=self.bg)
        lbl_bg.place(x=600, y=165, width=200, height=150)

        ######################Buttons on the med info frame#####
        add_button = Button(medinfo_frame, text="Add Medicine", font=("arial", 12, "bold"), command=self.addmedicine,
                            width=14, fg="white",
                            bg="grey", bd=3, relief=RIDGE, activebackground="green", activeforeground="black")
        add_button.grid(row=4, column=3)

        update_button = Button(medinfo_frame, text="Update", font=("arial", 12, "bold"), width=14, fg="white",
                               bg="grey", bd=3, relief=RIDGE, command=self.Update_new, activebackground="green",
                               activeforeground="black")
        update_button.place(x=440, y=180)

        delete_button = Button(medinfo_frame, text="Delete", font=("arial", 12, "bold"), command=self.delete,
                               width=14, fg="white",
                               bg="grey", bd=3, relief=RIDGE, activebackground="green", activeforeground="black")
        delete_button.place(x=620, y=180)

        reset_button = Button(medinfo_frame, text="Reset", font=("arial", 12, "bold"), width=14, fg="white",
                              command=self.clear_new,
                              bg="grey", bd=3, relief=RIDGE, activebackground="green", activeforeground="black")
        reset_button.place(x=440, y=250)

        exit_button = Button(medinfo_frame, text="Exit", font=("arial", 12, "bold"), width=14, fg="white", bg="grey",
                             bd=3, relief=RIDGE, activebackground="red", activeforeground="black", command=root.destroy)
        exit_button.place(x=620, y=250)

        ###################Entry box and labels in med info frame############
        ref_label = Label(medinfo_frame, text="Reference No. :", padx=2, pady=4, font=("times new roman", 13, "bold"),
                          bg="grey")
        ref_label.grid(row=0, column=0, sticky=W)

        def refresh(e):
            curs.execute("SELECT Ref_no FROM pharma")
            data = [row[0] for row in curs.fetchall()]
            self.ref_combo['values'] = data

        self.ref_combo = ttk.Combobox(medinfo_frame, textvariable=self.refno_var, width=23, font=(
            "times new roman", 13, "bold"), state="readonly")
        self.ref_combo.bind("<Button-1>", refresh)
        self.ref_combo.grid(row=0, column=1)

        company_label = Label(medinfo_frame, text="Company Name :", padx=2, pady=4,
                              font=("times new roman", 13, "bold"), bg="grey")
        company_label.grid(row=1, column=0, sticky=W)
        self.company_entry = Entry(medinfo_frame, textvariable=self.companyname_var, width=24,
                                   font=("times new roman", 13, "bold"), fg="black",
                                   bg="white")
        self.company_entry.grid(row=1, column=1)

        medicine_type_label = Label(medinfo_frame, text="Type Of Medicine :. :", padx=2, pady=4,
                                    font=("times new roman", 13, "bold"), bg="grey")
        medicine_type_label.grid(row=2, column=0, sticky=W)
        self.medicine_type_combo = ttk.Combobox(medinfo_frame, textvariable=self.typemed_var, width=23,
                                                font=("times new roman", 13, 'bold'), state="readonly")
        self.medicine_type_combo["values"] = (
            'Select', 'Tablet', 'Capsule', "Injection", "Ayurvedic", "Drops", "Inhales")
        self.medicine_type_combo.grid(row=2, column=1)
        self.medicine_type_combo.current(0)

        medicine_name_namelabel = Label(medinfo_frame, text="Medicine Name. :", padx=2, pady=4,
                                        font=("times new roman", 13, "bold"), bg="grey")
        medicine_name_namelabel.grid(row=3, column=0, sticky=W)
        curs.execute("SELECT Med_name FROM pharma")
        data2 = [row[0] for row in curs.fetchall()]
        self.medicine_name_combo = ttk.Combobox(medinfo_frame, values=data2, textvariable=self.medicine_var, width=23,
                                                font=("times new roman", 13, 'bold'), state="readonly")
        self.medicine_name_combo.grid(row=3, column=1)

        lot_label = Label(medinfo_frame, text=" Lot No. :", padx=2, pady=4, font=("times new roman", 13, "bold"),
                          bg="grey")
        lot_label.grid(row=4, column=0)
        self.lot_entry = Entry(medinfo_frame, width=24, textvariable=self.lotno_var,
                               font=("times new roman", 13, " bold"), fg="black", bg="white")
        self.lot_entry.grid(row=4, column=1)

        issue_label = Label(medinfo_frame, text=" Issue Date :", padx=2, pady=4, font=("times new roman", 13, "bold"),
                            bg="grey")
        issue_label.grid(row=5, column=0)
        self.issue_entry = Entry(medinfo_frame, width=24, textvariable=self.issuedt_var,
                                 font=("times new roman", 13, "bold"), fg="black", bg="white")
        self.issue_entry.grid(row=5, column=1)

        exp_label = Label(medinfo_frame, text=" Expiry Date :", padx=2, pady=4, font=("times new roman", 13, "bold"),
                          bg="grey")
        exp_label.grid(row=6, column=0)
        self.exp_entry = Entry(medinfo_frame, textvariable=self.expdt_var, width=24,
                               font=("times new roman", 13, " bold"), fg="black", bg="white")
        self.exp_entry.grid(row=6, column=1)

        use_label = Label(medinfo_frame, text=" Uses :", padx=2, pady=4, font=("times new roman", 13, "bold"),
                          bg="grey")
        use_label.grid(row=7, column=0)
        self.use_entry = Entry(medinfo_frame, textvariable=self.uses_var, width=24,
                               font=("times new roman", 13, " bold"), fg="black", bg="white")
        self.use_entry.grid(row=7, column=1)

        sideeffect_label = Label(medinfo_frame, text=" Side Effect :", padx=2, pady=4,
                                 font=("times new roman", 13, "bold"), bg="grey")
        sideeffect_label.grid(row=8, column=0)
        self.sideeffect_entry = Entry(medinfo_frame, textvariable=self.sideeffect_var, width=24,
                                      font=("times new roman", 13, " bold"), fg="black",
                                      bg="white")
        self.sideeffect_entry.grid(row=8, column=1)

        warn_label = Label(medinfo_frame, text=" Prec & warning:", padx=2, pady=4,
                           font=("times new roman", 13, "bold"), bg="grey")
        warn_label.grid(row=9, column=0)
        self.warn_entry = Entry(medinfo_frame, textvariable=self.warning_var, width=24,
                                font=("times new roman", 13, " bold"), fg="black", bg="white")
        self.warn_entry.grid(row=9, column=1)

        dosage_label = Label(medinfo_frame, text=" Dosage :", padx=2, pady=4, font=("times new roman", 13, "bold"),
                             bg="grey")
        dosage_label.grid(row=0, column=2)
        self.dosage_entry = Entry(medinfo_frame, textvariable=self.dosage_var, width=24,
                                  font=("times new roman", 13, " bold"), fg="black",
                                  bg="white")
        self.dosage_entry.grid(row=0, column=3)

        price_label = Label(medinfo_frame, text=" Tablet Price :", padx=2, pady=4,
                            font=("times new roman", 13, "bold"), bg="grey")
        price_label.grid(row=1, column=2)
        self.price_entry = Entry(medinfo_frame, textvariable=self.price_var, width=24,
                                 font=("times new roman", 13, " bold"), fg="black",
                                 bg="white")
        self.price_entry.grid(row=1, column=3)

        qt_label = Label(medinfo_frame, text=" Tablet Quantity :", padx=2, pady=4,
                         font=("times new roman", 13, "bold"), bg="grey")
        qt_label.grid(row=2, column=2)
        self.qt_entry = Entry(medinfo_frame, width=24, textvariable=self.quantity_var,
                              font=("times new roman", 13, " bold"), fg="black", bg="white")
        self.qt_entry.grid(row=2, column=3)

        ################frame displaying the medicine################
        side_frame = Frame(new_medframe, bd=5, relief=RIDGE, bg="grey")
        side_frame.place(x=0, y=70, width=250, height=250)

        sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        self.medicine_table = ttk.Treeview(side_frame, column=("ref", "medname"), xscrollcommand=sc_x.set,
                                           yscrollcommand=sc_y.set)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y.pack(side=RIGHT, fill=Y)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref", text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name")

        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("medname", width=100)

        self.medicine_table.bind("<ButtonRelease-1>", self.medget_cursor)
        self.fetch_datamed()

        ##################buttons in new medicine department###################
        add_button = Button(newframe_buttons, text="Add", font=("arial", 13, "bold"), command=self.AddMed, width=13,
                            activeforeground="white", fg="white", bg="grey", activebackground="green")
        add_button.grid(row=0, column=0)

        update_button = Button(newframe_buttons, text="update", command=self.update_med, bg="grey",
                               font=("arial", 13, "bold"), width=13, fg="white", bd=3, relief=RIDGE,
                               activebackground="green", activeforeground="white")
        update_button.grid(row=1, column=0)

        delete_button = Button(newframe_buttons, text="Delete", bg="grey", command=self.Delete_med,
                               font=("arial", 13, "bold"), width=13, fg="white", bd=3, relief=RIDGE,
                               activebackground="red", activeforeground="white")
        delete_button.grid(row=2, column=0)

        clear_button = Button(newframe_buttons, text="Clear", bg="grey", font=("arial", 13, "bold"), width=13,
                              command=self.clear_med, fg="white", bd=3, relief=RIDGE, activebackground="red",
                              activeforeground="white")
        clear_button.grid(row=3, column=0)

        ####################entry and label for new med frane###################33#
        no_label = Label(new_medframe, text="Reference No:", font=("times new roman", 11, "bold"), bg="grey")
        no_label.place(x=0, y=10)
        self.no_entry = Entry(new_medframe, textvariable=self.ref_variable, relief=RIDGE, width=36,
                              font=("times new roman", 11, "bold"), bg="white")
        self.no_entry.place(x=120, y=10)

        med_label = Label(new_medframe, text="Med name:", font=("times new roman", 11, "bold"), bg="grey")
        med_label.place(x=0, y=40)
        self.med_entry = Entry(new_medframe, textvariable=self.addmed_variable, relief=RIDGE, width=36,
                               font=("times new roman", 11, "bold"), bg="white")
        self.med_entry.place(x=120, y=40)

        ################search and show buttons and labels ###################
        search_by = Label(down_buttonframe, text="Search By", font=("arial", 15, "bold"), fg="black", bg="grey", bd=3,
                          padx=3)
        search_by.grid(row=0, column=5, sticky=W)

        self.search_combo = ttk.Combobox(down_buttonframe, width=12, font=("", 13, "bold"), state="readonly",
                                         textvariable=self.search_by)
        self.search_combo["values"] = ("Select Options", "Ref No.")
        self.search_combo.grid(row=0, column=6)
        self.search_combo.current(0)

        entry_button = Entry(down_buttonframe, font=("arial", 15, "bold"), fg="black", bg="white", bd=3, width=12,
                             relief=RIDGE, textvariable=self.search_txt)
        entry_button.grid(row=0, column=7)

        ##################button for search###################
        search_button = Button(down_buttonframe, text="Search", command=self.search_data, font=("arial", 13, "bold"),
                               width=10, fg="white", bg="grey", bd=3, relief=RIDGE, activebackground="black",
                               activeforeground="white")
        search_button.grid(row=0, column=8)
        show_button = Button(down_buttonframe, text="Show All", command=self.fetch_new,
                             font=("times new roman", 13, "bold"), fg="white", bg="grey", width=10, bd=3, relief=RIDGE,
                             activebackground="black", activeforeground="white")
        show_button.grid(row=0, column=9)

        ########################down frame with table############
        scroll_frame = Frame(down_frame, bd=2, bg="brown")
        scroll_frame.place(x=0, y=0, width=1370, height=195)

        scroll_x = ttk.Scrollbar(scroll_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(scroll_frame, orient=VERTICAL)
        self.info_table = ttk.Treeview(scroll_frame,
                                       column=("ref no", "comp name", "type", "med name", "lot no", "issue", "exp",
                                               "uses", "side effect", "warning", "dosage", "price", "product"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.info_table.xview)
        scroll_y.config(command=self.info_table.yview)

        self.info_table.heading("ref no", text="Ref No.")
        self.info_table.heading("comp name", text="Company Name")
        self.info_table.heading("type", text="Type Of Medicine")
        self.info_table.heading("med name", text="Medicine Name")
        self.info_table.heading("lot no", text="Lot No.")
        self.info_table.heading("issue", text="Issue Date")
        self.info_table.heading("exp", text="Expiry Date")
        self.info_table.heading("uses", text="Uses")
        self.info_table.heading("side effect", text="Side Effects")
        self.info_table.heading("warning", text="Prec & Warning")
        self.info_table.heading("dosage", text="Dosage")
        self.info_table.heading("price", text="Medicine Price")
        self.info_table.heading("product", text="Product Qt.")

        self.info_table["show"] = "headings"
        self.info_table.pack(fill=BOTH, expand=1)

        self.info_table.column("ref no", width=100)
        self.info_table.column("comp name", width=100)
        self.info_table.column("type", width=100)
        self.info_table.column("med name", width=100)
        self.info_table.column("lot no", width=100)
        self.info_table.column("issue", width=100)
        self.info_table.column("exp", width=100)
        self.info_table.column("uses", width=100)
        self.info_table.column("side effect", width=100)
        self.info_table.column("warning", width=100)
        self.info_table.column("dosage", width=100)
        self.info_table.column("price", width=100)
        self.info_table.column("product", width=100)

        self.fetch_datamed()
        self.fetch_new()
        self.info_table.bind("<ButtonRelease-1>",self.get_cursor)
    ########################################med depart###########################

    def AddMed(self):
        if self.ref_variable.get() == "" or self.addmed_variable.get() == "":
            messagebox.showerror("Error", "All fields required")

        else:
            curs.execute("Insert into pharma(Ref_no,Med_name) values(?,?)", (
                self.ref_variable.get(),
                self.addmed_variable.get(),))

            conn.commit()
            self.fetch_datamed()
            self.medget_cursor()

            messagebox.showinfo("Success", "MEDICINE ADDED")

    def fetch_datamed(self):
        curs.execute("select * from pharma")
        rows = curs.fetchall()

        if len(rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())

            for i in rows:
                self.medicine_table.insert("", END, values=i)
            conn.commit()

    def medget_cursor(self, event=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]
        self.ref_variable.set(row[0])
        self.addmed_variable.set(row[1])

    def update_med(self):
        if self.ref_variable.get() == "" or self.addmed_variable.get() == "":

            messagebox.showerror("Error", "Ref No. and med name is required")
        else:
            try:
                curs.execute("update pharma set Med_name=? where Ref_no=?", (
                    self.addmed_variable.get(),
                    self.ref_variable.get(),
                ))

                conn.commit()
                messagebox.showinfo("Update", "Successfully Updated", parent=self.root)
                self.fetch_datamed()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to:{str(e)}", parent=self.root)

    def Delete_med(self):
        sql = "delete from pharma where Ref_no=?"
        val = (self.ref_variable.get(),)
        curs.execute(sql, val)
        conn.commit()
        self.fetch_datamed()

    def clear_med(self):
        self.ref_variable.set("")
        self.addmed_variable.set("")

    ###########################################################################333

    def addmedicine(self):
        if self.refno_var.get() == "" or self.lotno_var.get() == "" or self.typemed_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            curs.execute(
                "Insert into Information(REF_NO,COMPANY_NAME,TYPE_OF_MED,Med_name,LOT_NO,ISSUE_DT,EXP_DT,USES,SIDE_EFFECT,PRECAUTION,DOSAGE,PRICE,QUANTITY) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (

                    self.refno_var.get(),
                    self.companyname_var.get(),
                    self.typemed_var.get(),
                    self.medicine_var.get(),
                    self.lotno_var.get(),
                    self.issuedt_var.get(),
                    self.expdt_var.get(),
                    self.uses_var.get(),
                    self.sideeffect_var.get(),
                    self.warning_var.get(),
                    self.dosage_var.get(),
                    self.price_var.get(),
                    self.quantity_var.get(),
                ))
            conn.commit()
            self.fetch_new()

            messagebox.showinfo("Success", "Successfully added")

    def fetch_new(self):
        curs.execute("select * from Information")
        row = curs.fetchall()

        if len(row) != 0:
            self.info_table.delete(*self.info_table.get_children())

            for i in row:
                self.info_table.insert("", END, values=i)

            conn.commit()

    def get_cursor(self, ev=""):
        curs_row = self.info_table.focus()
        content = self.info_table.item(curs_row)
        row = content["values"]
        self.refno_var.set(row[0])
        self.companyname_var.set(row[1])
        self.typemed_var.set(row[2])
        self.medicine_var.set(row[3])
        self.lotno_var.set(row[4])
        self.issuedt_var.set(row[5])
        self.expdt_var.set(row[6])
        self.uses_var.set(row[7])
        self.sideeffect_var.set(row[8])
        self.warning_var.set(row[9])
        self.dosage_var.set(row[10])
        self.price_var.set(row[11])
        self.quantity_var.set(row[12])

    def Update_new(self):
        if self.refno_var.get() == "" or self.lotno_var.get() == "" or self.typemed_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            curs.execute("update Information set Company_name=?,Type_of_med=?,Med_name=?,Lot_no=?,Issue_dt=?,Exp_dt=?,Uses=?, Side_effect=? ,Precaution=?,  Dosage=?, Price=? ,Quantity=?  where Ref_no=?", (
                        self.companyname_var.get(),
                        self.typemed_var.get(),
                        self.medicine_var.get(),
                        self.lotno_var.get(),
                        self.issuedt_var.get(),
                        self.expdt_var.get(),
                        self.uses_var.get(),
                        self.sideeffect_var.get(),
                        self.warning_var.get(),
                        self.dosage_var.get(),
                        self.price_var.get(),
                        self.quantity_var.get(),
                        self.refno_var.get(),
                    ))
            conn.commit()
            self.fetch_new()
            messagebox.showinfo("UPDATE","Record has been updated successfully")

    def clear_new(self):
        self.refno_var.set("")
        self.companyname_var.set("")
        self.typemed_var.set("")
        self.medicine_var.set("")
        self.lotno_var.set("")
        self.issuedt_var.set("")
        self.expdt_var.set("")
        self.uses_var.set("")
        self.sideeffect_var.set("")
        self.warning_var.set("")
        self.dosage_var.set("")
        self.price_var.set("")
        self.quantity_var.set("")

    def search_data(self):
        selected = self.search_combo.get()
        if selected == "Select Options":
            messagebox.showerror("Error", "You have to choose an option")

        else:
            row = curs.fetchone()

            if len(row) != 0:
                self.info_table.delete(*self.info_table.get_children())

                for i in row:
                    self.info_table.insert("", END, values=i)

                conn.commit()


    def delete(self):
        sql="delete from Information where Ref_no=?"
        val=(self.refno_var.get(),)
        curs.execute(sql,val)
        conn.commit()
        self.fetch_new()

        messagebox.showinfo("Update","Record has been deleted")



if __name__ == '__main__':
    root = Tk()
    obj = Pharmacy(root)
    root.mainloop()
