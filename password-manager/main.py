from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    char_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letter_list + char_list + number_list

    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():

    website = website_entry.get()
    mail = email_entry.get()
    password = password_entry.get()
    data_dict = {
        website: {"email": mail,"password": password}
    }

    if len(website) == 0 or len(mail) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please dont leave any fields as empty")
    else:
        confirmation =messagebox.askokcancel(title=website,message=f"These are the details entered:\n Email: {mail}\n Password: {password}\n Is it ok to save?")
        if confirmation:
            try:
                with open("data.json", mode="r") as data:
                    new_data = json.load(data)

            except FileNotFoundError:
                with open("data.json", mode="w") as data:
                    json.dump(data_dict, data, indent=4)
            else:
                new_data.update(data_dict)
                with open("data.json", mode="w") as data:
                    json.dump(new_data, data, indent=4)

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

## ---------------------------- Find Password ------------------------------- #

def search_password():
    search_website = website_entry.get()
    try:
        with open("data.json", mode="r") as data:
            data_file = json.load(data)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="First create a data to search for it")
    else:
        if search_website in data_file:
            email = data_file[search_website]["email"]
            password = data_file[search_website]["password"]
            messagebox.showinfo(title=search_website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showerror(title="Error", message="No data found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1, row=0)

#texts
website_txt = Label(text="Website:")
website_txt.grid(column=0, row=1)

email_txt = Label(text="Email/Username:")
email_txt.grid(column=0, row=2)

password_txt = Label(text="Password:")
password_txt.grid(column=0, row=3)

#text box
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1,sticky="ew")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2,sticky="ew")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3,sticky="ew")

#buttons
generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2, row=3)

search_button = Button(text="Search",width=13,command=search_password)
search_button.grid(column=2, row=1,sticky="ew")

add_button = Button(text="Add",width=36,command=add_data)
add_button.grid(column=1, row=4,columnspan=2, sticky="ew")
window.mainloop()
