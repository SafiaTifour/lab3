import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from MenuBar import MenuBar
from InputPanel import InputPanel
from ExpenseTable import ExpenseTable
from TotalPanel import TotalPanel
from Database import Database

class ExpenseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 600, 300)

        self.init_ui()
        self.db = Database()

    def init_ui(self):
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        self.setMenuBar(MenuBar(self))

        self.input_panel = InputPanel(self.add_expense)
        layout.addWidget(self.input_panel)

        self.expense_table = ExpenseTable(self)
        layout.addWidget(self.expense_table)

        self.total_panel = TotalPanel(self)
        layout.addWidget(self.total_panel)

        # Create and add the delete button
        self.delete_button = QPushButton("Delete Expense")
        self.delete_button.clicked.connect(self.delete_expense)
        layout.addWidget(self.delete_button)

        self.update_total()

    def add_expense(self, expense_name, price_text):
        self.expense_table.add_expense(expense_name, price_text)
        self.input_panel.expense_input.clear()
        self.input_panel.price_input.clear()
        self.update_total()

    def delete_expense(self):
        selected_row = self.expense_table.currentRow() 
        if selected_row >= 0: 
            self.expense_table.remove_expense(selected_row)
            self.update_total()  

    def update_total(self):
        total = self.expense_table.calculate_total()
        self.total_panel.update_total(total)

    def closeEvent(self, event):
        self.db.close()  # Close the database connection on exit
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseApp()
    window.show()
    sys.exit(app.exec_())
