import json, os
from fetcher import fetch



if __name__ == '__main__':
    data = fetch()
    print_date = data['printDate']
    
    location = 'data'
    filename = os.path.join(location, f'{print_date}.json')
    
    os.makedirs(location, exist_ok=True)
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=2))