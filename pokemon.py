import utils


class Pokemon:
    
    def __init__(self, name, hp, attack, defence, types):
        self.name = name
        self.hp = hp + defence
        self.max_hp = self.hp
        self.attack = attack
        self.types = types
        self.damage_relations = {}
        
        for t in types:
            dmg_rel = utils.get_damage_relations(t)
            for key, value in dmg_rel.items():
                if key in self.damage_relations:
                    self.damage_relations[key].extend(value)
                else:
                    self.damage_relations[key] = value
                    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        if not isinstance(other, Pokemon):
            return False
        else:
            return self.name == other.name
                    
    def get_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            return 0
        else:
            return self.hp
        
    def reset_hp(self):
        self.hp = self.max_hp
        
        
if __name__ == '__main__':
    pokemons = utils.get_pokemons(10)
    bulbasaur = utils.get_info(pokemons['bulbasaur'])
    
    bulbasaur1 = Pokemon(
        bulbasaur['name'],
        bulbasaur['stats']['hp'], 
        bulbasaur['stats']['attack'], 
        bulbasaur['stats']['defense'], 
        bulbasaur['types']
        )
    
    bulbasaur2 = Pokemon(
        bulbasaur['name'],
        bulbasaur['stats']['hp'], 
        bulbasaur['stats']['attack'], 
        bulbasaur['stats']['defense'], 
        bulbasaur['types']
        )
    
    print(bulbasaur1)
    print(set([bulbasaur1, bulbasaur2]))
