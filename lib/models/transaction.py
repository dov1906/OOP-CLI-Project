from models.__init__ import CONN, CURSOR

class Transaction:
    all = []

    def __init__(self, stock_index, quantity, stock_price, portfolio_id):
        self.stock_index = stock_index
        self.quantity = quantity
        self.stock_price = stock_price
        self.total_amount = stock_price * quantity
        self.portfolio_id = portfolio_id
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
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, int) and value > 0:
            self._quantity = value
        else:
            raise ValueError("Quantity must be a positive integer!")

    @property
    def stock_price(self):
        return self._stock_price

    @stock_price.setter
    def stock_price(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._stock_price = value
        else:
            raise ValueError("Stock price must be a positive number!")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                stock_index TEXT,
                quantity INTEGER,
                stock_price REAL,
                total_amount REAL,
                portfolio_id INTEGER,
                FOREIGN KEY(portfolio_id) REFERENCES portfolios(id)
            )
        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS transactions;
        """
        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO transactions (stock_index, quantity, stock_price, total_amount, portfolio_id)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.stock_index, self.quantity, self.stock_price, self.total_amount, self.portfolio_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        Transaction.all.append(self)

    @classmethod
    def create(cls, stock_index, quantity, stock_price, portfolio_id):
        transaction = cls(stock_index, quantity, stock_price, portfolio_id)
        transaction.save()
        return transaction

    @classmethod
    def instance_from_db(cls, row):
        transaction = cls(row[1], row[2], row[3], row[5])
        transaction.total_amount = row[4]
        transaction.id = row[0]
        return transaction

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM transactions
        """
        rows = CURSOR.execute(sql).fetchall()
        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM transactions WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def __repr__(self):
        return f"<Transaction #{self.id}: Stock = {self.stock_index}, Quantity = {self.quantity}, Total Amount = {self.total_amount}>"
