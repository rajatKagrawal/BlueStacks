from .user import UsersManager
from .resource import ResourceManager
from .role import RoleManager

from .user_view import UserView
from .main_view import MainView
from .admin_view import AdminView


class RBAC:

    def __init__(self):
        self.__logged_user = None
        self.user_manager = UsersManager()
        self.role_manager = RoleManager()
        self.resource_manager = ResourceManager()

    def init(self):
        self.user_manager.register_user('admin', 'admin', True)
        self.user_manager.register_user('user1', 'user1')
        self.user_manager.register_user('user2', 'user2')
        self.role_manager.register_role('role1')
        self.role_manager.register_role('role2')
        self.resource_manager.register_resource('res1', {'READ', 'WRITE'})
        self.resource_manager.register_resource('res2', {'READ', 'WRITE'})
        user = self.user_manager.get_user('user1')
        user.add_role('role1')
        role = self.role_manager.get_role('role1')
        role.add_resource_action('res1', 'READ')
        role.add_resource_action('res1', 'WRITE')

    def run(self):
        ctrl = 0
        menu = None
        while True:
            if ctrl == 0:
                menu = MainView(self.user_manager, self.role_manager,
                                self.resource_manager, self.__logged_user)
            elif ctrl == 1:
                menu = AdminView(self.user_manager, self.role_manager,
                                 self.resource_manager, self.__logged_user)
            elif ctrl == 2:
                menu = UserView(self.user_manager, self.role_manager,
                                self.resource_manager, self.__logged_user)
            option = menu.display()
            ctrl = menu.options(option)
            if option == '1':
                self.__logged_user = menu.get_logged_user()
