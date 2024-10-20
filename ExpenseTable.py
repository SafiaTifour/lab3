from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from Database import Database

class ExpenseTable(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["Expense", "Price"])
        

        # Initialize the database
        self.db = Database()
        self.load_expenses()

 
    def load_expenses(self):
        expenses = self.db.get_all_expenses()
        self.setRowCount(len(expenses))
        for row, (expense_name, price) in enumerate(expenses):
            self.setItem(row, 0, QTableWidgetItem(expense_name))
            self.setItem(row, 1, QTableWidgetItem(str(price)))

    def add_expense(self, expense_name, price_text):
        price = float(price_text)
        self.db.add_expense(expense_name, price)
        
        # Update the table view
        row_position = self.rowCount()
        self.insertRow(row_position)
        self.setItem(row_position, 0, QTableWidgetItem(expense_name))
        self.setItem(row_position, 1, QTableWidgetItem(price_text))
        
    def remove_expense(self, row_position):
        """Remove an expense from the table and database."""
        expense_id_item = self.item(row_position, 0)  
        if expense_id_item:
         expense_id = int(expense_id_item.text())
         # Call the database's delete_expense method
         Database.delete_expense(expense_id)
    
          # Remove the row from the table
         self.removeRow(row_position)


    def calculate_total(self):
        return self.db.calculate_total()
