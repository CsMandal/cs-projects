from tkinter import *
import hovertext
from datetime import date
from tkinter import messagebox
from selectdata import SelectData
from insertdata import InsertData
from createtable import CreateTable

today = date.today()
# today = "2024-04-20"


cur_admin_id = 0

# colors section
DARK_GREEN_COLOR = "#037762"
SECOND_GREEN_COLOR = "#00A581"
LIGHT_GREEN_COLOR = "#05B581"
DARK_WHITE = "#F5F6F7"
DARK_WHITE2 = "#bfbfbf"
WHITE = "#FFFFFF"
BLUE_COLOR = "#3b71ca"
RED_COLOR = "#dc4c64"

# font section
TEXT_FONT = ('Candara', 16, 'normal')
HEAD_FONT = ('Candara', 22, 'normal')
LOGO_FONT = ("MS Serif", 22, 'bold')
BUTTON_FONT = ('Candara', 14, 'normal')
LIST_FONT = ('Candara', 12, 'bold')
BUTTON_LIST_FONT = ('Candara', 10, 'normal')

root = Tk()
root.title("Daily task management")
root.geometry("1000x650")
root.resizable(False, False)
root.configure(background="white")

# image section
bestimage = PhotoImage(file="images/best.png")
everythingimage = PhotoImage(file="images/everything.png")
goodthingsimage = PhotoImage(file="images/goodthings.png")
greatimage = PhotoImage(file="images/great.png")
justimage = PhotoImage(file="images/just.png")
makeimage = PhotoImage(file="images/make.png")
perfectdayimage = PhotoImage(file="images/perfectday.png")
positiveimage = PhotoImage(file="images/positive.png")
smileimage = PhotoImage(file="images/smile.png")
todayimage = PhotoImage(file="images/today.png")
homeimage = PhotoImage(file="images/home.png")

# icon section
barimage = PhotoImage(file="icons/bar.png")
dailyimage = PhotoImage(file="icons/daily.png")
dashboardimage = PhotoImage(file="icons/dashboard.png")
marketingimage = PhotoImage(file="icons/marketing.png")
stopwatchimage = PhotoImage(file="icons/stopwatch.png")
trophyimage = PhotoImage(file="icons/trophy.png")
clipboardimage = PhotoImage(file="icons/clipboard.png")
remainderimage = PhotoImage(file="icons/reminder.png")
removeimage = PhotoImage(file="icons/remove.png")


def bgpage():

    greencanvas = Canvas(root,
                         width=1000,
                         height=300,
                         highlightthickness=0,
                         bg=DARK_GREEN_COLOR)
    greencanvas.place(x=0, y=0)

    formcanvas = Canvas(root,
                        width=1000,
                        height=350,
                        highlightthickness=0,
                        bg=DARK_WHITE)
    formcanvas.place(x=0, y=300)


def exitwindow():
    answer = messagebox.askokcancel(
        title="exit ", message="are you sure want to exit ")
    if answer:
        root.destroy()


