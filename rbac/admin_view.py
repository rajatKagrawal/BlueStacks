from .menu import Menu
from .resource import ActionType


class AdminView(Menu):

    def __init__(self, user_manager, role_manager, resource_manager,
                 logged_user):
        self.user_manager = user_manager
        self.role_manager = role_manager
        self.resource_manager = resource_manager
        self.__logged_user = logged_user

    def get_logged_user(self):
        return self.__logged_user

    def user_create_input(self):
        try:
            username = str(input("\nEnter username:: ")).lower()
            password = str(input("Enter password:: "))
            is_admin = str(input(
                "Enter is_admin:: (true if yes else enter anything)::"
            )).lower() in ["true"]
            return self.user_create(
                username=username,
                password=password,
                is_admin=is_admin
            )
        except Exception as e:
            print('\ninvalid input')
            return False

    def user_create(self, username, password, is_admin):
        success, message = self.user_manager.register_user(
            username=username,
            password=password,
            is_admin=is_admin
        )
        print(message)
        return success

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

    def print_users(self):
        users = self.user_manager.get_users()
        for username in users:
            print("\nusername:: {}\nis_admin:: {}".format(
                users[username].get_username(), users[username].is_admin()))

    def role_create_input(self):
        try:
            role_name = str(input("Enter role name:: "))
            success, message = self.role_manager.register_role(role_name)
            print(message)
            return success
        except Exception as e:
            print("Invalid input")
            return False

    def dispaly_role(self):
        roles = self.role_manager.get_all_roles()
        for role in roles:
            print("\n role_name:: " + str(roles[role].get_name()))
            print("resource_action ")
            for item in roles[role].get_all_resource_action():
                print(item)

    def resource_create_input(self):
        try:
            resource_name = str(input("Enter resource name::"))
            action_types = set()
            for action in ActionType:
                is_allowed = str(input(
                    str(action) + ":: yes or no ::")).lower() == 'yes'
                if is_allowed:
                    action_types.add(action.name)
            self.resource_manager.register_resource(resource_name, action_types)
            return True
        except Exception as e:
            print("Invalid Input")
            return False

    def display_resources(self):
        resources = self.resource_manager.get_all_resources()
        for resource in resources:
            print("resource_name:: " + resources[resource].get_name())
            print("allowed action_types")
            for action_type in resources[resource].get_action_types():
                print(action_type)

    def add_user_role(self):
        users = self.user_manager.get_users()
        print("username")
        for user in users:
            print(users[user].get_username())
        username = str(input("enter a username:: "))
        if self.user_manager.username_exists(username) is False:
            print("Invalid Username")
            return False
        user = users.get(username)
        user_roles = user.get_roles()
        roles = set(self.role_manager.get_all_roles().keys())
        available_roles = roles - user_roles

        print("Assign roles")
        for role in available_roles:
            print(role)

        role_name = str(input("enter a role_name:: "))
        if self.role_manager.role_name_exist(role_name) is False:
            print("Invalid Role Name")
            return False

        user.add_role(role_name)
        return True

    def view_user_role(self):
        users = self.user_manager.get_users()
        print("username")
        for user in users:
            print(users[user].get_username())
        username = str(input("enter a username:: "))
        if self.user_manager.username_exists(username) is False:
            print("Invalid Username")
            return False
        user = users.get(username)
        user_roles = user.get_roles()

        print("Assigned roles")
        for user_role in user_roles:
            print(user_role)

    def add_resource_role(self):
        roles = self.role_manager.get_all_roles()
        print("Roles:")
        for role in roles:
            print(roles[role].get_name())
        role_name = str(input("enter role name::"))
        if self.role_manager.role_name_exist(role_name) is False:
            print("Invalid Role Name")
            return False

        role = self.role_manager.get_role(role_name)

        resources = self.resource_manager.get_all_resources()
        print("Resources:")
        for resource in resources:
            print(resources[resource].get_name())

        resource_name = str(input("Enter a resource_name::"))
        if self.resource_manager.resource_name_exist(resource_name) is False:
            print("Invalid Resource Name")
            return False

        resource = self.resource_manager.get_resource_by_name(resource_name)

        resource_action_types = resource.get_action_types()
        print("ActionTypes:")
        for action_type in resource_action_types:
            print(action_type)
        print('ALL (to add all the above action types)')
        action_type = str(input("Enter an Action type::")).upper()
        if action_type not in resource_action_types and action_type != 'ALL':
            print("Invalid action type")
            return False

        if action_type == 'ALL':
            role.add_all_resource_action(resource)
        else:
            role.add_resource_action(resource.get_name(), action_type)
        print("Resource action type added to role")

    def view_resource_role(self):
        roles = self.role_manager.get_all_roles()
        print("Roles:")
        for role in roles:
            print(roles[role].get_name())
        role_name = str(input("enter role name::"))
        if self.role_manager.role_name_exist(role_name) is False:
            print("Invalid Role Name")
            return False

        role = self.role_manager.get_role(role_name)

        print("resource_actions:")
        for resource_action in role.get_all_resource_action():
            print(resource_action)

    def display(self):
        print(
            "\nHii!! you are logged in as " + self.__logged_user.get_username())
        print("press 1 to login as another user")
        print("press 2 to create user")
        print("press 3 to display users")
        print("press 4 to create role")
        print("press 5 to view roles")
        print("press 6 to crete resource")
        print("press 7 to view resource")
        print("press 8 to add user role")
        print("press 9 to view user role")
        print("press 10 to add role resource action")
        print("press 11 to view role resource action")
        print("press 12 to exit")
        return str(input())

    def options(self, option):
        ctrl = 1
        if option == '1':
            success = self.login_input()
            if success:
                ctrl = 1 if self.__logged_user.is_admin() else 2
        elif option == '2':
            self.user_create_input()

        elif option == '3':
            self.print_users()

        elif option == '4':
            self.role_create_input()

        elif option == '5':
            self.dispaly_role()

        elif option == '6':
            self.resource_create_input()

        elif option == '7':
            self.display_resources()

        elif option == '8':
            self.add_user_role()

        elif option == '9':
            self.view_user_role()

        elif option == '10':
            self.add_resource_role()

        elif option == '11':
            self.view_resource_role()
        elif option == '12':
            print("bye!!\n")
            exit(0)
        return ctrl
