# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
# 

import random

class StarWarsPlanetNameGenerator():
    @staticmethod
    def getName():
        Consonants = ["B", "C", "D", "F", "G", "J", "K", "L", "M", "N", "P", "QU", "S", "T", "V", "X", "Z" "H", "RR", "R", "W", "Y", "ST", "CH", "NG", "TH", "ND", "CK", "LL"]
        vowels = ["A", "AU", "E", "EA", "I", "O", "OO", "OU", "U"]
        endings = ["", "aan", "ooine", "afar", "ant"]
        # ends in ooine
        # aan
        # 

        name = random.choice(Consonants) + random.choice(vowels) + random.choice(Consonants) + random.choice(vowels) + random.choice(Consonants)
        return name[0].upper() + name[1:].lower()
