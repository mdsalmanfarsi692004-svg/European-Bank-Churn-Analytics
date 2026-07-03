# 🏦 European Banking: Customer Churn Analytics

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red.svg)
![Data Analysis](https://img.shields.io/badge/Data%20Analytics-Enterprise-success)
![Internship](https://img.shields.io/badge/Unified%20Mentor-ML%20Internship-orange)

An enterprise-grade data analytics project designed to identify customer retention risks, wealth flight, and regional disparities within the European retail banking sector. 

---

## 🖥️ Dashboard Preview
*(A comprehensive view of the interactive Streamlit dashboard featuring custom dark-theme UI and live KPIs)*

(<img width="1901" height="1078" alt="Dashboard" src="https://github.com/user-attachments/assets/25eb14bc-fe67-4aca-96a4-95b9da0af967" />)

---

## 🔗 Live Links
* **🔴 Live Streamlit Dashboard:** [Add your deployed app link here]
* **🎥 Project Demo Video:** [Add your YouTube/Loom video link here]
* **📄 Executive Research Report:** [View the PDF Report](European_Bank_Churn_Report.pdf)

## 📌 Project Overview
Customer churn represents one of the largest hidden costs in retail banking. This project bridges the gap between raw customer behavioral data and strategic policy formulation. Using a dataset of 10,000 proprietary retail banking profiles across France, Germany, and Spain, this project delivers actionable insights into churn patterns across geography, demographics, and financial profiles.

### Key Objectives Achieved:
- **Measured** overall churn rates and isolated high-risk segments using a custom-built interactive UI.
- **Identified** systemic risks in specific regional markets (e.g., Germany).
- **Quantified** the financial profile of churned customers to address premium capital migration.

## 💻 Tech Stack Used
* **Frontend & UI:** Streamlit (Custom Dark Theme UI, CSS injection)
* **Data Manipulation:** Pandas
* **Data Visualization:** Plotly Express (Interactive charts)
* **Data Source Handling:** Excel (`openpyxl`)
* **Reporting:** Native Python PDF generation (`fpdf`)

## 📊 Key Analytical Insights

1. **The German Market Anomaly 🌍** While France and Spain maintained stable churn rates (~16%), Germany experienced a massive capital exodus with a churn rate of **32.44%**.
   
2. **The "Critical Zone" (Age 46-60) 📈** The highest risk segment resides in the 46-60 age demographic, where over **51%** of customers exited the bank. This indicates a potential failure in retirement planning or wealth management suites for peak-earning professionals.

3. **Wealth Flight 💰** Premium customers (top 50% account balances) churned at a disproportionately higher rate (**24.16%**) compared to zero-balance accounts, representing a significant threat to institutional liquidity.

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/European-Bank-Churn-Analytics.git](https://github.com/your-username/European-Bank-Churn-Analytics.git)
   cd European-Bank-Churn-Analytics
   ```

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv .venv
   # On Windows use:
   .venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

## 👨‍💻 About the Author
Developed by **Md Salman Farsi** during the Machine Learning Internship at Unified Mentor. Connect with me on [LinkedIn](#).
