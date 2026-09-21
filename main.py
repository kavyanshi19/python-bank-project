import json
import random
import string
from pathlib import Path

class Bank:
    database='data.json'
    data=[]
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())
        else:
            print("no such file exist")
    except Exception as error:
        print(f"an exception occured as{error}")
        
    @staticmethod
    def __update():
        with open(Bank.database,'w') as fw:
            fw.write(json.dumps(Bank.data))
            
    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=4)
        num=random.choices(string.digits,k=4)
        sc=random.choices("!@#$%^&*+",k=2)
        id=alpha+num+sc
        random.shuffle(id)
        return"".join(id)
        
    def createaccount(self):
        info = {
            "name":input("enter your name: "),
            "age":int(input("enter your age: ")),
            "email":input("enter your email: "),
            "pin":int(input("enter your pin(4-digit): ")),
            "accountNo": Bank.__accountgenerate(),
            "balance": 0
        }
        if info['age']<18:
            print("Sorry not eligible for creating account.")
        elif len(str(info['pin']))!=4:
            print("invalid pin.")
        else:
            print("account created!")
            for i in info:
                print(f"{i}:{info[i]}")
            print("please remember your account number.")
        
            Bank.data.append(info)
            Bank.__update()
            
    def depositemoney(self):
        accnumber=input("please enter your account number:")
        pin = int(input("please enter your pin: "))
        
        userdata=[i for i in Bank.data if i['accountNo']== accnumber and i['pin']==pin]
        
        if userdata ==False:
            print("sorry no data found")
        else:
            amount=int(input("enter the amount you want to deposit: "))
            if amount>10000 or amount<0:
                print("amount range is too high/low (suitable range to deposit amount is 0-10000)")
            else:
                userdata[0]['balance']+=amount
                Bank.__update()
                print("amount deposited successfully!!")
        
            
    def withdrawmoney(self):
        accnumber=input("please enter your account number:")
        pin = int(input("please enter your pin: "))
        
        userdata=[i for i in Bank.data if i['accountNo']== accnumber and i['pin']==pin]
        
        if userdata ==False:
            print("sorry no data found")
        else:
            amount=int(input("enter the amount you want to withdraw: "))
            if userdata[0]['balance'] < amount:
                print("insufficient balance!!")
            else:
                userdata[0]['balance']-=amount
                Bank.__update()
                print("amount withdraw successfully!!")
        
    def checkdetails(self):
        accnumber=input("please enter your account number:")
        pin = int(input("please enter your pin: "))
        
        userdata=[i for i in Bank.data if i['accountNo']== accnumber and i['pin']==pin]
        
        print("your details are: \n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")
        
    def updatedetails(self):
        accnumber=input("please enter your account number:")
        pin = int(input("please enter your pin: "))
        
        userdata=[i for i in Bank.data if i['accountNo']== accnumber and i['pin']==pin]
            
        if not userdata :
            print("no such user found ")
            
        else:
            print("you cannot change the age, account number,balance!!")
            print("fill the details for change or leave it empty if no change ")
            
            newdata={
                "name":input("enter the new name or enter to skip: "),
                "email":input("enter the new email or enter if you want to skip: "),
                "pin":input("enter new pin or press enter to skip: ")
            } 
            if newdata["name"]=="":
                newdata["name"]=userdata[0]['name']
            if newdata["email"]=="":
                newdata["email"]=userdata[0]['email']
            if newdata["pin"]=="":
                newdata["pin"]=userdata[0]['pin']
                
            newdata['age']=userdata[0]['age']
                
            newdata['accountNo']=userdata[0]['accountNo']
            newdata['balance']=userdata[0]['balance']
            
            if type(newdata['pin'])==str:
                newdata['pin']=int(newdata['pin'])
                
            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]
            
            Bank.__update() 
            print("details are updated!")    
            
    def deleteaccount(self):
        accnumber=input("please enter your account number:")
        pin = int(input("please enter your pin: "))
        
        userdata=[i for i in Bank.data if i['accountNo']== accnumber and i['pin']==pin]
            
        if not userdata :
            print("no such user found ")
            
        else:
            check=input("enter y if you want to delete the account otherwise to continue with same account enter n")
            if check=='n' or check=='N':  
                print("no changes!")
            else:
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
                
                print("account has been deleted!!!")
            Bank.__update() 
                
user=Bank()
print("press 1: for creating an account")
print("press 2: for deleting an account")
print("press 3: for depositing an money")
print("press 4: for withdrawing an money")
print("press 5: for checking your details")
print("press 6: for updating your details")

resp=int(input("tell your response:-"))

if resp==1:
    user.createaccount()

if resp==2:
    user.deleteaccount()
    
if resp==3:
    user.depositemoney()

if resp==4:
    user.withdrawmoney()

if resp==5:
    user.checkdetails()
    
if resp==6:
    user.updatedetails()
