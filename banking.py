
class BankAccount:
    """an attempt to model a bank account"""

    def __init__(self, accountNumber, balance):
        """Initialization of attributes for BankAccount"""
        self.accountNumber = accountNumber
        self.balance = balance


    def withdrawl(self):
        """submit a number to subtract from balance"""
        withdrawl = float(input("Please Enter Withdrawl Amount: $"))
        self.balance -= withdrawl
        print(f"Your new balance is: $", self.balance)


    def deposit (self):
        """submite a number to add to balance"""
        deposit = float(input("Please Enter Deposit Amount: $"))
        self.balance += deposit
        print('Your new balance is: $', self.balance)


    def getBalance (self):
        """Display balance"""
        print(f"Your balance is: $", self.balance)

        


class CheckingAccount (BankAccount):
    """Represents a checking account at this particular bank"""
    
    def __init__ (self, accountNumber, balance):
       """Initializes attributes from BankAccount"""
       super().__init__(accountNumber, balance)
       self.balance -= 5
       
    def checkMinimumBalance (self):
        minimum = 25
        if self.balance < minimum:
            print("Your account is below the minimum requirement")
        else: print (self.balance)
        
    def deductFees (self):
        self.balance += 5
        print ("Your new balance is: $", self.balance)
        
        

class SavingsAccount (BankAccount):
    """Represents a savings account at this particular bank"""
    
    def __init__ (self, accountNumber, balance):
       """Initializes attributes from BankAccount"""
       super().__init__(accountNumber, balance)
       
    def addInterest (self):
        interest = 0.02
        self.balance *= (1 + interest)

        
        
# Assigns title to variable ("title")
title = "welcome to the fictional bank";
# Assigns author to variable ("author")
author = "by thomas blankenship";

# Prints to screen both variables
print(title.title());
print(author.title());

my_check = CheckingAccount (900001, 29)
my_sav = SavingsAccount (9000002, 100)
print ("\n\nYour Savings Account Balance is: $", my_sav.balance)

second = input("\nWould you like to check your Checking Account Balance? (y/n):\t")

if second == "y":
    print ("\nYour Checking Account Balance is : $", my_check.balance)
    my_check.checkMinimumBalance()
else: print("\nThank you, you may now exit the program")
