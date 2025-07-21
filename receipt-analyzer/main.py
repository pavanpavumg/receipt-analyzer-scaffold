from backend.database import init_db, insert_receipt

if __name__ == "__main__":
    try:
        init_db()
        insert_receipt({
            'vendor': 'Flipkart',
            'amount': 499.50,
            'date': '2025-07-20',
            'category': 'Books'
        })
        print("Receipt added.")
    except Exception as e:
        print(f"Error: {e}")