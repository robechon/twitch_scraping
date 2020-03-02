from bs4 import BeautifulSoup

def get_url():
    base_url = 'www.twitch.tv/'
    channel_name = input("Please enter the channel name you want to scrape: ")
    if channel_name.isalnum() and len(channel_name) >= 3 and len(channel_name) < 25: #Replace by a regEX
        return base_url + channel_name
    print('Incorrect username. Stop.')
    return None


if __name__ == "__main__":
    get_url()