import requests
import json
response = requests.get('https://api.github.com/repos/pratz0499/web-scraping/commits?since')
res=response.text
parsed=json.loads(res)
print(json.dumps(parsed,indent=4,sort_keys=True))
#print(parsed["date"])
#for i in parsed["date"]:
	#print(i)
for i in range(len(parsed)):
	for k,v in i.items():
		print(k,v)
