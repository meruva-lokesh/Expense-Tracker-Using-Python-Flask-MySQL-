import pandas as pd
import matplotlib.pyplot as plt
from database import get_expenses

def plot_expense_summary():
    expenses = get_expenses()
    if not expenses or len(expenses) == 0:
        return
    df = pd.DataFrame(expenses, columns=["id", "item", "category", "amount", "date"])
    if df.empty:
        return
    summary = df.groupby('category')['amount'].sum()
    if summary.empty:
        return
    summary.plot.pie(autopct='%1.1f%%')
    plt.title("Expense by Category")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("static/expense_summary.png")
    plt.close()

def plot_monthly_trend():
    expenses = get_expenses()
    if not expenses or len(expenses) == 0:
        return
    df = pd.DataFrame(expenses, columns=["id", "item", "category", "amount", "date"])
    if df.empty:
        return
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])
    if df.empty:
        return
    df['month'] = df['date'].dt.to_period('M')
    monthly = df.groupby('month')['amount'].sum()
    if monthly.empty:
        return
    monthly.plot.line(marker='o')
    plt.ylabel("Total Amount")
    plt.title("Monthly Expense Trend")
    plt.tight_layout()
    plt.savefig("static/monthly_trend.png")
    plt.close()