import requests
import json
response = requests.get('https://api.github.com/repos/pratz0499/web-scraping/commits?since')
res=response.text
parsed=json.loads(res)
print(json.dumps(parsed,indent=4,sort_keys=True))
