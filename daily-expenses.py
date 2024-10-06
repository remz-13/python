import json 
import time
import sys

# you can make this to record your daily expenses, it makes a json file when it is recorded and you can load it and see your expenses any time. just something i did when i was bored.

EXPENSE_FILE = 'expenses.json'

def load_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    
def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file)

def add_expense(description, amount):
    expenses = load_expenses()
    expenses.append({'description': description, 'amount': amount})
    save_expenses(expenses)
    print(f'Added expense: {description} - $ {amount:.2f}')

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded. ")
        return
    total = sum(expense['amount'] for expense in expenses)
    print("\nExpenses: ")
    for expense in expenses:
        print(f"{expense['description']}: $ {expense['amount']:.2f}")
        print(f"Total Spent: ${total:.2f}")

def main():
    while True:
        print("\nExpense Tracker")
        print("[1] Add Expense")
        print("[2] View Expenses")
        print("[3] Exit")

        choice = input("""input your choice:
-------------------------------> """)
        
        if choice == '1':
            description = input("enter expense description: ")
            try:
                amount = float(input("enter expense amount: "))
                add_expense(description, amount)
            except ValueError:
                print("please enter a valid amount.")

        elif choice == '2':
            view_expenses()


        elif choice == '3':
            print("exiting in 2 seconds...")
            time.sleep(2)
            sys.exit()

        else:
            print("please pick a valid number.")


if __name__=="__main__":
    main()
