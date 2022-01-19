from AccountClass import *

def main():

    AMOUNT_OF_ACCOUNTS = 10
    accounts = []
    for i in range(AMOUNT_OF_ACCOUNTS):
        account = Account(id=i)
        accounts.append(account)

    keep_going = True
    while keep_going:

        user_id = int(input("Enter an id: "))

        choice = get_a_choice()

        if choice == 1:
            print(accounts[user_id].get_balance())
        elif choice == 2:
            amount_to_withdraw = float( input("Amount to withdraw: ") )
            accounts[user_id].withdraw(amount_to_withdraw)
        elif choice == 3:
            amount_to_deposit = float( input("Amount to deposit: ") )
            accounts[user_id].deposit(amount_to_deposit)
        else:
            print("Exiting")
            keep_going == False

def get_a_choice():
    while True:
        print("\nMain menu");
        print("1: check balance");
        print("2: withdraw");
        print("3: deposit");
        print("4: exit");
        print("Enter a choice: ", end = "");
        choice = int(input())
        if choice < 1 or choice > 4:
            print("Wrong choice, try again: ", end = "")
        else:
            break

    return choice

main()