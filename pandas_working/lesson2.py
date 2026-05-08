import warnings
warnings.simplefilter("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# SERIES
# salaries = pd.Series([17000, 25000, 29000, 54000], index=['Mark', 'Carl', 'Klark', 'Anne'])
# print(salaries[salaries > 45000])

# salaries['Mike'] = np.nan
# salaries.fillna(salaries.median(), inplace=True)
# print(salaries)

# print(np.exp(salaries))

# DATAFRAME
df = pd.DataFrame([[5700, 6806, 4508, 3056, 8602],
                        [5200, 6100, 3700, 2100, 2580],
                        [3500, 4800, 2300, 1680, 1990],
                        [2600, 3400, 1430, 980, 1236],
                        [2390, 2700, 950, 740, 680]],
                  index=['2024', '2023', '2022', '2021', '2020'],
                  columns=['RUBYUSDT', 'AREUSDT', 'ETHUSDT', 'ORTUSDT', 'BIPEUSDT'])
# print(df)

df['TRELUSDT'] = np.nan
df['YUTUSDT'] = np.nan
# print(df)

# print(df.isnull())
# print(df.fillna(58))
# print(df.dropna(how='any'))