def registerpage():
    bgpage()

    def clearpage():
        nameentry.delete(0, END)
        ageentry.delete(0, END)
        phoneentry.delete(0, END)
        emailentry.delete(0, END)
        collegeentry.delete(0, END)
        usernameentry.delete(0, END)
        passwordentry.delete(0, END)
        confirmpasswordentry.delete(0, END)
        goalentry.delete(0, END)

    def clear():
        name = nameentry.get()
        phone = phoneentry.get()
        username = usernameentry.get()
        password = passwordentry.get()
        if len(password) or len(name) or len(phone) or len(username) != 0:
            answer = messagebox.askokcancel(
                title="clear data", message="all fields will be cleared")
            if answer:
                clearpage()

    def register():
        global cur_admin_id
        name = nameentry.get()
        age = ageentry.get()
        phone = phoneentry.get()
        email = emailentry.get()
        college = collegeentry.get()
        username = usernameentry.get()
        password = passwordentry.get()
        confirmpassword = confirmpasswordentry.get()
        goal = goalentry.get()
        if len(name) and len(phone) and len(email) and len(username) and len(password) and len(confirmpassword) != 0:
            if confirmpassword == password:
                data = (name, age, phone, email, college,
                        username, password, goal)
                InsertData.insert_admin(data)
                messagebox.showinfo(message="data saved succesfully")
                value = SelectData.login((username, password))
                cur_admin_id = value[0][0]
                maintaskpage()

            else:
                messagebox.showerror(
                    message="confirm password and password doesnt match ")
        else:
            messagebox.showerror(message="insert the data properly")

    formcanvas = Canvas(root,
                        width=800,
                        height=550,
                        highlightthickness=0,
                        bd=4,
                        relief='raised',
                        bg=WHITE)
    formcanvas.place(x=100, y=30)

    titlelabel = Label(formcanvas,
                       text="REGISTER ",
                       bd=2,
                       relief='solid',
                       font=HEAD_FONT,
                       width=47,
                       bg=DARK_WHITE
                       )
    titlelabel.place(x=20, y=10)

    registercanvas = Canvas(formcanvas,
                            width=760,
                            height=470,
                            highlightthickness=0,
                            bd=2,
                            relief='solid',
                            bg=WHITE)
    registercanvas.place(x=20, y=60)

    namelabel = Label(registercanvas,
                      font=TEXT_FONT,
                      text="Name(*) : ",
                      bg=WHITE
                      )
    namelabel.place(x=30, y=10)

    nameentry = Entry(registercanvas,
                      font=TEXT_FONT,
                      bg=DARK_WHITE,
                      width=30)
    nameentry.place(x=130, y=10)

    agelabel = Label(registercanvas,
                     font=TEXT_FONT,
                     text="Age: ",
                     bg=WHITE
                     )
    agelabel.place(x=530, y=10)

    ageentry = Entry(registercanvas,
                     font=TEXT_FONT,
                     bg=DARK_WHITE,
                     width=10)
    ageentry.place(x=590, y=10)

    phonelabel = Label(registercanvas,
                       font=TEXT_FONT,
                       text="Phone(*) : ",
                       bg=WHITE
                       )
    phonelabel.place(x=30, y=60)

    phoneentry = Entry(registercanvas,
                       font=TEXT_FONT,
                       bg=DARK_WHITE,
                       width=12)
    phoneentry.place(x=130, y=60)

    emaillabel = Label(registercanvas,
                       font=TEXT_FONT,
                       text="Email: ",
                       bg=WHITE
                       )
    emaillabel.place(x=280, y=60)

    emailentry = Entry(registercanvas,
                       font=TEXT_FONT,
                       bg=DARK_WHITE,
                       width=30)
    emailentry.place(x=350, y=60)

    collegelabel = Label(registercanvas,
                         font=TEXT_FONT,
                         text="College : ",
                         bg=WHITE
                         )
    collegelabel.place(x=30, y=110)

    collegeentry = Entry(registercanvas,
                         font=TEXT_FONT,
                         bg=DARK_WHITE,
                         width=48)
    collegeentry.place(x=130, y=110)

    usernamelabel = Label(registercanvas,
                          font=TEXT_FONT,
                          text="Username(*) : ",
                          bg=WHITE
                          )
    usernamelabel.place(x=30, y=160)

    usernameentry = Entry(registercanvas,
                          font=TEXT_FONT,
                          bg=DARK_WHITE,
                          width=30)
    usernameentry.place(x=180, y=160)

    passwordlabel = Label(registercanvas,
                          font=TEXT_FONT,
                          text="Password(*) : ",
                          bg=WHITE
                          )
    passwordlabel.place(x=30, y=210)
    password = StringVar()
    passwordentry = Entry(registercanvas,
                          font=TEXT_FONT,
                          bg=DARK_WHITE,
                          textvariable=password,
                          show="*",
                          width=30)
    passwordentry.place(x=180, y=210)

    hovertext.CreateToolTip(
        passwordlabel, "Password must contain\natleast 8 characters\n1 uppercase\n1 lowercase\n1 number\n1 special character")

    confirmpasswordlabel = Label(registercanvas,
                                 font=TEXT_FONT,
                                 text="Confirm Password (*): ",
                                 bg=WHITE
                                 )
    confirmpasswordlabel.place(x=30, y=260)

    password1 = StringVar()
    confirmpasswordentry = Entry(registercanvas,
                                 font=TEXT_FONT,
                                 bg=DARK_WHITE,
                                 textvariable=password1,
                                 show="*",
                                 width=38)
    confirmpasswordentry.place(x=250, y=260)

    goallabel = Label(registercanvas,
                      font=TEXT_FONT,
                      text="Goal : ",
                      bg=WHITE
                      )
    goallabel.place(x=30, y=310)

    goalentry = Entry(registercanvas,
                      font=TEXT_FONT,
                      bg=DARK_WHITE,
                      width=51)
    goalentry.place(x=90, y=310)

    resetregisterbutton = Button(registercanvas,
                                 text="Reset",
                                 font=BUTTON_FONT,
                                 width=10,
                                 command=clear)
    resetregisterbutton.place(x=180, y=400)

    exitbutton = Button(registercanvas,
                        text="Exit",
                        font=BUTTON_FONT,
                        width=10,
                        command=exitwindow)
    exitbutton.place(x=320, y=400)
    savenextbutton = Button(registercanvas,
                            text="Save & Next",
                            font=BUTTON_FONT,
                            bg=LIGHT_GREEN_COLOR,
                            width=15,
                            command=register
                            )
    savenextbutton.place(x=460, y=400)


