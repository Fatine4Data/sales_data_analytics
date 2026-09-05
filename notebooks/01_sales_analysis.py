import pandas as pd

df = pd.read_csv("data/sales.csv")
print(df)
# print(df.info())
# print(df.describe())
# print(df["product"].unique())
# print(df["product"].value_counts())
# print(df["city"].value_counts())
df["revenue"] = df["quantity"] * df["price"]

print(df)

#print(df["revenue"].max())

#print(df[df["revenue"] == 20000])

# print(df.groupby("product")["revenue"].sum().idxmax())
# print(df.groupby("city")["revenue"].sum().idxmax())
# print(df.groupby("city")["revenue"].sum())



# print(df.groupby("city")["revenue"].sum())

sales_by_product=df.groupby("product")["quantity"].sum()
print(sales_by_product)

revenue_by_product = df.groupby("product")["revenue"].sum()
print(revenue_by_product)

revenue_by_city=df.groupby("city")["revenue"].sum()
print(revenue_by_city)

product_by_city=df.groupby("city")["product"].value_counts()
print(product_by_city)

quantity_by_city_product = df.groupby(["city", "product"])["quantity"].sum()
print(quantity_by_city_product)


product_by_city_product_revenue = df.groupby(["city", "product"])[["quantity", "revenue"]].sum()
print(product_by_city_product_revenue)


average_revenue_by_product = df.groupby("product")["revenue"].mean()
print(average_revenue_by_product)


revenue_by_city_product = df.groupby(["city", "product"])["revenue"].sum()
print(revenue_by_city_product)



print(df["revenue"].sum())

df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")
revenue_by_month = df.groupby("month")["revenue"].sum()
print(revenue_by_month)


import matplotlib.pyplot as plt

# sales_by_product.plot(kind="bar")

# plt.title("Quantité vendue par produit")
# plt.xlabel("Produit")
# plt.ylabel("Quantité vendue")

# plt.show()




# revenue_by_product.plot(kind="bar")

# plt.title("Revenue par produit")
# plt.xlabel("Produit")
# plt.ylabel("Revenue")

# plt.show()


# revenue_by_city.plot(kind="bar")

# plt.title("Revene par city")
# plt.xlabel("city")
# plt.ylabel("Revenue")

# plt.show()



# import matplotlib.pyplot as plt

# revenue_by_city_product.plot(kind="bar")

# plt.title("Revenue par produit et par ville")
# plt.xlabel("Produit et city")
# plt.ylabel("Revenue")

# plt.show()



revenue_by_month.plot(kind="bar")

plt.title("Revenu par mois")
plt.xlabel("Mois")
plt.ylabel("Revenu")
plt.show()