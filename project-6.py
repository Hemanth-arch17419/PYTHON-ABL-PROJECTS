#ATM Transaction Simulation
balance = float(input("Enter opening balance: "))

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance = balance + amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))

        if amount > balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid amount")
        elif amount > 10000:
            print("Withdrawal limit exceeded")
        else:
            balance = balance - amount
            print("Withdrawal successful")

    elif choice == "3":
        print("Balance =", balance)

    elif choice == "4":
        print("Thank you")
        break

    else:
        print("Invalid choice")