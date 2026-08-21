def calculate_kpis(df):
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_quantity = df["Quantity"].sum()
    total_orders = df["Order ID"].nunique()

    margin = (total_profit / total_sales * 100) if total_sales else 0

    return {
        "Total Sales": total_sales,
        "Total Profit": total_profit,
        "Total Quantity": total_quantity,
        "Total Orders": total_orders,
        "Profit Margin %": margin
    }
