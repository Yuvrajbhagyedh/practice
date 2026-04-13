class bank:
    def __init__(self):
        self.__balance=80000

    def debit(self,amouttaken):
        self.__balance-=amouttaken
        print("the total amount is now :",self.balance)
    def credit(self,amount):
        self.__balance+=amount
        print("the toatal amount is now after credit is :",self.balance)

s1=bank()
s1.credit(67000)
s1.debit(12000)            