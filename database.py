import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Lokesh@2910",
        database="expense_db"#it hasnt changed yet so i am doing this commit again
    )

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            item VARCHAR(255),
            category VARCHAR(100),
            amount FLOAT,
            date VARCHAR(50)
        )
    """)
    conn.commit()
    conn.close()

def add_expense(item, category, amount, date):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO expenses (item, category, amount, date) VALUES (%s, %s, %s, %s)",
              (item, category, amount, date))
    conn.commit()
    conn.close()

def get_expenses():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    rows = c.fetchall()
    conn.close()
    return rows
