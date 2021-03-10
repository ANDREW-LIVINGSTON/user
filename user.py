class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def make_deposit(self, amount):
        self.account_balance += amount

    def display_user_balance(self):
        print(self.name, self.account_balance)

user1 = User("user1", "user1@python.com")
user2 = User("user2", "user2@python.com")
user3 = User("user3", "user3@python.com")

user1.make_deposit(500)
user1.make_deposit(450)
user1.make_deposit(1000)
user1.make_withdrawal(350)
user1.display_user_balance()

user2.make_deposit(575)
user2.make_deposit(897)
user2.make_withdrawal(273)
user2.make_withdrawal(7)
user2.display_user_balance()

user3.make_deposit(2500)
user3.make_withdrawal(12)
user3.make_withdrawal(37)
user3.make_withdrawal(150)
user3.display_user_balance()