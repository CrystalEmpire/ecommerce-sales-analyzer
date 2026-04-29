from analysis import *
from visualization import *

def main():
    df = load_data("data/sales_data.csv")

    print("\n📊 TOTAL REVENUE:")
    print(total_revenue(df))

    print("\n📊 SALES BY CATEGORY:")
    category = sales_by_category(df)
    print(category)

    print("\n🔥 TOP PRODUCTS:")
    print(top_products(df))

    print("\n📅 MONTHLY SALES:")
    monthly = monthly_sales(df)
    print(monthly)

    print("\n👑 TOP CUSTOMERS:")
    print(top_customers(df))

    print("\n💰 AVERAGE ORDER VALUE:")
    print(average_order_value(df))

    # Visualizations
    plot_category_sales(category)
    plot_monthly_sales(monthly)

if __name__ == "__main__":
    main()