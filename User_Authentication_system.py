import hashlib

print("====== User Authentication System ======")

FILE_NAME = "users.txt"

class AuthSystem:

    def __init__(self):
        self.users = self.load_users()

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def load_users(self):
        users = {}
        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    username, hashed_password = line.strip().split(",")
                    users[username] = hashed_password
        except FileNotFoundError:
            pass
        except Exception as e:
            print("Error loading users:", e)

        return users

    def save_user(self, username, hashed_password):
        try:
            with open(FILE_NAME, "a") as file:
                file.write(f"{username},{hashed_password}\n")
        except Exception as e:
            print("Error saving user:", e)

    @staticmethod
    def validate_password(password):
        if len(password) < 6:
            return False
        return True

    def register(self):
        username = input("Enter username: ")

        if username in self.users:
            print("Username already exists.")
            return

        password = input("Enter password: ")

        if not self.validate_password(password):
            print("Password must be at least 6 characters.")
            return

        hashed_password = self.hash_password(password)

        self.users[username] = hashed_password
        self.save_user(username, hashed_password)

        print("Registration successful.")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        hashed_password = self.hash_password(password)

        if username in self.users and self.users[username] == hashed_password:
            print("Login successful!")
        else:
            print("Invalid username or password.")


if __name__ == "__main__":

    auth = AuthSystem()

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            auth.register()
        elif choice == "2":
            auth.login()
        elif choice == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid choice.")