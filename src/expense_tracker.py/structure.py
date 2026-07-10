import json
from datetime import datetime
from pathlib import Path


HOME_DIR = Path.home()
DATA_FILE = HOME_DIR / ".expense_tracker_data.json"

class ExpenseTracker:
    def __init__(self, amount, description=None, id=None):
        self.id = id
        self.description = description
        self.amount = amount

    def add_expense(self):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                expenses = json.load(file)
                if not isinstance:
                    expenses = []
        except (FileNotFoundError, json.JSONDecodeError):
            expenses = []
        
        new_id = max([t["ID"] for t in expenses], default=0) + 1

        date = datetime.now().strftime("%d.%m.%Y")

        expense = {
            "ID": new_id,
            "DATE": date,
            "DESCRIPTION": self.description,
            "AMOUNT": self.amount
        }

        expenses.append(expense)

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4, ensure_ascii=False)
        
        return (f"# Expense added successfully (ID: {new_id})")

    
    def delete_expense(self, id):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                expenses = json.load(file)
                if not isinstance:
                    expenses = []
                updated_expenses = [i for i in expenses if i["ID"] != id]

                if len(updated_expenses) != len(expenses):
                    with open(DATA_FILE, "w", encoding="utf-8") as file:
                        json.dump(expenses, file, indent=4, ensure_ascii=False)
                    return(f"# Expense with id {id} deleted succesfully")
                else:
                    return(f"# Expense with id {id} not found")
        except (FileNotFoundError, json.JSONDecodeError):
            return "File not found or corrupted"
    
    def show_expenses(self, filter=None):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                expenses = json.load(file)
                if not isinstance:
                    expenses = []
        except (FileNotFoundError, json.JSONDecodeError):
            print("File not found or corrupted")

        if filter!= None:
            expenses = [s for s in expenses if s['DATE'].split(".")[1]==filter]
        
        print("#   ID    DATE        Description    AMOUNT")
        for i in expenses:
            print(f'#   {i.get("ID")}    {i.get("DATE")}   {i.get("DESCRIPTION")}          ${i.get("AMOUNT")}')
    
    def update_expense(self, id, amount=None, description=None):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            try:
                expenses = json.load(file)
            except json.JSONDecodeError:
                expenses = []

        if not isinstance(expenses, list):
            expenses = []

        expense_found = False
        for item in expenses:
            if item.get("ID") == id: 
                if amount is not None:
                    item["AMOUNT"] = amount
                if description is not None:
                    item["DESCRIPTION"] = description
                expense_found = True
                break 

        if expense_found:
            with open(DATA_FILE, "w", encoding="utf-8") as file:
                json.dump(expenses, file, indent=4, ensure_ascii=False)
                return f"# Expense with id {id} updated successfully"
        else:
            return f"# Expense with id {id} not found"




if __name__ == "__main__":
    test = ExpenseTracker(amount=20, description="chipsi")
    #print(test.add_expense())
    test.show_expenses()
    print(test.update_expense(id=1, description="Suhariki"))
    print(test.update_expense(id=2, amount="200"))
    test.show_expenses()
            




        
        


        

        




