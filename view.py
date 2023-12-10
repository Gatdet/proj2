from tkinter import *
import re
from tkinter import scrolledtext

class View(Tk): #Inherits from tk class
    def __init__(self) -> None:
        super().__init__()
        self.title("Contacts")
        self.geometry("900x500")
        self.resizable(False, False)
        self.config(bg="#D2B48C")

        Label(self, text="First Name", font=("arial",12)).place(x=20, y=10)
        Label(self, text="Last Name", font=("arial",12)).place(x=20, y=110)
        Label(self, text="Email", font=("arial",12)).place(x=20, y=210)
        Label(self, text="Phone", font=("arial",12)).place(x=20, y=310)
        Label(self, font=("arial", 20), text="CONTACTS").place(x=370, y=10)

        self.fname = Entry(self, font=("arial", 15), width=20)
        self.fname.place(x=20, y=40)
        
        self.lname = Entry(self, font=("arial", 15), width=20)
        self.lname.place(x=20, y= 140)

        self.email = Entry(self, font=("arial", 15), width=20)
        self.email.place(x=20, y= 240)
        
        self.phone = Entry(self, font=("arial", 15), width=20)
        self.phone.place(x=20, y= 340)

        self.submit = Button(self, font=("arial",15),text="Submit" )
        self.submit.place(x=80, y=400)

        self.frame = Frame(self)
        self.frame.place(relwidth=0.3, relheight=0.87, relx=0.66, rely=0.05)

        self.contacts = scrolledtext.ScrolledText(self.frame, font= ("Arial", 12), wrap = NONE)
        self.contacts.configure(state="normal")
        self.contacts.place(relwidth=1.0, relheight=1.0)


        with open("data.csv", 'r', newline="") as csvfile:
            
            
            for i in csvfile.readlines():
                
                self.contacts.insert("1.0",i)
        csvfile.close()
    def main(self):
        self.mainloop()


