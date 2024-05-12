import random
class Bank:
    def __init__(self):
        self.users = []
        self.total_bank_balance = 0
        self.total_loan_amount = 0
        self.loan_enabled = True


    def create_account(self, name, email, address, account_type):
        account_id = random.randint(100000, 999999)
        account = Account(account_id, name, email, address, account_type)
        self.users.append(account)
        return account_id

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                return True
        return False

    def user_account_number(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                return user
        return None

    def total_accounts(self):
        return self.users

    def total_balance(self):
        return sum(user.balance for user in self.users)

    def total_loan(self):
        return self.total_loan_amount

    def loan_system(self):
        self.loan_enabled = not self.loan_enabled





class Account:
    def __init__(self, account_id, name, email, address, account_type):
        self.account_number = account_id
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan_taken = 0
        self.loan_attempt = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited Successfully: {amount} USD")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdraw Amount Exceeded")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew Successfully: {amount} USD")

    def Balance(self):
        return self.balance

    def Ctransaction_history(self):
        return self.transaction_history


    def Loan(self, amount):
        if self.loan_attempt > 0 and self.balance >= amount:
            self.balance += amount
            self.loan_taken += amount
            self.loan_attempt -= 1
            self.transaction_history.append(f"Loan Amount: {amount} USD")
        elif not Bank().loan_enabled:  
            print("Bank loan system is disabled.")
        elif self.loan_attempt >= 2:
             print("You have already taken the maximum number of loans.")
        elif self.balance < amount:
            print("You don't have sufficient balance to take this loan.")
            
    def transfer(self, received_account, amount):
        recipient = Bank().user_account_number(received_account)
        if recipient:
            if self.balance >= amount:
                self.balance -= amount
                recipient.balance += amount
                self.transaction_history.append(f"Transferred {amount} USD to account {received_account}")
                recipient.transaction_history.append(f"Received {amount} USD from account {self.account_number}")
                print("Transfer successful!")
            else:
                print("Insufficient balance ")
        else:
            print("Recipient account does not exist.")





bank = Bank()





def admin():
    while True:
        print('\n******Admin Menu******')
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View Accounts")
        print("4. Check Total Loan Amount")
        print("5. Check Total Bank Balance")
        print("6. Loan System")
        print("7. Exit")

        admin_choice = input("Enter your choice: ")

        if admin_choice == '1':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            address = input("Enter customer address: ")
            account_type = input("Enter account type (Savings/Current): ")
            an = bank.create_account(name, email, address, account_type)
            print(f"Account created successfully. Account number: {an}")

        elif admin_choice == '2':
            account_number = int(input("Enter account number to delete: "))
            if bank.delete_account(account_number):
                print("Account deleted successfully.")
            else:
                print("Account not found.")

        elif admin_choice == '3':
            print("\nAll User Accounts:")
            for user in bank.total_accounts():
                print(f"Account Number: {user.account_number}, Name: {user.name}, Balance: {user.balance}, Account Type: {user.account_type}")

        elif admin_choice == '4':
            print(f"Total Loan Amount: {bank.total_loan()} USD")

        elif admin_choice == '5':
            print(f"Total Bank Balance: {bank.total_balance()} USD")

        elif admin_choice == '6':
            bank.loan_system()
            if bank.loan_enabled:
                print("Loan system enabled.")
            else:
                print("Loan system disabled.")

        elif admin_choice == '7':
            break

        else:
            print("Invalid choice")




def user_(account_number):
    user = bank.user_account_number(account_number)
    while True:
        print("\nUser Menu:")
        print("1. Deposit Amount")
        print("2. Withdraw Amount")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")

        choice_user = input("Enter your choice: ")

        if choice_user == '1':
            amount = float(input("Enter amount to deposit: "))
            user.deposit(amount)
            print("Amount deposited successfully.")

        elif choice_user == '2':
            amount = float(input("Enter amount to withdraw: "))
            user.withdraw(amount)

        elif choice_user == '3':
            print(f"Available Balance: {user.Balance()} USD")

        elif choice_user == '4':
            print("Transaction History:")
            for transaction in user.Ctransaction_history():
                print(transaction)

        elif choice_user == '5':
            amount = float(input("Enter amount to take as loan: "))
            user.Loan(amount)

        elif choice_user == '6':
            received_account = int(input("Enter recipient account number: "))
            amount = float(input("Enter amount to transfer: "))
            user.transfer(received_account, amount)

        elif choice_user == '7':
            break

        else:
            print("Invalid choice.")



#main 
while True:
    print("\nWelcome To The Bank Management System")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    choice = input("Enter Your Choice: ")
    if choice == '1':
        admin()
    elif choice == '2':
        account_number = int(input("Enter your account number: "))
        user_(account_number)
    elif choice == '3':
        break
    else:
        print("Invalid Choice.")
