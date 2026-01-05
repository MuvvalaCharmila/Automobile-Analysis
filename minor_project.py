import pandas as pd
df = pd.read_csv('Automobile_data.csv')
print(df.head())
import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv("Automobile_data.csv")
print("Original data (first 5 rows):")
print(df.head())

print("\nMissing values in each column:")
print(df.isnull().sum())

df.dropna(inplace=True)

df.reset_index(drop=True, inplace=True)

print("\nCleaned data (first 5 rows):")
print(df.head())
min_price = df['price'].min()
min_car = df[df['price'] == min_price]
print("\n Cheapest Car Details:")
print(min_car)

max_price = df['price'].max()
max_car = df[df['price'] == max_price]
print("\n Most Expensive Car Details:")
print(max_car)
avg_price_by_company = df.groupby('company')['price'].mean()
print("\n Average Price by Company:")
print(avg_price_by_company)

avg_price_by_body = df.groupby('body-style')['price'].mean()
print("\n Average Price by Body Style:")
print(avg_price_by_body)
import matplotlib.pyplot as plt

avg_price_by_company = df.groupby('company')['price'].mean().sort_values(ascending=False)

plt.figure(figsize=(10,6))  # chart size
avg_price_by_company.plot(kind='bar', color='skyblue')
plt.title('Average Car Price by Company')
plt.xlabel('Company')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("\n Data Analysis Completed Successfully!")
print("\n Summary:")
print(f"Total cars after cleaning: {len(df)}")
print(f"Cheapest car price: {df['price'].min()}")
print(f"Most expensive car price: {df['price'].max()}")
print(f"Average car price overall: {df['price'].mean():.2f}")