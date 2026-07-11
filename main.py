from src.expense_tracker.add import add_expense
from src.expense_tracker.delete import delete_expense
from src.expense_tracker.show import show_expenses
from src.expense_tracker.summary import show_summary
from src.expense_tracker.update import update_expense
import argparse 

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    month_parser = argparse.ArgumentParser(add_help=False, conflict_handler="resolve")
    month_parser.add_argument(
        "--month", 
        type=int, 
        choices=range(1, 13), 
        help="Month number (1-12) to filter results"
    )

    parser_add = subparsers.add_parser("add", help="Add a new expense")
    parser_add.add_argument("--description", required=True, help="Expense description")
    parser_add.add_argument("--amount", type=float, required=True, help="Expense amount")  
    parser_add.set_defaults(func=add_expense)

    parser_list = subparsers.add_parser("list", parents=[month_parser], help="List expenses")
    parser_list.set_defaults(func=show_expenses)

    parser_update = subparsers.add_parser("update", help="Update an existing expense")
    parser_update.add_argument("--id", type=int, required=True, help="Expense ID to update")
    parser_update.add_argument("--description", help="New expense description")
    parser_update.add_argument("--amount", type=float, help="New expense amount")
    parser_update.set_defaults(func=update_expense)

    parser_delete = subparsers.add_parser("delete", help="Delete an expense")
    parser_delete.add_argument("--id", type=int, required=True, help="Expense ID")
    parser_delete.set_defaults(func=delete_expense)

    parser_summary = subparsers.add_parser("summary", parents=[month_parser], help="Show summary of expenses")
    parser_summary.set_defaults(func=show_summary)

    args = parser.parse_args()
    
    args.func(args)

if __name__ == "__main__":
    main()