# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
import random, sys, os
import pickle
import getopt
from os.path import exists
class Utils():
    hex_key = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    @staticmethod
    def get_hex_from_decimal(decimal_number):
        if decimal_number < 10: return decimal_number
        elif decimal_number < 16: return Utils.hex_key[decimal_number]
class CharacterUtils():
    hex_key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    @staticmethod
    def get_species_traits(species):
        traits = []
        if species.lower() == "aslan":
            traits.append("Aslan Attributes: STR+2, DEX-2")
            traits.append("Dewclaw: All Aslan have a dewclaw which can be extended to make for a vicious close combat weapon. The dewclaw uses the Melee (natural) skill and does 1D+2 damage.")
            traits.append("Heightened Senses: Aslan have better night vision, hearing and sense of smell than humans. All Aslan receive DM+1 to any Recon and Survival checks they have to make.")
        elif species.lower() == "vargr":
            traits.append("Vargr Attributes: STR-1, DEX+1, END-1")
            traits.append("Bite: All Vargr possess pronounced canines which make for a nasty close combat weapon. This bite uses the Melee (natural) skill and does 1D+1 damage.")         
            traits.append("Heightened Senses: Vargr have better hearing and sense of smell than humans. All Vargr receive DM+1 to any Recon and Survival checks they have to make. However, their eyesight is worse in darkness and they suffer DM-1 to any skill check requiring sight in dark conditions.")
        else: # Human/Human-like
            pass 
        return traits
    @staticmethod
    def set_experience_levels_for_skill(traveller, skill):
        if   traveller.skills[skill] <= 1: traveller.skill_training[skill] = [traveller.skill_training[skill][0], 1]
        elif traveller.skills[skill] == 2: traveller.skill_training[skill] = [traveller.skill_training[skill][0], 2]
        elif traveller.skills[skill] == 3: traveller.skill_training[skill] = [traveller.skill_training[skill][0], 4]
        elif traveller.skills[skill] == 4: traveller.skill_training[skill] = [traveller.skill_training[skill][0], 8]
        elif traveller.skills[skill] == 5: traveller.skill_training[skill] = [traveller.skill_training[skill][0], 16]
        elif traveller.skills[skill] == 6: traveller.skill_training[skill] = [traveller.skill_training[skill][0], 32]
        elif traveller.skills[skill] >= 7: traveller.skill_training[skill] = [traveller.skill_training[skill][0], pow(2, traveller.skills[skill]-1)]
    @staticmethod
    def set_experience_levels_for_characteristic(traveller, characteristic):
        if characteristic in ["Strength", "Dexterity", "Endurance"]:
            for i in range(15):
                if traveller.characteristics[characteristic] == i+1: 
                    traveller.characteristics_training[characteristic] = [traveller.characteristics_training[characteristic][0], i+1]
        else:
            for i in range(15):
                if traveller.characteristics[characteristic] == i+1: 
                    traveller.characteristics_training[characteristic] = [traveller.characteristics_training[characteristic][0], 2*(i+1)]
    @staticmethod
    def set_experience_levels_for_skills(traveller):
        for key in traveller.skill_training.keys():
            CharacterUtils.set_experience_levels_for_skill(traveller, key)
    @staticmethod
    def set_experience_levels_for_characteristics(traveller):
        for key in traveller.characteristics_training.keys():
            CharacterUtils.set_experience_levels_for_characteristic(traveller, key)
class MapUtils():
    @staticmethod
    def get_decimal_from_hex(hex_value):
        if hex_value.lower() == "a": return 10
        elif hex_value.lower() == "b": return 11
        elif hex_value.lower() == "c": return 12
        elif hex_value.lower() == "d": return 13
        elif hex_value.lower() == "e": return 14
        elif hex_value.lower() == "f": return 15
        else: return int(hex_value)
    @staticmethod
    def get_distance_between_hexes(hex1, hex2):
        hex1A = int(hex1[:2])
        hex1B = int(hex1[2:])
        hex2A = int(hex2[:2])
        hex2B = int(hex2[2:])
        return abs(hex1A - hex2A) + abs(hex1B - hex2B)
class DiceUtils():
    @staticmethod
    def roll_dice_d6(value):
        if "D" in value or "d" in value:
            rolls = []
            for i in range( max(min(4, int(value)), 0)):
                rolls.append(random.randint(1, 6))
            if int(value) > 3:
                rolls.sort()
                rolls.reverse()
            value = rolls[0] + rolls[1]
        value = int(value)
        return value
    @staticmethod
    def roll_dice(value):
        if "d" in value:
            roll_values = value.split("d")
            v1 = int(roll_values[0])
            v2 = int(roll_values[1])
            total = 0
            for i in range(v1):
                total += random.randint(1,v2)
            value = total
        value = int(value)
        return value
class TerminalUtils():
    @staticmethod
    def selectMenuItem(options=["Yes", "No"], prompt="Select an option. $>"):
        for opt in options:
            print("{}. {}".format(options.index(opt)+1, opt))
        selection = input(prompt)
        for opt in options:
            if  selection.lower() in opt.lower():
                return opt
        value = max(1, min(int(selection), len(options)))
        if(value-1 >= 0 and value-1 <= len(options)-1):
            return options[value-1]
        return None
    @staticmethod
    def pprint(text, width=80, indent=0):
        if text == None: return None
        p = 0
        skip_space=False
        for i in text:
            p += 1
            if(skip_space and i==" "):
                skip_space=False
                continue
            elif(skip_space and i!=" "):
                skip_space=False
            sys.stdout.write('%s' % i)
            sys.stdout.flush()
            if ((p > width and i == " ") or i == "\n"):
                sys.stdout.write('\n')
                for i in range(indent):
                    sys.stdout.write(' ')
                sys.stdout.flush()
                skip_space=True
                p = 0
            #time.sleep(0.01)
        sys.stdout.write('\n')
        sys.stdout.flush()
    @staticmethod
    def get_choice_from_list(options, prompt, cannot_pick=[]):
        choice = ""
        one = False
        while not done:
            options = ""
            for opt in options:
                if opt not in cannot_pick:
                    print(opt)
            choice = input(prompt)
            for opt in options:
                if (choice.lower() == opt.lower() or choice.lower() in opt.lower()) and opt not in cannot_pick:
                    choice = opt
                    done = True
                    break
        return choice
    @staticmethod
    def get_choice_from_large_list(options, prompt, cannot_pick=[]):
        choice = ""
        done = False
        while not done:
            options = ""
            for opt in options:
                if opt not in cannot_pick:
                    options += "{}, ".format(opt)
            options = options[:-2]
            Utils.pprint(options)
            choice = input(prompt)
            for opt in options:
                if (choice.lower() in opt.lower() and opt not in cannot_pick):
                    choice = opt
                    done = True
                    break
            print("{} was not an option. please enter one of the available options.")
        return choice
# =====================================================================

# =====================================================================
# =====================================================================
# =====================================================================
# =====================================================================
# =====================================================================