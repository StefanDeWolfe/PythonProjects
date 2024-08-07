# Author: Stefan DeWolfe
# Date: 3/2024
#
from StatBlock import StatBlock


class Kindred:
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


class Human(Kindred):
    def __init__(self):
        super().__init__(name="Human",
                         desc="Standard Human",
                         stats=StatBlock([0,0,0, 0,0,0,0, 0,0,0, 0,0]),
                         attacks=[],
                         skills=[],
                         specials=[],
                         passives=[])


class Elf(Kindred):
    def __init__(self):
        super().__init__(name="Elf",
                         desc="Standard Elf",
                         stats=StatBlock([0,0,0, 0,0,0,0, 0,0,0, 0,0]),
                         attacks=[],
                         skills=[],
                         specials=[],
                         passives=[])


class Dwarf(Kindred):
    def __init__(self):
        super().__init__(name="Dwarf",
                         desc="Standard Dwarf",
                         stats=StatBlock([0,0,0, 0,0,0,0, 0,0,0, 0,0]),
                         attacks=[],
                         skills=[],
                         specials=[],
                         passives=[])


class Hobbit(Kindred):
    def __init__(self):
        super().__init__(name="Hobbit",
                         desc="Standard Hobbit",
                         stats=StatBlock([0,0,0, 0,0,0,0, 0,0,0, 0,0]),
                         attacks=[],
                         skills=[],
                         specials=[],
                         passives=[])


def kindred_tests() -> None:
    rpg_kindred = Kindred(name="Kindred",
                         desc="Kindred description",
                         stats=StatBlock([0,0,0, 0,0,0,0, 0,0,0, 0,0]),
                         attacks=[],
                         skills=[],
                         specials=[],
                         passives=[])
    print(str(rpg_kindred))

if __name__ == "__main__":
    kindred_tests()