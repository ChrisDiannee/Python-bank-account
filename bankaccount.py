
import time
import datetime

class CreateAccount:
    def __init__(self):
        self.balance = 0
    def name(self,name):
        self.name=name
    def sex(self,sex):
        self.sex=sex
    def dot(self,dot):
        self.dot=dot
    def address(self,address):
        self.address=address
    def work_position(self,work_position):
        self.work_position=work_position

        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
            
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def getbalance(self):
        return self.balance

    def CreateAccount():
        return CreateAccount()

    def create():
        CreateAccount1=CreateAccount()


        

class Create(CreateAccount):
    def __init__(self,amount):
        self.balance = amount
    
    def AddAccount():
        CreateAccount1=CreateAccount()
        print("ADD ACCOUNT\n")
        a= input("Full Name: ")
        CreateAccount1.name
        b= input("Sex: ")
        CreateAccount1.sex
        c= input("Date of Birth: ")
        CreateAccount1.dot
        d= input("Address: ")
        CreateAccount1.address
        e= input("Work/Possition: ")
        CreateAccount1.work_position
    def Initial():
        initial=0
        print("initial deposit is")
        print(initial)
        


    def manage():
        CreateAccount1=CreateAccount()
        print("1 Deposit")
        print("2 Withdraw")
        print("3 Balance Inquiry")
        print("4 Account Info")
        prom=int(input("Choice: "))
        if prom==1:
            deposit()
        if prom==2:
            withdraw()
            
        
        
        
    def deposit():
        CreateAccount1=CreateAccount()
        print("Deposit ACCOUNT\n")
        a= input("Deposit amount: ")
        CreateAccount1.deposit
        
    def withdraw():
        CreateAccount1=CreateAccount()
        print("Withdraw ACCOUNT\n")
        a= input("Withdraw amount: ")
        CreateAccount1.withdraw
    
        



        






    inp=int(input("1 CREATE account \n2 MANAGE account\n"))
    if inp==1:
        promp=int(input("1 for add account \n2 for Add initial deposit\n"))
        if promp==1:
            AddAccount()
        elif promp==2:
            Initial()

    if inp==2:
        print("1 Deposit")
        print("2 Withdraw")
        print("3 Balance Inquiry")
        print("4 Account Info")
        prom=int(input("Choice: "))

        if prom==1:
            deposit()
        if prom==2:
            withdraw()
        if prom==3:
            balance()
        if prom==4:
            AddAccount()

        
            



        


    
        
class ManageAccount(CreateAccount):


    
    def __init__(self,initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def getbalance(self):
        return self.balance

    def CreateAccount():
        return CreateAccount()

    def create():
        CreateAccount1=CreateAccount()


    

