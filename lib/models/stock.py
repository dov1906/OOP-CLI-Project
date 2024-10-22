from models.__init__ import CONN, CURSOR

class Stock:
    all = []
    
    def __init__(self, stock_index, name, price):
        self._stock_index = stock_index
        self._name = name
        self._price = price
        self.id = None
        
    @property
    def stock_index(self):
        return self._stock_index

    @stock_index.setter
    def stock_index(self, value):
        if isinstance(value, str):
            self._stock_index = value
        else:
            raise ValueError("Stock index must be a string!")
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string!")

        
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)):
            self._price = value
        else:
            raise ValueError("Price must be a number!")
    
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS stocks (
                id INTEGER PRIMARY KEY,
                stock_index TEXT,
                name TEXT,
                price REAL
            )
        """
        CURSOR.execute(sql)


    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS stocks
        """
        CURSOR.execute(sql)
    
    @classmethod
    def instance_from_db(cls, row):
        stock = cls(row[1], row[2], row[3])
        stock.id = row[0]
        return stock
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM stocks WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM stocks
        """
        rows = CURSOR.execute(sql).fetchall()
        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    def save(self):
        sql = """
            INSERT INTO stocks (stock_index, name, price)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.stock_index, self.name, self.price))
        CONN.commit()
        self.id = CURSOR.lastrowid
        Stock.all.append(self)
        
        
    @classmethod
    def create(cls, stock_index, name, price):
        stock = cls(stock_index, name, price)
        stock.save()
        return stock
    
    
    def delete(self):
        sql = """
            DELETE FROM stocks WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        Stock.all = [stock for stock in Stock.all if stock.id != self.id]
        
    
    def portfolios(self):
        from models.portfolio import Portfolio
        sql = """
            SELECT portfolios.* FROM portfolios
            JOIN portfolio_stocks ON portfolios.id = portfolio_stocks.portfolio_id
            WHERE portfolio_stocks.stock_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Portfolio.instance_from_db(row) for row in rows]
    
    
    def __repr__(self):
        return f"<Stock #{self.id}: Name = {self.name}, Index = {self.stock_index}, Price = {self.price}>"