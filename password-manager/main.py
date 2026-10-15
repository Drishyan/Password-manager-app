from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
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

    if len(website) == 0 or len(mail) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please dont leave any fields as empty")
    else:
        confirmation =messagebox.askokcancel(title=website,message=f"These are the details entered:\n Email: {mail}\n Password: {password}\n Is it ok to save?")
        if confirmation==True:
            with open("data.json", mode="a") as f:
                f.write(f"{website} | {mail} | {password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

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
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2,sticky="ew")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2,sticky="ew")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3,sticky="ew")

#buttons
generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add",width=36,command=add_data)
add_button.grid(column=1, row=4,columnspan=2, sticky="ew")
window.mainloop()