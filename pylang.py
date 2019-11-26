import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


df=pd.read_csv(r"D:\Organised\Projects\Minor Project\python_projects\github data\githubData\merge.csv",encoding = "ISO-8859-1",dtype={'Language': str},low_memory=False)
#Language plot
lang=df['Language'].str.strip().value_counts()
total_lang=lang.sum()
percent_lang=lang.apply(lambda x: 100*(x/total_lang))

lang1 = pd.DataFrame({'Language':percent_lang.head(10).keys().tolist(),'percent':percent_lang.head(10).values.tolist()})
lang1["Language"] = lang1["Language"].str.strip()
bar1=lang1.head(10).plot(x="Language",y="percent",kind='bar')
#forks plot
clean_forks=df[pd.to_numeric(df['Forks'], errors='coerce').notnull()]
aggregated = clean_forks.groupby('Language').agg({'Forks':'count'}).reset_index()
sum_ag = aggregated["Forks"].sum()
aggregated["new"]=aggregated["Forks"].apply(lambda x: 100*(x/sum_ag))
plot_data={'Language':aggregated['Language'],
      'Fork': aggregated['new']}
plot_data=pd.DataFrame(plot_data)
plot_data = plot_data.sort_values("Fork")

plot_data["Language"] = plot_data["Language"].str.strip()

s1 = pd.merge(lang1,plot_data.drop_duplicates(subset="Language",keep="first"),how="inner",on=["Language"])
bar2=s1.tail(10).plot(x="Language",y="Fork", kind='bar')

#stars plot
clean_stars=df[pd.to_numeric(df['Stars_count'], errors='coerce').notnull()]
aggregated_stars=clean_stars.groupby('Language').agg({'Stars_count':'count'}).reset_index()
sum_ags=aggregated_stars["Stars_count"].sum()
aggregated_stars["new"]=aggregated_stars["Stars_count"].apply(lambda x: 100*(x/sum_ags))
plot_data1={'Language':aggregated_stars['Language'],
      'Stars_count': aggregated_stars['new']}
plot_data1=pd.DataFrame(plot_data1)
plot_data1 = plot_data1.sort_values("Stars_count")

plot_data1["Language"] = plot_data1["Language"].str.strip()

s1 = pd.merge(s1,plot_data1.drop_duplicates(subset="Language",keep="first"),how="inner",on=["Language"])
bar3=s1.tail(10).plot(x="Language",y="Stars_count", kind='bar')

#watchers plot
clean_watchers=df[pd.to_numeric(df['watchers'], errors='coerce').notnull()]
aggregated_watchers=clean_watchers.groupby('Language').agg({'watchers':'count'}).reset_index()
sum_agw=aggregated_watchers["watchers"].sum()
aggregated_watchers["new"]=aggregated_watchers["watchers"].apply(lambda x: 100*(x/sum_agw))
plot_data2={'Language':aggregated_watchers['Language'],
      'watchers': aggregated_watchers['new']}
plot_data2=pd.DataFrame(plot_data2)
plot_data2 = plot_data2.sort_values("watchers")


plot_data2["Language"] = plot_data2["Language"].str.strip()
s1 = pd.merge(s1,plot_data2.drop_duplicates(subset="Language",keep="first"),how="inner",on=["Language"])
bar4=s1.tail(10).plot(x="Language",y="watchers", kind='bar')

#downloads plot
clean_downloads=df[pd.to_numeric(df['downloads'], errors='coerce').notnull()]
aggregated_downloads=clean_downloads.groupby('Language').agg({'downloads':'count'}).reset_index()
sum_agd=aggregated_downloads["downloads"].sum()
aggregated_downloads["new"]=aggregated_downloads["downloads"].apply(lambda x: 100*(x/sum_agd))
plot_data3={'Language':aggregated_downloads['Language'],
      'downloads': aggregated_downloads['new']}
plot_data3=pd.DataFrame(plot_data3)
plot_data3 = plot_data3.sort_values("downloads")


plot_data3["Language"] = plot_data3["Language"].str.strip()
s1 = pd.merge(s1,plot_data3.drop_duplicates(subset="Language",keep="first"),how="inner",on=["Language"])
bar5=s1.tail(10).plot(x="Language",y="downloads", kind='bar')
langs = s1["Language"].values.tolist()
s2 = s1.drop(["Language"],axis=1)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
s1_scaled = pd.DataFrame(scaler.fit_transform(s2),columns=s2.columns)
N = len(langs)
ind = np.arange(N)
perce = s1_scaled["percent"].values.tolist()
forke = s1_scaled["Fork"].values.tolist()
stars = s1_scaled["Stars_count"].values.tolist()
watchers = s1_scaled["watchers"].values.tolist()
downs = s1_scaled["downloads"].values.tolist()
width = 0.2
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(ind-(width),perce,width,color='r',label="Percent",align="center")
ax.bar(ind,forke,width,color='b',label="Fork",align="center")
# ax.bar(ind,perce,stars,color='g',label="Stars_count",align="center")
ax.bar(ind+width,watchers,width,color='y',label="Watchers",align="center")
ax.bar(ind+(2*width),downs,width,color='b',label="downloads",align="center")
ax.set_xticks(ind+width)
ax.set_xticklabels(langs)
ax.autoscale(tight=True)
ax.legend()
plt.show()
