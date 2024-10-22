#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.trader import Trader
from models.portfolio import Portfolio
from models.stock import Stock

def seed_database():

    Stock.drop_table()
    Portfolio.drop_table()
    Trader.drop_table()

    Stock.create_table()
    Portfolio.create_table()
    Trader.create_table()

    apple = Stock.create("AAPL", "Apple", 150.00)
    google = Stock.create("GOOGL", "Google", 2800.00)
    tesla = Stock.create("TSLA", "Tesla", 850.00)

    tech_portfolio = Portfolio.create("Tech Portfolio")
    energy_portfolio = Portfolio.create("Energy Portfolio")

    john = Trader.create("John Doe")
    jane = Trader.create("Jane Smith")

    john.portfolios.append(tech_portfolio)
    jane.portfolios.append(energy_portfolio)

    tech_portfolio.add_stock(apple, 10) 
    tech_portfolio.add_stock(google, 5)
    energy_portfolio.add_stock(tesla, 7)

seed_database()
print("🌱 Traders, Portfolios, and Stocks successfully seeded! 🌱")
