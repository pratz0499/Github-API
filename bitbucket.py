import requests
import json
count=0
for j in range(1,4):
    params = (
        ('page', str(j)),
    )

    response = requests.get('https://api.bitbucket.org/2.0/repositories/bmsce2019ccplabpb/', params=params)
    res=response.text


    with open('repo.txt',"w") as f:
        f.write(res)

    fp=open('repo.txt','r')
    x=json.loads(fp.read())

    for i in x['values']:
        print(i['links']['clone'][0]['href'])
        count=count+1
    print("Next page")
print(count)
