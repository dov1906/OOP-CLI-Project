# lib/helpers.py

from models.trader import Trader
from models.portfolio import Portfolio
from models.transaction import Transaction

def initialization():
    Trader.create_table()
    Portfolio.create_table()
    Transaction.create_table()

def exit_program():
    print("Thank you for using the Trading Platform! Goodbye!")
    exit()

def trader_data():
    while True:
        trader_menu()
        choice = input("Select an option from the menu: ")
        if choice == "1":
            get_trader()
        elif choice == "2":
            create_trader()
        elif choice == "3":
            update_trader()
        elif choice == "4":
            delete_trader()
        elif choice == "5":
            get_trader_portfolios()
        elif choice == "6":
            list_all_traders()  
        elif choice == "0":
            break
        else:
            print("Invalid option! Please select from the menu.\n")

def trader_menu():
    print("\nTrader Menu:")
    print("1: Retrieve Trader Data")
    print("2: Add a New Trader")
    print("3: Update a Trader")
    print("4: Delete a Trader")
    print("5: Retrieve Trader's Portfolios")
    print("6: List All Traders")  
    print("0: Back to Main Menu\n")

def list_all_traders():
    print("\nAll Traders:")
    traders = Trader.get_all()
    for trader in traders:
        print(trader)
    input("\nPress 'return' to continue...")


def create_trader():
    name = input("Enter the Trader's Name: ")
    new_trader = Trader.create(name)
    print(f"\nNew Trader Created: {new_trader}")
    input("Press 'return' to continue...")

def get_trader():
    trader_id = int(input("Enter Trader ID to retrieve: "))
    trader = Trader.find_by_id(trader_id)
    if trader:
        print(f"\nTrader Details: {trader}")
    else:
        print("\nTrader not found.")
    input("Press 'return' to continue...")

def update_trader():
    trader_id = int(input("Enter Trader ID to update: "))
    trader = Trader.find_by_id(trader_id)
    if trader:
        new_name = input("Enter new name for Trader: ")
        trader.name = new_name
        trader.update()
        print(f"\nUpdated Trader: {trader}")
    else:
        print("\nTrader not found.")
    input("Press 'return' to continue...")

def delete_trader():
    trader_id = int(input("Enter Trader ID to delete: "))
    trader = Trader.find_by_id(trader_id)
    if trader:
        trader.delete()
        print("\nTrader deleted.")
    else:
        print("\nTrader not found.")
    input("Press 'return' to continue...")

def get_trader_portfolios():
    trader_id = int(input("Enter Trader ID to retrieve portfolios: "))
    trader = Trader.find_by_id(trader_id)
    if trader:
        print(f"\nPortfolios for Trader #{trader.id}:")
        for portfolio in trader.portfolios():
            print(portfolio)
    else:
        print("\nTrader not found.")
    input("Press 'return' to continue...")

def portfolio_data():
    while True:
        portfolio_menu()
        choice = input("Select an option from the menu: ")
        if choice == "1":
            get_portfolio()
        elif choice == "2":
            create_portfolio()
        elif choice == "3":
            update_portfolio()
        elif choice == "4":
            delete_portfolio()
        elif choice == "5":
            get_portfolio_transactions()
        elif choice == "6":
            list_all_portfolios() 
        elif choice == "0":
            break
        else:
            print("Invalid option! Please select from the menu.\n")

def portfolio_menu():
    print("\nPortfolio Menu:")
    print("1: Retrieve Portfolio Data")
    print("2: Add a New Portfolio")
    print("3: Update a Portfolio")
    print("4: Delete a Portfolio")
    print("5: Retrieve Portfolio's Transactions")
    print("6: List All Portfolios")  
    print("0: Back to Main Menu\n")

def list_all_portfolios():
    print("\nAll Portfolios:")
    portfolios = Portfolio.get_all()
    for portfolio in portfolios:
        print(portfolio)
    input("\nPress 'return' to continue...")


def create_portfolio():
    name = input("Enter Portfolio Name: ")
    trader_id = int(input("Enter Trader ID to link this portfolio to: "))
    Portfolio.create(name, trader_id)
    print("\nNew Portfolio Created.")
    input("Press 'return' to continue...")

