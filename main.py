import pickle
import os
import pathlib
class Account :
        accNo = 0
            name = ''
                deposit=0
                    type = ''
                        
                            def createAccount(self):
                                        self.accNo= int(input("Enter the account no : "))
                                                self.name = input("Enter the account holder name : ")
                                                        self.type = input("Enter the type of account [C/S] : ")
                                                                self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current"))
                                                                        print("\n\n\nAccount Created")
                                                                            
                                                                                def showAccount(self):
                                                                                            print("Account Number : ",self.accNo)
                                                                                                    print("Account Holder Name : ", self.name)
                                                                                                            print("Type of Account",self.type)
                                                                                                                    print("Balance : ",self.deposit)
                                                                                                                        
                                                                                                                            def modifyAccount(self):
                                                                                                                                        print("Account Number : ",self.accNo)
                                                                                                                                                self.name = input("Modify Account Holder Name :")
                                                                                                                                                        self.type = input("Modify type of Account :")
                                                                                                                                                                self.deposit = int(input("Modify Balance :"))
                                                                                                                                                                        
                                                                                                                                                                            def depositAmount(self,amount):
                                                                                                                                                                                        self.deposit += amount
                                                                                                                                                                                            
                                                                                                                                                                                                def withdrawAmount(self,amount):
                                                                                                                                                                                                            self.deposit -= amount
                                                                                                                                                                                                                
                                                                                                                                                                                                                    def report(self):
                                                                                                                                                                                                                                print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)
                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                        def getAccountNo(self):
                                                                                                                                                                                                                                                    return self.accNo
                                                                                                                                                                                                                                                        def getAcccountHolderName(self):
                                                                                                                                                                                                                                                                    return self.name
                                                                                                                                                                                                                                                                        def getAccountType(self):
                                                                                                                                                                                                                                                                                    return self.type
                                                                                                                                                                                                                                                                                        def getDeposit(self):
                                                                                                                                                                                                                                                                                                    return self.deposit
                                                                                                                                                                                                                                                                                                        

                                                                                                                                                                                                                                                                                                        def intro():
                                                                                                                                                                                                                                                                                                                print("\t\t\t\t**********************")
                                                                                                                                                                                                                                                                                                                    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
                                                                                                                                                                                                                                                                                                                        print("\t\t\t\t**********************")

                                                                                                                                                                                                                                                                                                                            print("\t\t\t\tBrought To You By:")
                                                                                                                                                                                                                                                                                                                                print("\t\t\t\tprojectworlds.in")
                                                                                                                                                                                                                                                                                                                                    input()



                                                                                                                                                                                                                                                                                                                                    def writeAccount():
                                                                                                                                                                                                                                                                                                                                            account = Account()
                                                                                                                                                                                                                                                                                                                                                account.createAccount()
                                                                                                                                                                                                                                                                                                                                                    writeAccountsFile(account)

                                                                                                                                                                                                                                                                                                                                                    def displayAll():
                                                                                                                                                                                                                                                                                                                                                            file = pathlib.Path("accounts.data")
                                                                                                                                                                                                                                                                                                                                                                if file.exists ():
                                                                                                                                                                                                                                                                                                                                                                            infile = open('accounts.data','rb')
                                                                                                                                                                                                                                                                                                                                                                            