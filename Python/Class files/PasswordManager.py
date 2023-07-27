from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password
        self.passwords = {}
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def _encrypt(self, password):
        return self.fernet.encrypt(password.encode())

    def _decrypt(self, encrypted_password):
        return self.fernet.decrypt(encrypted_password).decode()

    def add_password(self, account, password):
        encrypted_password = self._encrypt(password)
        self.passwords[account] = encrypted_password

    def get_password(self, account):
        encrypted_password = self.passwords.get(account)
        if encrypted_password:
            return self._decrypt(encrypted_password)
        else:
            return "Account not found."

# Usage example
master_password = "my_secret_master_password"
password_manager = PasswordManager(master_password)
password_manager.add_password("example@gmail.com", "my_email_password")
password_manager.add_password("facebook", "my_facebook_password")

print("Email Password:", password_manager.get_password("example@gmail.com"))
print("Facebook Password:", password_manager.get_password("facebook"))