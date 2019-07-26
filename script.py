import requests
response = requests.get('https://api.github.com/repos/pratz0499/web-scraping/commits')
print(response.text)
