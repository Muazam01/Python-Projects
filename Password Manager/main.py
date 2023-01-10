




from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
COLOR="#FAF8F1"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    website = website_entry.get()
    email = email_entry.get()
    confirm=True
    while confirm:
        l = random.choices(letters, k=random.randint(3,9))
        s = random.choices(symbols, k=random.randint(3,7))
        n = random.choices(numbers, k=random.randint(1,6))

        p = l + s + n
        random.shuffle(p)
        j = ''.join(str(x) for x in p)
        password_entry.insert(END, string=f"{j}")
        password = password_entry.get()
        pyperclip.copy(password)
        ok = messagebox.askyesno(title="Confirmation", message="Do you want this to be your password")
        if ok:
            with open("data.txt", "a") as file:
                file.write(f"website:{website}\n email:{email}\nPassword:{password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)
                confirm=False
        else:
            password_entry.delete(0, END)

            l = random.choices(letters, k=random.randint(3,9))
            s = random.choices(symbols, k=random.randint(3,7))
            n = random.choices(numbers, k=random.randint(1,6))

            p = l + s + n
            random.shuffle(p)
            j = ''.join(str(x) for x in p)

            password_entry.insert(END, string=f"{j}")
            password=password_entry.get()
            pyperclip.copy(password)
            ok = messagebox.askyesno(title="Confirmation", message="Do you want this to be your password")
            password_entry.delete(0, END)
            continue



# ---------------------------- SAVE PASSWORD ------------------------------- #
def data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data={
        website:{
            "email":email,
            "Password":password,
        }
    }
    if len(website)==0:
      messagebox.showinfo(title="Oops", message="You have left website field empty ")

    if len(password)==0:
      messagebox.showinfo(title="Oops", message="You have left password field empty ")

    if len(email)==0:
      messagebox.showinfo(title="Oops", message="You have left email field empty ")

    elif len(website)!=0 and len(password)!=0 and len(email)!=0:
        ok=messagebox.askokcancel(title="Confirmation", message=f"The details for website: {website} entered are:\n email:{email}\n"
                                                         f"password: {password},press ok to continue")
        if ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except:
                with open("data.json","w") as file:
                    json.dump(new_data,file)
            else:
               data.update(new_data)
               with open("data.json", "w") as file:
                   json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)


#                    data = json.load(file)

def find_password():
    website=website_entry.get()
    password=password_entry.get()
    email=email_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            messagebox.showinfo(title=f"{website}",message=f"Email:{data[website]['email']}\nPassword:{data[website]['Password']}")
    except:
        messagebox.showinfo(title="Error", message="Data not found")



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password manager ")
window.config(padx=50,pady=50,bg=COLOR)

canvas=Canvas(height=200,width=200)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website")
website_label.grid(row=1, column=0)

website_entry=Entry(width=21)
website_entry.insert(END, string="")
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)


email_label=Label(text="Email/Username")
email_label.grid(row=2, column=0)

email_entry=Entry(width=35)
email_entry.insert(END, string="abc@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label=Label(text="Password")
password_label.grid(row=3, column=0)

password_entry=Entry(width=21)
password_entry.insert(END, string="")
password_entry.grid(row=3, column=1)

button_gen=Button(text="Generate Password", command=password_gen)
button_gen.grid(row=3,column=2)

button_add=Button(text="Add",width=36,command=data)
button_add.grid(row=4,column=1,columnspan=2)

button_find=Button(text="Search",command=find_password,width=10)
button_find.grid(row=1,column=2)

window.mainloop()







#Code without json
# from tkinter import *
# from tkinter import messagebox
# import random
# import pyperclip
#
# COLOR="#FAF8F1"
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# # ---------------------------- PASSWORD GENERATOR ------------------------------- #
# def password_gen():
#     website = website_entry.get()
#     email = email_entry.get()
#     confirm=True
#     while confirm:
#         l = random.choices(letters, k=random.randint(3,9))
#         s = random.choices(symbols, k=random.randint(3,7))
#         n = random.choices(numbers, k=random.randint(1,6))
#
#         p = l + s + n
#         random.shuffle(p)
#         j = ''.join(str(x) for x in p)
#         password_entry.insert(END, string=f"{j}")
#         password = password_entry.get()
#         pyperclip.copy(password)
#         ok = messagebox.askyesno(title="Confirmation", message="Do you want this to be your password")
#         if ok:
#             with open("data.txt", "a") as file:
#                 file.write(f"website:{website}\n email:{email}\nPassword:{password} \n")
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)
#                 email_entry.delete(0, END)
#                 confirm=False
#         else:
#             password_entry.delete(0, END)
#
#             l = random.choices(letters, k=random.randint(3,9))
#             s = random.choices(symbols, k=random.randint(3,7))
#             n = random.choices(numbers, k=random.randint(1,6))
#
#             p = l + s + n
#             random.shuffle(p)
#             j = ''.join(str(x) for x in p)
#
#             password_entry.insert(END, string=f"{j}")
#             password=password_entry.get()
#             pyperclip.copy(password)
#             ok = messagebox.askyesno(title="Confirmation", message="Do you want this to be your password")
#             password_entry.delete(0, END)
#             continue
#
#
#
# # ---------------------------- SAVE PASSWORD ------------------------------- #
# def data():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#
#     if len(website)==0:
#       messagebox.showinfo(title="Oops", message="You have left website field empty ")
#
#     if len(password)==0:
#       messagebox.showinfo(title="Oops", message="You have left password field empty ")
#
#     if len(email)==0:
#       messagebox.showinfo(title="Oops", message="You have left email field empty ")
#
#     elif len(website)!=0 and len(password)!=0 and len(email)!=0:
#         ok=messagebox.askokcancel(title="Confirmation", message=f"The details for website: {website} entered are:\n email:{email}\n"
#                                                          f"password: {password},press ok to continue")
#         if ok:
#             with open("data.txt", "a") as file:
#                 file.write(f"website:{website}\n email:{email}\nPassword:{password} \n")
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)
#                 email_entry.delete(0, END)
#
#
# # ---------------------------- UI SETUP ------------------------------- #
# window=Tk()
# window.title("Password manager ")
# window.config(padx=50,pady=50,bg=COLOR)
#
# canvas=Canvas(height=200,width=200)
# img=PhotoImage(file="logo.png")
# canvas.create_image(100,100,image=img)
# canvas.grid(row=0,column=1)
#
# website_label=Label(text="Website")
# website_label.grid(row=1, column=0)
#
# website_entry=Entry(width=35)
# website_entry.insert(END, string="")
# website_entry.focus()
# website_entry.grid(row=1, column=1, columnspan=2)
#
#
# email_label=Label(text="Email/Username")
# email_label.grid(row=2, column=0)
#
# email_entry=Entry(width=35)
# email_entry.insert(END, string="abc@gmail.com")
# email_entry.grid(row=2, column=1, columnspan=2)
#
# password_label=Label(text="Password")
# password_label.grid(row=3, column=0)
#
# password_entry=Entry(width=21)
# password_entry.insert(END, string="")
# password_entry.grid(row=3, column=1)
#
# button_gen=Button(text="Generate Password", command=password_gen)
# button_gen.grid(row=3,column=2)
#
# button_add=Button(text="Add",width=36,command=data)
# button_add.grid(row=4,column=1,columnspan=2)
#
#
# window.mainloop()
