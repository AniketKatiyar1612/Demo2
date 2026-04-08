def login(self):
        print("\n--- Login ---")
        username = input("Username: ")
        password = input("Password: ")
        if username == "admin" and password == "password":
            print("Login successful!")
            return True
        else:
            print("Invalid credentials. Please try again.")
            return False   