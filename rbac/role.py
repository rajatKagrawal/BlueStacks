class Role:
    def __init__(self, name):
        self.__name = name
        self.__scope = set()

    @staticmethod
    def get_scope_name(resource_name, action_type):
        return resource_name + ':' + action_type

    def get_name(self):
        return self.__name

    def add_resource_action(self, resource_name, action_type):
        self.__scope.add(self.get_scope_name(resource_name, action_type))

    def remove_resource_action(self, resource_name, action_type):
        self.__scope.discard(self.get_scope_name(resource_name, action_type))

    def add_all_resource_action(self, resource):
        for action_type in resource.get_action_types():
            self.add_resource_action(resource.get_name(), action_type)

    def remove_all_resource_action(self, resource):
        for action_type in resource.get_all_action_types():
            self.remove_resource_action(resource.get_name(), action_type)

    def get_all_resource_action(self):
        return self.__scope

    def check_resource_action(self, resource_name, action_type):
        return self.get_scope_name(resource_name, action_type) in self.__scope


class RoleManager:
    def __init__(self):
        self.__roles = {}

    def role_name_exist(self, role_name):
        return role_name in self.__roles

    def __add_role(self, role):
        self.__roles[role.get_name()] = role

    def register_role(self, role_name):
        if self.role_name_exist(role_name):
            return False, "role_name already exist"

        role = Role(role_name)
        self.__add_role(role)
        return True, "role_regitered successfully"

    def get_role(self, role_name):
        return self.__roles.get(role_name)

    def get_all_roles(self):
        return self.__roles
