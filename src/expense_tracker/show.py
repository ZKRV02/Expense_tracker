import calendar
from tabulate import tabulate
from .storage import load_expenses

def show_expenses(args):
    expenses = load_expenses()
    month_filter = args.month

    if month_filter is not None:
        filtered_expenses = []
        for s in expenses:
            try:
                expense_month = int(s['DATE'].split(".")[1])
                if expense_month == month_filter:
                    filtered_expenses.append(s)
            except (IndexError, ValueError):
                continue
        expenses = filtered_expenses
    if not expenses:
        if month_filter:
            month_name = calendar.month_name[month_filter]
            print(f"# No expenses found for {month_name}.")
        else:
            print("# Expense list is empty.")
        return

    print(tabulate(expenses, headers="keys"))