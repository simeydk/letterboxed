import requests

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'SOWPODS.txt')


sowpods_url = 'https://raw.githubusercontent.com/jesstess/Scrabble/master/scrabble/sowpods.txt'

SOWPODS = requests.get(sowpods_url).text

with open(filename, 'w') as f:
    f.write(SOWPODS)