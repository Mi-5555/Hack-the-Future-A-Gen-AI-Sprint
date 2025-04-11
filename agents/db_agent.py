import sqlite3

class DBAgent:
    def __init__(self, db_path="data/ecomm_dataset.sqlite"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def fetch_customer_profile(self, customer_id):
        self.cursor.execute("SELECT * FROM customers WHERE id=?", (customer_id,))
        return self.cursor.fetchone()

    def update_customer_profile(self, customer_id, new_data):
        self.cursor.execute("UPDATE customers SET profile=? WHERE id=?", (new_data, customer_id))
        self.conn.commit()

    def fetch_all_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def fetch_product(self, product_id):
        self.cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
        return self.cursor.fetchone()

    def insert_feedback(self, customer_id, product_id, score):
        self.cursor.execute("INSERT INTO feedback (customer_id, product_id, score) VALUES (?, ?, ?)",
                            (customer_id, product_id, score))
        self.conn.commit()
