# Author: Stefan DeWolfe
# Date: 2/2024
#
import os
class StatBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {"red": "\033[91m",
                    "purple": "\33[95m",
                    "blue": "\33[34m",
                    "blue2": "\33[36m",
                    "blue3": "\33[96m",
                    "green": "\033[92m",
                    "green2": "\033[32m",
                    "brown": "\33[33m",
                    "yellow": "\33[93m",
                    "grey": "\33[37m",
                    "default": "\033[0m"
                    }

    def __init__(self,
                 vc: int,
                 mv: int,
                 length: int = 20,
                 is_colored: bool = True,
                 color: str = "") -> None:
        self.length = length
        self.color = self.colors.get(color) or self.colors["default"]
        self.is_colored = is_colored
        self.current_value = vc
        self.max_value = mv

    def update(self) -> None:
        pass

    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}")
class HealthBar(StatBar):
    def __init__(self, entity, length: int = 20, is_colored: bool = True, color: str = "") -> None:
        super().__init__( 0, 0, length, is_colored, color)
        self.entity = entity
        self.current_value = self.entity.hp
        self.max_value = self.entity.hp_max

    def update(self) -> None:
        self.current_value = self.entity.hp

    def draw(self) -> None:
        print(f"{self.entity.name}'s HP: {self.entity.hp}/{self.entity.hp_max}")
        super().draw()
class ManaBar(StatBar):
    def __init__(self, entity, length: int = 20, is_colored: bool = True, color: str = "") -> None:
        super().__init__( 0, 0, length, is_colored, color)
        self.entity = entity
        self.current_value = self.entity.mana
        self.max_value = self.entity.mana_max

    def update(self) -> None:
        self.current_value = self.entity.mana

    def draw(self) -> None:
        print(f"{self.entity.name}'s Mana: {self.entity.mana}/{self.entity.mana_max}")
        super().draw()

