def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount can't be neagative or 0 ")
        else:
            print("Invalid ammount, please enter a valid amount")

    return amount 

deposit_amount = deposit()
print("you have deposited $", deposit_amount,"to your account.")