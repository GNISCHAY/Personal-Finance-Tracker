💰 Personal Finance Tracker 💰

A beginner-friendly "Personal Finance Tracker built with Python" that helps users record income and expenses, categorize transactions, and generate monthly financial summaries.

This project demonstrates fundamental Python programming concepts, including functions, file handling, dictionaries, lists, exception handling, and basic financial analysis using Python's standard library.

✨ Features ✨

Income Tracking: Record income from sources such as pocket money, salary, and scholarships.
Expense Tracking: Record daily expenses and organize them into categories.
Transaction History: View all previously recorded transactions.
Monthly Financial Summary: Calculate total income, total expenses, and net savings for a selected month.
Savings Rate: Calculate the percentage of income remaining after expenses.
Expense Analysis: Calculate average transaction expenses and identify spending by category.
Category Search: Find transactions belonging to a specific category.
Persistent Storage: Save transaction records in CSV files and application settings in JSON.
Input Validation: Handle invalid amounts, category choices, and dates.

🛠️ Technologies Used 🛠️

Language: Python 3
Libraries:

  * `csv` — Read and write transaction records.
  * `json` — Store application settings and categories.
  * `datetime` — Handle transaction dates and monthly reports.
  * `statistics` — Calculate average expenses.
  * `os` — Check whether application files exist.

All libraries used are part of Python's standard library. No external packages are required.

📁 Project Structure 📁

text
personal_finance_tracker/
│
├── main.py             # Main application
├── transactions.csv    # Transaction records (created automatically)
├── settings.json       # Application categories (created automatically)
└── README.md           # Project documentation


Note: `transactions.csv` and `settings.json` are generated automatically when the application runs for the first time.

🚀 Getting Started 🚀

Prerequisites

* Python 3 installed on your computer.
* A code editor such as Visual Studio Code.
* Basic familiarity with running Python programs.

Installation

1. Clone the repository

Open your terminal and run:

bash
git clone YOUR_GITHUB_REPOSITORY_URL


Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's actual URL.

2. Navigate to the project directory

bash
cd personal_finance_tracker

3. Run the application

bash
python main.py


On Windows, if the `python` command doesn't work, try:

bash
py main.py


No additional package installation is necessary.

🖥️ Application Menu 🖥️

When you run the program, the following menu appears:

text
========================================
       PERSONAL FINANCE TRACKER
========================================
1. Add Income
2. Add Expense
3. View All Transactions
4. Monthly Financial Summary
5. Search by Category
6. Exit

Enter your choice (1-6):


Select an option by entering its corresponding number.

📊 Example Usage 📊

Adding an Income Transaction

Example input:

text
Choose a category number: 1
Enter amount: 10000
Enter description: Monthly pocket money
Enter date (YYYY-MM-DD), or press Enter for today: 2026-10-01


The transaction is saved automatically.

Recording Expenses

Example transactions:

| Date       | Category  |  Amount | Description |
| ---------- | --------- | ------: | ----------- |
| 2026-10-02 | Food      |  500.00 | Lunch       |
| 2026-10-04 | Transport |  300.00 | Bus fare    |
| 2026-10-05 | Education | 1200.00 | Books       |
| 2026-10-08 | Shopping  |  800.00 | Clothes     |

These are illustrative examples for testing the application.

#Generating a Monthly Summary

Select option `4` and enter:

text
2026-10


Example output:

text
=============================================
MONTHLY FINANCIAL SUMMARY: 2026-10
=============================================
Total Income:   10000.00
Total Expenses: 2800.00
Net Savings:    7200.00
Savings Rate:   72.00%
Average Transaction Expense: 700.00

EXPENSES BY CATEGORY
-----------------------------------
Education: 1200.00
Shopping: 800.00
Food: 500.00
Transport: 300.00
=============================================


The report calculates these values from the transactions saved for the selected month.

🗂️ Data Storage 🗂️

# CSV File

Transactions are stored in `transactions.csv` using the following columns:

text
Date,Type,Category,Amount,Description


Each row represents one income or expense transaction.

# JSON File

The `settings.json` file stores the available income and expense categories.

Users can customize these categories by editing the JSON file.

🧠 Python Concepts Demonstrated 🧠

This project provides practical experience with:

* Variables and data types
* Functions and parameters
* Lists and dictionaries
* Conditional statements
* `for` and `while` loops
* File handling
* CSV and JSON data processing
* Exception handling with `try` and `except`
* Date formatting and validation
* Sorting and basic statistical calculations
* Modular programming

🔮 Future Improvements 🔮

Potential enhancements include:

* Monthly spending budgets and budget alerts
* Edit and delete transactions
* Savings goals and progress tracking
* Expense comparisons across multiple months
* Data export and backup functionality
* Automated unit tests
* Graphical user interface
* More robust financial calculations using Python's 'decimal' module

🎯 Project Objective 🎯

The objective of this project is to apply basic Python programming skills to a practical problem while developing an understanding of file handling, data organization, and financial calculations.

It is designed as a learning project for beginners who want to strengthen their Python fundamentals through hands-on development.

⚠️ Limitations ⚠️

* The application runs in the terminal.
* Transaction records are stored locally in CSV files.
* Financial data is not encrypted.
* The application is intended for educational use and is not a secure banking or financial management system.

**Important:** Do not upload personal financial records or other sensitive information to a public repository.

👨‍💻 Author 👨‍💻

"Nischay Gupta"

Aspiring Computer Science and AI/ML student interested in Python programming, problem-solving, and software development.


⭐ If you find this project useful, consider giving the repository a star! ⭐
