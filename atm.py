class ATM():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return 'Owner name is: {}\nBalance available: {}'.format(self.owner,self.balance)
        
    def deposit(self,depo):
        self.balance+=depo
        return 'After Deposit Balance is: {}'.format(self.balance)
    def withdraw(self,wid):
        if wid<self.balance:
            self.balance-=wid
            return 'Current balance: {}'.format(self.balance)
        else:
            return 'Insufficient Blance'
            
print('**********Developer Part***********')            
a=input("Enter name of Customer: ")
b=int(input("Balance: "))
aa=ATM(a,b)  
print(aa)

print("***********User Part**************")
d=aa.deposit(int(input("Deposit Ammount: ")))
print(d)

w=aa.withdraw(int(input("How much You want to withdraw: ")))

print(w)
