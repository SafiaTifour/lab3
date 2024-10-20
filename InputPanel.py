from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class InputPanel(QWidget):
    def __init__(self, add_expense_callback, parent=None):
        super().__init__(parent)
        self.add_expense_callback = add_expense_callback
        self.init_ui()

    def init_ui(self):
        self.layout = QHBoxLayout(self)

        self.expense_label = QLabel("Expense:")
        self.expense_input = QLineEdit()
        self.expense_input.setFixedWidth(150)

        self.price_label = QLabel("Price:")
        self.price_input = QLineEdit()
        self.price_input.setFixedWidth(100)

        self.add_button = QPushButton("Add Expense")
        self.add_button.clicked.connect(self.validate_and_add_expense)

        # Add widgets to the layout
        self.layout.addWidget(self.expense_label)
        self.layout.addWidget(self.expense_input)
        self.layout.addWidget(self.price_label)
        self.layout.addWidget(self.price_input)
        self.layout.addWidget(self.add_button)

    def validate_and_add_expense(self):
        expense_name = self.expense_input.text().strip()
        price_text = self.price_input.text().strip()

        if not expense_name:
            QMessageBox.warning(self, "Input Error", "Expense name cannot be empty.", QMessageBox.Ok)
            return

        try:
            price = float(price_text)
            if price < 0:
                raise ValueError("Price cannot be negative.")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid price.", QMessageBox.Ok)
            return

        self.add_expense_callback(expense_name, price_text)
