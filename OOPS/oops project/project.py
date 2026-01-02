class chatbook:
    def __init__(self):
        # print("init called")
        self.username = ''
        self.password = ''
        self.loggedin = False
        # print("about to call method")
        self.menu()


    def menu(self):
        user_input = input("""Welcome to chatbook!!! How would you be like to proceed?
                          1. Press 1 to sign up
                          2. Press 2 to sign in
                          3. Press 3 to write a post
                          4. Press 4 to message a friends
                          Press any other key to exit \n =>""")

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.sighin()
        elif user_input == "3":
            self.mypost()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()


    def signup(self):
        email = input("Enter your email here => ")
        pwd = input("Setup your password here => ")
        self.username = email
        self.password = pwd
        print("You have signed up successfullyyyyyyyyyyyy")
        print("\n")
        self.menu()

    def sighin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1 in main menu")
        else:
            uname = input("Enter your username/email Here => ")
            pwd = input("Enter your password here => ")

            if self.username == uname and self.password == pwd:
                print("You have signed up successfullyyyyyyyyyyyy")
                self.loggedin = True
            else:
                print("Please enter your correct username and password")
        print("\n")
        self.menu()


    def mypost(self):
        if self.loggedin==True:
            txt = input("Enter your post here => ")
            print(f"Following content has been posted => {txt}")
        else:
            print("You need to signin first to post")
        
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin==True:
            frnd = input ("Whom to send this msg => ")
            txt = input("Enter your msg here => ")
            print(f"Your msg has been send to {frnd}")
        else:
            print("Please enter your correct username and password")
        print("\n")
        self.menu()    


# user1 = chatbook()
# check importsfiles.py