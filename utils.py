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
    
    
def get_damage_relations(type_name):
    url = f'https://pokeapi.co/api/v2/type/{type_name}'
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    else:
        relations = {}
        data = response.json()['damage_relations']
        relations['double_from'] = [t['name'] for t in data['double_damage_from']]
        relations['half_from'] = [t['name'] for t in data['half_damage_from']]
        relations['double_to'] = [t['name'] for t in data['double_damage_to']]
        relations['half_to'] = [t['name'] for t in data['half_damage_to']]
        return relations
    
    
if __name__ == '__main__':
    pokemons = get_pokemons(20)
    charmander = get_info(pokemons['charmander'])
    print(charmander)
    
    for t in charmander['types']:
        damage_relations = get_damage_relations(t)
        print(damage_relations)