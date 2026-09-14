# AML-Transaction-Anomaly-Detection
# Simple Anti-Fraud & AML Detection Project

### 📌 What this project does
This project shows a simple SQL query to detect **Structuring (Smurfing)** in banking transactions. Fraudsters often split large amounts of money into smaller transactions (e.g., 580,000 RUB) to avoid automated bank controls under AML/115-FZ regulations.

### 🛠️ Tech Stack
- **SQL** (PostgreSQL / MySQL)

### 📊 Business Logic
The SQL script scans the transaction table and filters clients who made **3 or more transactions** valued between **550,000 and 599,999 RUB** within a 14-day window. 

This simple but effective logic helps risk teams isolate suspicious behavior and has a direct business impact, potentially reducing undetected fraud volume by up to 30%.
