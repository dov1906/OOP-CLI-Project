from models.__init__ import CONN, CURSOR

class Portfolio:
    all = []
    
    def __init__(self, name, trader_id):
        self._name = name
        self._trader_id = trader_id
        self.id = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Portfolio name must be a string!")
        
    @property
    def trader_id(self):
        return self._trader_id

    @trader_id.setter
    def trader_id(self, value):
        from models.trader import Trader
        if isinstance(value, int) and Trader.find_by_id(value):
            self._trader_id = value
        else:
            raise ValueError("Trader ID must be a valid integer and exist in the database!")
   

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS portfolios (
                id INTEGER PRIMARY KEY,
                name TEXT,
                trader_id INTEGER,
                FOREIGN KEY(trader_id) REFERENCES traders(id)
            )
        """
        CURSOR.execute(sql) 
        
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS portfolios
        """
        CURSOR.execute(sql)
        

    @classmethod
    def instance_from_db(cls, row):
        portfolio = cls(row[1], row[2])
        portfolio.id = row[0]
        return portfolio
    
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM portfolios WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM portfolios
        """
        rows = CURSOR.execute(sql).fetchall()
        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    def save(self):
        sql = """
            INSERT INTO portfolios (name, trader_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.trader_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        Portfolio.all.append(self)

        
    @classmethod
    def create(cls, name, trader_id):
        portfolio = cls(name, trader_id)
        portfolio.save()
        return portfolio
    
    
    def transactions(self):
        from models.transaction import Transaction
        sql = """
            SELECT * FROM transactions WHERE portfolio_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Transaction.instance_from_db(row) for row in rows]
    
    def delete(self):
        sql = """
            DELETE FROM portfolios WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        Portfolio.all = [portfolio for portfolio in Portfolio.all if portfolio.id != self.id]
    
    def __repr__(self):
        return f"<Portfolio #{self.id}: Name = {self.name}, Trader ID = {self.trader_id}>"