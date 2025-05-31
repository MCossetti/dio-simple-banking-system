menu = """
Choose an operation to perform:

[d] Deposit
[w] Withdraw
[s] Statement
[q] Quit

=> """

balance = 0
limit = 500
statement = ""
number_of_withdrawals = 0
WITHDRAWAL_LIMIT = 3

while True:

    option = input(menu)

    if option == "d":
        amount = float(input("Enter the deposit amount: "))

        if amount > 0:
            balance += amount
            statement += f"Deposit: $ {amount:.2f}\n"
            print(f"Deposit of $ {amount:.2f} completed successfully!")
        
        else:
            print("Operation failed! The amount entered is invalid.")
    
    elif option == "w":
        amount = float(input("Enter the withdrawal amount: "))

        exceeded_limit = amount > limit
        exceeded_balance = amount > balance
        exceeded_withdrawals = number_of_withdrawals >= WITHDRAWAL_LIMIT

        if exceeded_limit:
            print(f"Operation failed! The withdrawal amount exceeds the limit of $ {limit:.2f}.")
        
        elif exceeded_balance:
            print(f"Operation failed! You do not have enough balance to withdraw $ {amount:.2f}.")
        
        elif exceeded_withdrawals:
            print(f"Operation failed! Maximum number of daily withdrawals ({WITHDRAWAL_LIMIT}) exceeded.")
        
        elif amount > 0:
            balance -= amount
            statement += f"Withdrawal: $ {amount:.2f}\n"
            number_of_withdrawals += 1
            print(f"Withdrawal of $ {amount:.2f} completed successfully!")
        else:
            print("Operation failed! The amount entered is invalid.")

    elif option == "s":
        print("\n================ STATEMENT ================")
        if not statement:
            print("No transactions have been made.")
        
        else:
            print(statement)
        print(f"\nBalance: $ {balance:.2f}")
        print("==========================================")
    
    elif option == "q":
        break

    else:
        print("Invalid operation! Please select a valid option.")
