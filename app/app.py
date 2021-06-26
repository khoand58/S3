from tkinter import *
from functools import partial
import tkinter.messagebox

# from Tkinter import *
# from tkinter import Tk, BOTH
# from tkinter.ttk import Frame, Label, Style
# from tkinter import Tk, RIGHT, BOTH, RAISED
# from tkinter.ttk import Frame, Button, Style
font = "Arial Bold"


def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    if username.get() != "admin" and password.get() != "admin":
        tkinter.messagebox.showinfo(title="Login", message="login success", )

        usernameEntry.destroy()
        usernameLabel.destroy()
        loginButton.destroy()
        passwordEntry.destroy()
        passwordLabel.destroy()
        loginLabel.destroy()
        defaut()


    else:
        tkinter.messagebox.showerror(title="Login", message="login wrong username or password", )
    # Uploadfile.bind("<Button-1>", clica)

    # usernameEntry.unpack()
    return


# window
tkWindow = Tk()
tkWindow.geometry('800x600')
tkWindow['background'] = "#EEEEEE"
tkWindow.title('S3 Login Form - By Nguyễn Đình Khoa')

# def login():
#     # usernameEntry.pack()
#     usernameLabel.pack()
#     loginButton.pack()
#     # passwordEntry.pack()
#     passwordLabel.pack()
#     loginLabel.pack()



def defaut():
    tkWindow.title('S3 Server - By Nguyễn Đình Khoa')
    upload = Menu(tkWindow)
    file = Menu(upload, tearoff=0)
    folder = Menu(upload, tearoff=0)
    account = Menu(upload, tearoff=0)
    account.add_command(label="reset password", command=uploadfile)
    account.add_command(label="change password", command=uploadfile)
    account.add_command(label="view profile", command=uploadfile)
    # account.add_command(label="logout", command=login)
    file.add_command(label="Upfile", command=uploadfile)
    file.add_command(label="Downfile", command=uploadfile)
    folder.add_command(label="Upfolder", command=uploadfile)
    folder.add_command(label="Downfolder", command=uploadfile)
    upload.add_cascade(label="file", menu=file)
    upload.add_cascade(label="folder", menu=folder)
    upload.add_cascade(label="Account", menu=account)
    # upload.entryconfig(1, side=RIGHT)
    tkWindow.configure(menu=upload)


# username label and text entry box
# def login():
loginLabel = Label(tkWindow, text="Login", font=(font, 50), fg="#3300FF", pady=50)
loginLabel.pack()
usernameLabel = Label(tkWindow, text="User Name", font=(font, 14), pady=5)
usernameLabel.pack()
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username, width=20, font=(font, 14))
usernameEntry.pack()
passwordLabel = Label(tkWindow, text="Password", font=(font, 14), pady=5)
passwordLabel.pack()
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*', width=20, font=(font, 14))
passwordEntry.pack()
validateLogin = partial(validateLogin, username, password)
# login button
loginButton = Button(tkWindow, text="Login", command=validateLogin, font=(font, 14),
                     fg="#3300FF")
loginButton.pack()
# .grid(row=4, column=15, pady=10)

from tkinter.filedialog import askopenfilename


def uploadfile():
    # mode='r', filetypes=[('Python Files', '*.mp4')]
    filename = askopenfilename()
    # hide_me(self=loginButton)
    print(filename)


def hide_me(self, event):
    print('hide me')
    event.place_forget()


Uploadfile = Button(tkWindow, text="Uploadfile", command=uploadfile, font=(font, 14), width=10,
                    height=1, fg="#3300FF", bg='black')
Uploadfile1 = Button(tkWindow, text="Uploadfile", command=uploadfile, font=(font, 14), width=10,
                     height=1, fg="#3300FF", bg='black')

# .grid(row=6, column=15)
# Uploadfile.pack(side=TOP, pady=10)
# tkWindow.grid_rowconfigure(0, weight=1/)
# tkWindow.grid_columnconfigure(10, weight=1)
b = Button(tkWindow, text="Quit", command=tkWindow.destroy, font=(font, 14), fg="#FF3333")
b.pack(side="bottom", pady=20)
tkWindow.mainloop()
