class SupportAgent:
    def __init__(self, df):
        self.df = df

    def run(self, question):
        q = question.lower()

        if "column" in q or "available" in q:
            insight = (
                f"The dataset contains {len(self.df.columns)} columns: "
                + ", ".join(self.df.columns)
                + "."
            )
        elif "record" in q or "row" in q:
            insight = f"The dataset contains {len(self.df):,} transaction records."
        elif "region" in q:
            values = sorted(self.df["Region"].dropna().unique())
            insight = "Available regions: " + ", ".join(values)
        elif "category" in q:
            values = sorted(self.df["Category"].dropna().unique())
            insight = "Available categories: " + ", ".join(values)
        elif "ship mode" in q:
            values = sorted(self.df["Ship Mode"].dropna().unique())
            insight = "Available ship modes: " + ", ".join(values)
        else:
            insight = (
                "This dataset contains sales transactions with customer, "
                "product, geography, shipping, sales, discount and profit information."
            )

        action = (
            "Ask a Data Agent question when you need calculations, comparisons "
            "or business performance analysis."
        )

        return {"insight": insight, "action": action, "table": None, "chart": None}
