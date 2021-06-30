from tkinter import *
from functools import partial
import tkinter.messagebox

from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.ttk as ttk


class Application(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.initialize_user_interface()

    def initialize_user_interface(self):
        # Configure the root object for the Application
        self.root.title("Application")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(background="green")

        # Define the different GUI widgets
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_entry = tk.Entry(self.root)
        self.name_label.grid(row=0, column=0, sticky=tk.W)
        self.name_entry.grid(row=0, column=1)

        self.idnumber_label = tk.Label(self.root, text="ID")
        self.idnumber_entry = tk.Entry(self.root)
        self.idnumber_label.grid(row=1, column=0, sticky=tk.W)
        self.idnumber_entry.grid(row=1, column=1)

        self.submit_button = tk.Button(self.root, text="Insert", command=self.insert_data)
        self.submit_button.grid(row=2, column=1, sticky=tk.W)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=0, column=3)

        # Set the treeview
        self.tree = ttk.Treeview(self.root, columns=('Name', 'ID'))

        # Set the heading (Attribute Names)
        self.tree.heading('#0', text='Item')
        self.tree.heading('#1', text='Name')
        self.tree.heading('#2', text='ID')

        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)

        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree

        self.id = 0
        self.iid = 0

    def insert_data(self):
        self.treeview.insert('', 'end', iid=self.iid, text="Item_" + str(self.id),
                             values=("Name: " + self.name_entry.get(),
                                     self.idnumber_entry.get()))
        self.iid = self.iid + 1
        self.id = self.id + 1


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
        # app = Application(tkWindow)


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

# create all of the main containers
top_frame = Frame(tkWindow, bg='cyan', width=450, height=50, pady=3)
center = Frame(tkWindow, bg='gray2', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(tkWindow, bg='white', width=450, height=45, pady=3)
btm_frame2 = Frame(tkWindow, bg='lavender', width=450, height=60, pady=3)


# def login():
#     # usernameEntry.pack()
#     usernameLabel.pack()
#     loginButton.pack()
#     # passwordEntry.pack()
#     passwordLabel.pack()
#     loginLabel.pack()


def defaut():
    # layout all of the main containers
    tkWindow.grid_rowconfigure(1, weight=1)
    tkWindow.grid_columnconfigure(0, weight=1)
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
    folder.add_command(label="Upfolder", command=uploadfolder)
    folder.add_command(label="Downfolder", command=uploadfolder)
    upload.add_cascade(label="file", menu=file)
    upload.add_cascade(label="folder", menu=folder)
    upload.add_cascade(label="Account", menu=account)

    # ===================================================
    # and the sidebar is divided into a top and bottom section.
    pw = ttk.PanedWindow(orient="horizontal")
    sidebar = ttk.PanedWindow(pw, orient="vertical")
    main = tk.Frame(pw, width=400, height=400, background="black")
    sidebar_top = tk.Frame(sidebar, width=200, height=200, background="gray")
    sidebar_bottom = tk.Frame(sidebar, width=200, height=200, background="white")



    # layout the widgets in the top frame
    model_label.grid(row=0, columnspan=3)
    width_label.grid(row=1, column=0)
    length_label.grid(row=1, column=2)
    entry_W.grid(row=1, column=1)
    entry_L.grid(row=1, column=3)

    # create the center widgets
    center.grid_rowconfigure(0, weight=1)
    center.grid_columnconfigure(1, weight=1)
    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")
    btm_frame.grid(row=3, sticky="ew")
    btm_frame2.grid(row=4, sticky="ew")

    ctr_left.grid(row=0, column=0, sticky="ns")
    ctr_mid.grid(row=0, column=1, sticky="nsew")
    # ctr_right.grid(row=0, column=2, sticky="ns")
    # tv = Frame(tkWindow)
    # add the paned window to the root
    pw.grid()
    # pw.pack(fill="both", expand=True)

    # add the sidebar and main area to the main paned window
    pw.add(sidebar)
    pw.add(main)

    # add the top and bottom to the sidebar
    sidebar.add(sidebar_top)
    sidebar.add(sidebar_bottom)

    # ====================================================
    # tv = ttk.Treeview(ctr_left, column=0, show='headings', height=10)
    # # ctr_left.grid_rowconfigure(1, weight=1)
    # # ctr_left.grid_columnconfigure(0, weight=1)
    # tv.grid()
    # tv.heading(0, text="Bucket", )
    # # tv.heading(2, text="Size")
    #
    # # tv.pack(side="left")/
    # # ctr_mid.heading(1, text="Bucket")
    # tv1 = ttk.Treeview(ctr_mid, columns=(1, 2, 3, 4), show='headings', height=10)
    # # ctr_mid.grid_rowconfigure(1, weight=1)
    # # ctr_mid.grid_columnconfigure(0, weight=1)
    # tv1.grid()
    # # Separator object
    # separator = ttk.Separator(ctr_mid, orient='vertical')  # horizontal
    # separator.place(relx=0, rely=0.47, relwidth=1, relheight=1)
    #
    # # tv1.pack(side="top")
    # tv1.heading(1, text="File")
    # tv1.heading(2, text="Size")
    # tv1.heading(3, text="Type")
    # tv1.heading(4, text="Last Modified")
    # b.grid()
    # =====================================================================

    # # Show buttons
    # back = offset - limit  # This value is used by Previous button
    # next = offset + limit  # This value is used by Next button
    # b1 = tk.Button(tkWindow, text='< Prev', command=lambda: my_display(back))
    # b1.grid(row=2, column=2, sticky='E')
    # b2 = tk.Button(tkWindow, text='Next >', command=lambda: my_display(next))
    # b2.grid(row=2, column=3)
    # upload.entryconfig(1, side=RIGHT)
    # table = Table(tkWindow)
    tkWindow.configure(menu=upload)


# username label and text entry box
# def login():
# loginLabel = Label(top_frame, text='Login')
# usernameLabel = Label(top_frame, text='User Name')
# width_label = Label(top_frame, text='Width:')
# passwordLabel = Label(top_frame, text='Password')
# usernameEntry = Entry(top_frame, background="pink")
# passwordEntry = Entry(top_frame, background="orange")

loginLabel = Label(tkWindow, text="Login", font=(font, 50), fg="#3300FF", pady=10)
loginLabel.grid(row=0, column=2, pady=10)
usernameLabel = Label(tkWindow, text="User Name", font=(font, 14), pady=10)
usernameLabel.grid(row=1, column=1)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username, font=(font, 14))
usernameEntry.grid(row=1, column=2)
passwordLabel = Label(tkWindow, text="Password", font=(font, 14), pady=10)
passwordLabel.grid(row=2, column=1)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*', font=(font, 14))
passwordEntry.grid(row=2, column=2)
validateLogin = partial(validateLogin, username, password)
# login button
loginButton = Button(tkWindow, text="Login", command=validateLogin, font=(font, 14),
                     fg="#3300FF", pady=10)
