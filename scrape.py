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

    location = 'data'
    filename = os.path.join(location, f'{print_date}.json')
    print(print_date)
    os.makedirs(location, exist_ok=True)
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=2))
letterboxed_url = 'https://www.nytimes.com/puzzles/letter-boxed'

if __name__ == '__main__':
    scrape_gamedata(letterboxed_url, letterboxed_filename)
