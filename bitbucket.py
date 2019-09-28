curl -s "https://api.bitbucket.org/2.0/repositories/bmsce2019ccplabpb/?page=1"> temp.txt

fp=open("temp.txt")
x=json.load(fp)
for i in x['values']:
           print(i['links']['clone'][0]['href'])
