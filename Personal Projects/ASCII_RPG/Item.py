# Author: Stefan DeWolfe
# Date: 3/2024
#
class Item(object):
    def __init__(self,name="<ITEM>",category="Misc",attributes={},description="<A DESCRIPTION OF AN ITEM>"):
        self.id=name
        self.name=name
        self.category=category
        self.attributes=attributes
        self.description=description
    def __str__(self):
        text = f"{self.name} ({self.category})"
        return text
    def change_id(self,new_id_info):
        self.id = self.id + "-" + new_id_info
class ItemSlot():
    def __init__(self,name,item,amount):
        self.name=name
        self.item=item
        self.amount=amount
    def __str__(self):
        text = "{0:^6} {1}".format("x"+str(self.amount), self.item.name)
        return text
class Pocket():
    def __init__(self,name):
        self.name=name
        self.item_slot = {} # "ITEM_SLOT":item_slot
    def add(self,item,amount):
        item_id = item.id.lower()
        if (item_id not in self.item_slot.keys()):
            self.item_slot[item_id] = ItemSlot(item_id,item,amount)
            return True
        else:
            self.item_slot[item_id].amount+=amount
            return True
    def remove(self,item,amount):
        item_id = item.id.lower()
        if (item_id in self.item_slot.keys()):
            if(self.item_slot[item_id].amount >= amount):
                self.item_slot[item_id].amount-=amount
                if(self.item_slot[item_id].amount == 0):
                    del self.item_slot[item_id]
                return True
            else:
                return False
        else:
            return False
    def get_items_and_amount_as_list(self):
        item_list = []
        for key in sorted(list(self.item_slot.keys())):
            item_list.append(str(self.item_slot[key]))
        return item_list
    def get(self,item_name):
        if(item_name.lower() in self.item_slot.keys()):
            return self.item_slot[item_name.lower()].item
        return None
    def get_amount(self,item_name):
        if(item_name.lower() in self.item_slot.keys()):
            return self.item_slot[item_name.lower()].amount
        return 0
class Inventory(object):
    def __init__(self, list_of_pockets):
        self.pockets={}# "Name":POCKET
        for pocket in list_of_pockets:
            self.pockets[pocket] = Pocket(pocket)
        self.currencies={}# "currency":$$$amount
    def add(self,item=None,amount=1):
        if item is None or amount < 1: return False
        pocket = item.category.lower()
        if(pocket not in list(self.pockets.keys())):
            self.pockets[pocket] = Pocket(pocket)
            return self.pockets[pocket].add(item,amount)
        else:
            return self.pockets[pocket].add(item,amount)
    def remove(self,item=None,amount=1):
        if item is None or amount < 1: return False
        pocket = item.category.lower()
        if(pocket in list(self.pockets.keys())):
            return self.pockets[pocket].remove(item,amount)
        else:
            return False
    def show_all(self):
        print ("INVENTORY")
        for pocket in self.pockets.keys():
            pocket=pocket.lower()
            print ("  {}".format(pocket.upper()))
            stuff = self.pockets[pocket].get_items_and_amount_as_list()
            for item_entry in stuff:
                print("    {}".format(item_entry))
    def get(self,item_name,item_category):
        if(item_category.lower() in self.pockets.keys()):
            item = self.pockets[item_category.lower()].get(item_name)
            return item
        return None
    def get_amount(self,item_name,item_category):
        if(item_category.lower() in self.pockets.keys()):
            amount = self.pockets[item_category.lower()].get_amount(item_name)
            return amount
        return 0
    def add_currency(self, currency, amount):
        if currency not in self.currencies.keys():
            self.currencies[currency] = amount
        else:
            self.currencies[currency] += amount
        return True
    def remove_currency(self, currency, amount):
        if currency in self.currencies.keys():
            if self.currencies[currency] >= amount:
                self.currencies[currency] -= amount
                return True
        return False
    def get_pocket_contents_as_list_of_strings(self, pocket):
        if pocket in self.pockets.keys():
            return self.pockets[pocket].get_items_and_amount_as_list()
        else:
            return [f"{pocket} Is Not A Pocket"] + list(self.pockets.keys())
    def get_item_from_pocket_contents_string(self, item_pocket_str, pocket):
        pass

