import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Завантажуємо дані 
df = pd.read_excel('Sample - Superstore.xls')

# 2. Перетворюємо дати та обрізаємо їх до кварталу
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Quarter'] = df['Order Date'].dt.to_period('Q')

# 3. Визначаємо когорту для кожного клієнта
df_first_order = df.groupby('Customer ID')['Quarter'].min().reset_index()
df_first_order.columns = ['Customer ID', 'Cohort']
df = pd.merge(df, df_first_order, on='Customer ID')

# 4. Розраховуємо вік когорти в кварталах
df['Cohort Age'] = (df['Quarter'] - df['Cohort']).apply(lambda x: x.n)

# 5. Групуємо дані та рахуємо кумулятивний прибуток
cohort_data = df.groupby(['Cohort', 'Cohort Age'])['Profit'].sum().reset_index()

# 6. Створюємо матрицю для теплової карти
cohort_matrix = cohort_data.pivot_table(index='Cohort', columns='Cohort Age', values='Profit')
cumulative_ltv = cohort_matrix.cumsum(axis=1)

# 7. Візуалізуємо теплову карту
plt.figure(figsize=(12, 8))
sns.heatmap(cumulative_ltv, annot=True, fmt=".1f", cmap="YlGnBu")
plt.title('Кумулятивна LTV за когортами')
plt.ylabel('Квартал долучення (Когорта)')
plt.xlabel('Вік когорти (Квартал)')
plt.savefig('cumulative_ltv_heatmap.png')