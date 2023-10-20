import requests


def get_pokemons(limit):
    url = f'https://pokeapi.co/api/v2/pokemon?limit={str(limit)}'
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    else:
        return {i: (pokemon['name'], pokemon['url']) for i, pokemon in enumerate(response.json()['results'])}
    
    
def get_info(pokemon):
    response = requests.get(pokemon[1])
    info = {}
    
    if response.status_code != 200:
        return None
    else:
        data = response.json()
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
        types = [t['type']['name'] for t in data['types']]
        info['name'] = pokemon[0]
        info['stats'] = stats
        info['types'] = types
        return info
    
    
if __name__ == '__main__':
    pass
