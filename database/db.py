import sqlite3


DB_NAME = "database/users.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_tables():
    db = connect_db()
    cursor = db.cursor()

    # جدول کاربران و کیف پول
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        balance INTEGER DEFAULT 0
    )
    """)

    # جدول سفارش‌ها
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        service TEXT,
        amount INTEGER,
        status TEXT DEFAULT 'pending'
    )
    """)

    db.commit()
    db.close()


def add_user(user_id):
    db = connect_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
        (user_id,)
    )

    db.commit()
    db.close()


def get_balance(user_id):
    db = connect_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )

    result = cursor.fetchone()

    db.close()

    if result:
        return result[0]

    return 0


def add_balance(user_id, amount):
    db = connect_db()
    cursor = db.cursor()

    cursor.execute(
        """
        UPDATE users
        SET balance = balance + ?
        WHERE user_id=?
        """,
        (amount, user_id)
    )

    db.commit()
    db.close()


def remove_balance(user_id, amount):
    db = connect_db()
    cursor = db.cursor()

    cursor.execute(
        """
        UPDATE users
        SET balance = balance - ?
        WHERE user_id=?
        """,
        (amount, user_id)
    )

    db.commit()
    db.close()


def create_order(user_id, service, amount):
    db = connect_db()
    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO orders (user_id, service, amount)
        VALUES (?, ?, ?)
        """,
        (user_id, service, amount)
    )

    db.commit()
    db.close()
