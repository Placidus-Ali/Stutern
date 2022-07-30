# create a BankAccount class
class BankAccount:
    def __init__(self):
        self.balance = 0
        print('The account is created and initial account balance is 0')

    def deposit(self):
        amount = float(input("Now enter the amount you want to deposit: "))
        self.balance = self.balance + amount
        print("You have successfully depositted %f" %self.balance)

    def withdraw(self):
        amount = float(input("Now enter the amount you want to withdraw: "))
        if self.balance >= amount:
                self.balance = self.balance - amount
                print("Amount withdrawn successfully")

        else:
            print("Insuficient balance. Your current account balance is %f" %self.balance)

    def enquiry(self):
        print("Current balance is %f" % self.balance)

AccessBank = BankAccount()
AccessBank.deposit()
AccessBank.withdraw()
AccessBank.enquiry()