class InventoryTest():
    @staticmethod
    def main():
        item1 = Item("Item 1","Misc",{"weight":1},"THIS IS A DESCRIPTION OF AN Item")
        item2 = Item("Item 2","Misc",{"weight":1},"THIS IS A DESCRIPTION OF AN Item")
        weapon1 = Item("Weapon 1","Weapon",{"weight":1},"THIS IS A DESCRIPTION OF A Weapon")
        weapon2 = Item("Weapon 2","Weapon",{"weight":1},"THIS IS A DESCRIPTION OF A Weapon")
        weapon3 = Item("Weapon 3","Weapon",{"weight":1},"THIS IS A DESCRIPTION OF A Weapon")
        armor1 = Item("Armor 1","Armor",{"weight":10},"THIS IS A DESCRIPTION OF AN Armor")
        armor2 = Item("Armor 2","Armor",{"weight":10},"THIS IS A DESCRIPTION OF AN Armor")
        armor3 = Item("Armor 3","Armor",{"weight":10},"THIS IS A DESCRIPTION OF AN Armor")
        consumable1 = Item("Consumable 1","Consumable",{"weight":1},"THIS IS A DESCRIPTION OF A Consumable")
        consumable2 = Item("Consumable 2","Misc",{"weight":1},"THIS IS A DESCRIPTION OF A Consumable")
        temp_item = None
        inv=Inventory()
        print ("===== ITEMS ===================")
        print(str(item1))
        print(item1.id)
        print(item1.name)
        print(item1.category)
        print(item1.attributes)
        print(item1.description)
        print ("===== ADD ITEMS ===================")
        print ("Item \"{}\" Added".format(item1.name)) if inv.add(item1,1) else print("Failed to Add item \"{}\"".format(item1.name))
        print ("Item \"{}\" Added".format(item1.name)) if inv.add(item1,1) else print("Failed to Add item \"{}\"".format(item1.name))
        print ("Different Item \"{}\" Added".format(item2.name)) if inv.add(item2,1) else print("Failed to Add Different item \"{}\"".format(item2.name))
        inv.show_all()

        if inv.add(item2,3): print("{} x{} added.".format(item2.name, 3))

        if inv.add(weapon1,1): print("{} x{} added.".format(weapon1.name, 1))
        if inv.add(weapon2,3): print("{} x{} added.".format(weapon2.name, 3))
        if inv.add(armor1,1): print("{} x{} added.".format(armor1.name, 1))
        if inv.add(armor2,3): print("{} x{} added.".format(armor2.name, 3))
        
        inv.show_all()
        print ("===== REMOVE 2 ARMOR 10 ===================")
        if(inv.remove(armor2,10)): print("FAIL: removed 10 armor 2 when there was only 3")
        else: print("Success: cannot remove 10 armor 2 when there was only 3")
        
        inv.show_all()
        print ("===== ADD 1 ARMOR 1 BACK ===================")
        if(inv.remove(armor2,1)): print("Success: removed 1 armor 2, leaving only 2")
        else: print("FAIL: failed to remove item")
        
        inv.show_all()
        print ("===== REMOVE 2 ARMOR 2, should be deleted ===================")
        if(inv.remove(armor2,2)): print("Success: removed 1 armor 2, leaving only 0")
        else: print("FAIL: failed to remove item")
        inv.show_all()
        print ("===== REMOVE 2 ARMOR 2, should be FAIL because there is none ===================")
        if(inv.remove(armor2,2)): print("FAIL: There is no more armor 2")
        else: print("Success: Cannot remove what is not there")
        inv.show_all()
        print ("===== ADD 20k ITEM 1 ===================")
        inv.add(item1,19999)
        inv.show_all()
        print ("===== GET ITEM object FROM INVENTORY ===================")
        found_item1 = inv.get(item1.name,item1.category)
        found_item2 = inv.get(item1.name,weapon3.category)
        found_item3 = inv.get(weapon3.name,item1.category)
        print ("correct name, correct pocket: [S] "+str(found_item1))
        print ("correct name, bogus pocket:   [F] "+str(found_item2))
        print ("bogus name, correct pocket:   [F] "+str(found_item3))
        print ("===== GET ITEM 1 FROM INVENTORY ===================")
        amount_item1 = inv.get_amount(item1.name,item1.category)
        amount_item2 = inv.get_amount(item1.name,weapon3.category)
        amount_item3 = inv.get_amount(weapon3.name,item1.category)
        print ("correct name, correct pocket: [S] x"+str(amount_item1))
        print ("correct name, bogus pocket:   [F] x"+str(amount_item2))
        print ("bogus name, correct pocket:   [F] x"+str(amount_item3))
        print ("===== END ===================")
#
if __name__ == "__main__":
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    InventoryTest.main()
    #
