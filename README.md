# Expense Tracker CLI

A simple and efficient command-line Expense Tracker built with Python. It allows you to add, delete, update, and view expenses, as well as generate analytical summaries for all time or filtered by a specific month.

Your data is automatically saved in JSON format in your home directory (`~/.expense_tracker_data.json`), making the tool globally accessible from anywhere in your terminal.

## 🚀 Installation

1. Clone the repository or navigate to the project directory:
   ```bash
   cd expense-tracker-cli
Install the project in editable mode. This will automatically install the tabulate dependency and register the expense-tracker command globally:

Bash
pip install -e .
💻 Usage
Once installed, you can invoke the utility directly using the expense-tracker command.

1. Add an Expense (add)
Adds a new expense with a description and an amount. The ID is generated automatically.

Bash
expense-tracker add --description "Lunch at cafe" --amount 15.50
expense-tracker add --description "Book purchase" --amount 42
2. List Expenses (list)
Displays a clean, structured table of all your expenses.

Bash
expense-tracker list
You can filter expenses for a specific month using the --month flag (a number from 1 to 12):

Bash
expense-tracker list --month 7
3. Update an Expense (update)
Modifies the description and/or the amount of an existing expense by its ID.

Bash
# Update both description and amount:
expense-tracker update --id 1 --description "Business lunch" --amount 18.00

# Update only the amount:
expense-tracker update --id 1 --amount 20.00
4. Expense Summary (summary)
Shows the total sum of all expenses combined:

Bash
expense-tracker summary
Or shows the total summary filtered for a specific month:

Bash
expense-tracker summary --month 7
5. Delete an Expense (delete)
Removes an expense record from the database using its ID.

Bash
expense-tracker delete --id 1
🛠️ Tech Stack
Python 3.9+

Argparse — For parsing command-line interfaces

Tabulate — For rendering beautiful tables in the terminal

JSON — Used as a lightweight data storage mechanism
