from models.__init__ import CONN, CURSOR

class Portfolio:
    all = []
    
    def __init__(self, name):
        self.name = name
        self.id = None
        Portfolio.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) == str:
            self._name = value
        else:
            raise TypeError("Name must be a string!")
        
   
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS portfolios (
                id INTEGER PRIMARY KEY,
                name TEXT
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
        portfolio = cls(row[1])
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
            INSERT INTO portfolios (name) VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        Portfolio.all.append(self)
        
    @classmethod
    def create(cls, name):
        portfolio = cls(name)
        portfolio.save()
        return portfolio
    
    def delete(self):
        sql = """
            DELETE FROM portfolios WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        Portfolio.all = [portfolio for portfolio in Portfolio.all if portfolio.id != self.id]
    
    def __repr__(self):
        return f"<Portfolio {self.name}>"

    
    