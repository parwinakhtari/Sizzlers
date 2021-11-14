from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import pickle
import numpy as np
import pandas as pd
import cv2
import webbrowser

global a

loaded_model = pickle.load(open("final_model.sav", "rb"))


regex = "^\w([\.-]?\w+)*@\w([\.-]?\w+)*(\.\w{2,3})+$"


def filedreq():
    if Fname.get() == "":
        print("First Name Field is Empty!!")
        user = "First Name Field is Empty!!"
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(
            x=12, y=460
        )

    elif Lname.get() == "":
        print("Last Name Field is Empty!!")
        user = "Last Name Field is Empty!!"
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(
            x=12, y=460
        )

    elif Email.get() == "":
        print("Email Field is Empty!!")
        user = "Email Field is Empty!!"
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(
            x=12, y=460
        )

    elif Phone.get() == "":
        print("Phone Field is Empty!!")
        user = "Phone Field is Empty!!"
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(
            x=12, y=460
        )

    elif entry_Address.compare(
        "end-1c", "==", "1.0"
    ):  # or else  if len(text.get("1.0", "end-1c")) == 0:
        print("Address Field is Empty!!")
        user = "Address Field is Empty!!"
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(
            x=12, y=460
        )
    else:
        pass


def callback(url):
    webbrowser.open_new_tab(url)


def browse():
    filename = filedialog.askopenfilename(
        filetypes=(("All Files", "*.*"), ("File", "*.py"))
    )
    path.config(text=filename)

    a = filename
    global file
    file = a
    # print(a)


def test():
    print("Testing...")
    # Test code will go here....

    images = []
    flat_data = []

    img = cv2.imread(file)
    img_resized = cv2.resize(img, (200, 200))
    img = np.mean(img_resized, axis=2)
    img1 = img.reshape(1, -1) / 255

    result = loaded_model.predict(img1)
    # print(result)
    if result[0] == 0:
        print("Normal")
        person = Fname.get()
        user = person + " Healthy brain"
        a = user
        Label(win, text=".", fg="red", bg="white", font=("Calibri 12 bold")).place(
            x=12, y=460
        )
        Label(win, text=user, fg="red", bg="white", font=("Calibri 12 bold")).place(
            x=12, y=460
        )
        MsgBox = tk.messagebox.showwarning(
            "success", "Healthy Brain!! \nYour brain's a masterpiece!!", icon="success",
        )

    elif result[0] == 1:
        print("pituitary_tumor")
        person = Fname.get()
        user = person + " You have pituitary Tumor!!!"
        a = user
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 12 bold")).place(
            x=12, y=600
        )
        link1 = Label(
            win, text="treatment", fg="blue", bg="yellow", font=("Calibri 12 bold")
        )

        MsgBox = tk.messagebox.showinfo(
            "information",
            "Tumor!! \nYou are at risk!! \nConsult a doctor for medical advice!!",
        )

        link1.pack(pady=50)
        link1.bind(
            "<Button-1>",
            lambda e: callback(
                "https://www.hopkinsmedicine.org/neurology_neurosurgery/centers_clinics/pituitary_center/pituitary-tumor/treatment"
            ),
        )

    elif result[0] == 2:
        print("meningioma_tumor")
        person = Fname.get()
        user = person + " You have  Meningioma Tumor!!!"
        a = user
        Label(win, text=". ", fg="red", bg="white", font=("Calibri 12 bold")).place(
            x=12, y=460
        )
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 12 bold")).place(
            x=12, y=460
        )
        link2 = Label(
            win, text="treatment", fg="blue", cursor="hand2", font=("Calibri 12 bold")
        ).place(x=12, y=480,)

        MsgBox = tk.messagebox.showinfo(
            "information",
            "Tumor!! \nYou ae at risk!! \nConsult a doctor for medical advice!!",
        )
        link2.pack()
        link2.bind(
            "<Button-1>",
            lambda e: callback(
                "https://www.hopkinsmedicine.org/health/treatment-tests-and-therapies/meningioma-treatment"
            ),
        )

    else:
        print("glioma_tumor")
        person = Fname.get()
        user = person + " You have  Glioma_tumor!!!"
        a = user
        Label(win, text=". ", fg="red", bg="white", font=("Calibri 12 bold")).place(
            x=12, y=460
        )
        Label(win, text=user, fg="blue", bg="yellow", font=("Calibri 12 bold")).place(
            x=12, y=460
        )
        link3 = Label(
            win, text="treatment", fg="blue", cursor="hand2", font=("Calibri 12 bold")
        ).place(x=12, y=480)

        MsgBox = tk.messagebox.showinfo(
            "information",
            "Tumor!! \nYou are at risk!! \nConsult a doctor for medical advice!!",
        )
        link3.pack()
        link3.bind(
            "<Button-1>",
            lambda e: callback(
                "https://www.hopkinsmedicine.org/brain-tumor/specialty-centers/glioma/treatment.html"
            ),
        )
        save(a)


