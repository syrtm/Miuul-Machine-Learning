import seaborn as sns

titanic_df = sns.load_dataset("titanic")

titanic_df.head()

titanic_df['sex'].value_counts()

titanic_df.nunique()

titanic_df['pclass'].nunique()

titanic_df[['pclass','parch']].nunique()

print(titanic_df['embarked'].dtype)

titanic_df['embarked'] = titanic_df['embarked'].astype('category')

print(titanic_df['embarked'].dtype)

titanic_df[titanic_df['embarked'] == 'C']

titanic_df[titanic_df['embarked'] != 'S']

titanic_df[(titanic_df['age'] < 30) & (titanic_df['sex'] == 'female')]

titanic_df[(titanic_df['fare'] > 500) | (titanic_df['age'] < 70)]

titanic_df.isnull().sum()

titanic_df.drop(columns=['who'], inplace=True)

mode_deck = titanic_df['deck'].mode()[0]
titanic_df['deck'] = titanic_df['deck'].fillna(mode_deck)

median_age = titanic_df['age'].median()
titanic_df['age'] = titanic_df['age'].fillna(median_age)

titanic_df.groupby(['pclass','sex']).agg({'survived':['sum','count','mean']})

titanic_df['age_flag'] = titanic_df['age'].apply(lambda x: 1 if x < 30 else 0)

tips_df = sns.load_dataset("tips")
tips_df.head()

tips_df.groupby('time').agg({'total_bill': ['sum', 'min', 'max', 'mean']})

tips_df.groupby(['day','time']).agg({'total_bill': ['sum', 'min', 'max', 'mean']})

tips_df[(tips_df['time'] == 'Lunch') & (tips_df['sex'] == 'Female')].groupby('day').agg({'total_bill': ['sum', 'min', 'max', 'mean'], 'tip': ['sum', 'min', 'max', 'mean']})

tips_df.loc[(tips_df['size'] < 3) & (tips_df['total_bill'] > 10), ['total_bill', 'tip']].mean()

tips_df['total_bill_tip_sum'] = tips_df['total_bill'] + tips_df['tip']

tips_df.sort_values('total_bill_tip_sum', ascending = False).head(30)

