class Character:
    def __init__(self):
        self.hp = 1
        self.atk = 1
        self.defense = 1

    def attack(self, char):
        damage = self.atk - char.defense
        if damage <= 0:
            damage = 1
        char.hp -= damage
        return damage

    def defend(self):
        self.defense *= 2

    def stop_defending(self):
        self.defense /= 2
