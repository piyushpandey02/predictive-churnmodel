import pandas as pd
import sqlite3
import os

RAW_DATA_PATH = 'data/WA_Fn-UseC_-Telco-Customer-Churn.csv'
DB_PATH = 'data/telecom.db'

print(f"Loading raw data from {RAW_DATA_PATH}...")
df = pd.read_csv(RAW_DATA_PATH)

print("Cleaning and preparing data...")
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(subset=['TotalCharges'], inplace=True)
df['Churn'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

print("Creating normalized tables...")
customers = df[['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents']].copy()
contracts = df[['customerID', 'tenure', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn']].copy()

service_columns = [
    'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
    'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies'
]
services = df[['customerID'] + service_columns].copy()
services = services.melt(id_vars=['customerID'], var_name='service_name', value_name='service_value')
services = services[~services['service_value'].isin(['No phone service', 'No internet service'])]

print(f"Connecting to SQLite at {DB_PATH} and saving tables...")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
conn = sqlite3.connect(DB_PATH)

customers.to_sql('customers', conn, if_exists='replace', index=False)
contracts.to_sql('contracts', conn, if_exists='replace', index=False)
services.to_sql('services', conn, if_exists='replace', index=False)

conn.close()
print(f"Database '{DB_PATH}' created successfully with 3 tables.")