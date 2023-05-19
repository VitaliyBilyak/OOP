class User():
    def __init__(self, first_name, last_name, age, country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        self.login_attempts=0
    def describe_user(self):
        print(self.first_name,self.last_name)
    def greeting_user(self):
        print('Вітаю вас',self.first_name,self.last_name,self.age,self.country)
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts=0


user=User('Vitalik','Bilyak',17,'Ukraine')
user2=User('Jon','Bertam',25,'Ukraine')
user3=User('Tom','Vister',27,'Ukraine')
print('Завдання a')
user.describe_user()
user.greeting_user()

user2.describe_user()
user2.greeting_user()

user3.describe_user()
user3.greeting_user()
print('Завдання b')
user.increment_login_attempts()
user.increment_login_attempts()
print('Кількість:',user.login_attempts)
user.reset_login_attempts()
print('Рахунок обнульвся:',user.login_attempts)

