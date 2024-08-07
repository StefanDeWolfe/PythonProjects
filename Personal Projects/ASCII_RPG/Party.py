# Author: Stefan DeWolfe
# Date: 3/2024
#
from Item import Inventory
class Party:
    def __init__(self, name:str, members: list = [], max_party_members:int = 4, inventory: Inventory = None) -> None:
        self.name = name
        self.members = members
        self.max_party_members = max_party_members
        self.inventory = inventory

    def add_party_member(self, member):
        if member not in self.members:
            self.members.append(member)

    def __str__(self) -> str:
        return f"{self.name}"

def party_tests():
    rpg_party = Party()
if __name__ == "__main__":
    party_tests()