from .storage import load_expenses, save_expenses

def delete_expense(args):
    expense_id = args.id
    
    expenses = load_expenses()
    updated_expenses = [i for i in expenses if i["ID"] != expense_id]

    if len(updated_expenses) != len(expenses):
        save_expenses(updated_expenses)
        print(f"# Expense with id {expense_id} deleted successfully")
    else:
        print(f"# Expense with id {expense_id} not found")