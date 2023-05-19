from User import User
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print('Привілеїв адміністратора')
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self,first_name, last_name, age, country):
        super().__init__(first_name,last_name,age,country)
        self.privilege=Privileges(['Allowed to add message','Allowed to delete users','Allowed to ban users'])
print('Завдання d')
admin = Admin('Tom','Dolmar',17,'Ukraine')
admin.privilege.show_privileges()