def loginpage():
    bgpage()

    def clearpage():
        usernameentry.delete(0, END)
        passwordentry.delete(0, END)

    def clear():
        username = usernameentry.get()
        password = passwordentry.get()

        if len(username) or len(password) != 0:
            answer = messagebox.askokcancel(
                title="clear data", message="did you want to clear all")
            if answer:
                clearpage()

    def login():
        global cur_admin_id
        username = usernameentry.get()
        password = passwordentry.get()

        if len(username) and len(password) != 0:
            data = (username, password)
            value = SelectData.login(data)
            if value:
                messagebox.showinfo(
                    message=f"{value[0][1]} login sucess fully")
                cur_admin_id = value[0][0]
                homepage()
            else:
                messagebox.showerror(
                    message="password and username doesnt match")
                clearpage()

        else:
            messagebox.showerror(message="insert the required data")

    formcanvas = Canvas(root,
                        width=800,
                        height=550,
                        highlightthickness=0,
                        bd=4,
                        relief='raised',
                        bg=WHITE)
    formcanvas.place(x=100, y=30)

    titlelabel = Label(formcanvas,
                       text="LOGIN ",
                       bd=2,
                       relief='solid',
                       font=TEXT_FONT,
                       width=69,
                       bg=DARK_WHITE
                       )
    titlelabel.place(x=20, y=10)

    imagelabel = Label(formcanvas,
                       image=goodthingsimage,
                       bg=WHITE)
    imagelabel.place(x=30, y=150)

    logincanvas = Canvas(formcanvas,
                         width=480,
                         height=350,
                         highlightthickness=0,
                         bd=2,
                         relief='solid',
                         bg=WHITE)
    logincanvas.place(x=300, y=100)

    usernamelabel = Label(logincanvas,
                          font=TEXT_FONT,
                          text="Username : ",
                          bg=WHITE
                          )
    usernamelabel.place(x=30, y=40)

    usernameentry = Entry(logincanvas,
                          font=TEXT_FONT,
                          bg=DARK_WHITE,
                          width=26)
    usernameentry.place(x=150, y=40)

    password = StringVar()

    passwordlabel = Label(logincanvas,
                          font=TEXT_FONT,
                          text="Password : ",

                          bg=WHITE,

                          )
    passwordlabel.place(x=30, y=110)

    passwordentry = Entry(logincanvas,
                          font=TEXT_FONT,
                          bg=DARK_WHITE,
                          textvariable=password,
                          show="*",
                          width=26)
    passwordentry.place(x=150, y=110)

    loginbutton = Button(logincanvas,
                         text="Login",
                         font=BUTTON_FONT,
                         bg=LIGHT_GREEN_COLOR,
                         width=15,
                         command=login
                         )
    loginbutton.place(x=170, y=250)

    resetloginbutton = Button(formcanvas,
                              text="Reset",
                              font=BUTTON_FONT,
                              width=10,
                              command=clear)
    resetloginbutton.place(x=180, y=500)

    exitbutton = Button(formcanvas,
                        text="Exit",
                        font=BUTTON_FONT,
                        width=10,
                        command=exitwindow)
    exitbutton.place(x=320, y=500)
    registerbutton = Button(formcanvas,
                            text="Register",
                            font=BUTTON_FONT,
                            bg=LIGHT_GREEN_COLOR,
                            width=15,
                            command=registerpage)
    registerbutton.place(x=460, y=500)


