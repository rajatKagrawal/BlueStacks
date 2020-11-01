## **Role Based Access Control:**

Implementing a role based access control system.
The system can be used to provide role based access to users

##### _Requirements_

`python 3 (>=3.5)
`
###### _build_

`cd BlueStacks
`

`python run.py`

Note: if you ancounter error usch as rbac.rabc module not found run the below command once

`python -m rbac.rbac`

Then run the run.py file

#### **System Spectifications**

###### _Entities:_

**User:** These is the entity representing the system/person trying to access the resources

There are two types of users in the system Admin and Normal User (we will refer to them as Admin and User respectively)

Admin: These are the entity which can create user/role/resource in the system and can assign role to user and resource action to roles

User: These is the entity which can access the resource action if allowed

**Resource:** These represent the entity user is trying to access. Their are various action types assosiated with the resources

**Action Type** These entity represent various types of access resource allows. Ex: READ, WRITE, DELETE etc.
In the present System only those three types are configured by default.

To add more Action Type add it to `ActionType` class in _/rbac/resource.py_

**Role** These entity represent a group of resource action which when assigned to user can have access to

In the present system we also define something as resource_action or scope

**resurce_action/ scope** these is a resprentation of resource + action_type mapped to roles, the syntax is : resource_name:action_type example: UserApi:READ, UserApi:WRITE

scope helps the system to figure out both the resource as well as action type the user of role has access to with a single call



###### _Views:_

There are total 3 views/menus in the system

**Main View**

Welcome to RBAC

Press 1 to login    
Press 2 to exit

These view is the home screen and the first view of the system with below options:
1: to login with username and password
2: to exit from the system
