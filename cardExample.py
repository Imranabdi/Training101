class Card:
    balance = 0

    # created a constructor
    def __init__(self,bal):
        self.balance = bal

    #create a method for withdrawal
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount + (0.2 * amount)
            return self.printReceipt(self.balance,amount)

        else:
            return "Insufficient balance!"

    # method to print out the receipt
    def printReceipt(self,balance,withdraw):
        return """ 
                    RECEIPT
            WITHDRAWN AMOUNT:........{}
            BALANCE:.......{}
        """.format(withdraw,balance)



