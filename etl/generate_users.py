import numpy as np
import pandas as pd

records = 50000

user_id = np.arange(1, records + 1)

age = np.random.randint(18, 75, size=records)

income = np.random.randint(1200, 50000, size=records)

types_work = ['full_time','part_time','self_employed','unemployed']
employment_type = np.random.choice(types_work, size=records)

years_employed = np.random.randint(0,30, size=records)

credit_limit = income * np.random.uniform(2, 6, size=records)

current_balance = credit_limit * np.random.uniform(0.1, 0.95, size=records)

monthly_spending = income * np.random.uniform(0.3, 0.9, size=records)

number_of_loans = np.random.randint(0,10, size=records)

missed_payments = np.where(income < 3000,
                           np.random.randint(1,5,records),
                           np.random.randint(0,2,records))

credit_cards_open = np.random.randint(0,5,records)

debt_to_income = current_balance / income

df = pd.DataFrame({
    'user_id': user_id,
    'age': age,
    'income': income,
    'employment_type' : employment_type,
    'years_employed' : years_employed,
    'credit_limit' : credit_limit,
    'current_balance' : current_balance,
    'monthly_spending' : monthly_spending,
    'number_of_loans' : number_of_loans,
    'missed_payments' : missed_payments,
    'credit_cards_open' : credit_cards_open,
    'debt_to_income' : debt_to_income
})

df.to_csv('credit_risk.csv', index=False)

print(df.head())