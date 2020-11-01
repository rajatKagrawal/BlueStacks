from .menu import Menu


class MainView(Menu):

    def __init__(self, user_manager, role_manager, resource_manager,
                 logged_user):
        self.user_manager = user_manager
        self.role_manager = role_manager
        self.resource_manager = resource_manager
        self.__logged_user = logged_user

    def display(self):
        print("\nWelcome to RBAC\n")
        print("Press 1 to login")
        print("Press 2 to exit")
        return str(input())

    def get_logged_user(self):
        return self.__logged_user

    def login_input(self):
        username = str(input("\nEnter username:: "))
        password = str(input("Enter password:: "))
        return self.login(username, password)

    def login(self, username, password):
        success, message = self.user_manager.verify_username_password(
            username=username,
            password=password)
        if success:
            self.__logged_user = self.user_manager.get_user(username)
        print(message)
        return success

    def options(self, option):
        ctrl = 0
        if option == '1':
            success = self.login_input()
            if success:
                ctrl = 1 if self.__logged_user.is_admin() else 2
        elif option == '2':
            print("bye!!\n")
            exit(0)
        else:
            print("wrong input")
        return ctrl
