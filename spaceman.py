import requests

def inSpace():
    """
    Takes no parameters.
    prints out a list of the astronaughts in space and which spacestation they are on.
    """
    url = 'http://api.open-notify.org/astros.json'

    r = requests.get(url)
    space = r.json()
    num = len(space['people'])

    print(f'The are {num} people currently in space, they are:')
    for people in space['people']:
        name = people['name']
        craft = people['craft']
        print(name + ' -->', craft + '.')

def main():
    inSpace()

if __name__ == '__main__':
    main()
