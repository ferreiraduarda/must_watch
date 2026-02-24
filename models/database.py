import os
from sqlite3 import connect
from dotenv import load_dotenv

load_dotenv()

# DB_PATH = os.path.join(os.path.dirname(__file__), "mustwatch.db")
# os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
DB_PATH = os.getenv('DATABASE', './data/mustwatch.db')

def init_db(db_name: str = DB_PATH) -> None:
    with connect(db_name) as conn:
# def init_db():
#     with sqlite3.connect(DB_PATH) as con:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS midias(
            id_midia INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            tipo TEXT NOT NULL,
            indicado_por TEXT
        )
        """)
        conn.commit()
