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

**Admin View**

Hii!! you are logged in as admin

press 1 to login as another user

press 2 to create user

press 3 to display users

press 4 to create role

press 5 to view roles

press 6 to create resource

press 7 to view resource

press 8 to add user role

press 9 to view user role

press 10 to add role resource action

press 11 to view role resource action

press 12 to exit

These menu is for the admin users since admin users can create user, role and resources along with assigning them

1: Login to another user with username password

2: To create a new admin/user

3: To display all the users in the system 

4: To create role

5: To view all roles in the system

6: To create Resources with their action types

7: To view all Resources and their action type

8: To add role to a user

9: To view all roles of a user

10: To add resource to role along with their allowed action types

11: To view all resources of a role

12: to exit from the System

**User View**

Hii!! you are logged in as user1

press 1 to login as another user

press 2 to view roles

press 3 to access resources

press 4 to exit

These menu is for normal users who can access the resources if have required role

1: To login as another user

2: To view all roles assigned to the logged in user

3: To access a resource action

4: To exit from system


Note: For simplicity we assume admin has access to all resource action hence the access resource action option is provided only for normal user.

**Project Structure**

root:

`run.py`: is the main runner file to run, creates a rbac object and call its method to start the system

rbac/:

`rbac.py`: contains RBAC class which contains alll the resources and controlls which menu/view to display.

`menu.py`: contains Menu class which is the base class for all other view/menu classes

`main_view.py`: contains MainView class which inherits Menu class, it contians display method, options and other methods required for Main view.

`admin_view.py`: contains AdminView class which inherits Menu class, it contians display method, options and other methods required for Admin view.

`user_view.py`: contains UserView class which inherits Menu class, it contians display method, options and other methods required for User view.

`user.py`: contains User class which contains all attributes and method for User entity and UserManager class to act as store of all users in the system along with utility methods to manage them

`role.py`: contains User class which contains all attributes and method for Role entity and RoleManager class to act as store of all roles in the system along with utility methods to manage them

`resource.py`: contains Resource class which contains all attributes and method for Resource entity, ActionType class to define all the available action types  and ResourceManager class to act as store of all resources in the system along with utility methods to manage them


**Init**

The system initialises some default user, role, resources to start with:
* username: admin  password: admin :: this is a admin user
* username: user1  password: user1 :: this is a normal user
* usernmae: user2  password: user2 :: this is a another normal user
* resource: res1   action_types: [READ, WRITE]
* resource: res2   action_types: [READ, WRITE, DELETE]
* role: role1  this role has access to READ, WRITE res1
* role: role2  this role has access to READ, WRITE res2
* role 1 is assigned to user1
* role 2 is assigned to user2
* user 1 has READ, WRITE access to res1 and no access of res2
* user 2 has READ, WRITE access to res1 and no access of res1
* no user has access to DELETE res2
* system gives ACCESS_GRANTED if user has access and ACCESS DENIED if user doesn't have access

