class Bankaccount:
    def __init__(self,accountNo,__balance):
        self.__balance = __balance
        self.accountNo = accountNo

    def get_balance(self):
        return self.__balance
    
    def set_balance(self,balance):
        self.__balance = balance
    def withDraw(self,amount):
        self.__balance -= amount
        print(amount,"has withdrawn successfully")

    def deposit(self,amount):
        self.__balance += amount
        print(amount,"has added to your account successfully")
    

b1 = Bankaccount(101,1000)
print(b1.get_balance())
b1.set_balance(2500)
print(b1.get_balance())
b1.withDraw(100)
print(b1.get_balance())
b1.deposit(200)
print(b1.get_balance())
    