class DataAgent:
    def __init__(self, df):
        self.df = df

    def run(self, question):
        q = question.lower()

        metric = "Sales"
        if "profit" in q:
            metric = "Profit"
        elif "quantity" in q or "units" in q:
            metric = "Quantity"

        group_map = {
            "region": "Region",
            "category": "Category",
            "sub-category": "Sub-Category",
            "subcategory": "Sub-Category",
            "segment": "Segment",
            "state": "State",
            "city": "City",
            "product": "Product Name",
            "ship mode": "Ship Mode"
        }

        group_col = next(
            (col for keyword, col in group_map.items() if keyword in q),
            None
        )

        if group_col:
            grouped = (
                self.df.groupby(group_col)[metric]
                .sum()
                .sort_values(ascending=False)
            )

            best_name = grouped.index[0]
            best_value = grouped.iloc[0]

            insight = (
                f"{best_name} has the highest total {metric.lower()} "
                f"at {best_value:,.2f}."
            )

            action = (
                f"Prioritize inventory, marketing and operational attention for "
                f"{best_name}. Review lower-performing groups for pricing, "
                f"discount and product-mix improvements."
            )

            table = grouped.reset_index()
            table.columns = [group_col, f"Total {metric}"]

            return {
                "insight": insight,
                "action": action,
                "table": table,
                "chart": None
            }

        if "order" in q:
            order_count = self.df["Order ID"].nunique()
            insight = f"The dataset contains {order_count:,} unique orders."
            action = "Monitor order volume monthly as a core business KPI."
            return {"insight": insight, "action": action, "table": None, "chart": None}

        total_sales = self.df["Sales"].sum()
        total_profit = self.df["Profit"].sum()

        insight = (
            f"Total sales are ${total_sales:,.2f} and total profit is "
            f"${total_profit:,.2f}."
        )
        action = (
            "Track sales and profit together. A rise in sales without a "
            "corresponding rise in profit should trigger a margin review."
        )

        return {"insight": insight, "action": action, "table": None, "chart": None}
