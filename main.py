
from calculations import *
from charts import *
from reporting import *
from storage import *
from transactions import *


def transaction_menu():
    while True:
        print("=" * 40)

        aa = input(
            "TRANSACTION MENU\n"
            "1. Add Transaction\n"
            "2. View All Transactions\n"
            "3. Delete Transaction\n"
            "4. Edit Transaction\n"
            "5. Search Transaction\n"
            "6. Back to Main Menu\n\n"
            "Enter your choice (1-6): "
        )

        if aa == "1":
            add_items()

        elif aa == "2":
            view_transactions()

        elif aa == "3":
            delete_transactions()

        elif aa == "4":
            edit_transactions()

        elif aa == "5":
            search_transactions()

        elif aa == "6":
            break

        else:
            print("Invalid choice!")


def charts_menu():
    while True:
        print("=" * 40)

        aa = input(
            "CHARTS MENU\n"
            "1. Expense VS Income\n"
            "2. Category Wise Expense\n"
            "3. Expenses Over Months\n"
            "4. Category Wise Bar Chart\n"
            "5. Back to Main Menu\n\n"
            "Enter your choice (1-5): "
        )

        if aa == "1":
            pie_chart()

        elif aa == "2":
            category_wise_pie()

        elif aa == "3":
            monthly_expense_line_chart()

        elif aa == "4":
            category_wise_bar_chart()

        elif aa == "5":
            break

        else:
            print("Invalid choice!")


def calculations_menu():
    while True:
        print("=" * 40)

        aa = input(
            "CALCULATIONS MENU\n"
            "1. Total Income\n"
            "2. Total Expense\n"
            "3. Total Balance\n"
            "4. Category Wise Expenses\n"
            "5. Back to Main Menu\n\n"
            "Enter your choice (1-5): "
        )

        if aa == "1":
            print(total_income())

        elif aa == "2":
            print(total_expense())

        elif aa == "3":
            print(total_balance())

        elif aa == "4":
            print(category_total())

        elif aa == "5":
            break

        else:
            print("Invalid choice!")


def main():

    while True:
        print("=" * 40)
        print("       MONTHLY FINANCE TRACKER")
        print("=" * 40)

        aa = input(
            "MENUS\n"
            "1. Transaction Menu\n"
            "2. Calculations Menu\n"
            "3. Charts Menu\n"
            "4. Report Generation\n"
            "5. Quit\n\n"
            "Enter your choice (1-5): "
        )

        if aa == "1":
            transaction_menu()

        elif aa == "2":
            calculations_menu()

        elif aa == "3":
            charts_menu()

        elif aa == "4":
            report_generate()

        elif aa == "5":
            print("Thank you for using Monthly Finance Tracker!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
