# Author: Stefan DeWolfe
# Date: 2/2024
#
import os
import sys
import random
from Character import RpgCharacter
from GameMap import GameMap, Coord
from Interface import Interface
from Item import Inventory
from Kindred import Human, Elf, Dwarf, Hobbit
from Party import Party
from RpgClass import Hero
from Save import Save
from Skill import Skill
from StatBlock import StatBlock


class Game:
    def __init__(self):
        self.run = True
        self.menu = True
        self.play = False
        self.rules = False
        self.interface = Interface()
        self.save_file = None
        self.main_menu_options = ["New Game", "Load Game", "Rules", "Quit"]

    def save_game(self) -> None:
        self.save_file.save()

    def load_game(self):
        self.interface.clear_screen()
        results = [each for each in os.listdir(".") if each.endswith('.pkl')]
        opt = self.interface.get_item_from_menu("# Pick a save file", results+["back"])
        if opt.lower() in ["back", "cancel", "stop"]:
            return False
        else:
            self.save_file = Save.load(opt)
            if self.save_file is None:
                print(f"There was a problem loading the save file.\"{opt}\"")
                return False
            else:
                return True

    def display_rules(self) -> None:
        print("These are the rules.")
        print("Rules: Make choices by typing in the command or by inputting a menu item number.")
        print("Rules: type \"0\" in the input prompt to exit to the main menu.")
        self.rules = False

    def new_game(self) -> None:
        self.interface.clear_screen()
        player_name = self.interface.get_input("What is your name?")
        player_gender = self.interface.get_item_from_menu(prompt="What is your gender?", menu_options=["Male", "Female", "I don't care.", "Let me tell you."], zero_option=False)
        if "I don't care." == player_gender:
            player_gender = random.choice(["Male", "Female"])
            print(player_gender)
        elif "Let me tell you." == player_gender:
            player_gender = self.interface.get_input("What is your gender?")
        player_kindred = Human()
        #
        player_rpg_class = Hero()
        #

        player_stat_block = StatBlock([30,30,100, 40,20,40,20, 30,10,20, 100,100])

        new_character = RpgCharacter(
            name=player_name,
            level=1,
            exp=0,
            gender=player_gender,
            kindred=player_kindred,
            rpg_class=player_rpg_class,
            stat_block=player_stat_block
        )
        player_party_name = self.interface.get_input("What is your party's name?")
        #
        overworld = GameMap(width=80, height=40)
        overworld.generate_map(
            forest_patches=[3, 3, 6],
            pines_patches=[3, 3, 6],
            mountain_patches=[3, 3, 6],
            savannah_patches=[8, 3, 10],
            desert_patches=[8, 3, 10],
            water_patches=[3, 3, 6]
        )
        for _ in range(3):  #
            while not overworld.add_site(
                    tile=GameMap.town,
                    x=random.randint(0, overworld.width),
                    y=random.randint(0, overworld.height),
            ):
                pass
        for _ in range(6):  #
            while not overworld.add_site(
                    tile=GameMap.dungeon,
                    x=random.randint(0, overworld.width),
                    y=random.randint(0, overworld.height),
            ):
                pass
        overworld.player = Coord(overworld.width//2, overworld.height//2)
        #
        self.interface.clear_screen()
        #
        player_save_name = self.interface.get_input("Name your save file.")
        self.save_file = Save(
            name=player_save_name,
            player_character=new_character,
            party=Party(name=player_party_name,
                        members=[new_character],
                        max_party_members=4,
                        inventory=Inventory(list_of_pockets=["Items", "Weapons", "Armor", "Key Items"])
                        ),
            game_map=overworld
        )

    def display_party_members(self):
        for member in self.save_file.party.members:
            print(f"{member.name}"
                  f"({member.rpg_class.name}"
                  f"{member.kindred.name})"
                  f"Lv. {member.level}"
                  )
            self.interface.draw_bar(
                cv=member.current_stats.hp,
                mv=member.get_max_hp(),
                length=20,
                color='red')
            self.interface.draw_bar(
                cv=member.current_stats.mana,
                mv=member.get_max_mp(),
                length=20,
                color='blue')
            self.interface.draw_bar(
                cv=member.current_stats.special,
                mv=member.get_max_sp(),
                length=20,
                color='green')

    def game_menu(self):
        game_menu_options = ["Save & Exit", "Return to Game"]
        opt = self.interface.get_item_from_menu(prompt="Choose an option: ", menu_options=game_menu_options)
        if opt == "Save & Exit":
            self.save_game()
            self.play = False
            self.menu = True

    def display_nav_status(self):
        divider = "xXx" + "="*10 + "xXx"
        minimap_width = 20
        minimap_height = 10
        self.interface.draw_minimap(
            game_map=self.save_file.game_map,
            x_offset=min(max(0, self.save_file.game_map.player.x - (minimap_width // 2)),
                         self.save_file.game_map.width),
            y_offset=min(max(0, self.save_file.game_map.player.y - (minimap_height // 2)),
                         self.save_file.game_map.height),
            width=minimap_width, height=minimap_height
        )
        print(divider)
        print(
            f"Location: {self.save_file.game_map.map_data[self.save_file.game_map.player.y][self.save_file.game_map.player.x].name.upper()}")
        print(f"Coords: {self.save_file.game_map.player}")
        print(divider)
        self.display_party_members()
        print(divider)

    def move_player(self, direction):
        if direction == "north":
            return self.save_file.game_map.move_player(
                x=self.save_file.game_map.player.x,
                y=self.save_file.game_map.player.y-1
            )
        elif direction == "east":
            return self.save_file.game_map.move_player(
                x=self.save_file.game_map.player.x+1,
                y=self.save_file.game_map.player.y
            )
        elif direction == "south":
            return self.save_file.game_map.move_player(
                x=self.save_file.game_map.player.x,
                y=self.save_file.game_map.player.y+1
            )
        elif direction == "west":
            return self.save_file.game_map.move_player(
                x=self.save_file.game_map.player.x-1,
                y=self.save_file.game_map.player.y
            )
        # elif direction == "enter town":
        #     pass
        # elif direction == "enter dungeon":
        #     pass
        else:
            print(f"Cannot move in \"{direction}\" direction.")

    def navigate(self):
        divider = "xXx" + "="*10 + "xXx"
        self.interface.clear_screen()
        self.display_nav_status()
        available_directions = self.save_file.game_map.get_available_movement_directions() + ["Game Menu"]
        opt = self.interface.get_item_from_menu(prompt="Pick a direction to move", menu_options=available_directions)
        if opt.lower() == "game menu":
            self.game_menu()
            return
        if not self.move_player(opt.lower()):
            print(f"You cannot go that way!")

    def play_game(self) -> None:
        while self.play:
            # Main Game
            # Navigate around map
            self.navigate()

            # Reset for main menu

    def start_game(self) -> None:
        # run loop
        while self.run:
            # Menu loop
            while self.menu:
                self.interface.clear_screen()
                opt = self.interface.get_item_from_menu("# Main Menu", self.main_menu_options)
                if opt == self.main_menu_options[0]:  # New Game
                    self.play = True
                    self.menu = False
                    self.new_game()
                    self.save_game()
                elif opt == self.main_menu_options[1]:  # Load Game
                    if self.load_game():
                        self.play = True
                        self.menu = False
                elif opt == self.main_menu_options[2]:  # Show Rules Game
                    self.rules = True
                else:
                    self.run = False
                    self.menu = False
                if self.rules:
                    self.display_rules()
            # Game loop
            self.play_game()


if __name__ == "__main__":
    os.system("")
    game = Game()
    game.start_game()







