balance = 10000

while True:
    choice = input("1.Check 2.Deposit 3.Withdraw 4.Exit\nEnter choice: ")

    if choice == "1":
        print(f"Current Balance: n{balance}")
    elif choice == "2":
        balance += int(input("Enter deposit amount: "))
        print(f"Updated Balance: n{balance}")
    elif choice == "3":
        amount = int(input("Enter withdrawal amount: "))
        if amount > balance:
            print(f"Transaction failed: Insufficient balance.\nCurrent Balance: n{balance}")
        else:
            balance -= amount
            print(f"Updated Balance: n{balance}")
    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        break