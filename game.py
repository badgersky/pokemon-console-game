import os
import time
import random

from pokemon import Pokemon
import utils


class Game:
    
    def __init__(self, player, limit=50):
        if limit < 50:
            limit = 50
        self.pokemons = utils.get_pokemons(limit)
        self.pokedex = set()
        self.starters = ['Squirtle', 'Charmander', 'Bulbasaur']
        self.player = player
    
    @staticmethod
    def clear_console():
        if os.name != 'nt':
            os.system('clear')
        else:
            os.system('cls')
    
    def choose_starter(self):
        choice = '0'
        
        while choice not in ['1', '2', '3']:
            self.clear_console()
            print(f'Choose starter pokemon:\n1 - {self.starters[0]}\n2 - {self.starters[1]}\n3 - {self.starters[2]}\n')
            choice = input('Enter 1, 2 or 3: ')
            
        chosen_poke = self.starters[int(choice) - 1]
        print(f'Great choice, your {chosen_poke} is super cute!')
        pokemon = self.create_pokemon(chosen_poke)
        self.pokedex.add(pokemon)
        time.sleep(2)

    def create_pokemon(self, name):
        pokemon = utils.get_info(self.pokemons[name.lower()])
        return Pokemon(
            pokemon['name'],
            pokemon['stats']['hp'], 
            pokemon['stats']['attack'], 
            pokemon['stats']['defense'], 
            pokemon['types'] 
            )

    def encounter(self):
        encountered = random.choice(list(self.pokemons.keys()))
        enemy = self.create_pokemon(encountered)
        print(enemy)
        
    def update_pokemons(self):
        for pokemon in self.pokedex:
            if pokemon.name in self.pokemons:
                del self.pokemons[pokemon.name]
        
    def mainloop(self):
        self.choose_starter()
        
        while True:
            self.clear_console()
            self.update_pokemons()
            self.encounter()
            break
        
        
if __name__ == '__main__':
    game = Game('Nomis')
    game.mainloop()
    