import numpy as np
import pandas as pd

pd.set_option("display.max_columns", 100)
pd.set_option("display.max_rows", 100)


dt = pd.read_csv("../data/tips.csv")

### Что делаем при получении файла
# print(type(dt))
# print(dt.head())
# print(dt.shape)
# print(dt.info())
# print(dt.describe())

# For bool means
# print(dt['time'].value_counts())
# print(dt['smoker'].value_counts(normalize=True))

###Loc and Iloc

#loc
# loc_dt = dt.loc[dt["tip"] > 5]
# print(loc_dt.head())

# loc_dt = dt.loc[29:35, ['total_bill', 'tip']]
# print(loc_dt.head())

#iloc
# iloc_dt = dt.iloc[24:, 3:5]
# print(iloc_dt.head())


# print(dt[dt['smoker'] == "Yes"]['total_bill'].mean())
# print(dt[dt['smoker'] == "No"]['total_bill'].mean())

# who_pay_more_women = dt[(dt['smoker'] == "Yes") & (dt['sex'] == 'Female')]['total_bill'].mean()
# print('smoke_women:\n', who_pay_more_women)
# who_pay_more_man = dt[(dt['smoker'] == "Yes") & (dt['sex'] == 'Male')]['total_bill'].mean()
# print('smoke_man:\n', who_pay_more_man)

# Функция к каждому столбцу
# print(dt.apply(np.max))
# print(dt.apply(np.min))

# print(help(dt.head()))

### можно группировать так
# qroup = dt.groupby("size")
# for data, sub_data in qroup:
#     print(data)
#
#     print("средний чек = ", sub_data['total_bill'].mean())
#     print("средние чаевые = ", sub_data['tip'].mean())

### но лучше так
# group = dt.groupby("size")[['total_bill', 'tip']].mean()
# print(group)
#
# agr_group = dt.groupby("size")[['total_bill', 'tip']].agg(np.median)
# print(agr_group)

### crosstab
# cross_data = pd.crosstab(dt['sex'], dt['smoker'])
# print(cross_data)

# dt['tip_out_of_bill'] = (dt['tip'] / dt['total_bill']) * 100
# #
# d = {'Yes': 1, 'No': 0}
# dt['smoker'].map(d)
#
# dt = dt.sort_values(by='total_bill', ascending=False)
# print(dt.head())

# print(dt.pivot_table(['total_bill', 'tip', 'size'], ['sex'], aggfunc=np.mean))

# columns_to_show = ['total_bill', 'tip']
# print(dt.groupby(['size'])[columns_to_show].agg([np.mean, np.std, np.min, np.max]))

