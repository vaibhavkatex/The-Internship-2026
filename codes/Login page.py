class LoginPage:

    def __init__(self):
        self.database = {}

    def Create_account(self):
        username = input("Enter Username : ")
        password = input("Enter Password : ")

        if username in self.database:
            print("Username already exists!")
        else:
            self.database[username] = password
            print("Account Created Successfully!")

    def Login(self):
        username = input("Enter Username : ")
        password = input("Enter Password : ")

        if username in self.database:
            if self.database[username] == password:
                print("Login Successful")
            else:
                print("Wrong Password")
        else:
            print("Username not found")

        def view_database():
            


obj = LoginPage()

while True:

    print("\n1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        obj.Create_account()

    elif choice == "2":
        obj.Login()

    elif choice == "3":
        print("Thank You")
        break

    else:
        print("Please Enter Valid Choice")