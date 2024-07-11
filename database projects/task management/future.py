def forgetusernamewindow():
    window = Toplevel(root)
    window.title("Forget Username")
    window.geometry("500x500")
    window.resizable(False, False)
    window.configure(bg=DARK_WHITE)
    upcanvas = Canvas(window,
                      width=500,
                      height=250,
                      bg=DARK_GREEN_COLOR,
                      highlightthickness=0)
    upcanvas.place(x=0, y=0)
    downcanvas = Canvas(window,
                        width=500,
                        height=250,
                        bg=WHITE,
                        highlightthickness=0)
    downcanvas.place(x=0, y=250)

    main = Canvas(window,
                  width=400,
                  height=400,
                  bg=WHITE,
                  highlightthickness=0,
                  bd=2,
                  relief="raised")
    main.place(x=50, y=50)

    headinglabel = Label(main,
                         text="Forget Username/Password",
                         font=TEXT_FONT,
                         width=35,
                         bd=2,
                         relief="solid")
    headinglabel.place(x=10, y=10)
    formcanvas = Canvas(main,
                        height=340,
                        width=380,
                        bd=2,
                        relief="solid",
                        bg=WHITE)
    formcanvas.place(x=10, y=50)

    namelabel1 = Label(formcanvas,
                       text="Name :",
                       font=TEXT_FONT,
                       bg=WHITE)
    namelabel1.place(x=10, y=30)
    nameentry1 = Entry(formcanvas,
                       font=TEXT_FONT,
                       width=23,
                       bg=DARK_WHITE)
    nameentry1.place(x=80, y=30)

    phonelabel1 = Label(formcanvas,
                        text="Phone",
                        font=TEXT_FONT,
                        bg=WHITE)
    phonelabel1.place(x=10, y=90)
    phoneentry1 = Entry(formcanvas,
                        font=TEXT_FONT,
                        width=23,
                        bg=DARK_WHITE)
    phoneentry1.place(x=80, y=90)
    findbutton = Button(formcanvas,
                        text="Find",
                        width=10,
                        bg=LIGHT_GREEN_COLOR,
                        font=BUTTON_FONT)
    findbutton.place(x=140, y=210)

    forgetusernamebutton = Button(logincanvas,
                                  text="Forget Username/Password",
                                  font=BUTTON_FONT,
                                  width=30,
                                  command=forgetusernamewindow)
    forgetusernamebutton.place(x=80, y=190)


def updatepage():

    def update_value(data):

        def update_maintask():
            start = starttimeentry.get()
            end = endtimeentry.get()
            name = nameentry.get()
            desc = descentry.get()
            daycount = int(daycountentry.get())
            datas = (start, end, name, desc, daycount, data[1])
            InsertData.update_maintask(datas)
            messagebox.showinfo(message="pdated sucessfully")

        main = Canvas(root, width=480,
                      height=400,
                      bd=2,
                      relief="solid",
                      bg=WHITE)
        main.place(x=430, y=150)

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

        saveaddbutton = Button(main,
                               text="Save & Add Next Task",
                               font=BUTTON_FONT,
                               bg=LIGHT_GREEN_COLOR,
                               width=20,
                               command=update_maintask

                               )
        saveaddbutton.place(x=150, y=335)

    def update():
        name = nameentry.get()
        value = SelectData.count_report((name, cur_admin_id))
        if value[0]:
            data = SelectData.select_all_maintask((name, cur_admin_id))
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
                     text="Update task",
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
