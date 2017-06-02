class BankAccount:
    balance = 0

    def deposit(self,amount):
        self.balance += amount
        print('{0} is added into account. Total amount is {1}'.format(amount,self.balance))
    def withdraw(self,amount):
        if amount > self.balance:
            print('{0} is not available in the account'.format(amount))
        else:
            self.balance -= amount
            print("{0} is withdrawed from account. Total amount is {1}".format(amount,self.balance))

class MinimumBalanceAccount(BankAccount):

    def minimum_balance_check(self):
        if self.balance<1000:
            print('Minimum balance should be maintained in your account')
            return False
        return True
    def withdraw(self,amount):
        if amount > self.balance:
            print('{0} is not available in the account'.format(amount))
        else :
            self.balance -= amount
            if self.minimum_balance_check():
                print("{0} is withdrawed from account. Total amount is {1}".format(amount,self.balance))
