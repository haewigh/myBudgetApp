class Budget:
     
    def __init__(self, name, rate, balance):
        self.name = name
        self.rate = rate
        self.balance = balance
    '''
    This function will share the income among the categories, provided there is
    '''
    def share(self):
        income = int(input("enter income:\n"))
        budget_1.balance += (budget_1.rate * income)
        budget_2.balance += (budget_2.rate * income)
        budget_3.balance += (budget_3.rate * income)

    def deposit(self):
        credit = int(input("Amount to deposit: "))
        self.balance += credit
        return f"{credit} deposited into {self.name} account\n".format(credit, self.name)

    def withdraw(self):
        checker = False
        while checker == False:
            debit = int(input("Amount to withdraw: "))
            if (debit <= self.balance):
                self.balance -= debit
                checker = True
            else:
                print("Insufficient fund, please try again\n")
        return f"Debit: {debit}, {self.name} Account Balance: {self.balance}\n".format(debit, self.name, self.balance)

    def check_balance(self):
        return f"Your {self.name} account balance is {self.balance}\n".format(self.name, self.balance)

    def transfer(Budget):
        sender = int(input("Select Sender Account:ENTER(1-3)\n1. %s\t2. %s\t3. %s--->" %(budget_1.name, budget_2.name, budget_3.name)))   
        receiver= int(input("Select recipient Account:ENTER(1-3)\n1. %s\t2. %s\t3. %s--->" %(budget_1.name, budget_2.name, budget_3.name)))
        transfer_amount = int(input("Amount to Transfer:"))
        if sender == 1:
            if(transfer_amount <= budget_1.balance):
                budget_1.balance -= transfer_amount
                if receiver == 2:
                    budget_2.balance += transfer_amount
                elif receiver == 3:
                    budget_3.balance += transfer_amount
                return f"#{transfer_amount} transfered from {budget_1.name}\n".format(transfer_amount, budget_1.name)
            else:
                print(f"INSUFFICIENT FUND\n{budget_1.name} Balance is {budget_1.balance}\n".format(budget_1.name, budget_1.balance))

        if(sender == 2):
            if(transfer_amount <= budget_2.balance):
                budget_2.balance -= transfer_amount
                if receiver == 1:
                    budget_1.balance += transfer_amount
                elif receiver == 3:
                    budget_3.balance += transfer_amount
                return f"#{transfer_amount} transfered from {budget_2.name}\n".format(transfer_amount, budget_2.name)
            else:
                print(f"INSUFFICIENT FUND\n{budget_2.name} Balance is {budget_2.balance}\n".format(budget_2.name, budget_2.balance))

        elif sender == 3:
            if(transfer_amount <= budget_3.balance):
                budget_3.balance -= transfer_amount
                if receiver == 1:
                    budget_1.balance += transfer_amount
                elif receiver == 2:
                    budget_2.balance += transfer_amount
                return f"#{transfer_amount} transfered from {budget_3.name}\n".format(transfer_amount, budget_3.name)
            else:
                print(f"INSUFFICIENT FUND\n{budget_3.name} Balance is {budget_3.balance}\n".format(budget_3.name, budget_3.balance))
    '''
    To prepare spreadsheet that combine the Categories
    '''
    def budget_sheet(Budget):
        print("\n\n" + "Current Budget Status".center(34,"=")+"\n")
        print("S\'N\tCategory\t\tBalance\n")
        print(f"1.\t{budget_1.name}\t\t\t#{budget_1.balance}".format(budget_1.name, budget_1.balance))
        print(f"2.\t{budget_2.name}\t\t#{budget_2.balance}".format(budget_2.name, budget_2.balance))
        print(f"3.\t{budget_3.name}\t\t#{budget_3.balance}\n".format(budget_3.name, budget_3.balance))
        print("".center(34,"=") + "\n")