def maintaskpage():

    bgpage()

    def clearpage():
        nameentry.delete(0, END)
        starttimeentry.delete(0, END)
        endtimeentry.delete(0, END)
        descentry.delete(0, END)
        daycountentry.delete(0, END)

    def clear():
        start_time = starttimeentry.get()
        endtime = endtimeentry.get()
        name = nameentry.get()
        desc = descentry.get()
        daycount = int(daycountentry.get())
        if len(start_time) or len(endtime) or len(name) or len(desc) != 0:
            answer = messagebox.askokcancel(
                title="clear data", message="all fields will be cleared")
            if answer:
                clearpage()

    def addtask():
        start = starttimeentry.get()
        end = endtimeentry.get()
        name = nameentry.get()
        desc = descentry.get()
        daycount = int(daycountentry.get())
        if len(start) and len(end) and len(name) and len(desc) != 0:
            data = (cur_admin_id, start, end, name, desc, daycount)
            InsertData.insert_maintask(data)
            messagebox.showinfo(message="data saved successfully")
            clearpage()

        else:
            messagebox.showerror(message="insert the fields properly")

    maincanvas = Canvas(root,
                        width=800,
                        height=550,
                        highlightthickness=0,
                        bd=4,
                        relief='raised',
                        bg=WHITE)
    maincanvas.place(x=100, y=30)

    titlelabel = Label(maincanvas,
                       text="Add Your Task ",
                       bd=2,
                       relief='solid',
                       font=HEAD_FONT,
                       width=47,
                       bg=DARK_WHITE
                       )
    titlelabel.place(x=20, y=10)

    imagelabel = Label(maincanvas,
                       image=bestimage,
                       bg=WHITE)
    imagelabel.place(x=30, y=150)

    main = Canvas(maincanvas, width=480,
                  height=400,
                  bd=2,
                  relief="solid",
                  bg=WHITE)
    main.place(x=300, y=70)

    heading = Label(main,
                    text=" enter your task",
                    bd=2,
                    relief='solid',
                    font=TEXT_FONT,
                    width=40,
                    bg=DARK_WHITE
                    )
    heading.place(x=20, y=10)

    timelabel = Label(main,
                      font=TEXT_FONT,
                      text="time: ",
                      bg=WHITE,

                      )
    timelabel.place(x=30, y=80)
    starttimeentry = Entry(main,
                           font=TEXT_FONT,
                           bg=WHITE,
                           width=6,
                           justify="center")
    starttimeentry.insert(1, "start")
    starttimeentry.place(x=100, y=80)
    endtimeentry = Entry(main,
                         font=TEXT_FONT,
                         bg=WHITE,
                         width=6,
                         justify="center")
    endtimeentry.insert(1, "end")
    endtimeentry.place(x=200, y=80)

    namelabel = Label(main,
                      font=TEXT_FONT,
                      text="Task(*) : ",
                      bg=WHITE
                      )
    namelabel.place(x=30, y=130)

    nameentry = Entry(main,
                      font=TEXT_FONT,
                      bg=WHITE,
                      width=27)
    nameentry.place(x=130, y=130)
    desclabel = Label(main,
                      font=TEXT_FONT,
                      text="Description : ",
                      bg=WHITE
                      )
    desclabel.place(x=30, y=190)

    descentry = Entry(main,
                      font=TEXT_FONT,
                      bg=WHITE,
                      width=25)
    descentry.place(x=160, y=190)

    daycountlabel = Label(main,
                          font=TEXT_FONT,
                          text="Day Count : ",
                          bg=WHITE
                          )
    daycountlabel.place(x=30, y=250)

    daycountentry = Entry(main,
                          font=TEXT_FONT,
                          bg=WHITE,
                          width=25)
    daycountentry.place(x=160, y=250)

    saveaddbutton = Button(main,
                           text="Save & Add Next Task",
                           font=BUTTON_FONT,
                           bg=LIGHT_GREEN_COLOR,
                           width=20,
                           command=addtask
                           )
    saveaddbutton.place(x=150, y=335)

    resetbutton = Button(maincanvas,
                         text="Reset",
                         font=BUTTON_FONT,
                         width=10,
                         command=clear)
    resetbutton.place(x=180, y=500)

    exitbutton = Button(maincanvas,
                        text="Exit",
                        font=BUTTON_FONT,
                        width=10,
                        command=exitwindow)
    exitbutton.place(x=320, y=500)
    savenexttaskbutton = Button(maincanvas,
                                text="Save & Next",
                                font=BUTTON_FONT,
                                bg=LIGHT_GREEN_COLOR,
                                width=15,
                                command=homepage
                                )
    savenexttaskbutton.place(x=460, y=500)


