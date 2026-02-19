import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "mustwatch.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def init_db():
    with sqlite3.connect(DB_PATH) as con:
        con.execute("""
        CREATE TABLE IF NOT EXISTS midias(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            tipo TEXT NOT NULL,
            indicado_por TEXT
        )
        """)
        con.commit()