loginButton.grid(row=3, column=2, pady=10)
# .grid(row=4, column=15, pady=10)

from tkinter.filedialog import askopenfilename, askdirectory, asksaveasfile


def uploadfile():
    # mode='r', filetypes=[('Python Files', '*.mp4')]
    filename = askopenfilename()
    # hide_me(self=loginButton)
    print(filename)


def uploadfolder():
    # mode='r', filetypes=[('Python Files', '*.mp4')]
    filename = askdirectory()
    # hide_me(self=loginButton)
    print(filename)


def hide_me(self, event):
    print('hide me')
    event.place_forget()


# Uploadfile = Button(tkWindow, text="Uploadfile", command=uploadfile, font=(font, 14), width=10,
#                     height=1, fg="#3300FF", bg='black')
# Uploadfile1 = Button(tkWindow, text="Uploadfile", command=uploadfile, font=(font, 14), width=10,
#                      height=1, fg="#3300FF", bg='black')

# def table():
#     e = Entry(root, width=20, fg='blue', font=('Arial', 16, 'bold')

# return

# .grid(row=6, column=15)
# Uploadfile.pack(side=TOP, pady=10)
# tkWindow.grid_rowconfigure(0, weight=1/)
# tkWindow.grid_columnconfigure(10, weight=1)


# create the widgets for the top frame
pw = ttk.PanedWindow(orient="horizontal")
sidebar = ttk.PanedWindow(pw, orient="vertical")
model_label = Label(top_frame, text='Model Dimensions')
width_label = Label(top_frame, text='Width:')
length_label = Label(top_frame, text='Length:')
entry_W = Entry(top_frame, background="pink")
entry_L = Entry(top_frame, background="orange")

ctr_left = Frame(center, bg='blue', width=200, height=190)
ctr_mid = Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3)
# ctr_right = Frame(center, bg='green', width=100, height=190, padx=3, pady=3)

b = Button(tkWindow, text="Quit", command=tkWindow.destroy, font=(font, 14), fg="#FF3333")
# b.grid(column=2)
tkWindow.mainloop()
