# ==========================================================================
# Saya Rico Valentino 1909263 mengerjakan (TP1)
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak
# melakukan kecurangan seperti yang telah dispesifikasikan.
# ==========================================================================

from Player import Player
from Character import Character
from NPC import NPC
from Enemy import Enemy
from QuestGiver import QuestGiver
from ItemSeller import ItemSeller

nova = Player("Nova", "M", "Panah", "DPS", 60, 35)
jane = Player("Jane", "F", "Tongkat Sihir", "Healer", 80, 15)
sora = Player("Sora", "M", "Pedang", "DPS", 100, 20)
aloy = Player("Aloy", "F", "Tongkat Sihir", "Magic Power", 80, 15)
# Membuat karakter player dan NPC

lyra = ItemSeller("Lyra", "F", ["Health Potion", "Mana Potion", "Sword"])
adrian = QuestGiver("Adrian", "M", ["Defeat Monsters", "Collect Ingredients"])
# Menambahkan NPC penjual item dan pemberi misi

thor = Enemy("Thor", "M", 100, 10, "Kampak Hitam")
# Menambahkan NPC Jahat

# Interaksi antar karakter
nova.show_status()
jane.show_status()
sora.show_status()
aloy.show_status()
# melihat setiap status player

adrian.talk()
adrian.give_quest("Defeat Monsters", nova)
adrian.give_quest("Defeat Monsters", jane)
adrian.give_quest("Defeat Monsters", sora)
adrian.give_quest("Defeat Monsters", aloy)
# NPC pemberi misi memberikan misi kepada player

print("\nBertarung dengan Monster Thor")
nova.attack(thor)
sora.attack(thor)

thor.attack(sora)
thor.attack(sora)

nova.attack(thor)
sora.attack(thor)
thor.give_reward()
# Player menyerang NPC Musuh (Thor) untuk menyelesaikan misi

print("\nMisi Selesai :")
adrian.complete_quest("Defeat Monsters", nova)
adrian.complete_quest("Defeat Monsters", jane)
adrian.complete_quest("Defeat Monsters", sora)
adrian.complete_quest("Defeat Monsters", aloy)
# NPC pemberi misi mengungkapkan misi selesai dan mendapatkan 100 coin untuk setiap player

print("\nMembeli Item:")
lyra.sell_item("Health Potion", nova)
# NPC penjual item menjual produk ke Player nova

print("\nLevel Meningkat:")
nova.level_up()
nova.show_status()
# Status player nova meningkat 
