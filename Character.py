class Character:
    # Class Character yang digunakan untuk informasi NPC/Player dan aksi
    def __init__(self, name, gender, weapon, role, hp, atk, money=0, items=[]):
        # Constructor berisikan parameter (name, gender, weapon, role, hp, atk, money, item)
        self.name = name
        self.gender = gender
        self.weapon = weapon
        self.role = role
        self.hp = hp
        self.atk = atk
        self.money = money
        self.items = items
        # memindahkan value parameter ke properti

    def attack(self, target):
        # Method menyerang target
        print(f"{self.name} menyerang {target.name} dengan {self.weapon}!")
        target.take_damage(self.atk)

    def take_damage(self, damage):
        # Method menerima damage
        self.hp -= damage
        if(self.hp <= 0):
            print(f"{self.name} Mati")
        else:
            print(f"{self.name} menerima {damage} damage. Sisa HP: {self.hp}")

    def use_item(self, item):
        # Method menggunakan item
        if item in self.items:
            print(f"{self.name} menggunakan {item}.")
            # Implement logic for item usage
        else:
            print(f"{self.name} tidak memiliki {item}.")

    def collect_item(self, item):
        # Method mendapatkan item
        print(f"{self.name} mendapatkan {item}.")
        self.items.append(item)

    def show_status(self):
        # Method menampilkan status
        print(f"{self.name}'s Status Karakter:")
        print(f"HP: {self.hp}")
        print(f"ATK: {self.atk}")
        print(f"Uang: {self.money}")
        print(f"Items: {', '.join(self.items)}\n")