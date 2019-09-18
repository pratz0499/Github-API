import requests
import json

headers = {
    'Accept': 'application/vnd.github.preview',
}





contributers= requests.get('http://api.github.com/repos/jreynolds01/RealtimeRDeployment/stats/contributors')
commit_activity=requests.get('http://api.github.com/repos/jreynolds01/RealtimeRDeployment/stats/commit_activity')
code_frequency=requests.get('http://api.github.com/repos/jreynolds01/RealtimeRDeployment/stats/code_frequency')
participation=requests.get('http://api.github.com/repos/jreynolds01/RealtimeRDeployment/stats/participation')
punch_card=requests.get('http://api.github.com/repos/jreynolds01/RealtimeRDeployment/stats/punch_card')
followers= requests.get('http://api.github.com/users/:jreynolds01/followers')
stars = requests.get('http://api.github.com/repos/jasonrudolph/keyboard', headers=headers)



res_contributers=contributers.text
res_commit_activity=commit_activity.text
res_frequency=code_frequency.text
res_participation=participation.text
res_punchcard=punch_card.text
res_followers=followers.text
res_stars=stars.text


parsed_contributers=json.loads(res_contributers)
parsed_commit_activity=json.loads(res_commit_activity)
parsed_code_frequency=json.loads(res_frequency)
parsed_participation=json.loads(res_participation)
parsed_punchcard=json.loads(res_punchcard)
parsed_followers=json.loads(res_followers)
parsed_stars1=json.loads(res_stars)

#print(json.dumps(parsed,indent=4,sort_keys=True))
#print(json.dumps(parsed1,indent=4,sort_keys=True))
print(json.dumps(parsed_stars1,indent=4,sort_keys=True))

parsed_stars=tuple(json_tree.execute('$..owner[watchers_count]'))
print(len(parsed_stars))
for i in commit_time:
	print(i)
