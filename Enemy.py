from NPC import NPC
# import class NPC

class Enemy(NPC):
    # Class Enemy untuk NPC Musuh yang melakukan inheritance kepada class NPC

    def __init__(self, name, gender, hp, atk, weapon):
        super().__init__(name, gender, "Enemy", hp, atk)
        self.weapon = weapon
        # properti senjata

    def give_reward(self):
        # method memberikan hadiah ketika kalah
        print(f"{self.name} telah dikalahkan, kamu mendapatkan hadiah")