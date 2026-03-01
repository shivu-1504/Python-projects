print("====== Simple Password Manager ======")

FILE_NAME = "passwords.txt"


class PasswordManager:
    @staticmethod
    def encrypt(password):
        encrypted = ""
        for char in password:
            encrypted += chr(ord(char) + 3)
        return encrypted

    @staticmethod
    def decrypt(encrypted_password):
        decrypted = ""
        for char in encrypted_password:
            decrypted += chr(ord(char) - 3)
        return decrypted

    @staticmethod
    def add_password(website, password):
        try:
            encrypted_password = PasswordManager.encrypt(password)

            with open(FILE_NAME, "a") as file:
                file.write(f"{website},{encrypted_password}\n")

            print("Password saved successfully.")

        except Exception as e:
            print("Error saving password:", e)

    @staticmethod
    def retrieve_password(search_website):
        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    website, encrypted_password = line.strip().split(",")

                    if website.lower() == search_website.lower():
                        decrypted = PasswordManager.decrypt(encrypted_password)
                        print(f"Password for {website}: {decrypted}")
                        return

            print("Website not found in records.")

        except FileNotFoundError:
            print("Password file does not exist yet.")
        except Exception as e:
            print("Error retrieving password:", e)


if __name__ == "__main__":

    PasswordManager.add_password("gmail.com", "mySecure123")
    PasswordManager.add_password("facebook.com", "pass@456")

    PasswordManager.retrieve_password("gmail.com")
    PasswordManager.retrieve_password("instagram.com") 