
from storage import load_trans
import pandas as pd
import matplotlib.pyplot as plt


def pie_chart():
    transactions = load_trans()

    if not transactions:
        print("No transactions available!")
        return

    df = pd.DataFrame(transactions)

    summary_df = df.groupby('type')['amount'].sum()

    if summary_df.empty:
        print("No data available!")
        return

    summary_df.plot.pie(
        autopct='%1.1f%%',
        figsize=(7, 7),
        colors=['#66b3ff', '#ff9999'],
        startangle=90,
        wedgeprops={'edgecolor': 'white', 'linewidth': 2}
    )

    plt.title('Income vs Expense Breakdown', fontsize=15)
    plt.ylabel("")
    plt.tight_layout()
    plt.show()




def category_wise_pie():
    transactions = load_trans()

    if not transactions:
        print("No transactions available!")
        return

    df = pd.DataFrame(transactions)

    expenses = df[df['type'] == 'expense']

    if expenses.empty:
        print("No expenses available!")
        return

    summary_df = expenses.groupby('category')['amount'].sum()

    colors = plt.cm.Set3(range(len(summary_df)))

    summary_df.plot.pie(
        autopct='%1.1f%%',
        figsize=(7, 7),
        colors=colors,
        startangle=90,
        wedgeprops={'edgecolor': 'white', 'linewidth': 2}
    )

    plt.title('Category-wise Expense Distribution', fontsize=15)
    plt.ylabel("")
    plt.tight_layout()
    plt.show()



def monthly_expense_line_chart():
    transactions = load_trans()

    if not transactions:
        print("No transactions available!")
        return

    df = pd.DataFrame(transactions)

    expenses = df[df['type'] == 'expense'].copy()

    if expenses.empty:
        print("No expenses available!")
        return

    expenses['date'] = pd.to_datetime(
        expenses['date'],
        errors='coerce'
    )

    expenses = expenses.dropna(subset=['date'])

    if expenses.empty:
        print("No valid expense dates found!")
        return

    expenses.set_index('date', inplace=True)

    monthly_expenses = expenses.resample('ME')['amount'].sum()

    monthly_expenses.plot(
        kind='line',
        marker='o',
        color='#0088FE',
        linewidth=2,
        figsize=(9, 5)
    )

    plt.title('Monthly Expense Trend', fontsize=15)
    plt.xlabel('Month')
    plt.ylabel('Expense Amount (₹)')
    plt.tight_layout()
    plt.show()



def category_wise_bar_chart():
    transactions = load_trans()

    if not transactions:
        print("No transactions available!")
        return

    df = pd.DataFrame(transactions)

    expenses = df[df['type'] == 'expense']

    if expenses.empty:
        print("No expenses available!")
        return

    summary_df = expenses.groupby('category')['amount'].sum()

    summary_df = summary_df.sort_values()

    summary_df.plot.barh(
        color='#00C49A',
        figsize=(9, 5),
        edgecolor='black'
    )

    plt.title('Category-wise Expense Comparison', fontsize=15)
    plt.xlabel('Expense Amount (₹)')
    plt.ylabel('Category')
    plt.tight_layout()
    plt.show()

def exporting_part():
    transactions = load_trans()
    df = pd.DataFrame(transactions)
    df.to_csv("monthly_data.csv",index=False)