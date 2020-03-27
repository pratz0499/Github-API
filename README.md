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
Change the repository name from flutter to the desired repository name to extract the data. 
```bash
requests.get(f'https://api.github.com/users/flutter/repos?page={i}&per_page=100',params=params, auth=('pratz0499', api_access_token))
```
