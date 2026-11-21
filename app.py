import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Personal Budget Tracker", page_icon="💸", layout="centered")

st.title("💸 Personal Budget Tracker")
st.write("Adjust your monthly budget and expenses in the sidebar to see live updates.")

# 2. Sidebar Inputs
st.sidebar.header("Monthly Finances")
income = st.sidebar.number_input("Monthly Income ($)", min_value=500, max_value=50000, value=4000, step=100)
rent = st.sidebar.slider("Rent / Housing ($)", 0, 5000, 1200, step=50)
food = st.sidebar.slider("Food & Groceries ($)", 0, 2000, 500, step=25)
utilities = st.sidebar.slider("Utilities & Bills ($)", 0, 1000, 250, step=25)
entertainment = st.sidebar.slider("Entertainment ($)", 0, 1500, 300, step=25)

# 3. Calculations
total_expenses = rent + food + utilities + entertainment
savings = income - total_expenses
savings_rate = (savings / income) * 100 if income > 0 else 0

# 4. Top KPI Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Expenses", f"${total_expenses:,}")
col2.metric("Net Savings", f"${savings:,}", delta=f"{savings_rate:.1f}% saved")
col3.metric("Remaining Daily Budget", f"${max(savings / 30, 0):.2f}")

st.divider()

# 5. Data Table & Bar Chart
st.subheader("Expense Breakdown")
expense_data = pd.DataFrame({
    "Category": ["Rent", "Food", "Utilities", "Entertainment"],
    "Amount ($)": [rent, food, utilities, entertainment]
})

st.bar_chart(expense_data.set_index("Category"))
st.dataframe(expense_data, use_container_width=True, hide_index=True)