def save(a):

    First = Fname.get()
    Last = Lname.get()
    email = Email.get()
    address = entry_Address.get(1.0, END)
    phone = Phone.get()
    gender = str(radio.get())
    save_name = First + ".txt"

    file = open(save_name, "a")
    file.write("\n\nFirst Name: " + First + "\n")
    file.write("Last Name: " + Last + "\n")
    file.write("Phone: " + phone + "\n")
    file.write("Email: " + email + "\n")
    file.write("Address " + address)
    file.write("Gender: " + gender + "\n")
    file.write("Report: " + a + "\n")
    file.close()
    report = First + "'s Health Detection data have been saved "
    Label(win, text=report, fg="black", bg="green", font=("Calibri 10 bold")).place(
        x=12, y=500
    )
    # print("Printing Data: ")
    # print(First,Last,phone,email,address,gender)


def reset():
    Fname.set("")
    Lname.set("")
    Email.set("")
    Phone.set("")
    entry_Address.delete(1.0, END)


win = Tk()

win.geometry("950x750")
win.configure(background="grey")
win.title("Tumor Detection")
win.iconbitmap("class.ico")

title = Label(
    win,
    text="Tumor Analysis",
    bg="grey",
    width="300",
    height="2",
    fg="White",
    font=("Calibri 20 bold italic underline"),
).pack()

my_img = ImageTk.PhotoImage(Image.open("image.png"))
my_label = Label(image=my_img).pack()
# my_label.place(x=340, y=0)

Fname = Label(
    win, fg="white", text="First name: ", bg="grey", font=("Verdana 12")
).place(x=12, y=100)


Lname = Label(
    win, fg="white", text="Last name: ", bg="grey", font=("Verdana 12")
).place(x=12, y=140)


email = Label(win, fg="white", text="Email ID: ", bg="grey", font=("Verdana 12")).place(
    x=12, y=180
)


Phone = Label(win, fg="white", text="Phone: ", bg="grey", font=("Verdana 12")).place(
    x=12, y=220
)


Address = Label(
    win, fg="white", text="Address: ", bg="grey", font=("Verdana 12")
).place(x=12, y=260)


Gender = Label(win, fg="white", text="Gender: ", bg="grey", font=("Verdana 12")).place(
    x=12, y=300
)
radio = StringVar()
Male = Radiobutton(
    win,
    text="Male",
    fg="white",
    bg="black",
    variable=radio,
    value="Male",
    indicatoron=0,
    font=("Verdana 12"),
).place(x=12, y=340)
Female = Radiobutton(
    win,
    text="Female",
    fg="white",
    bg="black",
    variable=radio,
    value="Female",
    indicatoron=0,
    font=("Verdana 12"),
).place(x=120, y=340)


Fname = StringVar()
Lname = StringVar()
Email = StringVar()
Phone = StringVar()
Address = StringVar()
Gender = StringVar()
Courses = StringVar()


entry_Fname = Entry(win, textvariable=Fname, width=30)
entry_Fname.place(x=120, y=100)
entry_Lname = Entry(win, textvariable=Lname, width=30)
entry_Lname.place(x=120, y=140)
entry_email = Entry(win, textvariable=Email, width=30)
entry_email.place(x=120, y=180)
entry_Phone = Entry(win, textvariable=Phone, width=30)
entry_Phone.place(x=120, y=220)
entry_Address = Text(win, height=2, width=23)
entry_Address.place(x=119, y=260)

path = Label(win, bg="grey", font=("Verdana 8"))
path.place(x=140, y=380)
upload = Button(
    win,
    text="Upload",
    width="12",
    height="1",
    activebackground="blue",
    bg="Pink",
    font=("Calibri 12 "),
    command=browse,
).place(x=20, y=380)

reset = Button(
    win,
    text="Reset",
    width="12",
    height="1",
    activebackground="red",
    bg="Pink",
    font=("Calibri 12 "),
    command=reset,
).place(x=20, y=420)
submit = Button(
    win,
    text="Test",
    width="12",
    height="1",
    activebackground="violet",
    bg="Pink",
    command=test,
    font=("Calibri 12 "),
).place(x=240, y=420)

win.mainloop()
