from tkinter import *
from tkinter import messagebox
# from database import db
# from client import client
from pprint import *
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    # NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.dates as mdates
import matplotlib.pyplot as plt


class mainUI(Frame):
    def logout(self):
        self.controller.user = 1
        # client(-1)
        self.controller.show_frame("LoginFrame")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.welcome_msg = StringVar(parent)
        Label(self, textvariable=self.welcome_msg).grid(row=1, column=0, sticky='NW')
        Button(self, text="Logout", command=self.logout).grid(row=1, column=1, sticky='NE')
        self.content = StringVar()
        Label(self, textvariable=self.content).grid(row=2, column=0, columnspan=2, sticky='NSEW')

    def refresh(self):
        # add graph to column three

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        plot = ""\
            # db.user_sales_timeline(self.controller.user.user_id)
        a.plot(plot[0], plot[1])
        f.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
        f.gca().xaxis.set_major_locator(mdates.DayLocator())
        f.autofmt_xdate()

        # bring up the canvas
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().grid(row=3, columnspan=2, sticky='NSEW')
        # navigation toolbar
        self.toolbar_frame = Frame(self).grid(row=4, columnspan=2, sticky='NSEW')
        toolbar_frame = Frame(self)
        toolbar_frame.grid(row=4, columnspan=2, sticky=S + E + W)
        toolbar = NavigationToolbar2TkAgg(canvas, toolbar_frame)
        # toolbar = NavigationToolbar2TkAgg(self, self.toolbar_frame)
        toolbar.update()
        canvas._tkcanvas.grid()
        self.welcome_msg.set("Hello %s!" % self.controller.user.username)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        if (self.controller.user.is_admin):
            self.content.set("You are an admin!")
        else:
            self.content.set("You are a user.")
        if (self.controller.user.is_admin):
            pie = ""\
                # "db.sales_pie_chart()
            # Plot
            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(111)
            a.pie(pie[1], autopct='%1.1f%%', shadow=True, labels=pie[0])
            a.axis('equal')

            # plt.show()
            canvas = FigureCanvasTkAgg(f, self)
            canvas.show()
            canvas.get_tk_widget().grid(row=5, columnspan=2, sticky='NSEW')


class RegisterFrame(Frame):
    def refresh(self):
        self.pass1.set('')
        self.pass2.set('')
        self.usEntry_reg.set('')

    def create_account(self):
        if (self.pass1.get() != self.pass2.get()):
            self.pass1.set('')
            self.pass2.set('')
            messagebox.showwarning("Password not match.", "Please verify your password again.")
        elif (self.pass1.get() == ''):
            messagebox.showwarning("Blank fields.", "Please do not leave any fields blank.")
        else:
            try:
                # db.register(self.usEntry_reg.get(), self.pass1.get())
                messagebox.showinfo("Account created.", "Please login using new credentials. :)")
            except:
                messagebox.showwarning("Error.", "Please try another username or contact a technician")
            self.controller.show_frame("LoginFrame")
            self.controller.frames['LoginFrame'].usEntry.set(self.usEntry_reg.get())

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.usEntry_reg = StringVar(parent)
        Label(self, text="Username").grid(row=0, column=0)  # create the username label
        Entry(self, textvariable=self.usEntry_reg).grid(row=0, column=1)  # position the username box

        self.pass1 = StringVar(parent)
        self.pass1.set('')
        self.pass2 = StringVar(parent)
        self.pass2.set('')

        Label(self, text="Password").grid(row=1, column=0)
        Entry(self, show="*", textvariable=self.pass1).grid(row=1, column=1)

        Label(self, text="re-enter Password").grid(row=2, column=0)
        Entry(self, show="*", textvariable=self.pass2).grid(row=2, column=1)

        Button(self, borderwidth=4, text="Register", width=10, pady=4, command=self.create_account).grid(row=3,
                                                                                                         column=1)
        Button(self, borderwidth=4, text="Return", width=10, pady=4,
               command=lambda: self.controller.show_frame("LoginFrame")).grid(row=4, column=1)


class LoginFrame(Frame):
    def refresh(self):
        self.pwEntry.set('')
        self.lbl_status.set("IDLE.")
        self.usEntry.set('')

    def check_password(self):
        self.user_id = "1"
        # db.getuserid(self.usEntry.get(), self.pwEntry.get())
        self.pwEntry.set('')
        if (self.user_id == -1):
            self.login_failure()
        else:
            self.usEntry.set('')
            self.login_success()

    def login_success(self):
        self.lbl_status.set("Login succeed.")
        self.controller.user = \
            1
        # client(self.user_id)
        self.controller.show_frame("mainUI")

    def login_failure(self):
        self.lbl_status.set("Authentication failed.")
        self.wrongpass += 1
        if (self.wrongpass >= 3):
            self.btn_login.configure(state=DISABLED)
            self.lbl_status.set("Denied access.")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.wrongpass = 0
        # self = Frame(root, padx=20, pady=20)
        self.grid(row=0, column=0)  # Create a frame and set it's position
        self.usEntry = StringVar()
        self.pwEntry = StringVar()
        Label(self, text="Username").grid(row=0, column=0)  # create the username label
        Entry(self, textvariable=self.usEntry).grid(row=0, column=1)

        Label(self, text="Password").grid(row=1, column=0)  # create the password label
        Entry(self, show="*", textvariable=self.pwEntry).grid(row=1, column=1)

        self.btn_login = Button(self, borderwidth=4, text="Login", width=10, pady=4, command=self.check_password)
        self.btn_login.grid(row=2, column=1, columnspan=2)
        self.lbl_status = StringVar(parent)
        self.lbl_status.set("waiting input...")
        Button(self, borderwidth=4, text="Register", width=10, pady=4,
               command=lambda: self.controller.show_frame("RegisterFrame")).grid(row=3, column=1, columnspan=2)

        Label(self, textvariable=self.lbl_status).grid(row=4, column=0, columnspan=2, sticky='W')


class SampleApp(Tk):
    def onFrameConfigure(self, canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def FrameWidth(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.canvas = Canvas(self, borderwidth=0, background="#ffffff")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.user =\
            1
        # client(-1)
        container = Frame(self.canvas)
        vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas_frame = self.canvas.create_window((4, 4), window=container, anchor="nw")

        container.bind("<Configure>", lambda event, canvas=self.canvas: self.onFrameConfigure(canvas))
        self.canvas.bind('<Configure>', self.FrameWidth)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginFrame, RegisterFrame, mainUI):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        try:
            frame.refresh()
        except AttributeError:
            pass
        # create canvas
        frame.tkraise()


class Login(Tk):
    def register(self):
        pass


def main():
    app = SampleApp()
    app.mainloop()


if __name__ == '__main__': main()