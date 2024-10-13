import pandas as pd

df = pd.read_csv("Python Programming for Data Science/persona.csv")

print(df.info())
print(df.head())

print(df['SOURCE'].nunique())
print(df['SOURCE'].value_counts())

print(df['PRICE'].nunique())

print(df['PRICE'].value_counts())

print(df['COUNTRY'].value_counts())

print(df['SOURCE'].value_counts())

print(df.groupby('COUNTRY')['PRICE'].mean())

print(df.groupby('SOURCE')['PRICE'].mean())

print(df.groupby(['COUNTRY','SOURCE'])['PRICE'].mean())

grouped_avg = df.groupby(['COUNTRY','SOURCE','SEX','AGE'])['PRICE'].mean().reset_index()
print(grouped_avg)

sorted_gruped_avg = grouped_avg.sort_values(ascending=False ,by='PRICE')
print(sorted_gruped_avg)

agg_df = sorted_gruped_avg.reset_index()
print(agg_df.head())

agg_df['AGE_CAT'] = pd.cut(agg_df['AGE'], bins=[0, 18, 23, 30, 40, 70],
                           labels= ['0_18', '19_23', '24_30', '31_40', '41_70'])

print(agg_df.head())

agg_df['customers_level_based'] = agg_df['COUNTRY'].str.upper() + '_' + agg_df['SOURCE'].str.upper() + '_' + agg_df['SEX'].str.upper() +'_' + agg_df['AGE_CAT'].str.upper()

print(agg_df[['customers_level_based','PRICE']].head())

agg_df['SEGMENT'] = pd.qcut(agg_df['PRICE'], 4, labels=['D', 'C', 'B', 'A'])

print(agg_df.groupby('SEGMENT', observed=True).agg({'PRICE': ['mean', 'max', 'sum']}))

new_customer = "TUR_ANDROID_FEMALE_31_40"
segment = agg_df[agg_df['customers_level_based'] == new_customer]['SEGMENT'].values[0]
price_estimate = agg_df[agg_df['customers_level_based'] == new_customer]['PRICE'].values[0]

print(f"Segment: {segment}, Beklenen Gelir: {price_estimate}")

new_customer = "FRA_IOS_FEMALE_31_40"
segment = agg_df[agg_df['customers_level_based'] == new_customer]['SEGMENT'].values[0]
price_estimate = agg_df[agg_df['customers_level_based'] == new_customer]['PRICE'].values[0]

print(f"Segment: {segment}, Beklenen Gelir: {price_estimate}")