def todolistwindow():
    main = Canvas(root,
                  width=585,
                  height=650,
                  bg=DARK_WHITE,
                  highlightthickness=0,
                  )
    main.place(x=370, y=50)

    todolist = Label(main,
                     font=TEXT_FONT,
                     text="To Do List",
                     bg=DARK_WHITE,
                     width=43,
                     bd=2,
                     relief="solid"
                     )
    todolist.place(x=50, y=30)

    def add_task():
        task = task_entry.get()
        if task:
            InsertData.insert_todolist((cur_admin_id, task, today, 0))
            update_task_list()
            task_entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    # Function to mark a task as completed

    def complete_task():
        selected_task = task_listbox.curselection()
        if selected_task:
            task_id = task_listbox.get(selected_task)[0]
            SelectData.update_todolist(task_id,)
            update_task_list()

    # Function to delete a task

    def delete_task():
        selected_task = task_listbox.curselection()
        if selected_task:
            task_id = task_listbox.get(selected_task)[0]
            SelectData.delete_task(task_id)

            update_task_list()

    def update_task_list():
        task_listbox.delete(0, END)
        cursor = SelectData.update_task_list()
        for row in cursor:
            task_listbox.insert(
                END, f"{row[0]}  Date:-{row[1]}  ->  {row[2]}   ")

    task_entry = Entry(main,
                       width=32,
                       font=TEXT_FONT
                       )
    task_entry.place(x=50, y=120)

    # Create add task button
    add_button = Button(main,
                        text="Add Task",
                        font=BUTTON_FONT,
                        bg=LIGHT_GREEN_COLOR,
                        command=add_task)
    add_button.place(x=460, y=120)

    # Create task listbox
    task_listbox = Listbox(main,
                           width=40,
                           font=TEXT_FONT)
    task_listbox.place(x=50, y=200)

    # Create complete task button
    complete_button = Button(main, text="Complete Task",
                             font=BUTTON_FONT,
                             bg=LIGHT_GREEN_COLOR,
                             command=complete_task)
    complete_button.place(x=50, y=500)

    # Create delete task button
    delete_button = Button(main, text="Delete Task",
                           font=BUTTON_FONT,
                           bg=RED_COLOR,
                           command=delete_task)
    delete_button.place(x=450, y=500)

    # Update task list initially
    update_task_list()


def progresswindow():
    main = Canvas(root,
                  width=585,
                  height=650,
                  bg=DARK_WHITE,
                  highlightthickness=0,
                  )
    main.place(x=370, y=50)

    todolist = Label(main,
                     font=TEXT_FONT,
                     text="To Do List",
                     bg=DARK_WHITE,
                     width=43,
                     bd=2,
                     relief="solid"
                     )
    todolist.place(x=50, y=30)

    done = SelectData.select_count_done(cur_admin_id, today)
    fail = SelectData.select_count_fail(cur_admin_id, today)

    todolist = Label(main,
                     font=TEXT_FONT,
                     text=f"today task completed : {done[0]}\ntoday task failed :{fail[0]}",
                     bg=DARK_WHITE,
                     width=30,
                     )
    todolist.place(x=150, y=120)
    total = done[0]+fail[0]
    percent = done[0]/total * 100
    percent = str(round(percent, 2))
    todolist = Label(main,
                     font=TEXT_FONT,
                     text=f"Today Progress : {percent}%",
                     bg="light green",
                     width=30,
                     )
    todolist.place(x=150, y=220)


