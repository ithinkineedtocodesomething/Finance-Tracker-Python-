
from storage import save_trans, load_trans
from datetime import datetime
import uuid


def add_items():
    d = input("Income or Expense: ").lower()

    if d not in ["income", "expense"]:
        print("Invalid transaction type!")
        return

    try:
        a = float(input("Enter amount: "))
        if a <= 0:
            print("Amount must be greater than zero!")
            return
    except ValueError:
        print("Please enter a valid amount!")
        return

    b = input("Enter category: ").strip().lower()

    if not b:
        print("Category cannot be empty!")
        return

    transaction = {
        "id": str(uuid.uuid4()),
        "type": d,
        "amount": a,
        "category": b,
        "date": datetime.today().date().isoformat()
    }

    transactions = load_trans()
    transactions.append(transaction)
    save_trans(transactions)

    print("Transaction saved successfully!")


def view_transactions():
    transactions = load_trans()

    if not transactions:
        print("Empty file or no transactions!")
        return

    for trans in transactions:
        print("ID:", trans["id"])
        print("Type:", trans["type"])
        print("Amount:", trans["amount"])
        print("Category:", trans["category"])
        print("Date:", trans["date"])
        print("-------------------")


def delete_transactions():
    transactions = load_trans()

    if not transactions:
        print("File is empty!")
        return

    a = input("Enter the transaction ID you want to delete: ")

    for trans in transactions:
        if a == trans["id"]:
            b = input(f"Do you want to delete {a}? (y/n): ")

            if b.lower() == "y":
                transactions.remove(trans)
                save_trans(transactions)
                print("Deleted successfully!")
            else:
                print("Deletion cancelled!")

            return

    print("ID not found!")


def edit_transactions():
    transactions = load_trans()

    if not transactions:
        print("Empty file!")
        return

    a = input("Enter the transaction ID you want to edit: ")

    for trans in transactions:
        if a == trans["id"]:
            print("Transaction found!")
            print(trans)

            while True:
                a = input(
                    "What would you like to edit?\n"
                    "1. Type\n"
                    "2. Amount\n"
                    "3. Category\n"
                    "4. Date\n"
                    "5. Cancel\n"
                )

                if a == '1':
                    new_type = input(
                        "Income or Expense: "
                    ).lower()

                    if new_type in ["income", "expense"]:
                        trans["type"] = new_type
                    else:
                        print("Invalid transaction type!")
                        continue

                elif a == '2':
                    try:
                        new_amount = float(
                            input("Enter the amount: ")
                        )

                        if new_amount <= 0:
                            print("Amount must be greater than zero!")
                            continue

                        trans["amount"] = new_amount

                    except ValueError:
                        print("Enter a valid amount!")
                        continue

                elif a == '3':
                    new_category = input(
                        "Enter the category: "
                    ).strip().lower()

                    if not new_category:
                        print("Category cannot be empty!")
                        continue

                    trans["category"] = new_category

                elif a == '4':
                    new_date = input(
                        "Enter new date (DD-MM-YYYY): "
                    )

                    try:
                        trans["date"] = datetime.strptime(
                            new_date, "%d-%m-%Y"
                        ).date().isoformat()

                    except ValueError:
                        print("Invalid date!")
                        continue

                elif a == '5':
                    save_trans(transactions)
                    print("Editing stopped. Changes saved!")
                    return

                else:
                    print("Invalid output!")
                    continue

                b = input("Do you want to edit more? (y/n): ").lower()

                if b == "n":
                    save_trans(transactions)
                    print("Edits saved!")
                    print(trans)
                    return

                elif b == "y":
                    print("Current transaction:")
                    print(trans)

                else:
                    print("Invalid input!")


    print("ID not found!")


def search_transactions():
    transactions = load_trans()

    if not transactions:
        print("Transactions file empty!")
        return

    while True:
        a = input(
            "What would you like to search with?\n"
            "1. ID\n"
            "2. Category\n"
            "3. Date\n"
            "4. Exit\n"
        )

        if a == '1':
            b = input("Enter the ID: ")
            found = False

            for trans in transactions:
                if trans["id"] == b:
                    found = True
                    print("Transaction found!")
                    print(trans)

            if not found:
                print("ID not found!")

        elif a == '2':
            b = input("Enter the category: ").strip().lower()
            found = False

            for trans in transactions:
                if b in trans["category"].lower():
                    found = True
                    print("Transaction found!")
                    print(trans)

            if not found:
                print("Category not found!")

        elif a == '3':
            b = input("Enter the date (DD-MM-YYYY): ")

            try:
                date_search = datetime.strptime(
                    b, "%d-%m-%Y"
                ).date().isoformat()

                found = False

                for trans in transactions:
                    if date_search == trans["date"]:
                        found = True
                        print("Transaction found!")
                        print(trans)

                if not found:
                    print("Date not found!")

            except ValueError:
                print("Invalid date format!")

        elif a == '4':
            print("Exiting search!")
            return

        else:
            print("Invalid option!")
