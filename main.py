from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen():
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's''t', 'u',
              'v']
    symbol = ['!', '@', '$', '(', '&']
    number = ['1', '2', '3', '7', '8', '0']
    passletter = [random.choice(letter) for _ in range(8)]
    passsymbole = [random.choice(symbol) for _ in range(4)]
    passnumber = [random.choice(number) for _ in range(5)]
    pas = []
    rpass = []
    pas = passnumber + passletter + passsymbole
    random.shuffle(pas)
    password = "".join(pas)
    e3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    webname = e1.get()
    email = e2.get()
    password = e3.get()
    data = {
        webname: {
            "email": email,
            "password": password
        }
    }
    if len(webname) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="you Donkey!! \nleft some information empty")
    else:
        try:
            with open(file="data.json", mode="r") as f1:
                datas= json.load(f1)

        except FileNotFoundError:
            with open(file="data.json", mode="w") as f1:
                json.dump(data, f1)
        else:

            datas.update(data)
            with open("data.json","w") as f1:
                json.dump(datas,f1)
            e1.delete(0, END)
            e3.delete(0, END)
            e1.focus()

def search():
    user = e1.get().lower()
    try:
        with open("data.json","r") as f1:
            data = json.load(f1)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR",message="file not found")
    else:
        if user in data:
            email = data[user]["email"]
            password = data[user]["password"]
            messagebox.showinfo(title=user,message=f'Email:{email} \n password:{password}')
        else:
            messagebox.showinfo(title="report",message=f"there is no details about {user}")




# ---------------------------- UI SETUP ------------------------------- #
w1 = Tk()
w1.title("password generator")
can = Canvas(height=200, width=200)
w1.config(pady=50, padx=50)
logo = PhotoImage(file="logo.png")
can.create_image(100, 100, image=logo)
can.grid(column=1, row=0)

l1 = Label(text="Website")
l1.grid(row=1)
e1 = Entry(width=32)
e1.focus()
e1.grid(row=1, column=1, columnspan=1)

l2 = Label(text="Email/Username")
e2 = Entry(width=51)

e2.insert(END, "shabari.0019@gmail.com")
e2.grid(row=2, column=1, columnspan=2)
l2.grid(row=2)

l3 = Label(text="Password")
l3.grid(row=3)
e3 = Entry(width=32)
e3.grid(row=3, column=1)

b2 = Button(text="Generate password", command=gen)
b2.grid(row=3, column=2)

b1 = Button(text="Add", width=44, command=save)
b1.grid(row=4, column=1, columnspan=2)

b3 = Button(text="Search",width=13,command=search)
b3.grid(row=1,column=2)
w1.mainloop()
