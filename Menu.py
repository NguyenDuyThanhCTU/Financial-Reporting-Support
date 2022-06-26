from cProfile import label
from cgitb import text
from distutils.command.upload import upload
from tkinter import *
import tkinter as tk
from tkinter.messagebox import showwarning
from PIL import Image, ImageTk
import Controller.DAO as Conn
# import Menu
# import User_ID 
import tkinter.font as font

# def change_to_Home(self):
#     self.forget()
#     # them pack sau
#     go = HomePage()

# def change_to_C1(self):
#     self.forget()
#     go = C1Page()

# def change_to_C2(self):
#     self.forget()
#     go = C2Page()

def center_window_on_screen(root):

    window_width = 1000
    window_height = 600

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    screen = (f'{window_width}x{window_height}+{center_x}+{center_y}')
    return screen

class HomePage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Menu")
        self.iconbitmap('assets/img/logo/logo.ico')

        screen = center_window_on_screen(self)
        data = "{}".format(screen)
        self.geometry(data)

        self.configure(bg = "#ffffff")
        canvas = Canvas(
            self,
            bg = "#ffffff",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"assets/img/Menu/background.png")
        background = canvas.create_image(
            500, 300,
            image=background_img)

        def Home_clicked():
            return

        img_Home = PhotoImage(file = f"assets/img/Menu/Button_Home.png")
        button_home = Button(
            image = img_Home,
            borderwidth = 0,
            highlightthickness = 0,
            command = Home_clicked,
            relief = "flat")

        button_home.place(
            x = 0, y = 200,
            width = 200,
            height = 64)
        
        def C1_clicked():
            self.destroy()
            go = C1Page()

        img_C1 = PhotoImage(file = f"assets/img/Option/Button_C1.png")
        button_C1 = Button(
            image = img_C1,
            borderwidth = 0,
            highlightthickness = 0,
            command = C1_clicked,
            relief = "flat")

        button_C1.place(
            x = -3, y = 264,
            width = 207,
            height = 64)

        def C2_clicked():
            self.destroy()
            go = C2Page()

        img_C2 = PhotoImage(file = f"assets/img/Option/Button_C2.png")
        button_C2 = Button(
            image = img_C2,
            borderwidth = 0,
            highlightthickness = 0,
            command = C2_clicked,
            relief = "flat")

        button_C2.place(
            x = -3, y = 328,
            width = 207,
            height = 64)

        def Date_clicked():
            print("Button Clicked")

        img_Date = PhotoImage(file = f"assets/img/Menu/Button_Date.png")
        button_Date = Button(
            image = img_Date,
            borderwidth=0,
            highlightthickness=0,
            command=Date_clicked,
            relief = "flat"
        )

        button_Date.place(
            x = 939, y=538,
            width=40,
            height=40
        )
        img_ID = PhotoImage(file = f"assets/img/Menu/1.png")
        label_ID = Label(
            image=img_ID,
            highlightthickness=0,
        )

        label_ID.place(
            x=650, y= 89,
            width=170,
            height=41
        )
        

        self.resizable(False, False)
        self.mainloop()


class C1Page(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Menu")
        self.iconbitmap('assets/img/logo/logo.ico')

        screen = center_window_on_screen(self)
        data = "{}".format(screen)
        self.geometry(data)

        self.configure(bg = "#ffffff")
        canvas = Canvas(
            self,
            bg = "#ffffff",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"assets/img/Option/background.png")
        background = canvas.create_image(
            500, 302,
            image=background_img)

        def Home_clicked():
            self.destroy()
            go = HomePage()

        img0 = PhotoImage(file = f"assets/img/Option/Button_Home.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = Home_clicked,
            relief = "flat")

        b0.place(
            x = 0, y = 200,
            width = 200,
            height = 64)

        def C1_clicked():
            return

        img1 = PhotoImage(file = f"assets/img/C1/Button_C1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = C1_clicked,
            relief = "flat")

        b1.place(
            x = -3, y = 264,
            width = 207,
            height = 64)

        def C2_clicked():
            self.destroy()
            go = C2Page()

        img2 = PhotoImage(file = f"assets/img/Option/Button_C2.png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = C2_clicked,
            relief = "flat")

        b2.place(
            x = -3, y = 328,
            width = 207,
            height = 64)
        
        def Upload_clicked():
            self.destroy()
            go = Upload()

        img3 = PhotoImage(file = f"assets/img/C1/Button_Upload.png")
        b3 = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = Upload_clicked,
            relief = "flat")

        b3.place(
            x = 493, y =508,
            width = 221,
            height = 50)

        self.resizable(False, False)
        self.mainloop()


class C2Page(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Menu")
        self.iconbitmap('assets/img/logo/logo.ico')

        screen = center_window_on_screen(self)
        data = "{}".format(screen)
        self.geometry(data)

        self.configure(bg = "#ffffff")
        canvas = Canvas(
            self,
            bg = "#ffffff",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"assets/img/Option/background.png")
        background = canvas.create_image(
            500, 302,
            image=background_img)

        def Home_clicked():
            self.destroy()
            go = HomePage()

        img0 = PhotoImage(file = f"assets/img/Option/Button_Home.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = Home_clicked,
            relief = "flat")

        b0.place(
            x = 0, y = 200,
            width = 200,
            height = 64)

        def C1_clicked():
            self.destroy()
            go = C1Page()

        img1 = PhotoImage(file = f"assets/img/Option/Button_C1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = C1_clicked,
            relief = "flat")

        b1.place(
            x = -3, y = 264,
            width = 207,
            height = 64)

        def C2_clicked():
            return
        img2 = PhotoImage(file = f"assets/img/C2/Button_C2.png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = C2_clicked,
            relief = "flat")

        b2.place(
            x = -3, y = 328,
            width = 207,
            height = 64)

        self.resizable(False, False)
        self.mainloop()

class Upload(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Menu")
        self.iconbitmap('assets/img/logo/logo.ico')

        screen = center_window_on_screen(self)
        data = "{}".format(screen)
        self.geometry(data)

        canvas = Canvas(
            self,
            bg = "#ffffff",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"assets/img/Upload/background.png")
        background = canvas.create_image(
            500, 302,
            image=background_img)
        def btn_clicked():
            print("Button Clicked")
        img0 = PhotoImage(file = f"assets/img/Upload/Button_Select.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        b0.place(
            x = 181, y = 504,
            width = 159,
            height = 50)

        img1 = PhotoImage(file = f"assets/img/Upload/Button_Continue.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        b1.place(
            x = 763, y = 504,
            width = 159,
            height = 50)

        self.resizable(False, False)
        self.mainloop()

start = Upload()