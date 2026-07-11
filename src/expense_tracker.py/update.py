from storage import load_expenses, save_expenses

def update_expense(expense_id, amount=None, description=None):
        expenses = load_expenses()
        expense_found = False

        for item in expenses:
            if item.get("ID") == expense_id: 
                if amount is not None:
                    item["AMOUNT"] = amount
                if description is not None:
                    item["DESCRIPTION"] = description
                expense_found = True
                break 

        if expense_found:
                save_expenses(expenses)
                return f"# Expense with id {id} updated successfully"
        else:
            return f"# Expense with id {id} not found"