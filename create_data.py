import pandas as pd
import numpy as np

np.random.seed(0)

categories = ["Furniture", "Office Supplies", "Technology"]
sub_categories = ["Chairs","Tables","Binders","Phones","Storage","Accessories"]
regions = ["East","West","Central","South"]

data = {
    "Order Date": pd.date_range(start="2020-01-01", periods=500, freq="D"),
    "Category": np.random.choice(categories, 500),
    "Sub-Category": np.random.choice(sub_categories, 500),
    "Region": np.random.choice(regions, 500),
    "Sales": np.random.randint(100, 1000, 500),
    "Profit": np.random.randint(-100, 300, 500)
}

df = pd.DataFrame(data)
df.to_csv("superstore.csv", index=False)

print("✅ superstore.csv created successfully!")

