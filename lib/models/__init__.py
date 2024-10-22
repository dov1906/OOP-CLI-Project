import sqlite3

CONN = sqlite3.connect('trading_platform.db')
CURSOR = CONN.cursor()