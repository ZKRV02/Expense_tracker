from datetime import datetime
from storage import load_expenses, save_expenses

def add_expense(amount, description=None):
    expenses = load_expenses()

    new_id = max([t["ID"] for t in expenses], default=0) + 1
    date = datetime.now().strftime("%d.%m.%Y")

    expense = {
        "ID": new_id,
        "DATE": date,
        "DESCRIPTION": description,
        "AMOUNT": amount
    }
    expenses.append(expense)
    save_expenses(expenses)

    return f"# Expense added successfully (ID: {new_id})"
