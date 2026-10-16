import csv
import json
import os
from datetime import datetime
from statistics import mean

# File names
TRANSACTION_FILE = "transactions.csv"
SETTINGS_FILE = "settings.json"

# Default categories
DEFAULT_CATEGORIES = {
    "income": [
        "Pocket Money",
        "Salary",
        "Scholarship",
        "Other Income"
    ],
    "expense": [
        "Food",
        "Transport",
        "Education",
        "Shopping",
        "Entertainment",
        "Bills",
        "Other Expense"
    ]
}


# ----------------------------------------
# 1. Initialize application files
# ----------------------------------------

def initialize_files():
    if not os.path.exists(TRANSACTION_FILE):
        with open(TRANSACTION_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Date",
                "Type",
                "Category",
                "Amount",
                "Description"
            ])

    if not os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "w") as file:
            json.dump(DEFAULT_CATEGORIES, file, indent=4)


# ----------------------------------------
# 2. Load categories from JSON
# ----------------------------------------

def load_categories():
    with open(SETTINGS_FILE, "r") as file:
        return json.load(file)


# ----------------------------------------
# 3. Read all transactions
# ----------------------------------------

def load_transactions():
    transactions = []

    with open(TRANSACTION_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            transactions.append(row)

    return transactions


# ----------------------------------------
# 4. Add income or expense
# ----------------------------------------

def add_transaction(transaction_type):
    categories = load_categories()

    print("\nAvailable categories:")

    category_list = categories[transaction_type.lower()]

    for i, category in enumerate(category_list, start=1):
        print(str(i) + ".", category)

    try:
        choice = int(input("Choose a category number: "))

        if choice < 1 or choice > len(category_list):
            print("Invalid category choice.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    category = category_list[choice - 1]

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    description = input("Enter description: ").strip()

    date_input = input(
        "Enter date (YYYY-MM-DD), or press Enter for today: "
    ).strip()

    if date_input == "":
        transaction_date = datetime.today().strftime("%Y-%m-%d")
    else:
        try:
            transaction_date = datetime.strptime(
                date_input, "%Y-%m-%d"
            ).strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")
            return

    transaction = [
        transaction_date,
        transaction_type,
        category,
        "{:.2f}".format(amount),
        description
    ]

    with open(TRANSACTION_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(transaction)

    print("\nTransaction recorded successfully!")


# ----------------------------------------
# 5. Display transaction history
# ----------------------------------------

def view_transactions():
    transactions = load_transactions()

    if not transactions:
        print("\nNo transactions found.")
        return

    print("\n" + "=" * 85)
    print("TRANSACTION HISTORY")
    print("=" * 85)

    print(
        "{:<12} {:<10} {:<18} {:>12}   {}".format(
            "Date", "Type", "Category", "Amount", "Description"
        )
    )

    print("-" * 85)

    for transaction in transactions:
        print(
            "{:<12} {:<10} {:<18} {:>12}   {}".format(
                transaction["Date"],
                transaction["Type"],
                transaction["Category"],
                transaction["Amount"],
                transaction["Description"]
            )
        )

    print("=" * 85)


# ----------------------------------------
# 6. Generate monthly summary
# ----------------------------------------

def monthly_summary():
    transactions = load_transactions()

    month_input = input(
        "Enter month (YYYY-MM), or press Enter for current month: "
    ).strip()

    if month_input == "":
        month_input = datetime.today().strftime("%Y-%m")

    try:
        datetime.strptime(month_input, "%Y-%m")
    except ValueError:
        print("Invalid month. Use YYYY-MM.")
        return

    total_income = 0
    total_expenses = 0
    expense_amounts = []
    category_totals = {}

    for transaction in transactions:

        if not transaction["Date"].startswith(month_input):
            continue

        amount = float(transaction["Amount"])

        if transaction["Type"] == "income":
            total_income += amount

        elif transaction["Type"] == "expense":
            total_expenses += amount
            expense_amounts.append(amount)

            category = transaction["Category"]

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] += amount

    savings = total_income - total_expenses

    print("\n" + "=" * 45)
    print("MONTHLY FINANCIAL SUMMARY:", month_input)
    print("=" * 45)

    print("Total Income:   {:.2f}".format(total_income))
    print("Total Expenses: {:.2f}".format(total_expenses))
    print("Net Savings:    {:.2f}".format(savings))

    if total_income > 0:
        savings_rate = (savings / total_income) * 100
        print("Savings Rate:   {:.2f}%".format(savings_rate))

    if expense_amounts:
        print(
            "Average Transaction Expense: {:.2f}".format(
                mean(expense_amounts)
            )
        )

    print("\nEXPENSES BY CATEGORY")
    print("-" * 35)

    if category_totals:
        for category, amount in sorted(
            category_totals.items(),
            key=lambda item: item[1],
            reverse=True
        ):
            print("{}: {:.2f}".format(category, amount))
    else:
        print("No expenses recorded for this month.")

    print("=" * 45)


# ----------------------------------------
# 7. Search transactions by category
# ----------------------------------------

def search_category():
    category_name = input(
        "Enter category to search: "
    ).strip().lower()

    transactions = load_transactions()
    found = False

    print("\nSEARCH RESULTS")
    print("-" * 60)

    for transaction in transactions:
        if transaction["Category"].lower() == category_name:
            print(
                "{} | {} | {} | {}".format(
                    transaction["Date"],
                    transaction["Type"],
                    transaction["Amount"],
                    transaction["Description"]
                )
            )
            found = True

    if not found:
        print("No transactions found for this category.")


# ----------------------------------------
# 8. Main menu
# ----------------------------------------

def main():
    initialize_files()

    while True:
        print("\n" + "=" * 40)
        print("       PERSONAL FINANCE TRACKER")
        print("=" * 40)

        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. Monthly Financial Summary")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            add_transaction("income")

        elif choice == "2":
            add_transaction("expense")

        elif choice == "3":
            view_transactions()

        elif choice == "4":
            monthly_summary()

        elif choice == "5":
            search_category()

        elif choice == "6":
            print("Thank you for using Personal Finance Tracker!")
            break

        else:
            print("Invalid choice. Please select 1-6.")


# Run the application
if __name__ == "__main__":
    main()