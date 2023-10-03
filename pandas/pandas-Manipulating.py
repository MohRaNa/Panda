import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

#print(reviews.set_index("title"))

#print(reviews.country == 'Italy')

#print(reviews.loc[reviews.country == 'Italy'])

#print(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)])

#print(reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)])

#print(reviews.loc[reviews.country.isin(['Italy', 'France'])])

print(reviews.loc[reviews.price.notnull()])

