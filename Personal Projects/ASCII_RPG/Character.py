# Author: Stefan DeWolfe
# Date: 2/2024
#
from StatBlock import StatBlock
from Kindred import Kindred
from RpgClass import RpgClass


class RpgCharacter:
    def __init__(self,
                 name: str,
                 level: int,
                 exp: int,
                 gender: str = "androgynous",
                 kindred: Kindred = None,
                 rpg_class: RpgClass = None,
                 stat_block: StatBlock = None,
                 ):
        self.name = name
        self.gender = gender

        self.level = level
        self.exp = exp

        self.kindred = kindred
        self.rpg_class = rpg_class
        self.stat_block = stat_block
        self.current_stats = StatBlock()
        self.reset_current_stats()

        self.equipment = None

        self.attack = []  # Dependant on kindred, rpg_class, and equipment
        self.skills = []  # Dependant on kindred, rpg_class, and equipment
        self.special_skills = []  # Dependant on kindred, rpg_class, and equipment
        self.passive_skills = []  # Dependant on kindred, rpg_class, and equipment

    def get_max_hp(self):
        return self.kindred.stat_block.hp + self.rpg_class.stat_block.hp + self.stat_block.hp

    def get_max_mp(self):
        return self.kindred.stat_block.mana + self.rpg_class.stat_block.mana + self.stat_block.mana

    def get_max_sp(self):
        return self.stat_block.special

    def reset_current_stats(self):
        self.current_stats.hp = self.get_max_hp()
        self.current_stats.mana = self.get_max_mp()
        self.current_stats.special = 0

        self.current_stats.attack = self.kindred.stat_block.attack + self.rpg_class.stat_block.attack + self.stat_block.attack
        self.current_stats.defense = self.kindred.stat_block.defense + self.rpg_class.stat_block.defense + self.stat_block.defense
        self.current_stats.magic_attack = self.kindred.stat_block.magic_attack + self.rpg_class.stat_block.magic_attack + self.stat_block.magic_attack
        self.current_stats.magic_resistance = self.kindred.stat_block.magic_resistance + self.rpg_class.stat_block.magic_resistance + self.stat_block.magic_resistance

        self.current_stats.speed = self.kindred.stat_block.speed + self.rpg_class.stat_block.speed + self.stat_block.speed
        self.current_stats.luck = self.kindred.stat_block.luck + self.rpg_class.stat_block.luck + self.stat_block.luck
        self.current_stats.skill = self.kindred.stat_block.skill + self.rpg_class.stat_block.skill + self.stat_block.skill

        self.current_stats.accuracy = self.kindred.stat_block.accuracy + self.rpg_class.stat_block.accuracy + self.stat_block.accuracy
        self.current_stats.evasion = self.kindred.stat_block.evasion + self.rpg_class.stat_block.evasion + self.stat_block.evasion

    def __str__(self):
        return f"{self.name} {self.rpg_class.name} Lv {self.level} EXP: {self.exp}"


def character_tests():
    rpg_character = RpgCharacter(
        name="",
        level=1,
        exp=0,
        gender="androgynous",
        kindred=None,
        rpg_class=None,
        stat_block=None
    )
    print(f"{rpg_character}")


if __name__ == "__main__":
    character_tests()