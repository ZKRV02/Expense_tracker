from .storage import load_expenses, save_expenses

def update_expense(args):
    expenses = load_expenses()
    expense_found = False

    for item in expenses:
        if item.get("ID") == args.id: 
            if args.amount is not None:
                item["AMOUNT"] = args.amount
            if args.description is not None:
                item["DESCRIPTION"] = args.description
            expense_found = True
            break 

    if expense_found:
        save_expenses(expenses)
        print(f"# Expense with id {args.id} updated successfully")
    else:
        print(f"# Expense with id {args.id} not found")