import requests
import json
import objectpath
import pandas as pd
data_main=pd.DataFrame(columns=["Name of the repository","Description","Forks","Stars count","Language"])
for i in range(1,10):
  params = (
      ('type', 'all'),
  )
  api_access_token = "6bc3e6193e4af0824f7f51ac348c45491be45fb4"
  response = requests.get(f'https://api.github.com/users/zulip/repos?page={i}&per_page=100',params=params, auth=('pratz0499', api_access_token))
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
data_main.to_csv("zulip.csv",index=False)
print(len(data_main))
