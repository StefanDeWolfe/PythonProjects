# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
# 
import random, os, sys, re
import getopt
# 
from TravellerLibrary import *
from TravellerUtilsLibrary import *
from OtherLibrary import *
from OtherUtils import *
from tables import Tables, CustomTables
"""
This is an NPC generation tool.
"""
def in_args(args, arg):
    for a in args:
        if arg in a:
            return True
    return False
def get_arg_in_args(args, arg):
    for a in args:
        if arg in a:
            return a
    return None
def get_arg(args, arg):
    for a in args:
        if arg in a:
            result = a.split(":")[1]
            result = result.replace("_"," ")
            return result
    return None
def testNpc(name, surname, arguements):
    args = arguements.split("-")
    sex="random"
    if in_args(args, "sex"): sex = get_arg(args, "sex")
    if name is None:
        if sex.lower() in ["female"]:
            name = NameGenerator.normalize_name(NameGenerator.get_random_female_name())
        elif sex.lower() in ["male"]:
            name = NameGenerator.normalize_name(NameGenerator.get_random_male_name())
        else:
            name = NameGenerator.normalize_name(NameGenerator.get_random_name())
    if surname is None:
        surname = NameGenerator.normalize_name(NameGenerator.get_random_surname())
    age="random-adult"
    if in_args(args, "age"): age = get_arg(args, "age")
    if "adult" in age.lower(): age = "random-adult"
    elif "older" in age.lower(): age = "random-older"
    elif "longlife" in age.lower(): age = "random-longlife"
    elif "kid" in age.lower(): age = "random-kid"
    elif "longlifekid" in age.lower(): age = "random-longlife-kid"
    terms="random"
    if in_args(args, "terms"): terms = get_arg(args, "terms")
    apparent_gender="random"
    if in_args(args, "gender"): apparent_gender = get_arg(args, "gender")
    if apparent_gender.lower() in ["same"]: apparent_gender = "Same as sex"
    elif apparent_gender.lower() in ["opposite"]: apparent_gender = "Opposite of sex"
    else: apparent_gender = "Non-binary"
    
    species="random"
    if in_args(args, "species"): species = get_arg(args, "species")
    subspecies="random" 
    if in_args(args, "subspecies"): subspecies = get_arg(args, "subspecies")
    height="random"
    if in_args(args, "height"): height = get_arg(args, "height")
    weight="random"
    if in_args(args, "weight"): weight = get_arg(args, "weight")
    fitness="random"
    if in_args(args, "fitness"): fitness = get_arg(args, "fitness")

    upp="random"
    if in_args(args, "upp"): upp = get_arg(args, "upp")

    career="random"
    if in_args(args, "career"): career = get_arg(args, "career")

    hair_length = None
    if in_args(args, "hair_length"): hair_length = get_arg(args, "hair_length")
    hair_style = None
    if in_args(args, "hair_style"): hair_style = get_arg(args, "hair_style")
    hair_color = None
    if in_args(args, "hair_color"): hair_color = get_arg(args, "hair_color")
    hair_beard = None
    if in_args(args, "hair_beard"): hair_beard = get_arg(args, "hair_beard")
    if sex.lower() in ["female"] and apparent_gender.lower() in ["same as sex", "same", "non-binary"]:
        hair_beard = None
    hair={"length":hair_length, "style":hair_style, "color":hair_color, "beard":hair_beard}

    origin="random"
    if in_args(args, "origin"): origin = get_arg(args, "origin")
    elif origin.lower() in ["local"]:  origin = "Local Area"
    elif origin.lower() in ["inner"]:  origin = "Inner System"
    elif origin.lower() in ["outer"]:  origin = "Outer System"
    elif origin.lower() in ["neighboring"]:  origin = "Neighboring System"
    elif origin.lower() in ["neighboringsubsector"]:  origin = "Neighboring Subsector"
    disposition="random"
    if in_args(args, "disposition"): disposition = get_arg(args, "disposition")
    motivation1="random"
    motivation1_value="random"
    if in_args(args, "motivation1"): motivation1 = get_arg(args, "motivation1")
    if in_args(args, "motivation1_value"): motivation1_value = get_arg(args, "motivation1_value")
    motivation2="random"
    motivation2_value="random"
    if in_args(args, "motivation2"): motivation2 = get_arg(args, "motivation2")
    if in_args(args, "motivation2_value"): motivation2_value = get_arg(args, "motivation2_value")
    quirk1="random"
    quirk2="random"
    if in_args(args, "quirk1"): quirk1 = get_arg(args, "quirk1")
    if in_args(args, "quirk2"): quirk2 = get_arg(args, "quirk2")
    hex_location="random"
    system_location="random"
    local_location="random"
    if in_args(args, "hex"): quirk1 = get_arg(args, "hex")
    if in_args(args, "planet"): quirk1 = get_arg(args, "planet")
    if in_args(args, "location"): quirk2 = get_arg(args, "location")
    npc = Npc(Npc.generate(
            name=name, surname=surname, 
            age=age, terms=terms,
            sex=sex, apparent_gender=apparent_gender,
            species=species, subspecies=subspecies, 
            height=height, weight=weight, fitness=fitness,
            upp=upp, career=career,
            hair=hair,
            origin=origin, disposition=disposition, 
            motivation1=motivation1, motivation1_value=motivation1_value, 
            motivation2=motivation2, motivation2_value=motivation2_value, 
            quirk1=quirk1, quirk2=quirk2,
            hex_location=hex_location,
            system_location=system_location,
            local_location=local_location,
            ))
    displayNpc(npc)
    return npc

