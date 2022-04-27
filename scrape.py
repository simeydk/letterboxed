import os
from src.scrape import fetch, parse_puzzle, json_to_file


def scrape_gamedata(url, location_fn):
    html = fetch(url)
    data = parse_puzzle(html)    
    filename = location_fn(data)
    json_to_file(data, filename)


def letterboxed_filename(data):
    location = 'data/letterboxed'
    print_date = data['printDate']
    filename = os.path.join(location, f'{print_date}.json')
    return filename

def spellingbee_filename(data):
    location = 'data/spellingbee'
    print_date = data['today']['printDate']
    filename = os.path.join(location, f'{print_date}.json')
    return filename

letterboxed_url = 'https://www.nytimes.com/puzzles/letter-boxed'
spellingbee_url = 'https://www.nytimes.com/puzzles/spelling-bee'

if __name__ == '__main__':
    scrape_gamedata(letterboxed_url, letterboxed_filename)
    scrape_gamedata(spellingbee_url, spellingbee_filename)
