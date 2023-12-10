from view import View
import re, csv
from tkinter import messagebox


class Model:
    def __init__(self) -> None:
        """
        initializing 
        """
        self.view = View()
        
        self.info = []
        self.view.submit.config(command=self.submit)
        self.found_contacts = ""
        
    def valid_num(self) -> bool:

        """
        validates the number and checks to see if its long enough"""

        self.yesdashes = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
        self.nodashes = re.compile(r"\d\d\d\d\d\d\d\d\d\d")
        try:
            if len(self.view.phone.get())==10: #if len is 10
                self.Mobile = self.nodashes.search(self.view.phone.get()) #
                return True 
            elif len(self.view.phone.get())==12:
                self.Mobile = self.yesdashes.search(self.view.phone.get())
                return True
            
            else:
                messagebox.showerror("Error", "Check phone number")
                return False 



        except AttributeError: # when we get an error return a message box
            messagebox.showerror("Error", "Check phone number") 
            return False
    
    def valid_email(self) -> bool:
        """
        validates the email to see if it fits format
        """
        if self.view.email.get()=="":
            return True
        self.view.email.get().endswith(".")
        email_format = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b' #format
        if(re.fullmatch(email_format, self.view.email.get())): #if it fits
            return True
        else: #if it doesnt
            messagebox.showerror("Error", "Check email") 
            return False
    def valid_name(self) -> bool:
        """
        checks to see if the name is empty"""
        if len(self.view.fname.get())==0:
            messagebox.showerror("Error", "First name empty") 
            return False

        if len(self.view.lname.get())==0:
            messagebox.showerror("Error", "Last name empty") 
            return False
        return True



    def submit(self) -> bool:
        """
        when the button is clicked, it will add the info to the file and clear the entry boxes if the
        info is valid"""
        with open("data.csv", 'a', newline="") as csvfile:

            if self.valid_name() and self.valid_num()==True and self.valid_email():
                self.info.append([self.view.fname.get(), self.view.lname.get(), self.view.email.get(), self.Mobile.group()])                
                csvwriter = csv.writer(csvfile, delimiter="," )
                csvwriter.writerow(self.info[0])
                
                self.view.email.delete(0, "end")
                self.view.fname.delete(0, "end")
                self.view.lname.delete(0, "end")
                self.view.phone.delete(0, "end")
            
            self.info=[]
        csvfile.close()

    def main(self) -> None:
        """
        starts the gui"""
        self.view.main()
        