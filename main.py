import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def get_slot_machine_spin():
    all_symbols = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)




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


def bet_amount():
    while True:
        amount = input("Enter the amount you want to Bet: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The amount must be between ${MIN_BET} - ${MAX_BET} ")
        else:
            print("Invalid ammount, please enter a valid amount")

    return amount 


def main():
    balance = deposit()
    lines = number_of_lines()
    betting_amount = bet_amount()
    print("you have deposited $", balance , "and you are playing", lines, "lines." "and you are betting $", betting_amount, "per line")

main()                      