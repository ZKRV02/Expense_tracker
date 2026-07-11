# Expense Tracker CLI

A lightweight command-line tool to manage your daily expenses. It automatically saves everything to a JSON file (`~/.expense_tracker_data.json`) in your home directory so you can use it anywhere.

### 🚀 Quick Start

1. Clone project from repository
   ```bash
   clone https://github.com/ZKRV02/Expense_tracker
   ```

2. Navigate to the project folder:
   ```bash
   cd expense-tracker-cli
   ```
3. Install it globally in development mode:
    ```bash
    pip install -e .
    ```
💻 How to Use
After installation, run the tool using the expense-tracker command followed by an action:

**Add a new expense:**
```bash
expense-tracker add --description "Lunch at cafe" --amount 15.50
```

**View all expenses (renders a clean table):**
```bash
expense-tracker list
```

**Filter expenses by month (numbers from 1 to 12)**
```bash
expense-tracker list --month 7
```

**Update an expense (change description, amount, or both by ID)**
```bash
expense-tracker update --id 1 --description "Business lunch" --amount 18.00
```

**Get a budget summary (total spend for all time or a specific month)**
```bash
expense-tracker summary
```
```bash
expense-tracker summary --month 7
```

Delete an expense
```bash
expense-tracker delete --id 1
```

🛠️ Built With
Python 3.9+ & Argparse for the CLI structure

Tabulate for clean terminal tables

JSON for zero-configuration data storage
