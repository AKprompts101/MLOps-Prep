class chatbook:
    def __init__(self):
        print("init called")
        self.username = ''
        self.password = ''
        self.loggedin = False
        print("about to call method")
        self.menu()


    def menu(self):
        user_input = input("""Welcome to chatbook!!! How would you be like to proceed?
                          1. Press 1 to sign up
                          2. Press 2 to sign in
                          3. Press 3 to write a post
                          4. Press 4 to message a friends
                          Press any other key to exit""")

        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

obj = chatbook()