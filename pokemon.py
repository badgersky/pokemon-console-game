class Pokemon:
    
    def __init__(self, name, hp, attack, defence, types, speed):
        self.name = name
        self.hp = hp + defence
        self.max_hp = self.hp
        self.attack = attack + speed * 0.1
        self.types = types
        
    def get_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            return 0
        else:
            return self.hp
        
    def reset_hp(self):
        self.hp = self.max_hp