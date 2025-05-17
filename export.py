import pandas as pd
from database import get_expenses

def export_csv(path="expenses_export.csv"):
    data = get_expenses()
    df = pd.DataFrame(data, columns=["id", "item", "category", "amount", "date"])
    df.to_csv(path, index=False)
    return path

def export_pdf(path="expenses_report.pdf"):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    data = get_expenses()
    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter
    c.drawString(30, height-30, "Expense Report")
    y = height - 50
    for row in data:
        line = f"{row[1]} | {row[2]} | {row[3]} | {row[4]}"
        c.drawString(30, y, line)
        y -= 15
        if y < 40:
            c.showPage()
            y = height - 30
    c.save()
    return path