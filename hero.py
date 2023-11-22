from character import Character


class Hero(Character):
    def __init__(self, name):
        super().__init__()
        self.hp = 10
        self.atk = 5
        self.defense = 5
        self.name = name
