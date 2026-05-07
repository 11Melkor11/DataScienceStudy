import pandas as pd

dt = pd.read_csv("tips.csv")

### Что делаем при получении файла
# print(dt.head())
# print(dt.shape)
# print(dt.info())
# print(dt.describe())

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

### crosstab
# cross_data = pd.crosstab(dt['sex'], dt['smoker'])
# print(cross_data)

dt['tip_out_of_bill'] = (dt['tip'] / dt['total_bill']) * 100

d = {'Yes': 1, 'No': 0}
dt['smoker'].map(d)

dt = dt.sort_values(by='total_bill', ascending=False)
print(dt.head())

