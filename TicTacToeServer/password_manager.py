import bcrypt

class PasswordManager:
    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed

    @staticmethod
    def check_password(password, hashed):
        return bcrypt.checkpw(password.encode("utf-8"), hashed)
