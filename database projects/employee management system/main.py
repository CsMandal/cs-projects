from tkinter import *
from tkinter import messagebox
from datetime import date
from createtable import CrateTable
import inserttable
import selectdata

today = date.today()
start = 0

# colors
DARK_COLOR = "#1a535c"
COLOR = "#4ecdc4"
LIGHT_COLOR = "#f7fff7"
WHITE = "#FFFFFF"
BLUE_COLOR = "#3b71ca"
RED_COLOR = "#dc4c64"

# font
TEXT_FONT = ('Candara', 16, 'normal')
HEAD_FONT = ('Candara', 22, 'normal')
BUTTON_FONT = ('Candara', 14, 'normal')
TITLE_FONT = ('Candara', 18, 'normal')

root = Tk()
root.title("Daily task management")
root.geometry("1200x650")
root.resizable(False, False)
root.configure(background=COLOR)

perfectimage = PhotoImage(file="i.png")

cur_admin_id = None


def exitwindow():
    answer = messagebox.askokcancel(
        title="exit ", message="are you sure want to exit ")
    if answer:
        root.destroy()


def homewindow():
    main = Canvas(root,
                  height=550,
                  width=1200,
                  highlightthickness=0,
                  bg=LIGHT_COLOR)
    main.place(x=200, y=100)
    labelimage = Label(main,
                       image=perfectimage,
                       bg=LIGHT_COLOR)
    labelimage.place(x=200, y=20)


