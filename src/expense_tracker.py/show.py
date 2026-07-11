from storage import load_expenses, save_expenses

def show_expenses(filter=None):
        expenses = load_expenses()
        if filter!= None:
            expenses = [s for s in expenses if s['DATE'].split(".")[1]==filter]
        
        print("#   ID    DATE        Description    AMOUNT")
        for i in expenses:
            print(f'#   {i.get("ID")}    {i.get("DATE")}   {i.get("DESCRIPTION")}          ${i.get("AMOUNT")}')