def designhomepage(maincanvas, data, y):

    def edit():
        def clearpage():
            nameentry.delete(0, END)
            starttimeentry.delete(0, END)
            endtimeentry.delete(0, END)
            descentry.delete(0, END)
            daycountentry.delete(0, END)

        def update():
            start = starttimeentry.get()
            end = endtimeentry.get()
            name = nameentry.get()
            desc = descentry.get()
            daycount = int(daycountentry.get())
            InsertData.update_maintask(
                (start, end, name, desc, daycount, data[1]))
            messagebox.showinfo(message="Data updated successfully")
            maincanvas = Canvas(root,
                                width=300,
                                height=600,
                                highlightthickness=0)
            maincanvas.place(x=50, y=50)
            y = 0
            datas = SelectData.select_all_data(
                "maintask", "admin_id", cur_admin_id)
            for datan in datas:
                designhomepage(maincanvas, datan, y)
                y += 105
            clearpage()

        mainc = Canvas(root,
                       width=700,
                       height=650,
                       bg=DARK_WHITE,
                       highlightthickness=0,
                       )
        mainc.place(x=370, y=50)

        main = Canvas(mainc, width=480,
                      height=400,
                      bd=2,
                      relief="solid",
                      bg=WHITE)
        main.place(x=40, y=10)

        heading = Label(main,
                        text=" Update your task",
                        bd=2,
                        relief='solid',
                        font=TEXT_FONT,
                        width=40,
                        bg=DARK_WHITE
                        )
        heading.place(x=20, y=10)

        timelabel = Label(main,
                          font=TEXT_FONT,
                          text="time: ",
                          bg=WHITE,

                          )
        timelabel.place(x=30, y=80)
        starttimeentry = Entry(main,
                               font=TEXT_FONT,
                               bg=WHITE,
                               width=6,
                               justify="center")
        starttimeentry.insert(1, data[2])
        starttimeentry.place(x=100, y=80)
        endtimeentry = Entry(main,
                             font=TEXT_FONT,
                             bg=WHITE,
                             width=6,
                             justify="center")
        endtimeentry.insert(1, data[3])
        endtimeentry.place(x=200, y=80)

        namelabel = Label(main,
                          font=TEXT_FONT,
                          text="Task(*) : ",
                          bg=WHITE
                          )
        namelabel.place(x=30, y=130)

        nameentry = Entry(main,
                          font=TEXT_FONT,
                          bg=WHITE,
                          width=27)
        nameentry.insert(1, data[4])
        nameentry.place(x=130, y=130)
        desclabel = Label(main,
                          font=TEXT_FONT,
                          text="Description : ",
                          bg=WHITE
                          )

        desclabel.place(x=30, y=190)

        descentry = Entry(main,
                          font=TEXT_FONT,
                          bg=WHITE,
                          width=25)
        descentry.insert(1, data[5])
        descentry.place(x=160, y=190)

        daycountlabel = Label(main,
                              font=TEXT_FONT,
                              text="Day Count : ",
                              bg=WHITE
                              )
        daycountlabel.place(x=30, y=250)

        daycountentry = Entry(main,
                              font=TEXT_FONT,
                              bg=WHITE,
                              width=25)
        daycountentry.insert(1, data[6])
        daycountentry.place(x=160, y=250)
        updatebutton = Button(main,
                              text="Update Task",
                              font=BUTTON_FONT,
                              bg=LIGHT_GREEN_COLOR,
                              width=20,
                              command=update
                              )
        updatebutton.place(x=150, y=335)

    def comment():
        def add():
            note = noteentry.get()
            commentv = commententry.get()
            InsertData.insert_subtask((cur_admin_id, data[1], note, commentv))
            messagebox.showinfo(message="data saved succesfully")
            noteentry.delete(0, END)
            commententry.delete(0, END)

        mainc = Canvas(root,
                       width=700,
                       height=650,
                       bg=DARK_WHITE,
                       highlightthickness=0,
                       )
        mainc.place(x=370, y=50)

        main = Canvas(mainc, width=480,
                      height=400,
                      bd=2,
                      relief="solid",
                      bg=WHITE)
        main.place(x=40, y=10)

        heading = Label(main,
                        text=" Add comment to  task",
                        bd=2,
                        relief='solid',
                        font=TEXT_FONT,
                        width=40,
                        bg=DARK_WHITE
                        )
        heading.place(x=20, y=20)
        desclabel = Label(main,
                          font=TEXT_FONT,
                          text="Add note: ",
                          bg=WHITE
                          )

        desclabel.place(x=30, y=120)

        noteentry = Entry(main,
                          font=TEXT_FONT,
                          bg=WHITE,
                          width=25)
        noteentry.place(x=160, y=120)
        desclabel = Label(main,
                          font=TEXT_FONT,
                          text="Add comment: ",
                          bg=WHITE
                          )

        desclabel.place(x=30, y=200)

        commententry = Entry(main,
                             font=TEXT_FONT,
                             bg=WHITE,
                             width=25)
        commententry.place(x=160, y=200)
        Addbutton = Button(main,
                           text="Update Task",
                           font=BUTTON_FONT,
                           bg=LIGHT_GREEN_COLOR,
                           width=20,
                           command=add
                           )
        Addbutton.place(x=150, y=280)

    def disable():
        value = SelectData.check_done((cur_admin_id, data[1], today))

        if (value[0][0]):
            donebutton.config(state="disabled")
            failbutton.config(state="disabled")

    def done():
        InsertData.insert_status((cur_admin_id, data[1], today, 1))
        messagebox.showinfo(message="marked as doned task")
        disable()

    def fail():
        InsertData.insert_status((cur_admin_id, data[1], today, 0))
        messagebox.showinfo(message="marked as failed task")
        disable()

    main = Canvas(maincanvas,
                  width=290,
                  height=100,
                  bd=2,
                  relief="solid",
                  highlightthickness=0)
    main.place(x=5, y=5+y)
    startlabel = Label(main,
                       font=LIST_FONT,
                       text=f"start :{data[2]}  task :{data[4]} Time :{data[3]}",
                       )
    startlabel.place(x=5, y=5)
    desclabel = Label(main,
                      font=LIST_FONT,
                      text=f"desc  : {data[5]}  daycount :{data[6]}",
                      )
    desclabel.place(x=5, y=30)
    editbutton = Button(main,
                        font=BUTTON_LIST_FONT,
                        text="edit",
                        width=5,
                        command=edit
                        )
    editbutton.place(x=5, y=60)
    commentbutton = Button(main,
                           font=BUTTON_LIST_FONT,
                           text="comment",
                           width=8,
                           command=comment
                           )
    commentbutton.place(x=70, y=60)
    donebutton = Button(main,
                        font=BUTTON_LIST_FONT,
                        text="Done",
                        width=5,
                        command=done
                        )
    donebutton.place(x=160, y=60)
    failbutton = Button(main,
                        font=BUTTON_LIST_FONT,
                        text="Fail",
                        width=5,
                        command=fail
                        )
    failbutton.place(x=230, y=60)
    disable()


