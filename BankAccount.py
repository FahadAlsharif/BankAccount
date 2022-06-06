class BankAccount:
	def __init__(self, int_rate = 0.01, balance =0 ): 
		self.int_rate = int_rate
		self.balance = balance
	def deposit(self, amount):
		self.balance += amount
		return self
	def withdraw(self, amount):
		self.balance -= amount
		return self
	def display_account_info(self):
		print(self.int_rate,self.balance)
		return self
	def yield_interest(self):
		print(self.balance * (1 + self.int_rate))
		return self
account1 = BankAccount()
account2 = BankAccount()

account1.deposit(50).deposit(50).deposit(100).yield_interest().display_account_info()
account2.deposit(500).deposit(50).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()