import  pandas as pd
import os


print(os.listdir("./data_df"))
df = pd.read_csv("./data_df/data150.csv")
for i in os.listdir("./data_df"):
    df = pd.concat([df,pd.read_csv(f"./data_df/{i}")],ignore_index=True)
for i in os.listdir("./data_df1"):
    df = pd.concat([df, pd.read_csv(f"./data_df1/{i}")], ignore_index=True)

df = df.drop_duplicates()
print(len(df))
print(df)
df.to_csv("data.csv",index=False)