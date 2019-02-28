class myBankAccount:

    def __init__(self):
        self.__myBalance = 0

    def getBalance(self):
        return(self.__myBalance)
    
    def __setBalance(self, newBalance):
        self.__myBalance = newBalance
        
    def deposit(self, amount):
        self.__setBalance(self.__myBalance + amount)
        print("New balance: ", self.__myBalance)
        
    def withdraw(self, amount):
        if( amount > self.__myBalance):
            print("Not enough money!")
        else:
            self.__setBalance(self.__myBalance - amount)
            print("You withdrew: ", amount, "\nBalance remaining: ", self.__myBalance)


mba = myBankAccount('Zach')
mba.deposit(50)
print(mba.getBalance())
mba.withdraw(49)
print(mba.getBalance())
mba.withdraw(2)
print(mba.getBalance())


# mba.__setBalance(50)




