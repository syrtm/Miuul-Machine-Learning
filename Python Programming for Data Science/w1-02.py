#List Comprehensions

#Görev 1
import seaborn as sns

df = sns.load_dataset("car_crashes")

df.columns = [f"NUM_{col.upper()}" if df[col].dtype in ['int64', 'float64'] else col.upper() for col in df.columns]

print(df.columns.tolist())

#Görev 2
import seaborn as sns

df = sns.load_dataset("car_crashes")

df.columns = [f"{col.upper()}_FLAG" if "no" not in col.lower() else col.upper() for col in df.columns]

print(df.columns.tolist())

#Görev 3
import seaborn as sns
df = sns.load_dataset("car_crashes")

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]

new_df =df[new_cols]

print(new_df.head())