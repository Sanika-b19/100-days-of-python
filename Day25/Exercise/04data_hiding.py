# Exercise 4: Data Hiding

class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Private attribute for sensitive data

    def check_password(self, password):
        return self.__password == password

    def update_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Incorrect old password.")

account = UserAccount("user1", "securepassword")
print(account.check_password("securepassword"))

# Attempt to change password
account.update_password("securepassword", "newsecurepassword")
