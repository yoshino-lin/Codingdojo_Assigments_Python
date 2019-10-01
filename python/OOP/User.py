class user:
    def __init__(self,username,bal):
        self.name = username
        self.balance = bal
    def make_deposit(self, amount):
        self.balance += amount
    def make_withdrawal(self, amount):
        if amount > self.balance:
            print("ERRO: You do not have enough money to withdrawl")
        else:
            self.balance -= amount
    def display_user_balance(self):
        print("User: "+self.name+", Balance: $"+str(self.balance))
    def transfer_money(self, other_user, amount):
        if amount > self.balance:
            print("ERRO: You do not have enough money to withdrawl")
        else:
            self.balance -= amount
            other_user.balance += amount
            print("Transfer succeeds! Now:")
            self.display_user_balance()
            other_user.display_user_balance()

#Create 3 instances of the User class
user1 = user("Yudong_Lin", 1000)
user2 = user("mum", 10000)
user3 = user("poor friend", 10)

#Have the first user make 3 deposits and 1 withdrawal and then display their balance
user1.make_deposit(100)
user1.make_deposit(200)
user1.make_deposit(300)
user1.make_withdrawal(350)
user1.display_user_balance()

#Have the second user make 2 deposits and 2 withdrawals and then display their balance
user2.make_deposit(50)
user2.make_deposit(10)
user2.make_withdrawal(290)
user2.make_withdrawal(666)
user2.display_user_balance()

#Have the third user make 1 deposits and 3 withdrawals and then display their balance
user3.make_deposit(10)
user3.make_withdrawal(9)
user3.make_withdrawal(2)
user3.make_withdrawal(4)
user3.display_user_balance()

#BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
user1.transfer_money(user3,100)
