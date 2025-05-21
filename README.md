# 💸 Expense Tracker Using Python Flask & MySQL

A modern web app to track and analyze your expenses by uploading receipt images. Powered by Python Flask, MySQL, and OCR for automatic data extraction!

![Expense Tracker Screenshot](https://user-images.githubusercontent.com/your-github-id/your-demo-image.png) <!-- Replace with your screenshot URL if available -->

---

## 🚀 Features

- **Upload Receipts:** Snap and upload receipt images—no manual entry needed!
- **OCR Extraction:** Automatically reads and parses expense data using Tesseract OCR.
- **Category Detection:** Auto-categorizes expenses for smarter analytics.
- **Dashboard:** View your latest expenses in a clean, sortable table.
- **Download Reports:** Export your expense data as PDF reports.
- **MySQL Backend:** Fast and robust data storage.

## 📸 Screenshots

<!-- Add your own screenshots here -->
| Upload Receipt | Dashboard / Analytics |
| -------------- | -------------------- |
| ![Upload Example](https://user-images.githubusercontent.com/your-github-id/upload.png) | ![Dashboard Example](https://user-images.githubusercontent.com/your-github-id/dashboard.png) |

---

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8+
- MySQL Server
- Tesseract OCR (`sudo apt install tesseract-ocr` or download for Windows)
- pip

### 1. Clone the Repo

```sh
git clone https://github.com/meruva-lokesh/Expense-Tracker-Using-Python-Flask-MySQL.git
cd Expense-Tracker-Using-Python-Flask-MySQL
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

### 3. Configure MySQL

- Start your MySQL server.
- Create a database and user:

```sql
CREATE DATABASE expense_tracker_db;
CREATE USER 'expense_user'@'localhost' IDENTIFIED BY 'yourpassword';
GRANT ALL PRIVILEGES ON expense_tracker_db.* TO 'expense_user'@'localhost';
FLUSH PRIVILEGES;
```

- Update your `database.py` or `.env` with your MySQL credentials.

### 4. (Optional) Set Up Environment Variables

Create a `.env` file for sensitive info (recommended):

```
DB_HOST=localhost
DB_USER=expense_user
DB_PASSWORD=yourpassword
DB_NAME=expense_tracker_db
SECRET_KEY=your-super-secret-key
```

### 5. Run the App

```sh
python app.py
```
Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## ⚙️ Deployment

- Push code to GitHub.
- Deploy on a VPS, PythonAnywhere, or cloud provider.
- Set up Gunicorn and (optionally) Nginx for production.
- Point your deployed code to your production MySQL instance.

---

## 📦 Project Structure

```
Expense-Tracker-Using-Python-Flask-MySQL/
│
├── app.py                  # Main Flask application
├── database.py             # MySQL connection and helpers
├── export.py               # PDF/CSV export logic
├── templates/              # HTML templates (Jinja2)
├── static/                 # CSS, JS, images
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🧩 Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL
- **OCR:** pytesseract, Tesseract OCR
- **Frontend:** HTML5, CSS3, Jinja2 templates

---

## 🤝 Contributing

Pull requests welcome! Please open an issue to discuss your proposed changes.

---

## 📝 License

MIT License. See [LICENSE](LICENSE).

---

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [ReportLab](https://www.reportlab.com/)
- [Bootstrap](https://getbootstrap.com/) (if used in styling)

---

> Made with 💸 by [meruva-lokesh](https://github.com/meruva-lokesh)
