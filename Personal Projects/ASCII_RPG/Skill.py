# Author: Stefan DeWolfe
# Date: 3/2024
#
class Skill:
    def __init__(self) -> None:
        self.name = None

    def __str__(self) -> str:
        return f"{self.name}"

def skill_tests() -> None:
    rpg_skill = Skill()

if __name__ == "__main__":
    skill_tests()