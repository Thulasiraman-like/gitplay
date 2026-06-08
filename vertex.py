class ATM:
    def __init__(self):
        self.balance = 10000

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Amount Withdrawn")

atm = ATM()

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        atm.check_balance()

    elif choice == "2":
        amount = int(input("Enter amount: "))
        atm.deposit(amount)

    elif choice == "3":
        amount = int(input("Enter amount: "))
        atm.withdraw(amount)

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")