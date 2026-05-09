import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 100)
pd.set_option("display.max_rows", 100)
pd.set_option('display.width', 200)

df = pd.read_csv("titanic.csv")
print(df.head())

### Всего 891 пассажир, выжило - 0.383838, большинсвто пассажиров - 2 класс (средний);
### Средний возраст - 29.699118, самый молодой пассажир - 0.420000, самый старый - 80.000000
print(df.describe())

### Таблица весит 118.9 KB
print(df.info())

### На корабле было больше мужчин, чем женщин
print(df['Sex'].value_counts())

### Большинство погрузилось на корабль с причала S (644), меньше всего с причала Q (77)
print(df['Embarked'].value_counts())

### Из 577 мужчин выжило - 109 или 0.188908
print(df[df["Sex"] == 'male']['Survived'].agg([np.sum, np.mean]))

### Из 314 женщин выжило - 233 или 0.742038
print(df[df["Sex"] == 'female']['Survived'].agg([np.sum, np.mean]))

### Средний возраст мужчин на борту - 22
print(df[df['Sex'] == 'male']['Age'].mean)

### Средний возраст женщин на борту - 38
print(df[df['Sex'] == 'female']['Age'].mean)


### 0.742038 выживших женщин были возраста - 27.915709, их класс был - 2.159236
### 0.188908 выживших мужчин были возраста - 30.726645, их класс был - 2.389948
group_info = df.groupby('Sex')[['Survived', 'Age', 'Pclass']].mean()
print(group_info.head())

a = {'male': 1, 'female': 0}
df['Sex'] = df['Sex'].map(a)
print(df.head())

### 1 класс - 0.564815 (мужчин больше), выжило - 0.629630, средний возраст - 38.233441, средняя цена билета - 84.154687
### 2 класс - 0.586957 (мужчин больше), выжило - 0.472826, средний возраст - 29.877630, средняя цена билета - 20.662183
### 3 класс - 0.706721 (мужчин больше), выжило - 0.242363, средний возраст - 25.140620, средняя цена билета - 13.675550
group = df.groupby('Pclass')[['Sex', 'Survived', 'Age', 'Fare']].mean()
print(group)

### Мужчин 2-го класс
print(df[(df['Pclass'] == 2) & (df['Sex'] == 1)]['Sex'].count())

### Медиана и стандартное отклонение цены билета (Fare)
median_fare = np.median(df['Fare'])
std_fare = np.std(df['Fare'])
print(round(median_fare, 2))
print(round(std_fare, 2))

### Выживаемость молодых < 30, выживаемость стариков > 60
print(round(df[df['Age'] < 30.0]['Survived'].mean(), 3))
print(round(df[df['Age'] > 60.0]['Survived'].mean(), 3))

### Самое популярное имя среди мужчин
popular_name_search = df[df['Sex'] == 1]['Name']
d = {}

for name in popular_name_search:
    only_name = name.split(',')[0]

    if only_name in d:
        d[only_name] += 1
    else:
        d[only_name] = 1

names = pd.Series(d)
filtered_names = names[names >= 4]
print(filtered_names)


### Итоговая группировка
### Женщины 1 класса были в среднем - 34.611765 лет, из них выжило - 0.968085, цена билета - 106.125798
### Мужчин 1 класса были в среднем - 41.281386 лет, из них выжило - 0.368852, цена билета - 67.226127
### Женщины 2 класса были в среднем - 28.722973 лет, из них выжило - 0.921053, цена билета - 21.970121
### Мужчин 2 класса были в среднем - 30.740707 лет, из них выжило -  0.157407, цена билета - 19.741782
### Женщины 3 класса были в среднем - 21.750000 лет, из них выжило - 0.500000, цена билета - 16.118810
### Мужчин 3 класса были в среднем - 26.507589 лет, из них выжило - 0.135447, цена билета - 12.661633
age_groups = df.groupby(['Pclass', 'Sex'])[['Age', 'Survived', 'Fare']].mean()
print(age_groups)







