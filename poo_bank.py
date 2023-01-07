#simple banking system

import time
import os

class User:
    def __init__(self):
        User.name = validName()
        User.surname = validSurname(User.name)
        User.ID = validID()
        User.__pass = validPass()

class Bank(User):
    def __init__(self):
        super().__init__()
        Bank.__amount = 0
    
    def __deposit__(self):
        while True:
            try:
                amount = int(input("\nHow much money do you want to deposite?: "))
                if amount <= 0:
                    print("Error input. Please, choose a valid amount.")
                else:
                    Bank.__amount += amount
                    print("Deposite successfully made.")
                    break
            except ValueError:
                print("Error input. Please, use only numbers.")
    
    def __withdraw__(self):
        while True:
            try:
                amount = int(input("\nHow much money do you want to withdraw from your account?: "))
                if amount <= 0:
                    print("Error input. Please, choose a valid amount.")                   
                elif amount > Bank.__amount:
                    print("Insufficient funds.")
                    break
                else:
                    Bank.__amount -= amount
                    print("Withdraw successfully made.")
                    break
            except ValueError:
                print("Value error.")       
               

    def __showAmount__(self):
        print("\n------------CURRENT AMOUNT------------")
        print("\n$ {}".format(Bank.__amount))


def validName():
    var = input("Input your name: ").capitalize()
    while not var.isalpha() or len(var) > 30:
        print("Invalid input.")
        var = input("\nInput your name: ").capitalize()
    return var

def validSurname(x):
    var = input("Input your surname: ").capitalize()
    while not var.isalpha() or len(var) > 30 or var == x:
        print("Invalid input.")
        var = input("\nInput your name: ").capitalize()
    return var

def validID():
    var = input("Input your ID: ")
    while not var.isnumeric() or len(var) != 8:
        print("Invalid input.")
        var = input("\nInput your ID: ")
    return var

def validPass():
    var = input("Input your password (longer than 7 chars, include numbers): ")
    while var.isalpha() or len(var) < 7:
        print("Invalid input.")
        var = input("\nInput your password (longer than 7 chars, include numbers): ")
    return var

def menu():
    while True:
        print("\n---------LIST OF OPTIONS---------")
        print("\n1--Deposit\n2--Withdraw\n3--Show available amount\n4--Quit")
        try:
            action = int(input("\nWhat do you want to do today?: "))
            if action not in (1, 2, 3, 4):
                print("\nError input. Please, choose a valid option.")
                time.sleep(3)
                os.system('cls')
            else:
                return action
        except ValueError:
            print("Error input. Please, choose a valid option.")
            menu()
                
def main():
    print("\n-------------Welcome-------------")
    user = Bank()
    print("\nHello {}.".format(user.name))
    option = menu()
    while option!= 4:
        if option == 1:
            user.__deposit__()
        elif option == 2:
            user.__withdraw__()
        elif option == 3:
            user.__showAmount__()
        time.sleep(3)
        os.system('cls')
        option = menu()
    print("Closing your session.")
main()