def reportpage():

    def donefail(value):
        if value:
            return "done"
        else:
            return "fail"

    def search_task():
        name = nameentry.get()
        value = SelectData.count_report((name, cur_admin_id))
        task_listbox.delete(0, END)
        if value[0]:
            task = SelectData.select_task_id((name, cur_admin_id))
            datas = SelectData.select_all_report((task[0], cur_admin_id))
            for data in datas:
                task_listbox.insert(
                    1, f" date :{ data[3]}    task :{name}      {donefail(data[4])} ")
            print(type(task[0]))
            done = SelectData.done_report((task[0],))
            fail = SelectData.fail_report((task[0],))
            total = done[0] + fail[0]
            percent = done[0]/total * 100
            todolist.config(
                text=f" total done :{done[0]}  done percentage : {percent}%")
        else:
            messagebox.showerror(message="incorrect task name")

    main = Canvas(root,
                  width=700,
                  height=650,
                  bg=DARK_WHITE,
                  highlightthickness=0,
                  )
    main.place(x=370, y=50)

    todolist = Label(main,
                     font=TEXT_FONT,
                     text="Task Report",
                     bg=DARK_WHITE,
                     width=43,
                     bd=2,
                     relief="solid"
                     )
    todolist.place(x=50, y=30)
    namelabel = Label(main,
                      font=TEXT_FONT,
                      text="Task Name : ",

                      )
    namelabel.place(x=30, y=130)

    nameentry = Entry(main,
                      font=TEXT_FONT,

                      width=32)
    nameentry.place(x=150, y=130)
    saveaddbutton = Button(main,
                           text="Search",
                           font=BUTTON_FONT,
                           bg=LIGHT_GREEN_COLOR,
                           width=20,
                           command=search_task
                           )
    saveaddbutton.place(x=150, y=180)
    task_listbox = Listbox(main,
                           width=45,
                           font=TEXT_FONT)
    task_listbox.place(x=30, y=250)
    todolist = Label(main,
                     font=TEXT_FONT,
                     text="Task Report",
                     bg="light green",
                     width=43,
                     bd=2,
                     relief="solid"
                     )
    todolist.place(x=50, y=530)


