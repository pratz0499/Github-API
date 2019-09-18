import requests
import json
import objectpath


class github:
  def __init__(self):
    self.name_list=[]
    self.repo_list=[]
  def get_user_and_repositry(self):
    
      self.name=str(input("Enter the Username: "))
      self.name_list.append(self.name)

      self.repositry=str(input("Enter the Repositry Name: "))
      self.repo_list.append(self.repositry)
    
  def get_urls(self):
    headers = {'Accept': 'application/vnd.github.preview'}
    
    for i in self.name_list:
      for j in self.repo_list:
        self.contributers= requests.get('http://api.github.com/repos/i/j/stats/contributors')
        self.commit_activity=requests.get('http://api.github.com/repos/i/j/stats/commit_activity')
        self.code_frequency=requests.get('http://api.github.com/repos/i/j/stats/code_frequency')
        self.participation=requests.get('http://api.github.com/repos/i/j/stats/participation')
        self.punch_card=requests.get('http://api.github.com/repos/i/j/stats/punch_card')
        self.followers= requests.get('http://api.github.com/users/i/followers')
    
    self.stars = requests.get('http://api.github.com/repos/jasonrudolph/keyboard', headers=headers)
    
    
  def view_json(self):
    #getting_json_output of contributers
    self.res_contributers=contributers.text
    #getting_json_output of commit activites
    self.res_commit_activity=commit_activity.text
    #getting_json_output of code_frequency
    self.res_frequency=code_frequency.text
    #getting_json_output of participation
    self.res_participation=participation.text
    #getting_json_output of punch_cards
    self.res_punchcard=punch_card.text
    #getting_json_output of followers
    self.res_followers=followers.text
    #getting_json_output of stars
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
a.get_user_and_repositry()
a.get_urls()
a.view_json()
a.parse()
a.json_fy()
  
