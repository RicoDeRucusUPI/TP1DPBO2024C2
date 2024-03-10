from Character import Character
# import class Character

class Player(Character):
    # Class Player untuk pemain, yang melakukan inheritance kepada class Character
    def __init__(self, name, gender, weapon, role, hp, atk, money=0, items=[]):
        super().__init__(name, gender, weapon, role, hp, atk, money, items)
        self.quests = []
        # properti quest

    def level_up(self):
        # method level meningkat
        print(f"{self.name} Level Meningkat! ATK + 5 Ditambahkan!")
        self.atk += 5
        # menambahkan value properti atk