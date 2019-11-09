import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv(r"D:\Organised\Projects\Minor Project\python_projects\github data\githubData\mydataFromR.csv",encoding = "ISO-8859-1",dtype={'Language': str},low_memory=False)
df1=pd.read_csv(r"D:\Organised\Projects\Minor Project\python_projects\github data\githubData\trends.csv",encoding = "ISO-8859-1",dtype={'Language': str},low_memory=False)

merge=pd.concat([df,df1],sort=False)
new_data_set=merge.to_csv(r"D:\Organised\Projects\Minor Project\python_projects\github data\githubData\merge.csv",index=False,header=True)

unique=df['Language'].unique().tolist()
frequency_count=df['Language'].value_counts()

frequency_count.plot(kind='bar')
plt.show()
plt.close()




