
try:
    balance = int(input("Enter Account Balance: "))

    if balance <= 0:
        print("Error: Balance must be greater than zero.")

    else:
        withdraw = int(input("Enter withdrawal amount: "))

        if withdraw <= 0:
            print("Error: Withdrawal amount must be greater than zero.")

        elif withdraw > balance:
            print("Error: Insufficient balance.")

        else:
            amount = balance - withdraw

            if amount < 500:
                print("Error: Minimum balance of ₹500 must be maintained.")

            else:
                print("Status: Withdrawal successful!")

                if amount == 500:
                    print("Minimum balance reached!")

                print("----------- ATM Transaction Report -----------")
                print("Previous Balance  :", balance)
                print("Withdrawal Amount :", withdraw)
                print("Remaining Balance:", amount)

                print("ATM transaction completed successfully.")

except ValueError:
    print("Error: Enter a valid number.")

finally:
    print("ATM transaction process ended.")