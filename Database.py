import sqlite3

class Database:
    def __init__(self, db_name="expenses.db"):
        """Initialize the database and create the expenses table if it doesn't exist."""
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create the expenses table if it does not already exist."""
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    expense_name TEXT NOT NULL,
                    price REAL NOT NULL
                )
            """)

    def add_expense(self, expense_name, price):
        """Add a new expense to the database."""
        with self.connection:
            self.connection.execute(
                "INSERT INTO expenses (expense_name, price) VALUES (?, ?)",
                (expense_name, price)
            )
    def delete_expense(self, expense_id):
        """Delete an expense from the database by its ID."""
        with self.connection:
          self.connection.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

            
    def get_all_expenses(self):
        """Retrieve all expenses from the database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT expense_name, price FROM expenses")
        return cursor.fetchall()

    def calculate_total(self):
        """Calculate the total of all expenses in the database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT SUM(price) FROM expenses")
        return cursor.fetchone()[0] or 0.0

    def close(self):
        """Close the database connection."""
        self.connection.close()
