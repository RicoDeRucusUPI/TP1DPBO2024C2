from NPC import NPC
# import class NPC

class ItemSeller(NPC):
    # Class ItemSeller untuk NPC penjual item yang melakukan inheritance kepada Class NPC
    def __init__(self, name, gender, items_for_sale=None):
        if items_for_sale is None:
            items_for_sale = []
        super().__init__(name, gender, "Item Seller", 0, 0)
        self.items_for_sale = items_for_sale

    def sell_item(self, item, buyer):
        # Method menjual item
        if item in self.items_for_sale and buyer.money >= 10: 
            # jika item yang dingikan dan uang pembeli cukup maka item diberikan dan uang pembeli dikurangi
            buyer.collect_item(item)
            buyer.money -= 10
            print(f"{self.name} menjual {item} untuk {buyer.name}.")
        elif item not in self.items_for_sale:
            # jika item yang dicari tidak ada
            print(f"{self.name}, item {item} tidak dijual.")
        else:
            # Jika uang tidak cukup
            print(f"{buyer.name}, Uang tidak cukup untuk membeli item {item}.")

    def show_items_for_sale(self):
        # Menampilkan semua item yang dijual
        print(f"{self.name}, item yang dijual : {', '.join(self.items_for_sale)}")