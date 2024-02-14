# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
# 
import random, sys, os, getopt, pickle
from os.path import exists
from TravellerLibrary import *
from TravellerUtilsLibrary import *
from tables import Tables, CustomTables
"""
This is an application that accesses tools that help create and modify a Traveller character that will be stored in a pickle file.
"""
def usage():
    print("USAGE:")
    print("python ./character_manager.py <application> <args>")
    print("python ./character_manager.py new-traveller <name> <surname> <human> female> <height: inches> <weight: lbs>")
    print("python ./character_manager.py new-traveller Jack NPC Male Human 68 169")
    print("")
    print("Application: new-traveller")
    print("Application: view")
    print("Application: exp-characteristic|skill <skill>|char exp-value")
    print("Application: add-ally|contact|rival|enemy|relation")
    print("Application: remove-ally|contact|rival|enemy|relation")
    print("Application: edit-ally|contact|rival|enemy|relation")
    print("Application: edit-weapon|armor|equipment")
    print("Application: edit-notes|description|bio|homeworld")
    print("Application: edit-skill|characteristic")
    print("Application: add|edit|remove-trait")
    print("")
    print("Application: edit-weapons|armor")
    print("Application: edit-cash")
    print("")
    print("USAGE: python ./character_manager.py adjust-vitals <name> <surname> ")
    print("EG: python ./character_manager.py adjust-vitals Jack NPC")
    print("")
    print("USAGE: python ./character_manager.py view <name> <surname> ")
    print("EG: python ./character_manager.py view Jack NPC")

    print("")

def main():
    try:
        if (sys.argv[1].lower() in ["new-traveller"]):
            CreateTraveller.new_traveller()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["edit-cash"]):
            name = sys.argv[2] 
            surname = sys.argv[3] 
            traveller = Traveller.load(name, surname)
            CreateTraveller.edit_cash(traveller)
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["exp-char", "exp-characteristic"]):
            CreateTraveller.traveller_characteristic_exp_gain()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["exp-sk", "exp-skill"]):
            CreateTraveller.traveller_skill_exp_gain()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["add-relation"]):
            CreateTraveller.add_contact_character()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["remove-relation"]):
            CreateTraveller.remove_contact_character()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["add-ally"]):
            CreateTraveller.add_contact_character()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["edit-ally"]):
            CreateTraveller.edit_contact_character()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["remove-ally"]):
            CreateTraveller.remove_contact_character()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["add-contact"]):
            CreateTraveller.add_contact_character()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["edit-contact"]):
            CreateTraveller.edit_contact_character()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["remove-contact"]):
            CreateTraveller.remove_contact_character()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["add-rival"]):
            CreateTraveller.add_contact_character()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["edit-rival"]):
            CreateTraveller.edit_contact_character()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["remove-rival"]):
            CreateTraveller.remove_contact_character()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["add-enemy"]):
            CreateTraveller.add_contact_character()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["edit-enemy"]):
            CreateTraveller.edit_contact_character()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["remove-enemy"]):
            CreateTraveller.remove_contact_character()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["edit-weapon"]):
            name = sys.argv[2] 
            surname = sys.argv[3] 
            traveller = Traveller.load(name, surname)
            CreateTraveller.edit_weapons(traveller)
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["edit-armor"]):
            name = sys.argv[2] 
            surname = sys.argv[3] 
            traveller = Traveller.load(name, surname)
            CreateTraveller.edit_armor(traveller)
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["edit-equipment"]):
            name = sys.argv[2] 
            surname = sys.argv[3] 
            traveller = Traveller.load(name, surname)
            CreateTraveller.edit_equipment(traveller)
        elif (sys.argv[1].lower() in ["view"]): 
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["edit-notes"]):
            CreateTraveller.edit_text_field()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["edit-description"]):
            CreateTraveller.edit_text_field()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["edit-bio"]):
            name = sys.argv[2] 
            surname = sys.argv[3] 
            traveller = Traveller.load(name, surname)
            Utils.pprint(traveller.bio_summary)
            traveller.bio_summary = input("Overwrite bio: $>")
            traveller.save()
            view()
        elif (sys.argv[1].lower() in ["edit-homeworld"]):
            name = sys.argv[2] 
            surname = sys.argv[3] 
            traveller = Traveller.load(name, surname)
            Utils.pprint(traveller.homeworld)
            traveller.homeworld = input("Overwrite Homeworld: $>")
            traveller.save()
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["edit-skill"]):
            name = sys.argv[2] 
            surname = sys.argv[3] 
            traveller = Traveller.load(name, surname)
            CreateTraveller.setup_skills(traveller)
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["edit-characteristic", "edit-attribute"]):
            name = sys.argv[2] 
            surname = sys.argv[3] 
            traveller = Traveller.load(name, surname)
            CreateTraveller.setup_characteristics(traveller)
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["add-trait", "add-traits"]):
            name = sys.argv[2] 
            surname = sys.argv[3] 
            traveller = Traveller.load(name, surname)
            CreateTraveller.add_traits(traveller)
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["edit-trait", "edit-traits"]):
            name = sys.argv[2] 
            surname = sys.argv[3] 
            traveller = Traveller.load(name, surname)
            CreateTraveller.edit_traits(traveller)
            CreateTraveller.view()
        elif (sys.argv[1].lower() in ["remove-trait", "remove-traits"]):
            name = sys.argv[2] 
            surname = sys.argv[3] 
            traveller = Traveller.load(name, surname)
            CreateTraveller.remove_traits(traveller)
            CreateTraveller.view()
    except KeyboardInterrupt:
        print("Exiting...")
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()