import requests


def get_pokemons(limit):
    url = f'https://pokeapi.co/api/v2/pokemon?limit={str(limit)}'
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    else:
        return {pokemon['name']: pokemon['url'] for pokemon in response.json()['results']}
    
    
def get_info(url):
    response = requests.get(url)
    info = {}
    
    if response.status_code != 200:
        return None
    else:
        data = response.json()
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
        types = [t['type']['name'] for t in data['types']]
        info['name'] = data['name']
        info['stats'] = stats
        info['types'] = types
        return info
    
    
if __name__ == '__main__':
    pokemons = get_pokemons(20)
    print(get_info(pokemons['charmander']))
