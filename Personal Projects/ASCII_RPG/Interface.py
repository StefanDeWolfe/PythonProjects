# Author: Stefan DeWolfe
# Date: 2/2024
#
import os
import re
import sys
import time
import keyboard
import typing
from typing import List
from typing import Dict
class Interface:
    symbol_underscore: str = "_"
    barrier: str = "|"
    symbol_blk14: str = "░"
    symbol_blk12: str = "▒"
    symbol_blk34: str = "▓"
    symbol_block: str = "█"
    symbol_alpha: str = "α"  # ALPHA
    symbol_beta: str  = "β"   # BETA
    symbol_gamma: str = "γ"  # GAMMA
    symbol_omega: str = "Ω"  # OMEGA
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
    def __init__(self):
        self.settings = {

        }

    def clear_screen(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_input(self, prompt: str) -> str:
        return input(f"{prompt} #> ")

    def draw_map(self, game_map) -> None:
        frame = "x" + "=" * game_map.width + "x"
        print(frame)
        for row in game_map.map_data:
            row_tiles = [tile.symbol for tile in row]
            if game_map.map_data.index(row) == game_map.player.y:
                row_tiles[game_map.player.x] = game_map.player_symbol
            print("|" + "".join(row_tiles) + "|")
        print(frame)

    def draw_minimap(self, game_map, x_offset: int, y_offset: int, width: int, height: int) -> None:
        if x_offset >= game_map.width:
            raise IndexError(
                "IndexError in GameMap.display_part: The x offset is greater than the width of the map!")
        if y_offset >= game_map.height:
            raise IndexError(
                "IndexError in GameMap.display_part: The y offset is greater than the height of the map!")
        if width >= game_map.width:
            width = game_map.width - x_offset
        if height >= game_map.height:
            height = game_map.height - y_offset
        frame = "x" + "=" * width + "x"
        print(frame)
        for row in game_map.map_data[y_offset:y_offset + height]:
            row_tiles = [tile.symbol for tile in row[x_offset:x_offset + width]]
            if game_map.map_data[y_offset:y_offset+height].index(row) == game_map.player.y-y_offset:
                row_tiles[game_map.player.x-x_offset] = game_map.player_symbol
            print("|" + "".join(row_tiles) + "|")
        print(frame)

    def get_item_from_menu(
        self, 
        prompt: str, 
        menu_options: [str], 
        cannot_pick: List[str] = [],
        marked_options: Dict = {},
        zero_option=False
        ) -> str:
        is_selecting = True
        while is_selecting:
            chosen_option = None
            selected_index = 0
            print(f"{prompt} - Cannot pick {str(cannot_pick)}")
            for menu_option in menu_options:
                if menu_option in cannot_pick:
                    print(
                        f"{self.colors['red']}X.{self.colors['default']} {menu_option}"
                    )
                elif menu_option in marked_options.keys():
                    color = marked_options.get(menu_option, 'default')
                    print(
                        f"{self.colors[color]}{menu_options.index(menu_option) + 1}. "
                        f"{menu_option}{self.colors['default']}"
                    )
                else:
                    print(
                        f"{self.colors['default']}{menu_options.index(menu_option) + 1}."
                        f" {menu_option}{self.colors['default']}"
                    )
            chosen_option = input("#> ")
            if zero_option and chosen_option == "0":
                return chosen_option
            # Check to see if it is in the cannot pick category
            for menu_option in cannot_pick:
                if chosen_option.lower() in menu_option.lower():
                    print(f"you cannot pick {chosen_option}")
                    chosen_option = None
                    selected_index = 0
            if chosen_option is None:
                continue
            # check to see if it is in the available options
            for menu_option in menu_options:
                if chosen_option.lower() in menu_option.lower():
                    return menu_option
            # If input was a number, use re to strip it out of the string.
            selected_index = int(re.search(r'\d+', chosen_option).group())
            if menu_options[selected_index-1] in cannot_pick:
                print(f"you cannot pick {menu_options[selected_index-1]}")
                selected_index = 0
                chosen_option = None
                continue
            if 0 <= selected_index-1 < len(menu_options):
                return menu_options[selected_index-1]

    def print_list_picture(self, art_list: [str], delay: float = 0.001):
        for row in art_list:
            print(row)
            time.sleep(delay)

    def typewriter_text(self, text: str, delay: float = 0.01):
        for char in text:
            print(char, end="")
            sys.stdout.flush()
            time.sleep(delay)

    def typewriter_list(self, text_list: [str], delay: float = 0.01):
        for text in text_list:
            self.typewriter_text(text=text, delay=delay)

    def draw_bar(self, cv, mv, length, color='') -> None:
        remaining_bars = round(cv / mv * length)
        lost_bars = length - remaining_bars
        print(f"{self.barrier}"
              f"{self.colors[color] if color != '' else ''}"
              f"{remaining_bars * self.symbol_block}"
              f"{lost_bars * self.symbol_underscore}"
              f"{self.colors['default'] if color != '' else ''}"
              f"{self.barrier}")

def interface_tests():
    interface = Interface()
    interface.clear_screen()

    print(interface.get_item_from_menu(
        prompt="Select an option:",
        menu_options=["Option A", "Option B", "Option C"],
        zero_option=False,
        cannot_pick=["Option B"],
        marked_options={ "Option C": "yellow"}
        )
    )
    interface.print_list_picture([
        "|-----------------------------|",
        "|                             |",
        "|                             |",
        "|           ART!              |",
        "|                             |",
        "|                             |",
        "|-----------------------------|",
    ])
    interface.typewriter_text(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n")
    print("")
    interface.typewriter_list(
        ["In ultrices quis nisi vel sagittis.\nProin laoreet, ",
        "justo vitae elementum suscipit, lacus odio rutrum leo, ",
        "at pharetra sem quam vel enim.\nNunc porta laoreet est quis consequat.\n",
        "Nulla molestie, augue eget cursus gravida, turpis risus auctor dui, at ",
        "laoreet lacus metus vel odio.\n"]
        )
    interface.draw_bar(100, 100, 20, color='green')
    interface.draw_bar(66, 100, 20, color='yellow')
    interface.draw_bar(33, 100, 20, color='red')

if __name__ == "__main__":
    interface_tests()
