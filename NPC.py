from Character import Character
# import class Character

class NPC(Character):
    # Class NPC yang melakukan inhertance kepada Class Character
    def __init__(self, name, gender, role, hp, atk):
        super().__init__(name, gender, None, role, hp, atk)

    def talk(self):
        # Method talk untuk melakukan obrolan
        print(f"{self.name} mengatakan Sesuatu.")
