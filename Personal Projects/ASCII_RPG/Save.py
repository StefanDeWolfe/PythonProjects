# Author: Stefan DeWolfe
# Date: 2/2024
#
from datetime import date
from datetime import datetime
import os
import pickle

class Save:
    def __init__(self, name: str, player_character, party, game_map) -> None:
        self.name = name
        self.player_character = player_character
        self.party = party
        self.game_map = game_map
        self.date_created = date.today()
        self.date_last_saved = date.today()

    def __str__(self) -> str:
        return f"SAVE: {self.name } | Created: {self.date_created.strftime('%Y-%m-%d %H:%M:%S')} | Last Save: {self.date_last_saved.strftime('%Y-%m-%d %H:%M:%S')}"

    def save(self) -> None:
        self.date_last_saved = date.today()
        with open(f"{self.name}.pkl", "wb") as my_save_file:
            pickle.dump(self, my_save_file)

    @staticmethod
    def load(file_name):
        if os.path.exists(file_name):
            with open(file_name, "rb") as file:
                return pickle.load(file)
        return None
