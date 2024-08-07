# Author: Stefan DeWolfe
# Date: 3/2024
#
from StatBlock import StatBlock
class RpgClass:
    def __init__(self, name: str, desc: str, stats, attacks, skills, specials, passives) -> None:
        self.name = name
        self.description = desc
        self.stat_block = stats
        self.attack = attacks
        self.skills = skills
        self.special_skills = specials
        self.passive_skills = passives

    def __str__(self) -> str:
        return f"{self.name}"


class Hero(RpgClass):
    def __init__(self) -> None:
        super().__init__(name="",
                         desc="",
                         stats=StatBlock([0,0,0, 0,0,0,0, 0,0,0, 0,0]),
                         attacks=[],
                         skills=[],
                         specials=[],
                         passives=[]
                         )
def rpg_class_tests() -> None:
    rpg_class = RpgClass()
if __name__ == "__main__":
    rpg_class_tests()