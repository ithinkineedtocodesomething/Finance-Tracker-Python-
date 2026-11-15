from storage import load_trans
from calculations import total_income,total_expense,total_balance,category_total
import pandas as pd

def report_generate():
    transactions = load_trans()

    if not transactions:
        print("No transactions to generate report")

    else:

        df = pd.DataFrame(transactions)
        expenses = df[df['type']=="expense"].copy()
        expenses['date'] = pd.to_datetime(expenses['date'])
        monthly_expenses = expenses.groupby(expenses['date'].dt.to_period("M"))['amount'].sum()

        totalinc = total_income()
        totalexpen = total_expense()
        savings = totalinc - totalexpen
        categorytot = category_total()
        savings_rate = (savings/totalinc) * 100 if totalinc>0 else 0
        report = f"""_____________Montly Report_____________
        
        Total income = {totalinc}
        Total expense = {totalexpen}
        Net savings = {savings}
        Savings_rate = {savings_rate}%

        Category by expenses
        {categorytot}

        Montly expenses
        {monthly_expenses}
        """
        with open("Montly_report.txt","w") as file:
            file.write(report)

        
report_generate()