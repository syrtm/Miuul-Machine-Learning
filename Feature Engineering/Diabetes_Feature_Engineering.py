import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,roc_auc_score
from sklearn.model_selection import GridSearchCV, cross_validate
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import warnings
warnings.simplefilter(action="ignore")

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.3f' % x)


df = pd.read_csv("datasets/diabetes.csv")


def check_data(df):
    print("Veri Seti Şekli: ", df.shape)
    print("Veri Tipleri:\n",df.dtypes)
    print("Eksik Veri Sayısı:\n",df.isnull().sum())
    print("Benzersiz Değer Sayıları:\n",df.nunique())
    print("İlk 5 gözlem:\n",df.head())
    print("Özet İstatistikler:\n",df.describe().T)

check_data(df)


def grab_col_names(dataframe, cat_th=10, car_th=20):
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtype == 'O']
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and dataframe[col].dtype != 'O']
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and dataframe[col].dtype == "O"]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in dataframe.columns if dataframe[col].dtype != "O" and col not in num_but_cat]

    return cat_cols, num_cols, cat_but_car, num_but_cat

cat_cols, num_cols, cat_but_car, num_but_cat = grab_col_names(df)
print("Kategorik Değişkenler:", cat_cols)
print("Numerik Değişkenler:", num_cols)
print("Kategorik Ancak Kardinal Değişkenler:", cat_but_car)
print("Numerik Ancak Kategorik Değişkenler:", num_but_cat)


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show()

for col in cat_cols:
    cat_summary(df, col, plot=True)


def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist(bins=20)
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show()

for col in num_cols:
    num_summary(df, col, plot=True)


def target_summary_with_cat (dataframe, target, cat_cols):
    for col in cat_cols:
        print(pd.DataFrame({col: dataframe.groupby(col)[target].mean()}))

target_summary_with_cat(df, "Outcome", cat_cols)


def target_summary_with_num(dataframe, target, num_cols):
    for col in num_cols:
        print(f"{col} - Outcome Ortalamaları:\n", dataframe.groupby(target).agg({col: "mean"}), "\n")

target_summary_with_num(df, "Outcome", num_cols)


def replace_outliers (df, col):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    low_limit = q1 - 1.5 * iqr
    up_limit = q3 + 1.5 * iqr
    df.loc[(df[col] < low_limit), col] = low_limit
    df.loc[(df[col] > up_limit), col] = up_limit

for col in num_cols:
    replace_outliers(df, col)


def missing_values_table(dataframe):
    missing_data = dataframe.isnull().sum()
    missing_ratio = (dataframe.isnull().sum() / dataframe.shape[0]) * 100
    missing_df = pd.concat([missing_data, missing_ratio], axis=1, keys=['Eksik Değer Sayısı', '% Oran'])
    print(missing_df[missing_df['Eksik Değer Sayısı'] > 0])
    return missing_df[missing_df['Eksik Değer Sayısı'] > 0]

# İlk eksik gözlem analizi
print("İlk Eksik Gözlem Analizi:")
missing_values_table(df)

zero_columns = [col for col in df.columns if (df[col].min() == 0 and col not in ["Pregnancies", "Outcome"])]
for col in zero_columns:
    df[col] = df[col].replace(0, np.nan)

# 0 değerlerini NaN yaptıktan sonra eksik gözlem analizi
print("\n0 Değerlerini NaN Olarak Değiştirdikten Sonra Eksik Gözlem Analizi:")
missing_values_table(df)

df.fillna(df.median(), inplace=True)

missing_values_table(df) # şimdi çuk güzel oldu :)


# Korelasyon Matrisi
plt.figure(figsize=(12, 8))
sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Korelasyon Matrisi (Numerik Değişkenler)")
plt.show()
