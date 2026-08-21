import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


class MLAgent:
    def __init__(self, df):
        self.df = df

    def run(self, question):
        monthly = (
            self.df.groupby(self.df["Order Date"].dt.to_period("M"))["Sales"]
            .sum()
            .reset_index()
        )

        monthly["Date"] = monthly["Order Date"].dt.to_timestamp()
        monthly["TimeIndex"] = np.arange(len(monthly))

        model = LinearRegression()
        model.fit(monthly[["TimeIndex"]], monthly["Sales"])

        next_index = np.array([[monthly["TimeIndex"].max() + 1]])
        prediction = float(model.predict(next_index)[0])

        latest_sales = float(monthly["Sales"].iloc[-1])
        change = (
            ((prediction - latest_sales) / latest_sales) * 100
            if latest_sales else 0
        )

        insight = (
            f"The estimated sales for the next month are ${prediction:,.2f}. "
            f"This represents an estimated {change:+.1f}% change from the "
            f"latest month's sales."
        )

        action = (
            "Use this forecast as a planning indicator for inventory and sales "
            "activities. Validate the forecast with additional historical data "
            "before making high-impact decisions."
        )

        chart = monthly.set_index("Date")[["Sales"]]

        return {
            "insight": insight,
            "action": action,
            "table": monthly[["Date", "Sales"]],
            "chart": chart
        }
