import matplotlib.pyplot as plt

def plot_category_sales(category_sales):
    category_sales.plot(kind='bar')
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()

def plot_monthly_sales(monthly_sales):
    monthly_sales.plot(kind='line', marker='o')
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()