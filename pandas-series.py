import pandas as pd

serie1 = pd.Series([1, 2, 3, 4, 5])
print(serie1)

serie2 = pd.Series([30, 35, 40], index=['2021 Sales', '2022 Sales', '2023 Sales'], name='Product A')
print(serie2)
