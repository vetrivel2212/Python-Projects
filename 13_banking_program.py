def show_balance(balance):
    print(f"\n💰 Your Current Balance: ₹{balance}\n")


def deposit():
    try:
        amount = int(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("⚠️ Amount must be greater than 0\n")
            return 0
        return amount
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.\n")
        return 0


def withdraw(balance):
    try:
        amount = int(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("⚠️ Amount must be greater than 0\n")
            return 0
        elif amount > balance:
            print("❌ Insufficient Funds!\n")
            return 0
        return amount
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.\n")
        return 0


def main():
    is_running = True
    balance = 0
    while is_running:
        print("****************************************")
        print("🏦 WELCOME TO PYTHON BANK 🏦")
        print("1️⃣  Show Balance")
        print("2️⃣  Deposit")
        print("3️⃣  Withdraw")
        print("4️⃣  Exit")
        print("****************************************")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            amt = deposit()
            balance += amt
            if amt > 0:
                print(f"✅ Deposited ₹{amt} successfully!\n")

        elif choice == '3':
            amt = withdraw(balance)
            balance -= amt
            if amt > 0:
                print(f"✅ Withdrawn ₹{amt} successfully!\n")

        elif choice == '4':
            print("\n👋 Thank you for using Python Bank. Have a nice day!\n")
            is_running = False

        else:
            print("❌ Invalid Choice. Please enter 1, 2, 3, or 4.\n")


if __name__ == '__main__':
    main()
