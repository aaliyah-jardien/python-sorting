from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login Details")
root.geometry("500x500")
root.config(bg="#bf0000")

import time
start = time.time()

input_label1 = Label(root, text="Please enter username")
input_label1.place(x=50, y=40)

user_entry = Entry(root)
user_entry.place(x=250, y=40)

input_label2 = Label(root, text="Please enter password")
input_label2.place(x=50, y=90)

pass_entry = Entry(root, show="*")
pass_entry.place(x=250, y=90)

def signin():
    username = ["Zaid", "Aaliyah", "Lihle", "Thabo", "Zoe"]
    passwords = ["0000", "5555", "7700", "1234", "8697"]
    #x = input("Enter username")
    #y = input("Enter password")

    found = False

    for x1 in range(len(username)):
        if user_entry.get() == username[x1] and pass_entry.get() == passwords[x1]:
            found = True

    if found==True:
        messagebox.showinfo("STATUS", "Access granted")
        root.destroy()
        import nextscreen

    else:
        messagebox.showinfo("ERROR INFO", "Access denied")

# print(len(usernames))


log_btn = Button(root, text="Login", borderwidth="10", command=signin)
log_btn.place(x=50, y=180)


def clear():
    user_entry.delete(0, END)
    pass_entry.delete(0, END)


clear_btn = Button(root, text="Clear", borderwidth="10", command=clear)
clear_btn.place(x=180, y=180)

exit_btn = Button(root, text="Exit", borderwidth="10", command=exit)
exit_btn.place(x=320, y=180)

end = time.time()
print(end-start)

root.mainloop()