def viewpage():

    def update_value(datas):
        namelabel = Label(main,
                          font=TEXT_FONT,
                          text="Task note                      comment",
                          )
        namelabel.place(x=30, y=250)
        y = 0
        for data in datas:
            namelabel = Label(main,
                              font=TEXT_FONT,
                              text=f"{data[0]}                  {data[1]}",
                              )
            namelabel.place(x=30, y=300+y)
            y += 50

    def update():
        name = nameentry.get()
        value = SelectData.select_task_id((name, cur_admin_id))
        if value[0]:
            data = SelectData.select_note_comment((value[0], cur_admin_id))
            update_value(data)
        else:
            messagebox.showerror(message="name is incorrect")

    main = Canvas(root,
                  width=700,
                  height=650,
                  bg=DARK_WHITE,
                  highlightthickness=0,
                  )
    main.place(x=370, y=50)

    todolist = Label(main,
                     font=TEXT_FONT,
                     text="View note",
                     bg=DARK_WHITE,
                     width=43,
                     bd=2,
                     relief="solid"
                     )
    todolist.place(x=50, y=30)
    namelabel = Label(main,
                      font=TEXT_FONT,
                      text="Task Name : ",

                      )
    namelabel.place(x=30, y=130)

    nameentry = Entry(main,
                      font=TEXT_FONT,

                      width=32)
    nameentry.place(x=150, y=130)
    saveaddbutton = Button(main,
                           text="Search",
                           font=BUTTON_FONT,
                           bg=LIGHT_GREEN_COLOR,
                           width=20,
                           command=update

                           )
    saveaddbutton.place(x=150, y=180)


def homepage():

    maincanvas = Canvas(root,
                        width=1000,
                        height=650,
                        bg=DARK_WHITE,
                        highlightthickness=0,
                        )
    maincanvas.place(x=0, y=0)

    topbar = Canvas(maincanvas,
                    width=1000,
                    height=50,
                    bg=DARK_WHITE2,
                    highlightthickness=0)
    topbar.place(x=0, y=0)

    imagelabel = Label(topbar,
                       image=dailyimage,
                       highlightthickness=0,
                       bg=DARK_WHITE2,
                       fg=LIGHT_GREEN_COLOR)
    imagelabel.place(x=300, y=0)
    logolabel = Label(topbar,
                      text="Daily Task Management System",
                      font=LOGO_FONT,
                      bg=DARK_WHITE2,
                      )
    logolabel.place(x=355, y=7)
    imagelabel = Label(root,
                       image=greatimage,
                       highlightthickness=0,
                       bg=DARK_WHITE
                       )
    imagelabel.place(x=450, y=60)

    sidebar = Canvas(maincanvas,
                     width=70,
                     height=600,
                     bg=DARK_WHITE2,
                     highlightthickness=0)
    sidebar.place(x=0, y=50)
    maincanvas = Canvas(maincanvas,
                        width=300,
                        height=600,
                        highlightthickness=0)
    y = 0
    maincanvas.place(x=50, y=50)
    datas = SelectData.select_all_data("maintask", "admin_id", cur_admin_id)
    for data in datas:
        designhomepage(maincanvas, data, y)
        y += 105

    def currentmenu(buttonname):
        homebutton.config(bg=DARK_WHITE)
        todolistbutton.config(bg=DARK_WHITE)
        reportbutton.config(bg=DARK_WHITE)
        progressbutton.config(bg=DARK_WHITE)
        updatebutton.config(bg=DARK_WHITE)
        # deletebutton.config(bg=DARK_WHITE)
        buttonname.config(bg=LIGHT_GREEN_COLOR)

    def home():
        currentmenu(homebutton)
        homepage()

    def todolist():
        currentmenu(todolistbutton)
        todolistwindow()

    def progress():
        currentmenu(progressbutton)
        progresswindow()

    def report():
        currentmenu(reportbutton)
        reportpage()

    def update():
        currentmenu(updatebutton)
        viewpage()

    def delete():
        # currentmenu(deletebutton)
        pass

    homebutton = Button(sidebar,
                        image=dashboardimage,
                        command=home)
    homebutton.place(x=5, y=10)
    hovertext.CreateToolTip(homebutton, "home")

    todolistbutton = Button(sidebar,
                            image=marketingimage,
                            command=todolist)
    todolistbutton.place(x=5, y=90)
    hovertext.CreateToolTip(todolistbutton, "To Do List")

    progressbutton = Button(sidebar,
                            image=barimage,
                            command=progress)
    progressbutton.place(x=5, y=180)
    hovertext.CreateToolTip(progressbutton, "progress")

    reportbutton = Button(sidebar,
                          image=trophyimage,
                          command=report)
    reportbutton.place(x=5, y=270)
    hovertext.CreateToolTip(reportbutton, "Report")

    updatebutton = Button(sidebar,
                          image=clipboardimage,
                          command=update)
    updatebutton.place(x=5, y=360)
    hovertext.CreateToolTip(updatebutton, "View notes")

    # deletebutton = Button(sidebar,
    #                       image=removeimage,
    #                       command=delete)
    # deletebutton.place(x=5, y=450)
    # hovertext.CreateToolTip(deletebutton, "Delete")


def run():
    loginpage()


run()
root.mainloop()
