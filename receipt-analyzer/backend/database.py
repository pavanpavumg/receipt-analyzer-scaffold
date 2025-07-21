import sqlite3
import os
from contextlib import contextmanager

DB_PATH = 'data/receipts.db'

@contextmanager
def get_db_connection():
    """Context manager for database connections."""
    # Ensure the directory for the database exists.
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    """Initializes the database and creates the receipts table if it doesn't exist."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS receipts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vendor TEXT,
                amount REAL,
                date TEXT,
                category TEXT
            )
        ''')
        conn.commit()

def insert_receipt(data):
    """Inserts a receipt record into the database."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO receipts (vendor, amount, date, category)
            VALUES (?, ?, ?, ?)
        ''', (data.get('vendor'), data.get('amount'), data.get('date'), data.get('category')))
        conn.commit()
