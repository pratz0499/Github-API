import requests
import json
import objectpath
import pandas as pd
data_main=pd.DataFrame(columns=["Name of the repository","Description","Forks","Stars count","Language"])
for i in range(1,10):
  params = (
      ('type', 'all'),
  )
  api_access_token = "4f716bcc0b9f3fc182daabc7d22e7e5e967816fd" 
  response = requests.get(f'https://api.github.com/users/flutter/repos?page={i}&per_page=100',params=params, auth=('pratz0499', api_access_token))
  res=response.text
  parsed=json.loads(res)
  #print(json.dumps(parsed,indent=4, sort_keys=True))
  json_tree=objectpath.Tree(parsed)
  name=tuple(json_tree.execute('$..full_name'))
  description=tuple(json_tree.execute('$..description'))
  stars=tuple(json_tree.execute('$..stargazers_count'))
  forks=tuple(json_tree.execute('$..forks'))
  language=tuple(json_tree.execute('$..language'))
  # print(len(name))

  data=pd.DataFrame(columns=["Name of the repository","Description","Forks","Stars count","Language"])
  data["Name of the repository"]=name
  data["Description"]=description
  data["Forks"]=forks
  data["Stars count"]=stars
  data["Language"]=language
  data_main = data_main.append([data])
data_main.to_csv("flutter.csv",index=False)
print(len(data_main))
