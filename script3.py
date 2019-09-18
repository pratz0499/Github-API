import requests
import json
import objectpath


class github:
  def get_urls(self):
    headers = {'Accept': 'application/vnd.github.preview'}

    self.contributers= requests.get('http://api.github.com/repos/jreynolds01/RealtimeRDeployment/stats/contributors')
    self.commit_activity=requests.get('http://api.github.com/repos/jreynolds01/RealtimeRDeployment/stats/commit_activity')
    self.code_frequency=requests.get('http://api.github.com/repos/jreynolds01/RealtimeRDeployment/stats/code_frequency')
    self.participation=requests.get('http://api.github.com/repos/jreynolds01/RealtimeRDeployment/stats/participation')
    self.punch_card=requests.get('http://api.github.com/repos/jreynolds01/RealtimeRDeployment/stats/punch_card')
    self.followers= requests.get('http://api.github.com/users/:jreynolds01/followers')
    self.stars = requests.get('http://api.github.com/repos/jasonrudolph/keyboard', headers=headers)
    
    
  def view_json(self):
    #getting_json_output
    self.res_contributers=contributers.text
    self.res_commit_activity=commit_activity.text
    self.res_frequency=code_frequency.text
    self.res_participation=participation.text
    self.res_punchcard=punch_card.text
    self.res_followers=followers.text
    self.res_stars=stars.text
    

  def parse(self):
  
    self.parsed_contributers=json.loads(res_contributers)
    self.parsed_commit_activity=json.loads(res_commit_activity)
    self.parsed_code_frequency=json.loads(res_frequency)
    self.parsed_participation=json.loads(res_participation)
    self.parsed_punchcard=json.loads(res_punchcard)
    self.parsed_followers=json.loads(res_followers)
    self.parsed_stars=json.loads(res_stars)
    self.parsed_list=[parsed_contributers,parsed_commit_activity,parsed_code_frequency,parsed_participation,parsed_punchcard,parsed_followers]
    
    

    
  def json_fy(self):
    for self.i in self.parsed_list:
      print(json.dumps(self.i,indent=4,sort_keys=True))
    
  
    print(json.dumps(self.parsed_stars,indent=4,sort_keys=True))
    self.json_tree=objectpath.Tree(self.parsed_stars)
    self.parsed_stars=tuple(self.json_tree.execute('$..watchers_count'))
    print(self.parsed_stars)
   
a=github()
a.get_urls()
a.view_json()
a.parse()
a.json_fy()
  
