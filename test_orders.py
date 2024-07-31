import pandas as pd
from io import StringIO
import pytest

# Sample data for testing
data = """order_id,customer_id,order_date,product_id,product_name,product_price,quantity
1,1,2021-01-01,101,Product A,10.0,1
2,2,2021-02-01,102,Product B,20.0,2
3,1,2021-02-15,101,Product A,10.0,2
4,3,2021-03-01,103,Product C,30.0,1
"""

df = pd.read_csv(StringIO(data))
df['order_date'] = pd.to_datetime(df['order_date'])
df['revenue'] = df['product_price'] * df['quantity']

def test_monthly_revenue():
    monthly_revenue = df.groupby(df['order_date'].dt.to_period('M'))['revenue'].sum().reset_index()
    monthly_revenue.columns = ['month', 'total_revenue']
    # Print for debugging
    print("\nMonthly Revenue (Test Data):")
    print(monthly_revenue)
    assert monthly_revenue['total_revenue'].sum() == 100.0  # Adjusted expected value based on the test data

def test_product_revenue():
    product_revenue = df.groupby('product_name')['revenue'].sum().reset_index()
    product_revenue.columns = ['product_name', 'total_revenue']
    # Print for debugging
    print("\nProduct Revenue (Test Data):")
    print(product_revenue)
    assert product_revenue[product_revenue['product_name'] == 'Product A']['total_revenue'].values[0] == 30.0

def test_customer_revenue():
    customer_revenue = df.groupby('customer_id')['revenue'].sum().reset_index()
    customer_revenue.columns = ['customer_id', 'total_revenue']
    # Print for debugging
    print("\nCustomer Revenue (Test Data):")
    print(customer_revenue)
    assert customer_revenue[customer_revenue['customer_id'] == 1]['total_revenue'].values[0] == 30.0

def test_top_customers():
    customer_revenue = df.groupby('customer_id')['revenue'].sum().reset_index()
    customer_revenue.columns = ['customer_id', 'total_revenue']
    top_customers = customer_revenue.sort_values(by='total_revenue', ascending=False).head(3)
    # Print for debugging
    print("\nTop Customers (Test Data):")
    print(top_customers)
    assert len(top_customers) == 3
    # Adjusted the expected top customer ID based on the test data
    assert top_customers.iloc[0]['customer_id'] == 2
