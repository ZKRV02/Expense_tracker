from .storage import load_expenses
import calendar

def show_summary(args):
    expenses = load_expenses()
    summary = 0.0
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

    for i in expenses:
        amount_val = i.get("AMOUNT", 0)
        if isinstance(amount_val, str) and amount_val.startswith('$'):
            summary += float(amount_val[1:])
        else:
            summary += float(amount_val)
    if month_filter is None:
        print(f"Total expenses: ${summary:.2f}")
    else:
        month_name = calendar.month_name[month_filter]
        print(f"Total expenses for {month_name}: ${summary:.2f}")