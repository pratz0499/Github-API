import numpy as np
import pandas as pd
import scipy
from io import StringIO
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

class github:
    def data(self):
        self.df=pd.read_csv(r"D:\Organised\Projects\Minor Project\python_projects\github data\githubData\merge.csv",encoding = "ISO-8859-1",dtype={'Language': str},low_memory=False)
    
    def transformer(self):
        self.categorical_features = ['Forks','Stars_count','watchers','downloads']
        self.categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent', fill_value=None)),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    def language(self):
        self.lang=self.df['Language'].str.strip().value_counts()
        self.total_lang=self.lang.sum()
        self.percent_lang=self.lang.apply(lambda x: 100*(x/self.total_lang))
    
    def forks(self):
        self.clean_forks=self.df[pd.to_numeric(self.df['Forks'], errors='coerce').notnull()]
        self.aggregated =self.clean_forks.groupby('Language').agg({'Forks':'count'}).reset_index()
        self.sum_ag =self.aggregated["Forks"].sum()
        self.aggregated["new"]=self.aggregated["Forks"].apply(lambda x: 100*(x/self.sum_ag))

    def stars(self):
        self.clean_stars=self.df[pd.to_numeric(self.df['Stars_count'], errors='coerce').notnull()]
        self.aggregated_stars=self.clean_stars.groupby('Language').agg({'Stars_count':'count'}).reset_index()
        self.sum_ags=self.aggregated_stars["Stars_count"].sum()
        self.aggregated_stars["new"]=self.aggregated_stars["Stars_count"].apply(lambda x: 100*(x/self.sum_ags))

    def watchers(self):
        self.clean_watchers=self.df[pd.to_numeric(self.df['watchers'], errors='coerce').notnull()]
        self.aggregated_watchers=self.clean_watchers.groupby('Language').agg({'watchers':'count'}).reset_index()
        self.sum_agw=self.aggregated_watchers["watchers"].sum()
        self.aggregated_watchers["new"]=self.aggregated_watchers["watchers"].apply(lambda x: 100*(x/self.sum_agw))

    def downloads(self):
        self.clean_downloads=self.df[pd.to_numeric(self.df['downloads'], errors='coerce').notnull()]
        self.aggregated_downloads=self.clean_downloads.groupby('Language').agg({'downloads':'count'}).reset_index()
        self.sum_agd=self.aggregated_downloads["downloads"].sum()
        self.aggregated_downloads["new"]=self.aggregated_downloads["downloads"].apply(lambda x: 100*(x/self.sum_agd))

    def plot(self):
        #language plot
        self.bar1=self.percent_lang.head(20).plot(x="Languages",y="percent_lang",kind='bar')
        plt.show()
        plt.close()

        #forks plot
        self.plot_data={'Languages':self.aggregated['Language'],
      'Fork': self.aggregated['new']}
        self.plot_data=pd.DataFrame(self.plot_data)
        self.plot_data =self.plot_data.sort_values("Fork")
        self.bar2=self.plot_data.tail(20).plot(x="Languages",y="Fork", kind='bar')
        plt.show()
        plt.close()

        #Stars plot
        self.plot_data1={'Languages':self.aggregated_stars['Language'],
      'Stars_count':self.aggregated_stars['new']}
        self.plot_data1=pd.DataFrame(self.plot_data1)
        self.plot_data1 =self.plot_data1.sort_values("Stars_count")
        self.bar3=self.plot_data1.tail(20).plot(x="Languages",y="Stars_count", kind='bar')
        plt.show()
        plt.close()

        #watchers plot
        self.plot_data2={'Languages':self.aggregated_watchers['Language'],
      'watchers':self.aggregated_watchers['new']}
        self.plot_data2=pd.DataFrame(self.plot_data2)
        self.plot_data2 =self.plot_data2.sort_values("watchers")

        self.bar4=self.plot_data2.tail(20).plot(x="Languages",y="watchers", kind='bar')
        plt.show()
        plt.close()

        #downloads plot
        self.plot_data3={'Languages':self.aggregated_downloads['Language'],
      'downloads':self.aggregated_downloads['new']}
        self.plot_data3=pd.DataFrame(self.plot_data3)
        self.plot_data3 =self.plot_data3.sort_values("downloads")
        self.bar5=self.plot_data3.tail(20).plot(x="Languages",y="downloads", kind='bar')
        plt.show()
        plt.close()

    



a=github()
a.data()
a.transformer()
a.language()
a.forks()
a.stars()
a.watchers()
a.downloads()
a.plot()
