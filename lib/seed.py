#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.trader import Trader
from models.portfolio import Portfolio
from models.transaction import Transaction

def seed_database():

    Transaction.drop_table()
    Portfolio.drop_table()
    Trader.drop_table()

    Trader.create_table()
    Portfolio.create_table()
    Transaction.create_table()

    Trader.create("John Doe")
    Trader.create("Jane Smith")
    Trader.create("Alice Johnson")

    Portfolio.create("Tech Portfolio", 1)  
    Portfolio.create("Energy Portfolio", 2)  
    Portfolio.create("Growth Portfolio", 1)  
    Portfolio.create("Dividend Portfolio", 3)  

    Transaction.create("AAPL", 10, 150.00, 1)  # 10 shares of Apple at $150 each, linked to Tech Portfolio (ID = 1)
    Transaction.create("GOOGL", 5, 2800.00, 1) 
    Transaction.create("TSLA", 7, 850.00, 2)  
    Transaction.create("AMZN", 15, 3300.00, 3)  
    Transaction.create("XOM", 20, 90.00, 4)  
    Transaction.create("AAPL", 50, 145.00, 2)  

    print("Traders:")
    for trader in Trader.get_all():
        print(trader)

    print("\nPortfolios:")
    for portfolio in Portfolio.get_all():
        print(portfolio)

    print("\nTransactions:")
    for transaction in Transaction.get_all():
        print(transaction)

seed_database()
print("🌱 Database successfully seeded with Traders, Portfolios, and Transactions! 🌱")
