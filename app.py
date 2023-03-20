import sys
from Dbhelper import DBhelper
class Flipkart:
    def __init__(self):
        self.db=DBhelper()
        self.menu()
    def menu(self):
        user_self=input("""
        1.Enter 1 to register
        2.Enter 2 to login
        3.Anything else to leave
        """)
        if user_self=="1":
            self.register()
        elif user_self=="2":
            self.login()
        else:
            sys.exit(1000)
    def login_menu(self):
        input("""1.Enter 1 to see profile
        2.Enter 2 to edit profile
        3.Enter 3 to delete profile
        4.Enter 4 to logout
        """)
    def register(self):
        name=input("Enter the name")
        emai=input("Enter the email")
        password=input("Enter the password")
        response=self.db.register(name,emai,password)
        if response:
            print("Registration successful")
        else:
            print("Registration failed")
        self.menu()
    def login(self):
        emai=input("Enter email")
        password=input("Enter Password")
        data=self.db.search(emai,password)
        if len(data)==0:
            print("Incorrect email/password")
            self.login()
        else:
            print("Hello",data[0][1])
            self.login_menu()
obj=Flipkart()
