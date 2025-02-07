import pandas as pd
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_column',50)

df_csv = pd.read_csv("C:/Users/PRANAV SHARMA/OneDrive/Desktop/ms office files/A669580010_15709_7_2025_sales dataset.csv")
print("\nDataFrame Info : ")
print(df_csv.info())
print("\nSummary Statistics:\n ", df_csv.describe())
print("\n Functions: ")

max_sales = df_csv['Sales_Amt'].max()
print("maximum amount in sales amount: ",max_sales)
max_sales
retval = df_csv[df_csv['Sales_Amt'] == max_sales]
print("Details of elements with maximum sales: \n",retval)
df_csv
print("\n")
fnc = df_csv[df_csv['Sales_Amt']>1000]
print("Details of financial Department with sales greater than 1000: \n",fnc)
df_csv