def displayNpc(npc):
    print("NPC:")
    print("Name:          {} {}".format(npc.name, npc.surname))
    print("UPP:           {}".format(npc.upp))
    print("Age:           {}".format(npc.age))
    print("Sex / Gender:  {}/{}".format(npc.sex, npc.apparent_gender))
    print("Species:       {} {}".format(npc.species, npc.subspecies))
    print("Career/ Terms: {}".format(npc.career, npc.terms))
    print("Height:        {} {}".format(npc.height, npc.height_description))
    print("Mass:          {} {}".format(npc.weight, npc.mass_description))
    print("Hair Length:   {}".format(npc.hair["length"]))
    print("Hair Style:    {}".format(npc.hair["style"]))
    print("Hair Color:    {}".format(npc.hair["color"]))
    if npc.hair.get("beard", None) not in [None, "None"]: 
        print("Facial Hair:   {}".format(npc.hair["beard"]))
    print("Origin:        {}".format(npc.origin))
    print("Disposition:   {}".format(npc.disposition))
    print("Motivation:    {}".format(npc.motivation1))
    if npc.motivation2 not in [None, "None"]: print("Motivation 2:  {}".format(npc.motivation2))
    print("Quirk:         {}".format(npc.quirk1))
    if npc.quirk2 not in [None, "None"]: print("Quirk 2:       {}".format(npc.quirk2))
    print("Combat Skills:")
    for skill in npc.combatSkills.keys():
        print("- {}-{}".format(skill, npc.combatSkills[skill]))
    print("Business Skills:")
    for skill in npc.businessSkills.keys():
        print("- {}-{}".format(skill, npc.businessSkills[skill]))

def testDebug():
    npc = testNpc()
# =====================================================================
def usage():
    print("USAGE:")
    print("python tool8_3_npc_generator.py --name Jack-NPC ")
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvs:f:a:", ["help", "name=", "file=", "arguments="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    viewHexCoord = False
    full_name = None
    name = None
    surname = None
    fileName = None
    uwp = None
    arguements = None
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-n", "--name"):
            full_name = a.split("-")
            name = full_name[0]
            if len(full_name) > 1:
                surname = full_name[1]
        elif o in ("-a", "--arguments"):
            arguements = a
        elif o in ("-f", "--file"):
            fileName = a
        else:
            assert False, "unhandled option"
    #
    npc = testNpc(name, surname, arguements)
    
    #
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
