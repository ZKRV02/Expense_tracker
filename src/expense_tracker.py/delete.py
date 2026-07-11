from storage import load_expenses, save_expenses

def delete_expense(expense_id):
    expenses = load_expenses()
    updated_expenses = [i for i in expenses if i["ID"] != expense_id]

    if len(updated_expenses) != len(expenses):
        save_expenses(updated_expenses)
        return f"# Expense with id {expense_id} deleted successfully"
    return f"# Expense with id {expense_id} not found"
