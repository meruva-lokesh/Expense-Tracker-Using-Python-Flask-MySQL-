import os
from flask import Flask, render_template, request, redirect, send_file, flash
from ocr import extract_text, parse_receipt
from categorize import categorize_receipt
from database import init_db, add_expense, get_expenses
from analytics import plot_expense_summary, plot_monthly_trend
from export import export_csv, export_pdf

app = Flask(__name__)
app.secret_key = 'supersecret'
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["receipt"]
        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            text = extract_text(path)
            parsed = parse_receipt(text)
            items = categorize_receipt(parsed["items"])
            for item in items:
                add_expense(item["item"], item["category"], parsed["total"], parsed["date"])
            flash("Receipt processed and expenses logged!")
            return redirect("/dashboard")
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    plot_expense_summary()
    plot_monthly_trend()
    expenses = get_expenses()
    has_expense_summary = os.path.exists("static/expense_summary.png")
    has_monthly_trend = os.path.exists("static/monthly_trend.png")
    return render_template(
        "dashboard.html",
        expenses=expenses,
        has_expense_summary=has_expense_summary,
        has_monthly_trend=has_monthly_trend
    )

@app.route("/export/<format>")
def export(format):
    if format == "csv":
        path = export_csv()
    elif format == "pdf":
        path = export_pdf()
    else:
        flash("Unknown export format!")
        return redirect("/dashboard")
    return send_file(path, as_attachment=True)

@app.route("/report")
def report():
    expenses = get_expenses()
    return render_template("report.html", expenses=expenses)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)