import pandas as pd

def _col(df, name):
    return name in df.columns

def generate_code(question, df):
    q = question.lower().strip()

    if "total revenue" in q and _col(df, "revenue"):
        return 'print(f"Total revenue: {df["revenue"].sum():,.2f}")', "Calculated by summing revenue."

    if ("average revenue" in q or "mean revenue" in q) and _col(df, "revenue"):
        return 'print(f"Average revenue: {df["revenue"].mean():,.2f}")', "Calculated using the mean of revenue."

    if ("average unit price" in q or "mean unit price" in q) and _col(df, "unit_price"):
        return 'print(f"Average unit price: {df["unit_price"].mean():,.2f}")', "Calculated using the mean of unit_price."

    if ("number of transactions" in q or "how many transactions" in q) and "transaction_id" in df.columns:
        return 'print(f"Transactions: {df["transaction_id"].nunique()}")', "Counted unique transaction IDs."

    if ("highest revenue" in q or "most revenue" in q) and "region" in q and _col(df, "region") and _col(df, "revenue"):
        code = '''x = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
print(f"Top region: {x.index[0]}")
print(f"Revenue: {x.iloc[0]:,.2f}")'''
        return code, "Grouped revenue by region and selected the maximum."

    if ("highest revenue" in q or "most revenue" in q) and "product" in q and _col(df, "product") and _col(df, "revenue"):
        code = '''x = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
print(f"Top product: {x.index[0]}")
print(f"Revenue: {x.iloc[0]:,.2f}")'''
        return code, "Grouped revenue by product and selected the maximum."

    if "profit" in q and "profit" not in [c.lower() for c in df.columns]:
        return None, "The dataset has no verified profit field. Profit cannot be determined reliably."

    if any(word in q for word in ["currency", "usd", "eur", "inr"]) and "currency" not in [c.lower() for c in df.columns]:
        return None, "Currency information is not present as a verified field, so a currency comparison cannot be established."

    if "total" in q:
        for c in df.columns:
            if c.lower() in q and pd.api.types.is_numeric_dtype(df[c]):
                return f'print(f"Total {c}: {{df["{c}"].sum():,.2f}}")', f"Summed the numeric column '{c}'."

    if "average" in q or "mean" in q:
        for c in df.columns:
            if c.lower() in q and pd.api.types.is_numeric_dtype(df[c]):
                return f'print(f"Average {c}: {{df["{c}"].mean():,.2f}}")', f"Computed the mean of '{c}'."

    return None, "This prototype cannot safely map that question to a verified calculation, so it refuses instead of inventing an answer."
