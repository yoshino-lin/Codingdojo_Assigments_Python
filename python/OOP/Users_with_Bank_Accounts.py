class BankAccount:
    def __init__(self, int_rate, bal): # don't forget to add some default values for these parameters!
        # your code here! (remember, this is where we specify the attributes for our class)
        # don't worry about user info here; we'll involve the User class soon
        self.rate = int_rate
        self.balance = bal
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display(self):
        print("Balance: $"+str(self.balance))
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance*=(self.rate+1)
        return self

class user:
    def __init__(self,username,acount_number=1):
        self.name = username
        self.acount = []
        for i in range(acount_number):
            self.acount.append(BankAccount(int_rate=0.02,bal=100))
    def make_deposit(self, amount,id=0):
        self.acount[id].deposit(amount)
        print("account: "+str(id+1))
        self.acount[id].display()
    def make_withdrawal(self, amount,id=0):
        self.acount[id].withdraw(amount)
        print("account: "+str(id+1))
        self.acount[id].display()
    def display_user_balance(self,id=0):
        self.acount[id].display()
    def transfer_money(self, amount,id_from,id_to):
        if amount > self.acount[id_from-1].balance:
            self.acount[id_from-1].balance -= amount
            self.acount[id_to-1].balance += amount
            print("The money is successfully transfered from account"+str(id_from)+" to acoount"+str(id_to)+"!")
    """
    def test(self):
        print("testing:")
        for i in range(len(self.acount)):
            print(str(i+1)+": "+str(self.acount[i].balance))
    """
#user with 1 account
#user1 = user("name")

user1 = user("name",5)
user1.display_user_balance(1)

user1.make_deposit(100)
user1.make_withdrawal(100)

user1.transfer_money(500,1,2)
user1.display_user_balance(1)
user1.display_user_balance(2)

#warning: this testing function works well but please do not use it unless you have questions about the question
#user1.test()
