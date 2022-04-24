import requests
import json
from bs4 import BeautifulSoup

def fetch() -> str:
    '''
        Return today's puzzle data as a dict
    '''
    response = requests.get('https://www.nytimes.com/puzzles/letter-boxed')
    soup = BeautifulSoup(response.text, 'html.parser')
    scripts = soup.find_all('script')
    game_data_script = [script.text for script in scripts
                        if script.text.startswith('window.gameData')][0]
    data = json.loads(game_data_script.replace("window.gameData = ", ""))
    return data