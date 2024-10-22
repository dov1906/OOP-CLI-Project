from models.__init__ import CONN, CURSOR

class Trader:
    all = []
    
    def __init__(self, name):
        self.name = name
        self.id = None
        Trader.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Trader's name must be a string!")
        

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS traders (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS traders
        """
        CURSOR.execute(sql)
    
    
    @classmethod
    def instance_from_db(cls, row):
        trader = cls(row[1])
        trader.id = row[0]
        return trader
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM traders WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM traders
        """
        rows = CURSOR.execute(sql).fetchall()
        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    def save(self):
        sql = """
            INSERT INTO traders (name) VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        Trader.all.append(self)


    @classmethod
    def create(cls, name):
        trader = cls(name)
        trader.save()
        return trader
    
    def delete(self):
        sql = """
            DELETE FROM traders WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        Trader.all = [trader for trader in Trader.all if trader.id != self.id]
        
    def portfolios(self):
        from models.portfolio import Portfolio
        sql = """
            SELECT * FROM portfolios WHERE trader_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Portfolio.instance_from_db(row) for row in rows]
        
    

    def __repr__(self):
        return f"<Trader {self.name}>"
