from storage import save_trans, load_trans
import pandas as pd

def total_income():
    transactions = load_trans()
    total = 0
    for trans in transactions:
        if trans['type'] == "income":
            total += trans['amount'] 
    return total

def total_expense():
    transactions = load_trans()
    total = 0
    for trans in transactions:
        if trans['type'] == "expense":
            total += trans['amount'] 
    return total

def total_balance():
    transactions = load_trans()
    income_total = 0
    expense_total = 0
    for trans in transactions:
        if trans['type'] == "income":
            income_total += trans['amount']
        elif trans['type'] == "expense":
            expense_total += trans['amount']
    balance = income_total - expense_total
    return balance

def category_total():
    transactions = load_trans()
    df = pd.DataFrame(transactions)
    expenses = df[df['type'] == 'expense']
    category_totals = expenses.groupby('category')['amount'].sum()
    return category_totals


    


    