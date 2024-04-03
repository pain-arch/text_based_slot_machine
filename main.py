MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5


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

def number_of_lines():
    while True:
        lines = input("Enter the number of Lines you want to play (1 - "+str(MAX_LINES) +"):")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("the number of the lines should be between 1 and " + str(MAX_LINES))
        else:
            print("Invalid number of lines, please entere a valid number of lines.")
    return lines  

def main():
    balance = deposit()
    lines = number_of_lines()

    print("you have deposited $", balance , "and you are playing", lines, "lines.")

main()                      