def add_employeepage():

    def clear():
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        job_entry.delete(0, END)
        adress_entry.delete(0, END)
        income_entry.delete(0, END)
        tax_entry.delete(0, END)
        did_entry.delete(0, END)

    def insert_emp():
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        job = job_entry.get()
        adress = adress_entry.get()
        income = float(income_entry.get())
        tax = float(tax_entry.get())
        dept_id = did_entry.get()
        if selectdata.SelectData.if_value_present(" department", "dept_id", dept_id):

            if selectdata.SelectData.if_value_present("employee", "emp_id", "E101"):

                did = selectdata.SelectData.select_last_element("emp_id",
                                                                "employee", "emp_id")

                value = int(did[1:])
                did = "E"+str(value+1)

            else:
                did = "E"+str(cur_admin_id[1:])

            data = (cur_admin_id, did, name, phone, job,
                    email, adress, income, tax, dept_id)
            inserttable.InsertData.insert_employee(data)
            messagebox.showinfo(
                title="sucess", message="Data saved successfully")
            clear()
        else:
            messagebox.showerror(
                title="wrong", message="Dept id doesnt exist or entered wrong dept id")

    main = Canvas(root,
                  height=550,
                  width=1200,
                  highlightthickness=0,
                  bg=LIGHT_COLOR)
    main.place(x=200, y=100)

    head_label = Label(main, text="Add Employee",
                       font=HEAD_FONT,
                       bd=2,
                       width=60,
                       relief="solid",
                       bg=COLOR)
    head_label.place(x=20, y=20)

    name_label = Label(main, text="Name*",
                       font=TEXT_FONT,
                       bg=LIGHT_COLOR)
    name_label.place(x=80, y=100)
    name_entry = Entry(main,
                       width=50,
                       font=TEXT_FONT)
    name_entry.place(x=160, y=100)
    phone_label = Label(main,
                        text="Phone*",
                        font=TEXT_FONT,
                        bg=LIGHT_COLOR)
    phone_label.place(x=80, y=170)
    phone_entry = Entry(main, width=15, font=TEXT_FONT)
    phone_entry.place(x=160, y=170)
    job_label = Label(main,
                      text="Desigination",
                      font=TEXT_FONT,
                      bg=LIGHT_COLOR)
    job_label.place(x=370, y=170)
    job_entry = Entry(main, width=20, font=TEXT_FONT)
    job_entry.place(x=520, y=170)

    email_label = Label(main, text="Email",
                        font=TEXT_FONT,
                        bg=LIGHT_COLOR)
    email_label.place(x=80, y=240)
    email_entry = Entry(main, width=50, font=TEXT_FONT)
    email_entry.place(x=160, y=240)
    adress_label = Label(main, text="Adress*",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
    adress_label.place(x=80, y=310)
    adress_entry = Entry(main, width=47, font=TEXT_FONT)
    adress_entry.place(x=180, y=310)
    income_label = Label(main, text="Income*",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
    income_label.place(x=80, y=380)
    income_entry = Entry(main, width=15, font=TEXT_FONT)
    income_entry.place(x=180, y=380)
    tax_label = Label(main, text="tax",
                      font=TEXT_FONT,
                      bg=LIGHT_COLOR)
    tax_label.place(x=380, y=380)
    tax_entry = Entry(main, width=5, font=TEXT_FONT)
    tax_entry.place(x=430, y=380)

    did_label = Label(main, text="Dept.ID",
                      font=TEXT_FONT,
                      bg=LIGHT_COLOR)
    did_label.place(x=530, y=380)
    did_entry = Entry(main, width=10, font=TEXT_FONT)
    did_entry.place(x=630, y=380)

    submit_button = Button(main, text="Submit",
                           font=TEXT_FONT,
                           width=15,
                           bg=COLOR,
                           command=insert_emp
                           )
    submit_button.place(x=200, y=450)
    reset_button = Button(main, text="Reset",
                          font=TEXT_FONT,
                          width=15,
                          command=clear
                          )
    reset_button.place(x=400, y=450)

    exitbutton = Button(main,
                        text="Exit",
                        font=TEXT_FONT,
                        width=10,
                        command=exitwindow)
    exitbutton.place(x=620, y=450)


def search_employeepage():

    def designpage(data):
        main = Canvas(root,
                      height=550,
                      width=1200,
                      highlightthickness=0,
                      bg=LIGHT_COLOR)
        main.place(x=200, y=100)
        head_label = Label(main, text=f"The details of {data[0][2]}",
                           bd=2,
                           relief="solid",
                           bg=COLOR,
                           width=60,
                           font=HEAD_FONT)
        head_label.place(x=20, y=20)
        id_label = Label(main, text=f"Employee ID  : - {data[0][1]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=160, y=100)
        id_label = Label(main, text=f"Name   : - {data[0][2]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=160, y=150)
        id_label = Label(main, text=f"phone  : - {data[0][3]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=160, y=200)
        id_label = Label(main, text=f"designation  : - {data[0][4]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=460, y=200)
        id_label = Label(main, text=f"email  : - {data[0][5]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=160, y=250)
        id_label = Label(main, text=f"adress : - {data[0][6]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=160, y=300)
        id_label = Label(main, text=f"salary  : - {data[0][7]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=160, y=350)
        id_label = Label(main, text=f"Tax  : - {data[0][8]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=360, y=350)
        id_label = Label(main, text=f"department id  : - {data[0][9]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=560, y=350)

    def search_phone():
        phone = phone_entry.get()
        if selectdata.SelectData.if_value_present_date("employee", "phone", phone, "admin_id", cur_admin_id):
            data = selectdata.SelectData.select_all_data(
                "employee", "phone", phone)
            phone_entry.delete(0, END)
            designpage(data)
        else:
            messagebox.showerror(
                title="not exist", message="the phone no. doesnt matched")
            phone_entry.delete(0, END)

    def search_id():
        phone = id_entry.get()
        if selectdata.SelectData.if_value_present_date("employee", "emp_id", phone, "admin_id", cur_admin_id):
            data = selectdata.SelectData.select_all_data(
                "employee", "emp_id", phone)
            id_entry.delete(0, END)
            designpage(data)
        else:
            messagebox.showerror(
                title="not exist", message="the employee id. doesnt matched")
            id_entry.delete(0, END)

    def search_email():
        phone = email_entry.get()
        if selectdata.SelectData.if_value_present_date("employee", "email", phone, "admin_id", cur_admin_id):
            data = selectdata.SelectData.select_all_data(
                "employee", "email", phone)
            email_entry.delete(0, END)
            designpage(data)

        else:
            messagebox.showerror(
                title="not exist", message="the email name . doesnt matched")
            email_entry.delete(0, END)

    main = Canvas(root,
                  height=550,
                  width=1200,
                  highlightthickness=0,
                  bg=LIGHT_COLOR)
    main.place(x=200, y=100)
    head_label = Label(main, text="Search by Employee_ID / Phone no. /email ",
                       bd=2,
                       relief="solid",
                       bg=COLOR,
                       width=60,
                       font=HEAD_FONT)
    head_label.place(x=20, y=20)

    id_label = Label(main, text="Employee ID ",
                     font=TEXT_FONT,
                     bg=LIGHT_COLOR)
    id_label.place(x=160, y=100)
    id_entry = Entry(main, width=33,
                     font=TEXT_FONT)
    id_entry.place(x=300, y=100)
    search_id_button = Button(main, text="Search",
                              width=10,
                              font=BUTTON_FONT,
                              bg=COLOR,
                              command=search_id
                              )
    search_id_button.place(x=800, y=100)

    phone_label = Label(main, text="Phone No.  ",
                        font=TEXT_FONT,
                        bg=LIGHT_COLOR)
    phone_label.place(x=160, y=220)
    phone_entry = Entry(main, width=33,
                        font=TEXT_FONT)
    phone_entry.place(x=300, y=220)
    search_phone_button = Button(main, text="Search",
                                 width=10,
                                 font=BUTTON_FONT,
                                 bg=COLOR,
                                 command=search_phone
                                 )
    search_phone_button.place(x=800, y=220)

    email_label = Label(main, text="Email ",
                        font=TEXT_FONT,
                        bg=LIGHT_COLOR)
    email_label.place(x=160, y=360)
    email_entry = Entry(main, width=33,
                        font=TEXT_FONT)
    email_entry.place(x=300, y=360)
    search_email_button = Button(main, text="Search",
                                 width=10,
                                 font=BUTTON_FONT,
                                 bg=COLOR,
                                 command=search_email
                                 )
    search_email_button.place(x=800, y=360)
    resetregisterbutton = Button(main,
                                 text="Reset",
                                 font=BUTTON_FONT,
                                 width=10,
                                 )
    resetregisterbutton.place(x=180, y=460)

    exitbutton = Button(main,
                        text="Exit",
                        font=BUTTON_FONT,
                        width=10,
                        command=exitwindow)
    exitbutton.place(x=320, y=460)


def attendancepage():
    emp_list = selectdata.SelectData.select_all_data(
        "employee", "admin_id", cur_admin_id)

    def checkattendance(emp_id):
        if selectdata.SelectData.if_value_present_date("attendance", "emp_id", emp_id, "date", today):
            absent_button.config(state="disabled")
            halfday_button.config(state="disabled")
            present_button.config(state="disabled")
            id_label.config(text="-------------------")
            name_label.config(text="-------------------")
            phone_label.config(text="--------------------")

            footer_label.config(text="all employee attendance done")
            holidaybutton.config(state="disabled")

    def holiday():

        for start in range(len(emp_list)):
            if selectdata.SelectData.if_value_present("attendance", "attend_id", 2):
                value = selectdata.SelectData.select_last_element(
                    "attend_id", "attendance", "attend_id")
            else:
                value = 1
            data = (cur_admin_id, emp_list[start][1],
                    value+1, emp_list[start][2], today, 2)
            inserttable.InsertData.insert_attendance(data)
        messagebox.showinfo(
            title="present", message="All employe marked as present")

    def status_attendance(value):

        if value == 2:
            return "Present"
        elif value == 1:
            return "Half Day"
        else:
            return "Absent"

    def show_attendance():
        count = 0
        main = Canvas(root,
                      height=550,
                      width=1200,
                      highlightthickness=0,
                      bg=LIGHT_COLOR)
        main.place(x=200, y=100)
        head_label = Label(main,
                           text=f"details of {today} attendance",
                           bd=2,
                           relief="solid",
                           bg=COLOR,
                           width=60,
                           font=HEAD_FONT)
        head_label.place(x=20, y=20)

        task_listbox = Listbox(main,
                               width=60,
                               font=TEXT_FONT,
                               height=10
                               )
        task_listbox.place(x=50, y=100)
        data_list = selectdata.SelectData.select_all_data_2_values(
            "attendance", "admin_id", cur_admin_id, "date", today)
        for i in range(len(data_list)):
            data = f"""{data_list[count][1]}  ::  {data_list[count][3]}  ::  {data_list[count][4]}  ::  {status_attendance(data_list[count][5])}"""
            task_listbox.insert(END, data)
            count += 1

    def update_value(value):
        id_label.config(text=value[0])
        name_label.config(text=value[1])
        phone_label.config(text=value[2])

    def absent():
        global start
        checkattendance(emp_list[start][1])
        if selectdata.SelectData.if_value_present("attendance", "attend_id", 1):
            value = selectdata.SelectData.select_last_element(
                "attend_id", "attendance", "attend_id")

        else:
            value = 0

        data = (cur_admin_id, emp_list[start][1],
                value+1, emp_list[start][2], today, 0)
        inserttable.InsertData.insert_attendance(data)
        messagebox.showinfo(title="present", message="marked as absent")
        start += 1
        send_value = (emp_list[start][1],
                      emp_list[start][2], emp_list[start][3])
        update_value(send_value)

    def present():
        global start
        checkattendance(emp_list[start][1])
        if selectdata.SelectData.if_value_present("attendance", "attend_id", 1):
            value = selectdata.SelectData.select_last_element(
                "attend_id", "attendance", "attend_id")

        else:
            value = 0

        data = (cur_admin_id, emp_list[start][1],
                value+1, emp_list[start][2], today, 2)
        inserttable.InsertData.insert_attendance(data)
        messagebox.showinfo(title="present", message="marked as present")
        start += 1
        send_value = (emp_list[start][1],
                      emp_list[start][2], emp_list[start][3])
        update_value(send_value)

    def halfday():
        global start
        checkattendance(emp_list[start][1])
        if selectdata.SelectData.if_value_present("attendance", "attend_id", 1):
            value = selectdata.SelectData.select_last_element(
                "attend_id", "attendance", "attend_id")

        else:
            value = 0

        data = (cur_admin_id, emp_list[start][1],
                value+1, emp_list[start][2], today, 1)
        inserttable.InsertData.insert_attendance(data)
        messagebox.showinfo(title="present", message="marked as halfday")
        start += 1
        send_value = (emp_list[start][1],
                      emp_list[start][2], emp_list[start][3])
        update_value(send_value)

    maincav = Canvas(root,
                     height=550,
                     width=1200,
                     highlightthickness=0,
                     bg=LIGHT_COLOR)
    maincav.place(x=200, y=100)
    head_label = Label(maincav,
                       text="Mannage Attendance",
                       bd=2,
                       relief="solid",
                       bg=COLOR,
                       width=60,
                       font=HEAD_FONT)
    head_label.place(x=20, y=20)

    main = Canvas(
        maincav,
        width=600,
        height=350,
        bg=LIGHT_COLOR,
        bd=2,
        relief="solid",
        highlightthickness=0
    )
    main.place(x=40, y=100)

    date_label = Label(
        main,
        text=f"Today Attendance ({today})",
        bd=2,
        relief="solid",
        font=TEXT_FONT,
        width=52,
        bg=COLOR
    )
    date_label.place(x=10, y=10)

    staff_id_label = Label(main, text="Emp ID", font=TEXT_FONT,
                           bg=LIGHT_COLOR)
    staff_id_label.place(x=20, y=80)

    id_label = Label(main, text=emp_list[0][1], font=TEXT_FONT,
                     bg=LIGHT_COLOR,
                     bd=2,
                     width=40,
                     relief='solid')
    id_label.place(x=100, y=80)

    staff_name_label = Label(main, text="Name : ", font=TEXT_FONT,
                             bg=LIGHT_COLOR)
    staff_name_label.place(x=20, y=130)

    name_label = Label(main, text=emp_list[0][2], font=TEXT_FONT,
                       bg=LIGHT_COLOR,
                       bd=2,
                       width=40,
                       relief='solid')
    name_label.place(x=100, y=130)
    staff_phone_label = Label(main, text="Phone", font=TEXT_FONT,
                              bg=LIGHT_COLOR)
    staff_phone_label.place(x=20, y=170)

    phone_label = Label(main, text=emp_list[0][3], font=TEXT_FONT,
                        bg=LIGHT_COLOR,
                        bd=2,
                        width=40,
                        relief='solid')
    phone_label.place(x=100, y=170)

    absent_button = Button(main, text="Absent", bg="#ff474c", width=10,
                           font=BUTTON_FONT,
                           command=absent
                           )
    absent_button.place(x=40, y=220)
    halfday_button = Button(main, text="Half Day", width=10,
                            font=BUTTON_FONT,
                            command=halfday

                            )
    halfday_button.place(x=200, y=220)
    present_button = Button(main, text="Present", bg="green",
                            width=10,
                            font=BUTTON_FONT,
                            command=present
                            )
    present_button.place(x=360, y=220)

    footer_label = Label(main, text="STATUS OF ATTENDANCE",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR,
                         bd=2,
                         width=47,
                         relief='solid')
    footer_label.place(x=20, y=310)

    holidaybutton = Button(maincav,
                           text="Holiday",
                           font=BUTTON_FONT,
                           width=20,
                           command=holiday
                           )
    holidaybutton.place(x=750, y=100)

    checkattendance(emp_list[start][1])

    showattendancebutton = Button(maincav,
                                  text="Show Attendance",
                                  font=BUTTON_FONT,
                                  width=20,
                                  command=show_attendance
                                  )
    showattendancebutton.place(x=750, y=200)

    exitbutton = Button(maincav,
                        text="Exit",
                        font=BUTTON_FONT,
                        width=10,
                        command=exitwindow)
    exitbutton.place(x=320, y=500)


def departmentpage():

    def clear():
        name_entry.delete(0, END)
        desc_entry.delete(0, END)

    def design_department(data):
        total = len(data)
        main = Canvas(root,
                      height=550,
                      width=1200,
                      highlightthickness=0,
                      bg=LIGHT_COLOR)
        main.place(x=200, y=100)
        head_label = Label(main, text=" Department Details",
                           font=HEAD_FONT,
                           bd=2,
                           width=60,
                           relief="solid",
                           bg=COLOR)
        head_label.place(x=20, y=20)
        m = 0
        name_label = Label(main, text=f"Dept id ",
                           font=TEXT_FONT,
                           bg=LIGHT_COLOR)
        name_label.place(x=100, y=100)
        name_label = Label(main, text=f"dept Name ",
                           font=TEXT_FONT,
                           bg=LIGHT_COLOR)
        name_label.place(x=250, y=100)
        name_label = Label(main, text=f"dept desc ",
                           font=TEXT_FONT,
                           bg=LIGHT_COLOR)
        name_label.place(x=450, y=100)
        for i in range(total):
            name_label = Label(main, text=data[i][1],
                               font=TEXT_FONT,
                               bg=LIGHT_COLOR)
            name_label.place(x=100, y=150+m)
            name_label = Label(main, text=data[i][2],
                               font=TEXT_FONT,
                               bg=LIGHT_COLOR)
            name_label.place(x=250, y=150+m)
            name_label = Label(main, text=data[i][3],
                               font=TEXT_FONT,
                               bg=LIGHT_COLOR)
            name_label.place(x=450, y=150+m)

            m += 50

    def search_all():
        if selectdata.SelectData.if_value_present("department", "admin_id", cur_admin_id):
            data = selectdata.SelectData.select_all_data(
                "department", "admin_id", cur_admin_id)
            design_department(data)

        else:
            messagebox.showinfo(title='insert data',
                                message="first insert the department data")

    def add_dept():
        name = name_entry.get()
        desc = desc_entry.get()
        if selectdata.SelectData.if_value_present("department", "dept_id", "D101"):
            did = selectdata.SelectData.select_last_element("dept_id",
                                                            "department", "dept_id")
            value = int(did[1:])
            did = "D"+str(value+1)

        else:
            did = "D"+str(cur_admin_id[1:])
        data = (cur_admin_id, did, name, desc)
        inserttable.InsertData.insert_department(data)
        messagebox.showinfo(title="sucess", message="Data saved successfully")
        clear()

    def search_id():
        id = deptid_entry.get()
        if selectdata.SelectData.if_value_present("department", "dept_id", id):
            data = selectdata.SelectData.select_all_data(
                "department", "dept_id", id)
            design_department(data)

        else:
            messagebox.showinfo(title="wrong details",
                                message="Id doesnt match")

    def search_name():
        id = deptname_entry.get()
        if selectdata.SelectData.if_value_present("department", "dept_name", id):
            data = selectdata.SelectData.select_all_data(
                "department", "dept_name", id)
            design_department(data)

        else:
            messagebox.showinfo(title="wrong details",
                                message="Id doesnt match")

    main = Canvas(root,
                  height=550,
                  width=1200,
                  highlightthickness=0,
                  bg=LIGHT_COLOR)
    main.place(x=200, y=100)

    head_label = Label(main, text="Add Department",
                       font=HEAD_FONT,
                       bd=2,
                       width=60,
                       relief="solid",
                       bg=COLOR)
    head_label.place(x=20, y=20)

    name_label = Label(main, text="Department Name",
                       font=TEXT_FONT,
                       bg=LIGHT_COLOR)
    name_label.place(x=80, y=100)
    name_entry = Entry(main,
                       width=50,
                       font=TEXT_FONT)
    name_entry.place(x=260, y=100)
    desc_label = Label(main,
                       text="Department Info",
                       font=TEXT_FONT,
                       bg=LIGHT_COLOR)
    desc_label.place(x=80, y=170)
    desc_entry = Entry(main, width=50, font=TEXT_FONT)
    desc_entry.place(x=260, y=170)
    add_button = Button(main, text="Add",
                        font=BUTTON_FONT,
                        width=15,
                        bg=COLOR,
                        command=add_dept
                        )
    add_button.place(x=450, y=240)
    show_button = Button(main, text="Show ALL",
                         font=BUTTON_FONT,
                         width=15,
                         command=search_all
                         )
    show_button.place(x=200, y=240)

    head_label = Label(main, text="Search Department By Name/ Id",
                       font=HEAD_FONT,
                       bd=2,
                       width=60,
                       relief="solid",
                       bg=COLOR)
    head_label.place(x=20, y=310)

    deptname_label = Label(main, text="Department Name",
                           font=TEXT_FONT,
                           bg=LIGHT_COLOR)
    deptname_label.place(x=80, y=400)
    deptname_entry = Entry(main,
                           width=30,
                           font=TEXT_FONT)
    deptname_entry.place(x=260, y=400)
    search_name_button = Button(main, text="search",
                                font=BUTTON_FONT,
                                width=20,
                                bg=COLOR,
                                command=search_name
                                )
    search_name_button.place(x=750, y=400)

    deptid_label = Label(main, text="Department Id",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
    deptid_label.place(x=80, y=470)
    deptid_entry = Entry(main,
                         width=30,
                         font=TEXT_FONT)
    deptid_entry.place(x=260, y=470)
    search_id_button = Button(main, text="search",
                              font=BUTTON_FONT,
                              width=20,
                              bg=COLOR,
                              command=search_id
                              )
    search_id_button.place(x=750, y=470)


def salarypage():

    def search_salary():
        id = id_entry.get()
        start_date = startdate_entry.get()
        end_date = enddate_entry.get()
        if selectdata.SelectData.if_value_present("employee", "emp_id", id):
            if selectdata.SelectData.if_value_present_date("attendance", "emp_id", id, "date", start_date) and selectdata.SelectData.if_value_present_date("attendance", "emp_id", id, "date", end_date):
                value = selectdata.SelectData.attendance_status(
                    id, start_date, end_date)
                value2 = selectdata.SelectData.select_all_data_2_values(
                    "employee", "admin_id", cur_admin_id, "emp_id", id)
                designpage(value, value2)
            else:
                messagebox.showerror(
                    title="date wrong", message=" date is wrong or enter date YYYY-MM-DD")
        else:
            messagebox.showerror(
                title="not found", message="employee id doesnt found")

    def designpage(attend_status, data):
        main = Canvas(root,
                      height=400,
                      width=1200,
                      highlightthickness=0,
                      bg=LIGHT_COLOR)
        main.place(x=200, y=300)
        id_label = Label(main, text=f"Employee ID  : - {data[0][1]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=160, y=10)
        id_label = Label(main, text=f"Name   : - {data[0][2]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=160, y=60)
        id_label = Label(main, text=f"phone  : - {data[0][3]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=160, y=110)
        id_label = Label(main, text=f"designation  : - {data[0][4]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=460, y=110)
        id_label = Label(main, text=f"salary  : - {data[0][7]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=160, y=160)
        id_label = Label(main, text=f"Tax  : - {data[0][8]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=360, y=160)
        id_label = Label(main, text=f"department id  : - {data[0][9]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=560, y=160)
        id_label = Label(main, text=f"total  present  : - {attend_status[0]} ::  Halfday  : - {attend_status[1]} ::   Absent  : - {attend_status[2]}",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=160, y=210)

        day_count = attend_status[0]*2 + attend_status[1]
        per_day = data[0][7]/60
        salary = per_day*day_count
        total_salry = salary*(1-data[0][8]*0.01)

        id_label = Label(main, text=f"total salary : -  {salary}   after tax : {total_salry} ",
                         font=TEXT_FONT,
                         bg=LIGHT_COLOR)
        id_label.place(x=160, y=260)

    main = Canvas(root,
                  height=550,
                  width=1200,
                  highlightthickness=0,
                  bg=LIGHT_COLOR)
    main.place(x=200, y=100)
    head_label = Label(main,
                       text="Salary",
                       bd=2,
                       relief="solid",
                       bg=COLOR,
                       width=60,
                       font=HEAD_FONT)
    head_label.place(x=20, y=20)
    id_label = Label(main, text="Employee ID ",
                     font=TEXT_FONT,
                     bg=LIGHT_COLOR)
    id_label.place(x=160, y=100)
    id_entry = Entry(main, width=33,
                     font=TEXT_FONT)
    id_entry.place(x=300, y=100)

    startdate_label = Label(main, text="From date  ",
                            font=TEXT_FONT,
                            bg=LIGHT_COLOR)
    startdate_label.place(x=160, y=150)
    startdate_entry = Entry(main, width=10,
                            font=TEXT_FONT)
    startdate_entry.place(x=300, y=150)

    enddate_label = Label(main, text="To date  ",
                          font=TEXT_FONT,
                          bg=LIGHT_COLOR)
    enddate_label.place(x=450, y=150)
    enddate_entry = Entry(main, width=10,
                          font=TEXT_FONT)
    enddate_entry.place(x=570, y=150)

    search_id_button = Button(main, text="Search",
                              width=10,
                              font=BUTTON_FONT,
                              bg=COLOR,
                              command=search_salary
                              )
    search_id_button.place(x=800, y=120)


def update_page():

    def clear():
        didupdate_entry.delete(0, END)
        nameupdate_entry.delete(0, END)
        descupdate_entry.delete(0, END)

    def update_emp_page():

        main = Canvas(root,
                      height=550,
                      width=1200,
                      highlightthickness=0,
                      bg=LIGHT_COLOR)
        main.place(x=200, y=100)

        def update_emp():
            id = empid_entry.get()

            def clear():
                name_entry.delete(0, END)
                phone_entry.delete(0, END)
                email_entry.delete(0, END)
                job_entry.delete(0, END)
                adress_entry.delete(0, END)
                income_entry.delete(0, END)
                tax_entry.delete(0, END)
                did_entry.delete(0, END)

            def update_data():
                name = name_entry.get()
                phone = phone_entry.get()
                job = job_entry.get()
                email = email_entry.get()
                adress = adress_entry.get()
                income = income_entry.get()
                tax = tax_entry.get()
                did = did_entry.get()
                inserttable.InsertData.update_employee(
                    (name, phone, job, email, adress, income, tax, did, id))
                messagebox.showinfo(message="updated sucessfully")
                clear()

            if selectdata.SelectData.if_value_present("employee", "emp_id", id):
                data = selectdata.SelectData.select_all_data(
                    "employee", "emp_id", id)
                name_label = Label(main, text="Name*",
                                   font=TEXT_FONT,
                                   bg=LIGHT_COLOR)
                name_label.place(x=80, y=170)
                name_entry = Entry(main,
                                   width=33,
                                   font=TEXT_FONT)
                name_entry.insert(0, data[0][2])
                name_entry.place(x=180, y=170)

                phone_label = Label(main,
                                    text="Phone*",
                                    font=TEXT_FONT,
                                    bg=LIGHT_COLOR)
                phone_label.place(x=80, y=230)
                phone_entry = Entry(main, width=15, font=TEXT_FONT)
                phone_entry.insert(0, data[0][3])
                phone_entry.place(x=180, y=230)
                job_label = Label(main,
                                  text="Desigination",
                                  font=TEXT_FONT,
                                  bg=LIGHT_COLOR)
                job_label.place(x=370, y=230)
                job_entry = Entry(main, width=20, font=TEXT_FONT)
                job_entry.insert(0, data[0][4])
                job_entry.place(x=520, y=230)

                email_label = Label(main, text="Email",
                                    font=TEXT_FONT,
                                    bg=LIGHT_COLOR)
                email_label.place(x=80, y=300)
                email_entry = Entry(main, width=50, font=TEXT_FONT)
                email_entry.insert(0, data[0][5])
                email_entry.place(x=180, y=300)
                adress_label = Label(main, text="Adress*",
                                     font=TEXT_FONT,
                                     bg=LIGHT_COLOR)
                adress_label.place(x=80, y=370)
                adress_entry = Entry(main, width=47, font=TEXT_FONT)
                adress_entry.insert(0, data[0][6])
                adress_entry.place(x=180, y=370)
                income_label = Label(main, text="Income*",
                                     font=TEXT_FONT,
                                     bg=LIGHT_COLOR)
                income_label.place(x=80, y=430)
                income_entry = Entry(main, width=15, font=TEXT_FONT)
                income_entry.insert(0, data[0][7])
                income_entry.place(x=180, y=430)
                tax_label = Label(main, text="tax",
                                  font=TEXT_FONT,
                                  bg=LIGHT_COLOR)
                tax_label.place(x=380, y=430)
                tax_entry = Entry(main, width=5, font=TEXT_FONT)
                tax_entry.insert(0, data[0][8])
                tax_entry.place(x=430, y=430)

                did_label = Label(main, text="Dept.ID",
                                  font=TEXT_FONT,
                                  bg=LIGHT_COLOR)
                did_label.place(x=530, y=430)
                did_entry = Entry(main, width=10, font=TEXT_FONT)
                did_entry.insert(0, data[0][9])
                did_entry.place(x=630, y=430)

                submit_button = Button(main, text="update",
                                       font=TEXT_FONT,
                                       width=15,
                                       bg=COLOR,
                                       command=update_data

                                       )
                submit_button.place(x=200, y=500)
                reset_button = Button(main, text="Reset",
                                      font=TEXT_FONT,
                                      width=15,
                                      command=clear

                                      )
                reset_button.place(x=400, y=500)
            else:
                messagebox.showerror(message="employee id doesnt exist")

        head_label = Label(main, text="Update Employee",
                           font=HEAD_FONT,
                           bd=2,
                           width=60,
                           relief="solid",
                           bg=COLOR)
        head_label.place(x=20, y=20)

        name_label = Label(main, text="Emp. Id",
                           font=TEXT_FONT,
                           bg=LIGHT_COLOR)
        name_label.place(x=80, y=100)
        empid_entry = Entry(main,
                            width=5,
                            font=TEXT_FONT)
        empid_entry.place(x=160, y=100)

        emp_button = Button(main, text="search",
                            font=TEXT_FONT,
                            width=15,
                            bg=COLOR,
                            command=update_emp
                            )
        emp_button.place(x=300, y=100)

    def update_dept():
        did = didupdate_entry.get()
        name = nameupdate_entry.get()
        desc = descupdate_entry.get()
        if selectdata.SelectData.if_value_present("department", "dept_id", did):
            inserttable.InsertData.update_department((name, desc, did))
            messagebox.showinfo(message="updated successfully")
            clear()
        else:
            messagebox.showerror(
                message="Department id is wrong cant be updated")

    main = Canvas(root,
                  height=550,
                  width=1200,
                  highlightthickness=0,
                  bg=LIGHT_COLOR)
    main.place(x=200, y=100)

    head_label = Label(main, text="Update  Department/ Employee",
                       font=HEAD_FONT,
                       bd=2,
                       width=60,
                       relief="solid",
                       bg=COLOR)
    head_label.place(x=20, y=20)

    did_label = Label(main,
                      text="Department Id",
                      font=TEXT_FONT,
                      bg=LIGHT_COLOR)
    did_label.place(x=80, y=100)
    didupdate_entry = Entry(main, width=5, font=TEXT_FONT)
    didupdate_entry.place(x=260, y=100)
    name_label = Label(main, text="Department Name",
                       font=TEXT_FONT,
                       bg=LIGHT_COLOR)
    name_label.place(x=80, y=180)
    nameupdate_entry = Entry(main,
                             width=50,
                             font=TEXT_FONT)
    nameupdate_entry.place(x=260, y=180)
    desc_label = Label(main,
                       text="Department Info",
                       font=TEXT_FONT,
                       bg=LIGHT_COLOR)
    desc_label.place(x=80, y=260)
    descupdate_entry = Entry(main, width=50, font=TEXT_FONT)
    descupdate_entry.place(x=260, y=260)
    update_button = Button(main, text="Update",
                           font=BUTTON_FONT,
                           width=15,
                           bg=COLOR,
                           command=update_dept
                           )
    update_button.place(x=450, y=320)
    update_emp_button = Button(main, text="Update Employee",
                               font=BUTTON_FONT,
                               width=25,
                               bg=LIGHT_COLOR,
                               command=update_emp_page

                               )
    update_emp_button.place(x=300, y=420)


def delete_page():
    def clear():
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        emp_name_entry.delete(0, END)
        emp_id_entry.delete(0, END)

    def delete_dept():
        id = id_entry.get()
        name = name_entry.get()
        print(id, name)
        if selectdata.SelectData.if_value_present_date("department", "dept_id", id, "dept_name", name):
            answer = messagebox.askokcancel(
                message="are you sure want to delete")
            if answer:
                selectdata.SelectData.delete_dept("department", "dept_id", id)
                messagebox.showinfo(message="deleted successfully")
                clear()
        else:
            messagebox.showerror(
                title="error", message="Id or name doesnt matched")

    def delete_emp():
        id = emp_id_entry.get()
        name = emp_name_entry.get()
        print(id, name)
        if selectdata.SelectData.if_value_present_date("employee", "emp_id", id, "name", name):
            answer = messagebox.askokcancel(
                message="are you sure want to delete")
            if answer:
                selectdata.SelectData.delete_dept("employee", "emp_id", id)
                messagebox.showinfo(message="deleted successfully")
                clear()
        else:
            messagebox.showerror(
                title="error", message="Id or name doesnt matched")

    main = Canvas(root,
                  height=550,
                  width=1200,
                  highlightthickness=0,
                  bg=LIGHT_COLOR)
    main.place(x=200, y=100)
    head_label = Label(main,
                       text="Delete",
                       bd=2,
                       relief="solid",
                       bg=COLOR,
                       width=60,
                       font=HEAD_FONT)
    head_label.place(x=20, y=20)
    id_label = Label(main, text="department ID ",
                     font=TEXT_FONT,
                     bg=LIGHT_COLOR)
    id_label.place(x=160, y=100)
    id_entry = Entry(main, width=20,
                     font=TEXT_FONT)
    id_entry.place(x=400, y=100)

    startdate_label = Label(main, text="department name   ",
                            font=TEXT_FONT,
                            bg=LIGHT_COLOR)
    startdate_label.place(x=160, y=150)
    name_entry = Entry(main, width=30,
                       font=TEXT_FONT)
    name_entry.place(x=400, y=150)
    delete_dept_button = Button(main, text="Delete department",
                                width=25,
                                font=BUTTON_FONT,
                                bg="red",
                                command=delete_dept
                                )
    delete_dept_button.place(x=300, y=200)

    id_label = Label(main, text="Employee ID ",
                     font=TEXT_FONT,
                     bg=LIGHT_COLOR)
    id_label.place(x=160, y=350)
    emp_id_entry = Entry(main, width=20,
                         font=TEXT_FONT)
    emp_id_entry.place(x=400, y=350)

    startdate_label = Label(main, text="Employee name   ",
                            font=TEXT_FONT,
                            bg=LIGHT_COLOR)
    startdate_label.place(x=160, y=410)
    emp_name_entry = Entry(main, width=30,
                           font=TEXT_FONT)
    emp_name_entry.place(x=400, y=410)
    delete_emp_button = Button(main, text="Delete Employee",
                               width=25,
                               font=BUTTON_FONT,
                               bg="red",
                               command=delete_emp
                               )
    delete_emp_button.place(x=300, y=460)


def add_task_page():

    def add_task():
        task = task_entry.get()
        id = id_entry.get()
        name = name_entry.get()

        if task:
            inserttable.InsertData.insert_status(
                (cur_admin_id, id, name, task, today, 0))
            update_task_list()
            task_entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    # Function to mark a task as completed

    def complete_task():
        selected_task = task_listbox.curselection()
        if selected_task:
            task_id = task_listbox.get(selected_task)[0]
            selectdata.SelectData.update_todolist(task_id,)
            update_task_list()

    # Function to delete a task

    def delete_task():
        selected_task = task_listbox.curselection()
        if selected_task:
            task_id = task_listbox.get(selected_task)[0]
            selectdata.SelectData.delete_task(task_id)

            update_task_list()

    def update_task_list():
        task_listbox.delete(0, END)
        cursor = selectdata.SelectData.update_task_list()
        for row in cursor:
            task_listbox.insert(
                END, f"{row[0]}  Date:-{row[1]}  -> Name : {row[2]}     task: {row[3]}   ")
        task_entry.delete(0, END)
        name_entry.delete(0, END)
        id_entry.delete(0, END)

    main = Canvas(root,
                  height=550,
                  width=1200,
                  highlightthickness=0,
                  bg=LIGHT_COLOR)
    main.place(x=200, y=100)
    head_label = Label(main,
                       text="Add task",
                       bd=2,
                       relief="solid",
                       bg=COLOR,
                       width=60,
                       font=HEAD_FONT)
    head_label.place(x=20, y=20)
    id_label = Label(main, text="Employee ID  ",
                     font=TEXT_FONT,
                     bg=LIGHT_COLOR)
    id_label.place(x=80, y=100)
    id_entry = Entry(main, width=5,
                     font=TEXT_FONT)
    id_entry.place(x=260, y=100)
    id_label = Label(main, text="Employee name  ",
                     font=TEXT_FONT,
                     bg=LIGHT_COLOR)
    id_label.place(x=360, y=100)
    name_entry = Entry(main, width=30,
                       font=TEXT_FONT)
    name_entry.place(x=550, y=100)
    id_label = Label(main, text="Task ",
                     font=TEXT_FONT,
                     bg=LIGHT_COLOR)
    id_label.place(x=80, y=160)
    task_entry = Entry(main, width=50,
                       font=TEXT_FONT)
    task_entry.place(x=170, y=160)
    add_button = Button(main, text="Add",
                        width=10,
                        font=BUTTON_FONT,
                        bg=COLOR,
                        command=add_task
                        )
    add_button.place(x=820, y=150)

    task_listbox = Listbox(main,
                           width=65,
                           font=TEXT_FONT)
    task_listbox.place(x=50, y=200)

    # Create complete task button
    complete_button = Button(main, text="Complete Task",
                             font=BUTTON_FONT,
                             bg=COLOR,
                             command=complete_task)
    complete_button.place(x=50, y=500)

    # Create delete task button
    delete_button = Button(main, text="Delete Task",
                           font=BUTTON_FONT,
                           bg=RED_COLOR,
                           command=delete_task)
    delete_button.place(x=700, y=500)

    # Update task list initially
    update_task_list()


def homepage():

    def currentmenu(buttonname):
        homebutton.config(bg=LIGHT_COLOR)
        attendancebutton.config(bg=LIGHT_COLOR)
        salarybutton.config(bg=LIGHT_COLOR)
        addemployeebutton.config(bg=LIGHT_COLOR)
        searchemployeebutton.config(bg=LIGHT_COLOR)
        departmentbutton.config(bg=LIGHT_COLOR)
        update_button.config(bg=LIGHT_COLOR)
        delete_button.config(bg=LIGHT_COLOR)
        addtaskbutton.config(bg=LIGHT_COLOR)
        buttonname.config(bg=DARK_COLOR)

    def home():
        currentmenu(homebutton)
        homewindow()

    def add_employee():
        currentmenu(addemployeebutton)
        add_employeepage()

    def search_employee():
        currentmenu(searchemployeebutton)
        search_employeepage()

    def attendance():
        currentmenu(attendancebutton)
        attendancepage()

    def salary():
        currentmenu(salarybutton)
        salarypage()

    def department():
        currentmenu(departmentbutton)
        departmentpage()

    def update():
        currentmenu(update_button)
        update_page()

    def delete():
        currentmenu(delete_button)
        delete_page()

    def add_task():
        currentmenu(addtaskbutton)
        add_task_page()
    maincanvas = Canvas(root,
                        width=1200,
                        height=650,
                        bg=LIGHT_COLOR,
                        highlightthickness=0,
                        )
    maincanvas.place(x=0, y=0)

    topbar = Canvas(maincanvas,
                    width=1200,
                    height=100,
                    bg=COLOR,
                    highlightthickness=0)
    topbar.place(x=0, y=0)
    logolabel = Label(topbar,
                      text="Employee Manangement System",
                      font=HEAD_FONT,
                      bg=COLOR,
                      )
    logolabel.place(x=450, y=7)
    logolabel = Label(topbar,
                      text="Admin user :- Admin",
                      font=HEAD_FONT,
                      bg=COLOR,
                      )
    logolabel.place(x=200, y=50)
    sidebar = Canvas(maincanvas,
                     width=200,
                     height=600,
                     bg=COLOR,
                     highlightthickness=0)
    sidebar.place(x=0, y=50)

    homebutton = Button(sidebar,
                        text="Home",
                        font=BUTTON_FONT,
                        width=15,
                        command=home)
    homebutton.place(x=10, y=70)

    addemployeebutton = Button(sidebar,
                               text="Add Employee",
                               font=BUTTON_FONT,
                               width=15,
                               command=add_employee)
    addemployeebutton.place(x=10, y=130)

    searchemployeebutton = Button(sidebar,
                                  text="Search Employee",
                                  font=BUTTON_FONT,
                                  width=15,
                                  command=search_employee)
    searchemployeebutton.place(x=10, y=190)
    departmentbutton = Button(sidebar,
                              text="Department",
                              font=BUTTON_FONT,
                              width=15,
                              command=department)
    departmentbutton.place(x=10, y=250)
    update_button = Button(sidebar,
                           text="Update",
                           font=BUTTON_FONT,
                           width=15,
                           command=update)
    update_button.place(x=10, y=310)
    delete_button = Button(sidebar,
                           text="Delete",
                           font=BUTTON_FONT,
                           width=15,
                           command=delete)
    delete_button.place(x=10, y=370)

    attendancebutton = Button(sidebar,
                              text="Attendance",
                              font=BUTTON_FONT,
                              width=15,
                              command=attendance)
    attendancebutton.place(x=10, y=430)

    salarybutton = Button(sidebar,
                          text="Salary",
                          font=BUTTON_FONT,
                          width=15,
                          command=salary)
    salarybutton.place(x=10, y=490)
    addtaskbutton = Button(sidebar,
                           text="add task",
                           font=BUTTON_FONT,
                           width=15,
                           command=add_task)
    addtaskbutton.place(x=10, y=550)
    labelimage = Label(maincanvas,
                       image=perfectimage,
                       bg=LIGHT_COLOR)
    labelimage.place(x=400, y=100)


def registerpage():

    def register():
        global cur_admin_id
        name = nameentry.get()
        gender = radio_state.get()
        age = int(ageentry.get())
        phone = phoneentry.get()
        email = emailentry.get()
        adress = adressentry.get()
        cmp_name = company_nameentry.get()
        username = usernameentry.get()
        password = passwordentry.get()
        cnfm_password = cnfm_passwordentry.get()

        check = inserttable.Check.empty_table("admin")
        if check == 'true':
            admin_id = 'A101'
        else:
            value = selectdata.SelectData.select_last_element(
                "admin_id", "admin", "admin_id")
            numeric_value = int(value[1:])
            admin_id = "A"+str(numeric_value+1)

        data = (admin_id, name, age, gender, phone, email,
                adress, cmp_name, username, password)
        if cnfm_password == password:
            inserttable.InsertData.insert_register(data)
            inserttable.InsertData.insert_login((admin_id, username, password))
            messagebox.showinfo(
                title='sucess', message="data saved successfully")
            cur_admin_id = admin_id
            homepage()
        else:
            messagebox.showinfo(
                title="issue", message="Password and confirm password doesnt match")

    def clear():
        name = nameentry.get()
        gender = radio_state.get()
        age = int(ageentry.get())
        phone = phoneentry.get()
        email = emailentry.get()
        adress = adressentry.get()
        cmp_name = company_nameentry.get()
        username = usernameentry.get()
        password = passwordentry.get()
        cnfm_password = cnfm_passwordentry.get()
        if len(password) or len(name) or len(phone) or len(username) != 0:
            answer = messagebox.askokcancel(
                title="clear data", message="all fields will be cleared")
        if answer:
            nameentry.delete(0, END)
            ageentry.delete(0, END)
            phoneentry.delete(0, END)
            adressentry.delete(0, END)
            emailentry.delete(0, END)
            company_nameentry.delete(0, END)
            usernameentry.delete(0, END)
            passwordentry.delete(0, END)
            cnfm_passwordentry.delete(0, END)

    main = Canvas(root,
                  width=1000,
                  height=580,
                  highlightthickness=0,
                  bd=4,
                  relief='raised',
                  bg=LIGHT_COLOR)
    main.place(x=100, y=30)

    titlelabel = Label(main,
                       text="REGISTER ",
                       bd=2,
                       relief='solid',
                       font=HEAD_FONT,
                       width=60,
                       bg=COLOR
                       )
    titlelabel.place(x=20, y=10)

    registercanvas = Canvas(main,
                            width=950,
                            height=450,
                            highlightthickness=0,
                            bd=2,
                            relief='solid',
                            bg=LIGHT_COLOR)
    registercanvas.place(x=20, y=60)

    namelabel = Label(registercanvas,
                      font=TEXT_FONT,
                      text="Name(*) : ",
                      bg=LIGHT_COLOR
                      )
    namelabel.place(x=80, y=10)

    radio_state = StringVar()
    radiobutton1 = Radiobutton(
        registercanvas, text="Male", value="M", font=TEXT_FONT, variable=radio_state, bg=LIGHT_COLOR)
    radiobutton2 = Radiobutton(
        registercanvas, text="Female", value="F", bg=LIGHT_COLOR, variable=radio_state, font=TEXT_FONT,)
    radiobutton1.place(x=800, y=10)
    radiobutton2.place(x=800, y=60)

    nameentry = Entry(registercanvas,
                      font=TEXT_FONT,
                      bg=LIGHT_COLOR,
                      width=30)
    nameentry.place(x=180, y=10)

    agelabel = Label(registercanvas,
                     font=TEXT_FONT,
                     text="Age: ",
                     bg=LIGHT_COLOR
                     )
    agelabel.place(x=580, y=10)

    ageentry = Entry(registercanvas,
                     font=TEXT_FONT,
                     bg=LIGHT_COLOR,
                     width=10)
    ageentry.place(x=640, y=10)

    phonelabel = Label(registercanvas,
                       font=TEXT_FONT,
                       text="Phone(*) : ",
                       bg=LIGHT_COLOR
                       )
    phonelabel.place(x=80, y=90)

    phoneentry = Entry(registercanvas,
                       font=TEXT_FONT,
                       bg=LIGHT_COLOR,
                       width=12)
    phoneentry.place(x=180, y=90)
    emaillabel = Label(registercanvas,
                       font=TEXT_FONT,
                       text="Email: ",
                       bg=LIGHT_COLOR
                       )
    emaillabel.place(x=330, y=90)

    emailentry = Entry(registercanvas,
                       font=TEXT_FONT,
                       bg=LIGHT_COLOR,
                       width=30)
    emailentry.place(x=400, y=90)
    adresslabel = Label(registercanvas,
                        font=TEXT_FONT,
                        text="Adress ",
                        bg=LIGHT_COLOR
                        )
    adresslabel.place(x=80, y=170)
    adressentry = Entry(registercanvas,
                        font=TEXT_FONT,
                        bg=LIGHT_COLOR,
                        width=46)
    adressentry.place(x=200, y=170)

    company_namelabel = Label(registercanvas,
                              font=TEXT_FONT,
                              text="Company Name  ",
                              bg=LIGHT_COLOR
                              )
    company_namelabel.place(x=80, y=250)
    company_nameentry = Entry(registercanvas,
                              font=TEXT_FONT,
                              bg=LIGHT_COLOR,
                              width=42)
    company_nameentry.place(x=240, y=250)

    usernamelabel = Label(registercanvas,
                          font=TEXT_FONT,
                          text="Username ",
                          bg=LIGHT_COLOR
                          )
    usernamelabel.place(x=80, y=330)
    usernameentry = Entry(registercanvas,
                          font=TEXT_FONT,
                          bg=LIGHT_COLOR,
                          width=30)
    usernameentry.place(x=200, y=330)

    passwordlabel = Label(registercanvas,
                          font=TEXT_FONT,
                          text="Password : ",
                          bg=LIGHT_COLOR
                          )
    passwordlabel.place(x=80, y=410)

    password = StringVar()

    passwordentry = Entry(registercanvas,
                          font=TEXT_FONT,
                          bg=LIGHT_COLOR,
                          textvariable=password,
                          show="*",
                          width=15)
    passwordentry.place(x=240, y=410)
    cnfm_passwordlabel = Label(registercanvas,
                               font=TEXT_FONT,
                               text="Confirm Password",
                               bg=LIGHT_COLOR
                               )
    cnfm_passwordlabel.place(x=450, y=410)

    password1 = StringVar()

    cnfm_passwordentry = Entry(registercanvas,
                               font=TEXT_FONT,
                               bg=LIGHT_COLOR,
                               textvariable=password1,
                               show="*",
                               width=15)
    cnfm_passwordentry.place(x=650, y=410)

    resetregisterbutton = Button(main,
                                 text="Reset",
                                 font=BUTTON_FONT,
                                 width=10,
                                 command=clear
                                 )
    resetregisterbutton.place(x=180, y=520)

    exitbutton = Button(main,
                        text="Exit",
                        font=BUTTON_FONT,
                        width=10,
                        command=exitwindow)
    exitbutton.place(x=320, y=520)
    savenextbutton = Button(main,
                            text="Register",
                            font=BUTTON_FONT,
                            bg=COLOR,
                            width=15,
                            command=register
                            )
    savenextbutton.place(x=460, y=520)


def loginpage():

    def clear():

        username = usernameentry.get()
        password = passwordentry.get()

        if len(username) or len(password) != 0:
            answer = messagebox.askokcancel(
                title="clear data", message="did you want to clear all")
            if answer:
                usernameentry.delete(0, END)
                passwordentry.delete(0, END)

    def login():
        global cur_admin_id
        username = usernameentry.get()
        password = passwordentry.get()
        ch = (username, password)
        if len(selectdata.SelectData.authorize(ch)) != 0:
            data = selectdata.SelectData.authorize((ch))
            cur_admin_id = data[0][0]
            homepage()
        else:
            messagebox.showinfo(
                title="missing", message="Incorrect username and password")

    main = Canvas(root, width=600, height=550,
                  highlightthickness=0, bd=4, relief='raised', bg=LIGHT_COLOR)
    main.place(x=300, y=30)

    titlelabel = Label(main,
                       text="LOGIN ",
                       bd=2,
                       relief='solid',
                       font=HEAD_FONT,
                       width=35,
                       bg=COLOR
                       )
    titlelabel.place(x=20, y=10)

    logincanvas = Canvas(main,
                         width=540,
                         height=300,
                         highlightthickness=0,
                         bd=2,
                         relief='solid',
                         bg=LIGHT_COLOR)
    logincanvas.place(x=30, y=100)

    usernamelabel = Label(logincanvas,
                          font=TEXT_FONT,
                          text="Username : ",
                          bg=LIGHT_COLOR
                          )
    usernamelabel.place(x=30, y=40)

    usernameentry = Entry(logincanvas,
                          font=TEXT_FONT,
                          bg=LIGHT_COLOR,
                          width=26)
    usernameentry.place(x=150, y=40)

    password = StringVar()

    passwordlabel = Label(logincanvas,
                          font=TEXT_FONT,
                          text="Password : ",
                          bg=LIGHT_COLOR,

                          )
    passwordlabel.place(x=30, y=110)

    passwordentry = Entry(logincanvas,
                          font=TEXT_FONT,
                          bg=LIGHT_COLOR,
                          textvariable=password,
                          show="*",
                          width=26)
    passwordentry.place(x=150, y=110)

    loginbutton = Button(logincanvas,
                         text="Login",
                         font=BUTTON_FONT,
                         bg=COLOR,
                         width=15,
                         command=login
                         )
    loginbutton.place(x=170, y=250)

    resetloginbutton = Button(main,
                              text="Reset",
                              font=BUTTON_FONT,
                              width=10,
                              command=clear
                              )
    resetloginbutton.place(x=60, y=460)
    exitbutton = Button(main,
                        text="Exit",
                        font=BUTTON_FONT,
                        width=10,
                        command=exitwindow
                        )
    exitbutton.place(x=220, y=460)
    registerbutton = Button(main,
                            text="Register",
                            font=BUTTON_FONT,
                            bg=COLOR,
                            width=15,
                            command=registerpage
                            )
    registerbutton.place(x=360, y=460)


def run():
    loginpage()


run()

root.mainloop()
