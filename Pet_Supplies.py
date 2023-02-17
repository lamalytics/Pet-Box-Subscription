import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import csv file of data
raw_data = pd.read_csv("pet_supplies_2212.csv")
# show data
print(raw_data.head())

# count na for each col
print(raw_data.isna().sum())

# show unique values for each column
# for col in raw_data.columns:
#     unique_values = raw_data[col].unique()
#     print(f"Unique values in {col}: {unique_values}")

# print col types
column_types = raw_data.dtypes
print(column_types)

# print(raw_data.info())

# need to fill in unknown for category
raw_data['category'] = raw_data['category'].replace('-', "Unknown")
# print(raw_data['category'].unique())
# change size capitalization
raw_data['size'] = [size.capitalize() for size in raw_data['size']]
# print(raw_data['size'].unique())
# fill unlisted to median for price and cast to float
raw_data['price'] = raw_data['price'].replace('unlisted', '0')
raw_data['price'] = raw_data['price'].astype(float)
raw_data['price'] = raw_data['price'].replace(0, np.median(raw_data['price']))
# print(raw_data.info())
# print(np.median(raw_data['price']))
# print(raw_data['price'].unique())

# fill in rating
raw_data['rating'] = raw_data['rating'].replace(np.nan, 0)
print(raw_data.info())

# show count of different product ids that are recent purchases
repeat_purchases = raw_data[raw_data['repeat_purchase'] == 1]
repeat_categories = repeat_purchases.groupby('category')['product_id'].agg('count').sort_values(ascending=True)
print(repeat_categories)
repeat_categories.plot(kind='barh')



raw_data['sales'].plot(kind='hist')
# plt.show()

# create a pivot table of the data
pivot = raw_data.pivot_table(index='price', columns='sales', aggfunc=len, fill_value=0)

# create the heatmap
corr_matrix = raw_data.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
print(raw_data['price'].corr(raw_data['sales']))
sns.lmplot(data=raw_data, x='price', y='sales')