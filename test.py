# Create global variable
users_list = []

#Create class for user 
# class User:
#     def __init__(self,name,surname,age) -> None:
#         self.name = name
#         self.surname = surname
#         self.age = age 
        

#Define functions interfaceAge
def create_user(user):
    users_list.append(user)         # with .append you add user to users_list

def update_user(index,attribute,value):
    users_list[index][attribute] = value

def delete_user(index):
    users_list.pop(index)

user = {'Name': 'George', 'Surname': 'Batas', 'Age': 32}

create_user(user)
print(users_list)

user = {'Name': 'Marianna', 'Surname': 'Kostopoulou', 'Age': 35}

create_user(user)
print(users_list)

update_user(1, 'Age', 30)
print(users_list)

delete_user(0)
print(users_list)