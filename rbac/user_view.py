from .menu import Menu


class UserView(Menu):

    def __init__(self, user_manager, role_manager, resource_manager,
                 logged_user):
        self.user_manager = user_manager
        self.role_manager = role_manager
        self.resource_manager = resource_manager
        self.__logged_user = logged_user

    def get_logged_user(self):
        return self.__logged_user

    def display(self):
        print(
            "\nHii!! you are logged in as " + self.__logged_user.get_username())
        print("press 1 to login as another user")
        print("press 2 to view roles")
        print("press 3 to access resources")
        print("press 4 to exit")
        return str(input())

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

    def view_logged_user_roles(self):
        roles = self.__logged_user.get_roles()
        print("Roles:")
        for role_name in roles:
            print('\nrole_name:: '+ role_name)
            role = self.role_manager.get_role(role_name)
            print('Action_items:')
            for action_item in role.get_all_resource_action():
                print(action_item)

    def check_for_access(self, resource_name, action_item):
        for role_name in self.__logged_user.get_roles():
            role=self.role_manager.get_role(role_name)
            if role.check_resource_action(resource_name, action_item):
                return True

    def get_resource_access(self):
        resources = self.resource_manager.get_all_resources()
        print("Resources:")
        for resource in resources:
            print(resources[resource].get_name())

        resource_name = str(input("Enter a resource_name::"))
        if self.resource_manager.resource_name_exist(resource_name) is False:
            print("Invalid Resource Name")
            return False
        resource_actions = resources[resource_name].get_action_types()
        print("Action items")
        for action_item in resource_actions:
            print(action_item)
        action_type = str(input("Enter an Action type::")).upper()
        if action_type not in resource_actions:
            print("Invalid action type")
            return False

        if self.check_for_access(resource_name, action_type):
            print("ACCESS GRANTED")
        else:
            print("ACCESS DENIED")

    def options(self, option):
        ctrl = 2
        if option == '1':
            success = self.login_input()
            if success:
                ctrl = 1 if self.__logged_user.is_admin() else 2

        elif option == '2':
            self.view_logged_user_roles()

        elif option == '3':
            self.get_resource_access()

        elif option == '4':
            exit(0)
        return ctrl
