"""
This work has been submitted by:
    Name: Shubham Singh
    Student No.: 201538011
    Date of Submission: 19th March 2021
"""

# import datetime to generate expiry date for the cards
from datetime import datetime
# import randint from random module to generate random numbers
from random import randint

# Basic Bank Account class
class BasicAccount:

    # initialise class variables
    num: int = 0
    cardNumbers = set()

    # class initialiser
    def __init__(self, acName, openingBalance: float=0):
        self.name: str = acName
        self.balance = openingBalance
        BasicAccount.cardNumbers
        BasicAccount.num += 1
        self.acNum = BasicAccount.num
        self.cardNum: str = ""
        self.cardExp: (int, int) = ()
        self.closed: bool = False

    def generateCardDate(self):
        """
        method to generate an expiry date
        3 years from today returing a tuple 
        of (month,year)
        """
        month = int(datetime.now().month)
        year = int(datetime.now().year) + 3
        cardExpiry = (month, year)
        return cardExpiry

    def generateCardNumber(self):
        """
        method to generate a random 
        16 digit number between 
        (1000000000000000, 999999999999999)
        and return in a string format
        """
        return str(randint(10**14, (10**15)-1))
    
    # deposit method
    def deposit(self, amount: float):
        """
        method to deposit the amount 
        (float) in to the bank account
        """
        if not self.closed:
            if amount >= 0:
                self.balance += amount
            else:
                print("Cannot deposit a negative amount")
        else:
            print("This account has been closed. No transactions allowed.\n")
    
    # withdraw method
    def withdraw(self, amount: float):
        """
        method to widthdraw amount(float)
        from the bank account, check if 
        requested amount is less or equal
        to the account balance
        """
        if not self.closed:
            if amount <= self.balance:
                self.balance -= amount
                print("{} has widthdrawn ￡{}".format(self.name, amount))
                print("New balance is ￡{}".format(self.balance))
            else:
                print("Cannot withdraw ￡{}, insufficient balance".format(amount))
        else:
            print("This account has been closed with no balance. No transactions allowed.\n")

    # return the bank balance
    def getBalance(self) -> float:
        if self.closed:
             print("This account has been closed. No transactions allowed.\n")
        else:
            return self.balance

    # print the balance
    def printBalance(self):
        if not self.closed:
            print("Your account balance is ￡{}".format(self.balance))
        else:
            print("This account has been closed. No transactions allowed.\n")

    def getName(self) -> str:
        """
        return the name 
        of the account holder
        """
        if not self.closed:
            return self.name
        else:
            print("This account has been closed.\n")

    # return the account number
    def getAcNum(self) -> int:
        if self.closed:
            print("This account has been closed. No transactions allowed.\n")
        else:
            return self.acNum

    def issueNewCard(self):
        """
        issue a new card calling
        helper functions defined
        """
        if not self.closed:
            self.cardNum = self.generateCardNumber()
            while self.cardNum in self.cardNumbers:
                self.cardNum = self.generateCardNumber()
            self.cardNumbers.add(self.cardNum)
            self.cardExp = self.generateCardDate()
            return self.cardNum, self.cardExp
        else:
            print("This account has been closed. No transactions allowed.\n")

    
    def closeAccount(self):
        """
        close the bank account
        return money to the holder
        return True
        """
        self.withdraw(self.balance)
        self.closed = True
        return self.closed

    
    def __str__(self):
        """
        __str__ method to represent 
        class object as string when called
        """
        if self.closed:
            return "This account has been closed."
        return self.name + ' has a Basic account with a balance of: ￡' + str(self.balance)


# Premium bank account class inherited from BasicAccount class
class PremiumAccount(BasicAccount):

    # initialise class variables
    def __init__(self, acName: str, openingBalance: float=0, initialOverdraft: float=0, overdraft: bool=False):
        super().__init__(acName, openingBalance)
        self.overdraftlimit = initialOverdraft
        self.overdraft = overdraft

    # method to set overdraftlimit to a new value
    def setOverdrafLimit(self, newLimit=0):
        self.overdraftlimit = newLimit

    def deposit(self, amount: float):
        """
        deposit method uses BasicAccount method with
        addtional overdraft checks
        """
        if self.closed:
            print("This account has been closed. No transactions allowed.\n")
        else:
            if amount >= 0:
                BasicAccount.deposit(self, amount)
                if BasicAccount.getBalance(self) >= 0:
                    self.overdraft = False
            else:
                print("Cannot deposit a negative amount")
    
    def withdraw(self, amount: float):
        """
        withdraw method for PremiumAccount class
        with use of BasicAccount methods with 
        additional overdraft checks
        """
        if not self.closed:
            if amount <= BasicAccount.getBalance(self) + self.overdraftlimit:
                self.balance -= amount
                if BasicAccount.getBalance(self) < 0:
                    self.overdraft = True
                print("{} has widthdrew ￡{}".format(self.name, amount))
                print("New balance is ￡{}".format(self.balance))
            else:
                print("Cannot withdraw ￡{}".format(amount))

        else:
            print("This account has been closed. No transactions allowed.\n")

    # return available balance (basic balance + overdraft)
    def getAvailableBalance(self):
        if not self.closed:
            return BasicAccount.getBalance(self) + self.overdraftlimit
        else:
            print("This account has been closed. No transactions allowed.\n")
        
    def printBalance(self):
        """
        print the basic balance 
        and the overdraft for the premium account
        """
        if not self.closed:
            BasicAccount.printBalance(self)
            if overdraft == True:
                print("You have an available overdraft of ￡{}".format(self.overdraftlimit+self.balance))
            else:
                print("You have an available overdraft of ￡{}".format(self.overdraftlimit))
        else:
            print("This account has been closed. No transactions allowed.\n")

    def closeAccount(self):
        """
        method check if the account 
        is overdrawn and close the account
        """
        if self.overdraft:
            print("Cannot close account due to customer being overdrawn by ￡{}".format(-self.balance))
            return False
        else:
            PremiumAccount.withdraw(self, self.balance)
            return True
    
    def __str__(self):
        """
        string representation method 
        for the class object when called
        """
        if self.closed:
            print("This account has been closed. No transactions allowed.\n")
        else:
            return self.name + ' has a Premium account with an available balance of: ￡' \
            + str(self.balance) + ' and an overdraft limit of: ￡' + str(self.overdraftlimit)
