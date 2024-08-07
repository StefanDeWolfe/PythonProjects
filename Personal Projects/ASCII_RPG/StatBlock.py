# Author: Stefan DeWolfe
# Date: 3/2024
#
class StatBlock:
    def __init__(self, stat_list: [int] = [0,0,0, 0,0,0,0, 0,0,0, 0,0]) -> None:
        self.hp = stat_list[0]
        self.mana = stat_list[1]
        self.special = stat_list[2]

        self.attack = stat_list[3]
        self.defense = stat_list[4]
        self.magic_attack = stat_list[5]
        self.magic_resistance = stat_list[6]

        self.speed = stat_list[7]
        self.luck = stat_list[8]
        self.skill = stat_list[9]
        self.accuracy = stat_list[10]
        self.evasion = stat_list[11]
    def __str__(self) -> str:
        return f"HP {self.hp} | MP {self.mana} | SP {self.special}"

def stat_block_tests() -> None:
    rpg_stat_block = StatBlock()
if __name__ == "__main__":
    stat_block_tests()