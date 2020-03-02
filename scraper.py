from bs4 import BeautifulSoup

BASE_URL = 'www.twitch.tv/'

def get_channel_name():
    channel_name = input('Please enter the channel name you want to scrape: ')
    if channel_name.isalnum() and len(channel_name) >= 3 and len(channel_name) < 25: #Replace by a regEX
        return BASE_URL + channel_name
    print('Incorrect username. Stop.')
    return None

def get_ressource_type():
    ressource = input('Please make a choice between:\n1. Clips\n2. Videos\nYour choice: ')
    if ressource == '1':
        ressource = '/clips?filter=clips'
    elif ressource == '2':
        ressource = '/videos'
    else:
        print('Incorrect input. Stop.')
        return None
    return ressource