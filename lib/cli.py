# lib/cli.py

from helpers import (
    exit_program,
    trader_data,
    initialization,
    portfolio_data,
    transaction_data
)

def main():
    initialization()

    while True:
        menu()
        choice = input("Select an option from the menu: ")
        if choice == "1":
            trader_data()
        elif choice == "2":
            portfolio_data()
        elif choice == "3":
            transaction_data()
        elif choice == "0":
            exit_program()
        else:
            print("\nInvalid option! Please select from the menu.")
            input("\nPress 'return' to continue...")

def menu():
    print("\nWelcome to the Trading Platform!\n")
    print("Main Menu:")
    print("1: Access Trader Data")
    print("2: Access Portfolio Data")
    print("3: Access Transaction Data")
    print("0: Exit the Platform\n")

if __name__ == "__main__":
    main()
