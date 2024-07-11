from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
character = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-']


def generate():
    alpha = [choice(alphabet) for _ in range(randint(8, 10))]
    digit = [choice(digits) for _ in range(randint(2, 4))]
    charcter = [choice(character) for _ in range(randint(2, 4))]

    password_list = alpha + digit + charcter
    shuffle(password_list)

    password = "".join(str(elem) for elem in password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def search():
    website = website_entry.get()

    try:
        with open('data.json') as data:
            data_file = json.load(data)
        data = data_file[website]
        print(data, data["email"],data["password"])
        messagebox.showinfo(title="already present", message=f'website :{website}\n email:{data["email"]}\npassword: {data["password"]}')
    except FileNotFoundError:
        messagebox.showinfo(title='not registered', message='Not inserted in the database')
    except KeyError:
        messagebox.showinfo(title='not registered' , message='Not inserted in the database')



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        },
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='incomplete data', message="some fields are empty")
    else:
        try:
            with open('data.json', 'r') as data:
                data_file = json.load(data)
                data_file.update(new_data)
        except FileNotFoundError:
            with open('data.json', 'w') as data:
                json.dump(new_data, data, indent=4)
        else:
            with open('data.json', 'w') as data:
                json.dump(data_file, data, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text='Website ')
website_label.grid(row=1, column=0)
website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(row=1, column=1)

search_button = Button(text='Search',width=15, command=search)
search_button.grid(row=1,column=2)

email_label = Label(text='Email')
email_label.grid(row=2, column=0)
email_entry = Entry(width=52)
email_entry.insert(0, 'csramdev@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text='Password ')
password_label.grid(row=3, column=0)
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()

