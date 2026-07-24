class BankAccount():
    def __init__(self,accHolder,accBalance,pin):
        self.accHolder=accHolder
        self.accBalance=accBalance
        self.pin=pin
        self.hisotry=[]

    def deposit(self,amount,PIN):
        if PIN==self.pin:
            self.accBalance+=amount
            print("Account Balance :", self.accBalance)
            self.hisotry.append(f"Deposited ${amount}")
        else:
            print("Incorrected PIN!")

    def withdraw(self,amount,enter_pin):
        if enter_pin==self.pin:
            if amount<=self.accBalance:
                self.accBalance-=amount
                print("Account balance :",self.accBalance)
                self.hisotry.append(f"Withdrawal of ${amount}")
            else:
                print("Insufficent Balance")
        else :
            print("Invalid PIN")
    def show_balance(self):
        print("Account Balance :",self.accBalance)
    def transaction(self):
        if len(self.hisotry)==0:
            print("Empty Transactions")
        else:
            print("Transaction History")
            for t in self.hisotry:
                print(t)

        
class SavingsAcc(BankAccount):
    def savIntrest(self,rate):
        intrest_amt=self.accBalance*rate/100
        self.accBalance+=intrest_amt
        print("Intrest Added :",intrest_amt)
        return intrest_amt

class currentAcc(BankAccount):
    def currIntrest(self,rate):
        intrest_amt=self.accBalance*rate/100
        self.accBalance+=intrest_amt
        print("Intrest Added :",intrest_amt)
obj=BankAccount('Febin',5000,1234)
o=BankAccount('Alan',10000,2222)
b=BankAccount('Amal',15000,4321)
obj1=SavingsAcc('Febin',1000,1234)
obj2=currentAcc('Febin',2000,1234)

obj1.savIntrest(5)
obj2.currIntrest(2)
obj1.show_balance()
obj1.withdraw(600,1234)
obj1.deposit(200,1234)
         


while(True):
    print("\n ------Banking System-------"
          "\n1.Deposit"
          "\n2.Withdraw"
          "\n3.Check Balance"
          "\n4.SavingsAcc - Intrest"
          "\n5.CurrentAcc - Intrest"
          "\n6.Transaction History"
          "\n7.Exit")

    choice=int(input("Enter your Choice :"))

    if choice==1:
        amount=int(input("Enter the deposit amount :"))
        pin=int(input("Enter the PIN:"))
        obj.deposit(amount,pin)
    elif choice==2 :
        amount=int(input("Enter the Withdraw amount:"))
        pin=int(input("Enter the PIN:"))
        obj.withdraw(amount,pin)
    elif choice==3:
        obj.show_balance()
    elif choice==4:
        obj1.savIntrest(5)
    elif choice==5:
        obj2.currIntrest(2)
    elif choice==6:
        obj.transaction()
    elif choice==7:
        print("Exit")
        break
    else:
        print("Please enter a valid choice...")       



        

        




