from character import Character


class Hero(Character):
    def __init__(self, name):
        super().__init__()
        self.max_hp = 10
        self.hp = self.max_hp
        self.atk = 5
        self.defense = 5
        self.name = name
        self.level = 1
        self.exp = 0
        self.exp_required = 10

    def level_up(self, enemy):
        self.exp += enemy.exp
        while self.exp >= self.exp_required:
            print("You levelled up!")
            self.level += 1
            self.exp -= self.exp_required
            self.calculate_exp_required()
            self.max_hp += self.level
            print(f"Your hp rose to {self.max_hp}")
            self.hp = self.max_hp
            self.atk += self.level
            print(f"Your atk rose to {self.atk}")
            self.defense += self.level
            print(f"Your defense rose to {self.defense}")

    def calculate_exp_required(self):
        self.exp_required = self.level * 10
