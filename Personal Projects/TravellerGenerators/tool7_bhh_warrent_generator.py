# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
# 
import random, os, sys
from tables import Tables, CustomTables
"""
This is a WIP of the Bounty system implemented for the Cepheus engine by Ian Stead, Tomb Price, and Ade Steward, published by Moon Toad Publishing.
I own the book and wanted to make a random bounty generator for solo play or as a GM tool.
"""
class Warrent():
    def __init__(self):
        self.warrent_type = None
        self.warrent_value = None
        self.target_description = None
        self.target_location = None
        self.plot_twist = None

class SophontWarrent(Warrent):
    def __init__(self):
        super().__init__()
        self.target_activity = None
        self.target_assets = None

class ShipWarrent(Warrent):
    def __init__(self):
        super().__init__()
        self.target_cargo = None

class ArtifactWarrent(Warrent):
    def __init__(self):
        super().__init__()

class SimpleWarrent():
    def __init__(self):

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    #
#