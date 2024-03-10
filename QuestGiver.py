from NPC import NPC
# import class NPC

class QuestGiver(NPC):
    # Class QuestGiver untuk NPC pemberi misi yang melakukan inheritance kepada Class NPC
    def __init__(self, name, gender, quests=None):
        if quests is None:
            quests = []
        super().__init__(name, gender, "Quest Giver", 0, 0)
        self.quests = quests
        # properti quest

    def give_quest(self, quest, player):
        # method memberikan misi kepada player
        if quest in self.quests:
            # jika misi yang dicari tersedia
            print(f"{self.name} memberikan {player.name} sebuah misi: {quest}.")
            player.quests.append(quest)
            # tambahkan misi ke player
        else:
            print(f"{self.name} tidak ada misi untuk saat ini.")
            # jika misi tidak ada

    def complete_quest(self, quest, player):
        # method jika misi selesai
        if quest in player.quests:
            # jika misi selesai
            print(f"{player.name} menyelesaikan misi: {quest}.")
            player.quests.remove(quest)
            # hapus misi pada player
            player.money += 100;
            # berikan uang kepada player
            print(f"{player.name} mendapatkan uang 100 Coin")
        else:
            # jika misi sudah tidak ada
            print(f"{player.name} tidak memiliki misi {quest}.")

    def show_available_quests(self):
        # menampilkan semua misi
        print(f"{self.name}, misi yang tersedia: {', '.join(self.quests)}")