class BankAccount:
    def __init__(self, int_rate=0, bal=0): # don't forget to add some default values for these parameters!
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
    def display_account_info(self):
        print("Balance: $"+str(self.balance))
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance*=(self.rate+1)
        return self

user1 = BankAccount(0.01,669)
user2 = BankAccount()

#To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code
user1.deposit(100).deposit(150).deposit(200).withdraw(80).yield_interest().display_account_info()
#To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)
user2.deposit(100).deposit(150).withdraw(50).withdraw(50).withdraw(50).withdraw(105).yield_interest().display_account_info()
