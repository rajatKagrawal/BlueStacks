from enum import Enum


class ActionType(Enum):
    READ = 1
    WRITE = 2
    DELETE = 3


class Resource:
    def __init__(self, name, allowed_action_types):
        self.__name = name
        self.__action_types = allowed_action_types

    def is_action_type_allowed(self, action_type):
        return action_type in self.__action_types

    def get_name(self):
        return self.__name

    def get_action_types(self):
        return self.__action_types


class ResourceManager:
    def __init__(self):
        self.__resources = {}

    def __add_resource(self, resource):
        self.__resources[resource.get_name()] = resource

    def resource_name_exist(self, resoure_name):
        return resoure_name in self.__resources

    def register_resource(self, resource_name, action_types):
        if self.resource_name_exist(resource_name):
            return False, "resource name already exist"
        action_types = set(action_types)
        resource = Resource(resource_name, action_types)
        self.__add_resource(resource)
        return True, "resource registered successfully"

    def get_all_resources(self):
        return self.__resources

    def get_resource_by_name(self, resource_name):
        return self.__resources.get(resource_name)
