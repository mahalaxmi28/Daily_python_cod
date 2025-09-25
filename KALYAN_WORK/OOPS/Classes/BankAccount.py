class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance


    def deposit(self,amount):
        self.balance += amount

        print(amount," has added successfully to your account")
        print("Total balance: ",self.balance)

    def withDraw(self,amount):
        self.balance -= amount
        print(amount, "has withdrawm successfully")
        print("Total balance: ",self.balance)


acount1 = BankAccount("102010",1000)
acount1.deposit(500)
acount1.withDraw(300)