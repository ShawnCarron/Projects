import requests

url = 'http://api.open-notify.org/astros.json'

r = requests.get(url)
space = r.json()
num = len(space['people'])

print(f'The are {num} people currently in space, they are:')
for people in space['people']:
    name = people['name']
    craft = people['craft']
    print(name + ', on the', craft + '.')