budget_1 = Budget("Food", 0.6, 0)
budget_2 = Budget("Clothing", 0.3, 0)
budget_3 = Budget("Entertainment", 0.1, 0)

def init():
    print("AVAILABLE FEATURES\n1. Monthly Allocation\n2. Deposit Funds\n3. Withdraw Funds\n4. Transfer Funds\n5. Check Balance\n6. Close App\n")
    selectOption = int(input("SELECT OPTION(enter 1-6)---->"))
    
    if selectOption == 1:
        Budget.share(Budget)
        print("\n" + "INCOME ALLOCATION".center(34,"=")+"\n")
        print("Category\tAmount\n%s\t\t%d\n%s\t%d\n%s\t%d" %(budget_1.name, budget_1.balance, budget_2.name, budget_2.balance, budget_3.name, budget_3.balance))
        print("".center(34,"=") + "\n")
        print("Thank you for using the App\nWant to do more transaction\n(Press 6 to exit)\n")
        init()
        
    elif selectOption == 2:
        print("\n" + "FUND DEPOSIT".center(34,"="))
        choiceAccount = int(input("1. Food\n2. Clothing\n3. Entertainment\nEnter 1, 2 " +"or"+" 3---->"))
        if choiceAccount == 1:
            print(budget_1.deposit())
            print("Thank you for using the App\nWant to do more transaction\n(Press 6 to exit)\n")
            init()
        elif choiceAccount == 2:
            print(budget_2.deposit())
            print("Thank you for using the App\nWant to do more transaction\n(Press 6 to exit)\n")
            init()
        elif choiceAccount == 3:
            print(budget_3.deposit())
            print("Thank you for using the App\nWant to do more transaction\n(Press 6 to exit)\n")
            init()

    elif selectOption == 3:
        print("\n" + "FUND WITHDRAWAL".center(34,"="))
        choiceAccount = int(input("1. Food\n2. Clothing\n3. Entertainment\nEnter 1, 2 "+"or"+" 3---->"))
        if choiceAccount == 1:
            print(budget_1.withdraw())
            print("Thank you for using the App\nWant to do more transaction\n(Press 6 to exit)\n")
            init()
        elif choiceAccount == 2:
            print(budget_2.withdraw())
            print("Thank you for using the App\nWant to do more transaction\n(Press 6 to exit)\n")
            init()
        elif choiceAccount == 3:
            print(budget_3.withdraw())
            print("Thank you for using the App\nWant to do more transaction\n(Press 6 to exit)\n")
            init()

    elif selectOption == 4:
        print("\n" + "FUND TRANSFER".center(34,"="))
        print(Budget.transfer(Budget))
        print("Thank you for using the App\nWant to do more transaction\n(Press 6 to exit)\n")
        init()

    elif selectOption == 5:
        print("\n" + "ACCOUNT BALANCE".center(34,"="))
        choiceAccount = int(input("1. Food\n2. Clothing\n3. Entertainment\n4. Budget Balancesheet\nEnter 1, 2, 3 "+"or"+" 4---->"))
        if choiceAccount == 1:
            print(budget_1.check_balance())
            print("Thank you for using the App\nWant to do more transaction\n(Press 6 to exit)\n")
            init()
        elif choiceAccount == 2:
            print(budget_2.check_balance())
            print("Thank you for using the App\nDo you want to do another transaction?\n(Press 6 to exit)\n")
            init()
        elif choiceAccount == 3:
            print(budget_3.check_balance())
            print("Thank you for using the App\nWant to do more transaction\n(Press 6 to exit)\n")
            init()
        elif choiceAccount == 4:
            Budget.budget_sheet(Budget)
            print("Thank you for using the App\nWant to do more transaction\n(Press 6 to exit)\n")
            init()

    elif selectOption == 6:
        exit()

    else:
        print("Invalid Entry, Please Enter the correct number(1-6)\n")
        init()

print("Welcome to your Budget App\n")
init()
