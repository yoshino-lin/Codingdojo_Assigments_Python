class user:
    def __init__(self,username,bal):
        self.name = username
        self.balance = bal
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

yudong = user("Yudong_Lin", 100)
mum = user("MUM", 1000)
yudong.display_user_balance()
yudong.make_withdrawal(50)
yudong.display_user_balance()
mum.display_user_balance()
yudong.transfer_money(mum,10)
yudong.display_user_balance()
mum.display_user_balance()
