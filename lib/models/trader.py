from models.__init__ import CONN, CURSOR

class Trader:
    all = []
    
    def __init__(self, name):
        self.name = name
        self.id = None
        self.portfolios = []  # Each trader has multiple portfolios
        Trader.all.append(self)