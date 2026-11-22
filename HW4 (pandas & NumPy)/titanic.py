import pandas as pd
import numpy as np

n = int(input('Сколько строк таблицы показать: '))
df = pd.DataFrame(pd.read_csv('tested.csv'))
pd.set_option('display.max_columns', None)

print(f'7. Первые {n} строк(и):\n{df.head(n)}')
print(f'8. Последние 5 строк\n{df.tail(5)}')
shape_before = df.shape
print(f'9. Размер таблицы: {shape_before}')
print(f'10. Названия столбцов таблицы: {df.columns.tolist()}')
print(f'11. Типы данных каждого столбца\n{df.dtypes.to_string()}')
num_pr = ['Age', 'SibSp', 'Parch', 'Fare']
kat_pr = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
print(f'12.1 Список числовых признаков {num_pr}')
print(f'12.2 Список категориальных признаков {kat_pr}')
print(f'13.\n{df[num_pr].agg(['mean', 'median', 'min', 'max', 'std'])}')
print(f'14. Количество пассажиров каждого класса:\n{df['Pclass'].value_counts().sort_index().to_string()}')
print(f'15. Количество уникальных значений в cтолбце Embarked: {df['Embarked'].nunique()}')

print(f'16. Количество пропусков в каждом столбце:\n{df.isna().sum()}')
per_skips = (df.isna().sum() / len(df)) * 100
print(f'17. Процент пропусков:\n{per_skips}')
max_skips = df.isna().sum().idxmax()
print(f'18. Столбец с максимальным количеством пропусков: {max_skips}')
print('19. Данные для Age до заполнения пропусков:')
age_before = {
    'Среднее арифметическое': df['Age'].mean(),
    'Медиана': df['Age'].median(),
    'Минимальный возраст': df['Age'].min(),
    'Максимальный возраст': df['Age'].max(),
    'Стандартное отклонение': df['Age'].std(),
    'Количество известных значений': df['Age'].count()
}
print(pd.DataFrame({'Данные': age_before}))
df['Age'] = df['Age'].fillna(df['Age'].median()) # 20
print('21. Данные для Age после заполнения пропусков:')
age_after = {
    'Среднее арифметическое': df['Age'].mean(),
    'Медиана': df['Age'].median(),
    'Минимальный возраст': df['Age'].min(),
    'Максимальный возраст': df['Age'].max(),
    'Стандартное отклонение': df['Age'].std(),
    'Количество известных значений': df['Age'].count()
}
print(pd.DataFrame({'Данные': age_after}))

print('22. Сравнение данных до и после')
print(pd.DataFrame({'До': age_before, 'После': age_after}))

df = df.dropna(subset=['Embarked']) # 23

cab_miss = (df['Cabin'].isna().mean() * 100).round(2)
print(f'24. Доля пропусков в Cabin: {cab_miss}')
if cab_miss > 50:
    df = df.drop(columns=['Cabin'])
    print('Столбец Cabin удален')

print(f'25. Проверка оставшихся пропусков:\n{df.isna().sum()}')
df = df.dropna(subset=['Fare'])
print(f'26. Размер таблицы ДО: {shape_before}, ПОСЛЕ: {df.shape}')

survived = df['Survived'].to_numpy()
sex = df['Sex'].to_numpy()
age = df['Age'].to_numpy()
fare = df['Fare'].to_numpy()

print(f'31. Общий процент выживших: {(np.mean(survived == 1) * 100).round(2)}%')

print(f'32\nПроцент выживших мужчин: {(np.mean(survived[sex == 'male'] == 1) * 100).round(2)}%,\n'
f'Процент выживших женщин: {(np.mean(survived[sex == 'female'] == 1) * 100).round(2)}%')

print(f'33\nСредний возраст мужчин: {(np.mean(age[sex == 'male'])).round(2)},'
      f'\nСредний возраст женщин: {(np.mean(age[sex == 'female'])).round(2)}')

m_surv_age = age[(sex == 'male') & (survived == 1)]
m_died_age = age[(sex == 'male') & (survived == 0)]
f_surv_age = age[(sex == 'female') & (survived == 1)]
f_died_age = age[(sex == 'female') & (survived == 0)]

res_34 = pd.DataFrame({
    'Мужчины': [(np.sum(m_surv_age) / m_surv_age.size).round(2) if m_surv_age.size else 'Нет данных',
        (np.sum(m_died_age) / m_died_age.size).round(2) if m_died_age.size else 'Нет данных'],
    'Женщины': [(np.sum(f_surv_age) / f_surv_age.size).round(2) if f_surv_age.size else 'Нет данных',
        (np.sum(f_died_age) / f_died_age.size).round(2) if f_died_age.size else 'Нет данных']},
    index=['Средний возраст выживших', 'Средний возраст погибших'])

print(f'34. Средний возраст\n{res_34}')

print(f'35.\nМинимальная стоимость билета: {(np.min(fare)).round(2)},\n'
      f'Максимальная стоимость билета: {(np.max(fare)).round(2)},\nСредняя стоимость: {(np.mean(fare)).round(2)}')

print(f'36. Стандартное отклонение возраста: {(np.std(age)).round(2)}\n')

print('Фильтрация данных')
man301 = df[(df['Sex'] == 'male') & (df['Age'] > 30) & (df['Pclass'] == 1)]
print(f'Количество мужчин старше 30 лет в 1 классе: {len(man301)}')
print(f'Первые 10 строк:\n{man301.head(10)}')

child_woman_surv = df[((df['Sex'] == 'female') | (df['Age'] < 18)) & (df['Survived'] == 1)]
print(f'Количество выживших детей и женщин: {len(child_woman_surv)}')

mean_fare3 = df[df['Pclass'] == 3]['Fare'].mean()
tickets = df[(df['Pclass'] == 3) & (df['Fare'] > mean_fare3)]
print(f'Количество пассажиров 3 класса с билетами дороже среднего по классу: {len(tickets)}')

ps2040 = df[((20 <= df['Age']) & (df['Age'] <= 40)) & (df['Embarked'] == 'S')]
print(f'Количество пассажиров 20-40 лет из порта S: {len(ps2040)}\n')


print('Группировка и агрегирование')
g_pclass_sex = df.groupby(['Pclass', 'Sex']).agg(pass_cnt=('PassengerId', 'count'), mean_age=('Age', 'mean'),
    survived=('Survived', lambda x: x.mean() * 100), mean_cost=('Fare', 'mean')).round(2)

print(f'37. Группировка по классу и полу:\n{g_pclass_sex}')

g_embarked = df.groupby('Embarked').agg(pass_cnt=('PassengerId', 'count'),
    survived=('Survived', lambda x: x.mean() * 100)).round(2)

print(f'38. Группировка по порту посадки:\n{g_embarked}')

g_class_max = df.groupby('Pclass')['Survived'].mean().idxmax()
print(f'39. Класс с наибольшей долей выживших: {g_class_max}')


g_pclass_sex.to_csv('titanic_statistics.csv')

df.to_csv('titanic_processed.csv', index=False)
processed = pd.DataFrame(pd.read_csv('titanic_processed.csv'))
print(f'Проверка размера titanic_processed.csv: {processed.shape}')

