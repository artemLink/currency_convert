import requests

url = 'https://cdn.cur.su/api/latest.json'
data = requests.get(url).json()['rates']
keys = list(data.keys())

print(keys)