from character import Character


class Slime(Character):
    def __init__(self):
        super().__init__()
        self.hp = 20
        self.atk = 1
        self.defense = 2
