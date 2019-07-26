import requests
import json
import objectpath
response = requests.get('https://api.github.com/repos/pratz0499/web-scraping/commits?since')
res=response.text
parsed=json.loads(res)
#print(json.dumps(parsed,indent=4,sort_keys=True))
json_tree=objectpath.Tree(parsed)
commit_time=tuple(json_tree.execute('$..date'))
for i in commit_time:
	print(i)
