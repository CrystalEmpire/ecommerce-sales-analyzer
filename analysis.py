import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def total_revenue(df):
    return df['Sales'].sum()

def sales_by_category(df):
    return df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

def top_products(df):
    return df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5)

def monthly_sales(df):
    df['Month'] = df['Date'].dt.to_period('M')
    return df.groupby('Month')['Sales'].sum()

def top_customers(df):
    return df.groupby('Customer')['Sales'].sum().sort_values(ascending=False)

def average_order_value(df):
    return df['Sales'].mean()