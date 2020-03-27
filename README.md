# Github-Log Analysis
The project is about analyzing data extracted from GitHub.
## Popularity Indexes
There are various Programming Language Popularity Indexes, among which PYPL and TIOBE indexes are the most prominently used. PYPL(Popularity of Programming Language Index) measures how often Language tutorials are googled while TIOBE index measures the sheer quantity of search engine hits. The results provided by these indexes are not reliable as their parameters are not based on industry deployed projects. This project focuses on parameters which will be more reliable. 

## Installation
```bash
pip install Pandas
pip install Numpy
pip install matplotlib
pip install seaborn
pip install scikit-learn
```
## Step 1:
Change the repository name from flutter to the desired repository name to extract the data in data_collection.py.
```bash
requests.get(f'https://api.github.com/users/flutter/repos?page={i}&per_page=100',params=params, auth=('pratz0499', api_access_token))
```
You can automate this process by setting a cron job. Note that We can authenticate the requests by creating a personal access token to get up to 5000 requests per hour. 
If Extracting more than 1 repository, then all the stored csv files need to be merged into single csv file.

## Step 2:
Change the path, where the merged csv file is stored in pylang.py.
```bash
df=pd.read_csv(r"D:\Organised\Projects\Minor Project\python_projects\github data\githubData\merge.csv",encoding = "ISO-8859-1",dtype={'Language': str},low_memory=False)
```
