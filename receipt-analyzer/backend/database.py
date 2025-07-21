import sqlite3
import os

DB_PATH = 'data/receipts.db'

def init_db():
    os.makedirs('data', exist_ok=True)  # ✅ Make sure the 'data' folder exists
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS receipts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vendor TEXT,
            amount REAL,
            date TEXT,
            category TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_receipt(data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO receipts (vendor, amount, date, category)
        VALUES (?, ?, ?, ?)
    ''', (data['vendor'], data['amount'], data['date'], data.get('category')))
    conn.commit()
    conn.close()

def get_all_receipts():
    conn = sqlite3.connect('data/receipts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT vendor, amount, date, category FROM receipts")
    rows = cursor.fetchall()
    conn.close()
    return [
        {'vendor': r[0], 'amount': r[1], 'date': r[2], 'category': r[3]}
        for r in rows
    ]
