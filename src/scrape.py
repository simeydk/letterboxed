import os, json
import requests
from bs4 import BeautifulSoup


def json_to_file(data, filename: str) -> None:
    location = os.path.split(filename)[0]
    os.makedirs(location, exist_ok=True)
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=2))


def fetch(url: str) -> str:
    return requests.get(url).text

def parse_puzzle(html: str) -> dict:
    '''
        Return today's puzzle data as a dict
    '''
    soup = BeautifulSoup(html, 'html.parser')
    scripts = soup.find_all('script')
    game_data_script = [script.text for script in scripts
                        if script.text.startswith('window.gameData')][0]
    text = game_data_script.replace("window.gameData = ", "")
    data = json.loads(text)
    return data