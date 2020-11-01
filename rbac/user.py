

class User:
    def __init__(self, username, password, is_admin):
        self.__username = username
        self.__password = hash(password)
        self.__is_admin = is_admin
        self.__roles = set()

    def check_password(self, password):
        return self.__password == hash(password)

    def add_role(self, role_name):
        self.__roles.add(role_name)

    def remove_role(self, role_name):
        self.__roles.discard(role_name)

    def get_roles(self):
        return self.__roles

    def get_username(self):
        return self.__username

    def is_admin(self):
        return self.__is_admin


class UsersManager:
    def __init__(self):
        self.__users = {}

    def username_exists(self, username):
        return username in self.__users

    def __add_user(self, user):
        self.__users[user.get_username()] = user

    def register_user(self, username, password, is_admin=False):
        if self.username_exists(username):
            return False, "username already exist"
        user = User(username, password, is_admin)
        self.__add_user(user)
        return True, "user registered sucessfully"

    def get_user(self, username):
        return self.__users.get(username, None)

    def get_users(self):
        return self.__users

    def verify_username_password(self, username, password):
        if self.username_exists(username):
            user = self.get_user(username)
            return (True, "Login Successful") if user.check_password(
                password) else (False, "Incorrect Password")

        return False, "UserName not found"
