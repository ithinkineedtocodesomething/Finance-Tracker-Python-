# Monthly Finance Tracker

A Python-based personal finance management application that helps users track their income, expenses, savings and spending patterns.

This project was built to practise Python programming, data handling, calculations and data visualization through a practical application.

## Features

### 1. Transaction Management
- Add income and expense transactions.
- View all recorded transactions.
- Edit existing transactions.
- Delete transactions.
- Search transactions.

### 2. Financial Calculations
- Calculate total income.
- Calculate total expenses.
- Calculate current balance.
- Analyse expenses by category.

### 3. Data Visualization
The application provides visual insights into financial data through:
- Income vs Expense Pie Chart.
- Category-wise Expense Pie Chart.
- Monthly Expense Line Chart.
- Category-wise Expense Bar Chart.

### 4. Monthly Reports
- Generate monthly financial reports.
- Calculate total income, expenses and net savings.
- Calculate savings rate.
- View category-wise expenses.
- View monthly expense summaries.
- Export reports into TXT files.

### 5. Data Storage
- Stores transaction records in JSON format.
- Loads previously saved transactions.
- Maintains transaction data between application sessions.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| Matplotlib | Data visualization |
| JSON | Transaction data storage |

## Project Structure

```text
Monthly-Finance-Tracker/
│
├── data/
│   └── transactions.json
│
├── reports/
│
├── main.py
├── transactions.py
├── calculations.py
├── charts.py
├── reporting.py
├── storage.py
│
├── README.md
└── requirements.txt
```

## Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/ithinkineedtocodesomething/Finance-Tracker-Python-
```

**2. Navigate to the project folder**

```bash
cd Monthly-Finance-Tracker
```

**3. Install the required libraries**

```bash
pip install pandas matplotlib
```

**4. Run the application**

```bash
python main.py
```

## Learning Outcomes

While developing this project, I practised:

- Python functions and modules.
- Conditional statements and loops.
- File handling and JSON operations.
- Working with dictionaries and lists.
- Pandas DataFrames and GroupBy operations.
- Data visualization using Matplotlib.
- Organizing a Python project into multiple modules.

## Future Improvements

Some features I would like to explore in future versions:

- Interactive web dashboard using Streamlit.
- Monthly budget planning.
- Budget limit notifications.
- CSV data export.
- Improved financial analytics.

## Author

Developed as a personal learning project to strengthen my Python programming and data analysis skills.

