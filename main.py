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
                                                                                    