def get_portfolio():
    portfolio_id = int(input("Enter Portfolio ID to retrieve: "))
    portfolio = Portfolio.find_by_id(portfolio_id)
    if portfolio:
        print(f"\nPortfolio Details: {portfolio}")
    else:
        print("\nPortfolio not found.")
    input("Press 'return' to continue...")

def update_portfolio():
    portfolio_id = int(input("Enter Portfolio ID to update: "))
    portfolio = Portfolio.find_by_id(portfolio_id)
    if portfolio:
        new_name = input("Enter new Portfolio Name: ")
        portfolio.name = new_name
        portfolio.update()
        print(f"\nUpdated Portfolio: {portfolio}")
    else:
        print("\nPortfolio not found.")
    input("Press 'return' to continue...")

def delete_portfolio():
    portfolio_id = int(input("Enter Portfolio ID to delete: "))
    portfolio = Portfolio.find_by_id(portfolio_id)
    if portfolio:
        portfolio.delete()
        print("\nPortfolio deleted.")
    else:
        print("\nPortfolio not found.")
    input("Press 'return' to continue...")

def get_portfolio_transactions():
    portfolio_id = int(input("Enter Portfolio ID to retrieve transactions: "))
    portfolio = Portfolio.find_by_id(portfolio_id)
    if portfolio:
        print(f"\nTransactions for Portfolio #{portfolio.id}:")
        for transaction in portfolio.transactions():
            print(transaction)
    else:
        print("\nPortfolio not found.")
    input("Press 'return' to continue...")

def transaction_data():
    while True:
        transaction_menu()
        choice = input("Select an option from the menu: ")
        if choice == "1":
            get_transaction()
        elif choice == "2":
            create_transaction()
        elif choice == "3":
            update_transaction()
        elif choice == "4":
            delete_transaction()
        elif choice == "5":
            list_all_transactions()  # New Option
        elif choice == "0":
            break
        else:
            print("Invalid option! Please select from the menu.\n")

def transaction_menu():
    print("\nTransaction Menu:")
    print("1: Retrieve Transaction Data")
    print("2: Add a New Transaction")
    print("3: Update a Transaction")
    print("4: Delete a Transaction")
    print("5: List All Transactions")  # New Option
    print("0: Back to Main Menu\n")

def list_all_transactions():
    print("\nAll Transactions:")
    transactions = Transaction.get_all()
    for transaction in transactions:
        print(transaction)
    input("\nPress 'return' to continue...")

def create_transaction():
    stock_index = input("Enter Stock Index: ")
    quantity = int(input("Enter Quantity: "))
    stock_price = float(input("Enter Stock Price: "))
    portfolio_id = int(input("Enter Portfolio ID: "))
    Transaction.create(stock_index, quantity, stock_price, portfolio_id)
    print("\nNew Transaction Created.")
    input("Press 'return' to continue...")

def get_transaction():
    transaction_id = int(input("Enter Transaction ID to retrieve: "))
    transaction = Transaction.find_by_id(transaction_id)
    if transaction:
        print(f"\nTransaction Details: {transaction}")
    else:
        print("\nTransaction not found.")
    input("Press 'return' to continue...")

def update_transaction():
    transaction_id = int(input("Enter Transaction ID to update: "))
    transaction = Transaction.find_by_id(transaction_id)
    if transaction:
        stock_index = input("Enter new Stock Index: ")
        quantity = int(input("Enter new Quantity: "))
        stock_price = float(input("Enter new Stock Price: "))
        transaction.stock_index = stock_index
        transaction.quantity = quantity
        transaction.stock_price = stock_price
        transaction.update()
        print(f"\nUpdated Transaction: {transaction}")
    else:
        print("\nTransaction not found.")
    input("Press 'return' to continue...")

def delete_transaction():
    transaction_id = int(input("Enter Transaction ID to delete: "))
    transaction = Transaction.find_by_id(transaction_id)
    if transaction:
        transaction.delete()
        print("\nTransaction deleted.")
    else:
        print("\nTransaction not found.")
    input("Press 'return' to continue...")
