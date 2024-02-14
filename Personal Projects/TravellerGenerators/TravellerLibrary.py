# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
import random, sys, os
import pickle
import getopt
from os.path import exists
from TravellerUtilsLibrary import *

class Demographics():
    @staticmethod
    def getZenophobicPercents(): return [97,3]
    @staticmethod
    def getIsolatedPercents(): return [97,2,1]
    @staticmethod
    def getSemiMixedPercents(): return [79,9,5,4,3]
    @staticmethod
    def getMixedPercents(): return [79,9,5,3,2,1,1]
    @staticmethod
    def getIntegratedPercents(): return [37,20,18,10,7,5,3]
    @staticmethod
    def getInclusivePercents(): return [30,20,18,10,7,5,3,2,2,1,1,1]
    @staticmethod
    def getSpeciesFromDelographicPercents(percents, species_list):
        if len(percents) < 1:
            raise Exception("Demographics Error: List of percents is greater than list of species. Add more species then run again.")
        if len(percents) > len(species_list):
            raise Exception("Demographics Error: List of percents is greater than list of species. Add more species then run again.")
        roll = random.randint(1,100)
        total=0
        for i in percents:
            total+=i
            if roll <= total:
                return species_list[percents.index(i)] 
        return species_list[len(species_list)-1]


class NameGenerator():
    consonants = ["b","b","c","c","d","d","d","d","f","f","g","g","g","h","h","j","k",
                    "l","l","l","l","m","m","n","n","n","n","n","n","p","p","qu","r","r","r","r","r","r",
                    "s","s","s","s","t","t","t","t","t","t","v","v","w","w","x","y","z"]
    vowels = ["a", "e", "i", "o", "u","a", "e", "e", "i", "o", "a", "e", "e", "i", "o", 
                "a", "e", "e", "i", "o", "a", "e", "i", "y", "u","a", "e", "i", "o", 
                "a", "e", "i", "o", "u","a", "e", "i", "o","a", "e", "i", "o", "u"]
    consonant_combos = ["ts","st","gh","ck", "ll", "sh","ch","sp","th","wh","nd"]
    vowel_combos = ["au","ai", "ea", "ae","ao","oo","ou","oi","io","eu","ui"]
    vowels_lesser = ["a","o","i"]
    vowels_greater = ["a","e","i","o","u"]
    @staticmethod
    def normalize_name(name="NAME"): return name[0].upper() + name[1:].lower()
    @staticmethod
    def get_random_male_name():
        pass
        return NameGenerator.get_random_name_from_file(file="MaleFirstNames.txt")
    @staticmethod
    def get_random_female_name():
        pass
        return NameGenerator.get_random_name_from_file(file="FemaleFirstNames.txt")
    @staticmethod
    def get_random_surname():
        pass
        return NameGenerator.get_random_name_from_file(file="Surnames.txt")
    @staticmethod
    def get_random_name_from_file(file="FemaleFirstNames.txt"):
        file1 = open(file, 'r') 
        Lines = file1.readlines() 
        names=[]
        count = 0
        # Strips the newline character 
        for line in Lines: 
            name = line.strip()
            #print(name) 
            names.append(name)
            #print("{}".format(name)) 
        return NameGenerator.normalize_name(names[random.randint(0,len(names)-1)])
    @staticmethod
    def get_random_name(selected_name_type=""):
        name=""
        first = True
        name_types = [
        "cv","vc",
        "cvc","vcv", "cvc","vcv",
        "cVc","vCv",
        "cvcv","vcvc", "cvcv","vcvc",
        "cVcv","vCvc",
        "cvCv","vcVc",
        "cvcvc","vcvcv", "cvcvc","vcvcv",
        "cvCvc","vcVcv",
        "cVcvc","vcvCv",
        "cvcvcv","vcvcvc"
        #"",
        ]
        if(selected_name_type==""):
            selected_name_type = name_types[random.randint(0,len(name_types)-1)]
        for i in selected_name_type:
            if(i == "v"):
                name += NameGenerator.vowels[random.randint(0,len(NameGenerator.vowels)-1)]
            elif(i == "c"):
                name += NameGenerator.consonants[random.randint(0,len(NameGenerator.consonants)-1)]
            if(i == "V"):
                name += NameGenerator.vowel_combos[random.randint(0,len(NameGenerator.vowel_combos)-1)]
            elif(i == "C"):
                name += NameGenerator.consonant_combos[random.randint(0,len(NameGenerator.consonant_combos)-1)]
        name = NameGenerator.normalize_name(name)            
        return name
class PseudoMarkovNameGenerator():
    @staticmethod
    def readLinesFromFile(filename):
        lines = []
        with open(filename) as file:
            lines = file.readlines()
            lines = [line.lower().rstrip() for line in lines]
        return lines
    @staticmethod
    def getName(lines, verbose=False):
        name1 = lines[random.randint(0,len(lines)-1)]
        name2 = lines[random.randint(0,len(lines)-1)]
        part1 = name1[:len(name1)//2] 
        part2 = name2[len(name2)//2:]
        if (verbose): print("{} - {}".format(part1, part2))
        return part1[0].upper() + part1[1:] + part2
class StarWarsPlanetNameGenerator():
    @staticmethod
    def getName():
        starting_consonants = ["B", "C", "D", "F", "G", "J", "K", "L", "M", "N", "P", "QU", "S", "T", "V", "X", "Z" "H",  "R", "W", "Y", "ST", "CH", "TH",]
        consonants = ["B", "C", "D", "F", "G", "J", "K", "L", "M", "N", "P", "QU", "S", "T", "V", "X", "Z" "H", "RR", "R", "W", "Y", "ST", "CH", "NG", "TH", "ND", "CK", "LL"]
        vowels = ["A", "AU", "E", "EA", "I", "O", "OO", "OU", "U"]
        endings = ["", "", "aan", "ooine", "afar", "ant"]
        # ends in ooine
        # aan
        # 

        name = random.choice(starting_consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(endings)
        return name[0].upper() + name[1:].lower()
class DescriptionGenerator(object):
    species = { 
        # 1-4 Common
        "Human":["Standard"], 

        # 5 Rare
        "Vargr": ["Standard"],
        # 6 Rare
        "Aslan": ["Standard"],
    }
    species_descriptions = {
        "Human":"Your standard 4 limbed terran upright primeape, 2 arms with 5 digits, 2 legs, a generally hairless torso, and head with two eyes a nose with poor sense of smell and omnivorous teeth filled mouth.", 
        "Vargr": "The Vargr are the only major race to have been uplifted by the Ancients, a fact that the Vargr are extremely proud of. They are typically seen by other races as aggressive pirates and scavengers but the Vargr actually have a diverse culture that is deeply rooted in their pack mentality and the desire for companionship, charisma and loyalty. Their constant struggle for charisma and leadership results in a culture fuelled by conflict and change.",
        "Aslan": "The Aslan are the youngest of the great powers, an expansionist race of feuding clans and predatory warriors, eager to seize all the universe has to offer. Aslan are descended from four-limbed carnivorous pouncer stock which was originally near the top of the food chain in the forests of their homeworld, Kusyu. True to their pouncer ancestry, Aslan are capable of short bursts of speed somewhat greater than that manageable by humans. They also have slightly superior hearing and night vision. Otherwise, they are one of the most humanlike of all alien races, excepting, of course, the Vargr (who are, after all, genetically-altered mammalian stock  originally from Earth).",
        
    }
    species_sexes = {
        "Human":["Male", "Female"], 
        "Vargr": ["Male", "Female"],
        "Aslan": ["Standard"],
    }
    tagData = {
        "Abandoned Colony": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Alien Ruins": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Altered Humanity": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Anarchists": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Anthropomorphs": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Area 51": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Badlands World": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Battleground": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Beastmasters": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Bubble Cities": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Cheap Life": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Civil War": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Cold War": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Colonized Population": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Cultural Power": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Cybercommunists": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Cyborgs": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Cyclical Doom": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Desert World": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Doomed World": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Dying Race": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Eugenic Cult": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Exchange Consulate": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Fallen Hegemon": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Feral World": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Flying Cities": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Forbidden Tech": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Former Warriors": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Freak Geology": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Freak Weather": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Friendly Foe": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Gold Rush": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Great Work": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Hatred": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Heavy Industry": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Heavy Mining": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Hivemind": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Holy War": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Hostile Biosphere": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Hostile Space": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Immortals": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Local Specialty": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Local Tech": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Major Spaceyard": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Mandarinate": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Mandate Base": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Maneaters": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Megacorps": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Mercenaries": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Minimal Contact": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Misandry/Misogyny": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Night World": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Nomads": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Oceanic World": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Out of Contact": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Outpost World": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Perimeter Agency": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Pilgrimage Site": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Pleasure World": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Police State": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Post-Scarcity": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Preceptor Archive": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Pretech Cultists": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Primitive Aliens": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Prison Planet": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Psionics Academy": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Psionics Fear": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Psionics Worship": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Quarantined World": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Radioactive World": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Refugees": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Regional Hegemon": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Restrictive Laws": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Revanchists": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Revolutionaries": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Rigid Culture": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Rising Hegemon": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Ritual Combat": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Robots": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Seagoing Cities": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Sealed Menace": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Secret Masters": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Sectarians": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Seismic Instability": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Shackled World": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Societal Despair": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Sole Supplier": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Taboo Treasure": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Terraform Failure": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Theocracy": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Tomb World": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Trade Hub": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Tyranny": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Unbraked AI": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Urbanized Surface": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Utopia": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Warlords": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Xenophiles": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Xenophobes": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        "Zombies": {"Description": "", "Entity Type": "Planet", "Enemies": [], "Friends": [], "Complications": [], "Things": [], "Places": []},
        }
    @staticmethod
    def getSpeciesDistribution(species=["Human", "Minor Human Race"], distribution=None):
        ''' http://www.ianewilliamson.co.uk/rpg/DnD/rules/worldgen/settlement.html
            Official race percentages
            Race                            Isolated    Mixed   Integrated
            Main race (eg human)            97%         79%         37%
            Main minority (eg halfling)     2%          9%          20%
            Second minority (eg elf)        1%          5%          18%
            Third minority (eg dwarf)                   3%          10%
            Fourth minority (eg gnome)                  2%          7%
            Fifth minority (eg half-elf)                1%          5%
            Sixth minority (eg half-orc)                1%          3%
            '''
        if distribution is None: distribution = "semi-integrated"
        distribution_map = {}
        for race in DescriptionGenerator.species.keys():
            distribution_map[race] = 0
        if distribution.lower() == "integrated":
            if len(species) < 7:
                for i in range(7-len(species)):
                    species.append(random.choice(list(distribution_map.keys())))
            distribution_map[species[0]] = 37
            distribution_map[species[1]] = 20
            distribution_map[species[2]] = 18
            distribution_map[species[3]] = 10
            distribution_map[species[4]] = 7
            distribution_map[species[5]] = 5
            distribution_map[species[6]] = 3
        elif distribution.lower() == "mixed":
            if len(species) < 7:
                for i in range(7-len(species)):
                    species.append(random.choice(list(distribution_map.keys())))
            distribution_map[species[0]] = 79
            distribution_map[species[1]] = 9
            distribution_map[species[2]] = 5
            distribution_map[species[3]] = 3
            distribution_map[species[4]] = 2
            distribution_map[species[5]] = 1
            distribution_map[species[6]] = 1
        elif distribution.lower() == "isolated":
            if len(species) < 3:
                for i in range(3-len(species)):
                    species.append(random.choice(list(distribution_map.keys())))
            distribution_map[species[0]] = 97
            distribution_map[species[1]] = 2
            distribution_map[species[2]] = 1
        else:
            if len(species) < 5:
                for i in range(5-len(species)):
                    species.append(random.choice(list(distribution_map.keys())))
            distribution_map[species[0]] = 79
            distribution_map[species[1]] = 9
            distribution_map[species[2]] = 5
            distribution_map[species[3]] = 4
            distribution_map[species[4]] = 3
        return distribution_map

    @staticmethod
    def getSizeDescription(value):
        if(value in [1]): return "1,600 km (Triton), 0.05g" 
        elif(value in [2]): return "3,200 km (Luna,Europa), 0.15g" 
        elif(value in [3]): return "4,800 km (Mercury, Ganymede), 0.25g" 
        elif(value in [4]): return "6,400 km (<Mars), 0.35g" 
        elif(value in [5]): return "8,000 km (Mars), 0.45g" 
        elif(value in [6]): return "9,600 km (>Mars), 0.7g" 
        elif(value in [7]): return "11,200 km (<Earth), 0.9g" 
        elif(value in [8]): return "12,800 km (Earth), 1.0g" 
        elif(value in [9]): return "14,400 km (>Earth), 1.25g" 
        elif(value in [10]): return "16,000 km (large Earth), 1.4g"
        #A
        else: return "Less that 1000km (Asteroid, orbital complex) negligible Gravity"
    @staticmethod
    def getAtmosphereDescription(value):
        if(value in [1]): return "Trace (Mars). Pressure 0.001 to 0.09 atmos. Vacc suit Required." 
        elif(value in [2]): return "Very Thin, Tainted.  Pressure 0.01 to 0.42 atmos. Respirator & Filter Required." 
        elif(value in [3]): return "Very Thin. Pressure 0.01 to 0.42 atmos. Respirator Required." 
        elif(value in [4]): return "Thin, Tainted. Pressure 0.43 to 0.7 atmos. Filter Required." 
        elif(value in [5]): return "Thin (like high mountains). Pressure 0.43 to 0.7 atmos. Breathable unassisted." 
        elif(value in [6]): return "Standard (Earth-like). Pressure 0.71 to 0.1.49 atmos. Breathable unassisted." 
        elif(value in [7]): return "Standard, Tainted.  Pressure 0.71 to 0.1.49 atmos. Filter Required." 
        elif(value in [8]): return "Dense. Pressure 1.5 to 2.49 atmos. Breathable unassisted." 
        elif(value in [9]): return "Dense, Tainted. Pressure 1.5 to 2.49 atmos. Filter Required."  
        elif(value in [10]): return "Exotic. Various pressure values.  Air Supply Required." 
        elif(value in [11]): return "Corrosive (Venus). Various pressure values. Vacc suit Required."
        elif(value in [12]): return "Insidious. Various pressure values. Vacc suit Required."
        elif(value in [13]): return "Very Dense. Pressure >2.5 atmos. possibly allows breathing unassisted, but only from high in atmosphere, where pressure is lower"
        elif(value in [14]): return "Low. Pressure <0.5 atmos. no assistance required when at sealevel; higher levels required assistive breathing equipment."
        elif(value in [15]): return "Unusual. Various pressure values. Various Assistance Required"
        else: return "None (Luna). Pressure 0.00 atmos. Vacc suit Required."
    @staticmethod
    def getHydrographicsDescription(value):
        if(value in [1]): return "6-15% water coverage.  Dry world." 
        elif(value in [2]): return "16-25% water coverage.  Few small seas." 
        elif(value in [3]): return "26-35% water coverage.  Small seas and oceans." 
        elif(value in [4]): return "36-45% water coverage.  Wet world." 
        elif(value in [5]): return "46-55% water coverage.  Large oceans." 
        elif(value in [6]): return "56-65% water coverage.  Large oceans." 
        elif(value in [7]): return "66-75% water coverage.  Earth-like world." 
        elif(value in [8]): return "76-85% water coverage.  Water world." 
        elif(value in [9]): return "86-95% water coverage.  Only a few small islands and archipelagos" 
        elif(value in [10]): return "96-100% water coverage.  Almost entirely covered with water."
        else: return "0-5% water coverage.  Desert world."
    @staticmethod
    def getTemperatureDescription(value):
        if(value <=2 or value in ["2","1","0","-1","-2","-3","-4","-5","-6"]): return "Frozen world. -51c or less. Frozen world. No liquid water, very dry atmosphere." 
        elif(value in [3, 4, "3","4"]): return "Cold. -51c to 0c. Icy world. Little liquid water, extensive ice caps, few clouds." 
        elif(value in [5, 6, 7, 8, 9, "5", "6", "7", "8", "9"]): return "Temperate. 0c to 30c. Temperate world. Earth-like. Liquid & vaporized water are common, moderate ice caps." 
        elif(value in [10, 11, "A","B"]): return "Hot. 31c to 80c. Hot world. Small or no ice caps, little liquid water.  Most water in the form of clouds." 
        elif(value >= 12 or value in ["C","D","E","F","16","17","18","19","20"]): return "Boiling. 81c or more. Boiling world. No ice caps, little liquid water." 
        else: return "ERROR IN Temperature Description"
    @staticmethod
    def getPopulationDescription(value):
        if(value in [1]): return "Few, 1-100 people. A tiny farmstead, work crew, or single family." 
        elif(value in [2]): return "Hundreds, 100+ people. A village" 
        elif(value in [3]): return "Thousands , 1k+ people."
        elif(value in [4]): return "Tens of thousands, 10k+. Small town." 
        elif(value in [5]): return "Hundreds of thousands, 100k+ people. Average city." 
        elif(value in [6]): return "Millions, 1,000k+ people." 
        elif(value in [7]): return "Tens of millions, 10M+ people. Large city." 
        elif(value in [8]): return "Hundreds of millions, 100M+ people." 
        elif(value in [9]): return "Billions, 1,000M+ people. Present-day Earth." 
        elif(value in [10]): return "Tens of billions, 10B+ people. "
        elif(value in [11]): return "Hundreds of billions, 100B+ people. Incredibly crowded world."
        elif(value in [12]): return "Trillions, 1,000B+ people. World city / orbital habitats."
        else: return "None, 0 population. No one around."
    @staticmethod
    def getPopulationTotal(value):
        if(value in [1]):  return 10
        elif(value in [2]): return 100
        elif(value in [3]): return 1000
        elif(value in [4]): return 10000 
        elif(value in [5]): return 100000 
        elif(value in [6]): return 1000000
        elif(value in [7]): return 10000000 
        elif(value in [8]): return 100000000 
        elif(value in [9]): return 1000000000 
        elif(value in [10]): return 10000000000
        elif(value in [11]): return 100000000000
        elif(value in [12]): return 1000000000000
        else: return 1
    @staticmethod
    def getGovernmentDescription(value):
        if(  value in [1,"1"]): return "Company/Corperation.  Ruling functions are assumed by a company managerial elite, and most citizenry are company employees or dependants. (Corporate outpost, asteroid mine, feudal domain.) Contraband [Weapons,Drugs,Travellers]" 
        elif(value in [2,"2"]): return "Participating Democracy.  Ruling functinos are reached by the advice and concent of the citizenry directly. (Collective, tribal council, commlinked consensus) Contraband [Drugs]"  
        elif(value in [3,"3"]): return "Self-Perpetuating Oligarchy. Ruling functions are performed by a restricted minority, with little or no input from the mass of citizenry. (Plutocracy, hereditary ruling caste) Contraband [Technology, Weapons, Travellers]" 
        elif(value in [4,"4"]): return "Representitive Democracy. Ruling functions are performed by elected representitives. (Republic, democracy) [Drugs, Weapons, Psionics]"
        elif(value in [5,"5"]): return "Feudal Technocracy. Ruling functions are performed by specific individuals for persons who agree to be ruled by them. Relationship are based on the performance of technical activities which are mutually benefitial. (Technology = Social status) Contraband [Technology, Weapons, Computers]" 
        elif(value in [6,"6"]): return "Captive Govenment. Ruling functions are performed by an imposed leadership answerable to an outside group. (A colony or conquered area) Contraband [Weapons, Technology, Travellers]" 
        elif(value in [7,"7"]): return "Balkanisation. No central authority exists; rival governments compete for control. Law levels refer to the government nearest starport. (Multiple governments, civil war) Contraband [Varies]" 
        elif(value in [8,"8"]): return "Civil Service Bureaucracy. Ruling functions are performed by government agencies employing individuals selected for their expertise. (Techocracy, Communism) Contraband [Drugs, Weapons]" 
        elif(value in [9,"9"]): return "Impersonal Bureaucracy. Ruling functions are performed by agencies which have become insulated from the governed citizens. (Entrenched castes of bureaucrats, decaying empire) Contraband [Technology, Weapons, Drugs, Travellers, Psionics]" 
        elif(value in [10,"10","a","A"]): return "Charismatic Dictator. Ruling functions are performed by agencies directed by a single leader who enjoys the overwhelming confidence of the citizens. (Revolutionary leader, Messiah, emperor) Contraband [None]"
        elif(value in [11,"11","b","B"]): return "Non-Charismatic Leader. A previous charismatic dictator has been replaced by a leader through normal channels. (Military dictatorship, hereditary kingship) Contraband [Weapons, Technology, Computers]"
        elif(value in [12,"12","c","C"]): return "Charismatic Oligarchy. Ruling functions are performed by a select group of members of an organisation or class which enjoys the overwhelming confidence of the citizens. (Junta, Revolutionary Council) Contraband [Weapons]"
        elif(value in [13,"13","d","D"]): return "Religious Dictatorship.  Ruling functions are performed by a religious organisation without regard to the specific individual needs of the citizenry. (Cult, transcendent philosophy, psionic group mind) Contraband [Varies]"
        elif(value in [14,"14","e","E"]): return "Religious Autocracy.  Government by a single religious leader having absolute power over its citizenry. (Messiah) Contraband [Varies]"
        elif(value in [15,"15","f","F"]): return "Totalitarian Oligarchy. Government by an all-powerful minority which maintains absolute control through widespread coercian and oppression. (World Church, Ruthless Corperation) Contraband [Varies]"
        else: return "None.  No government structure.  In most cases, family bons predominate. (Family Clan, Anarchy) Contraband [None]"
    @staticmethod
    def getCultureDescription(value):
        if(str(value)=="11"): return "Sexist – one gender is considered subservient or inferior to the other." 
        elif(str(value)=="12"): return "Religious – culture is heavily influenced by a religion or belief systems, possibly one unique to this world" 
        elif(str(value)=="13"): return "Artistic – art and culture are highly prized. Aesthetic design is important in all artefacts produced on world." 
        elif(str(value)=="14"): return "Ritualised – social interaction and trade is highly formalised. Politeness and adherence to traditional forms is considered very important." 
        elif(str(value)=="15"): return "Conservative – the culture resists change and outside influences." 
        elif(str(value)=="16"): return "Xenophobic – the culture distrusts outsiders and alien influences. Offworlders will face considerable prejudice." 
        elif(str(value)=="21"): return "Taboo – a particular topic is forbidden and cannot be discussed. Travellers who unwittingly mention this topic will be ostracised." 
        elif(str(value)=="22"): return "Deceptive – trickery and equivocation are considered acceptable. Honesty is a sign of weakness." 
        elif(str(value)=="23"): return "Liberal – the culture welcomes change and offworld influence. Travellers who bring new and strange ideas will be welcomed." 
        elif(str(value)=="24"): return "Honourable – one’s word is one’s bond in the culture. Lying is both rare and despised." 
        elif(str(value)=="25"): return "Influenced – the culture is heavily influenced by another, neighbouring world. Roll again for a cultural quirk that has been inherited from the culture." 
        elif(str(value)=="26"): return "Fusion – the culture is a merger of two distinct cultures. Roll again twice to determine the quirks inherited from these cultures. If the quirks are incompatible, then the culture is likely divided." 
        elif(str(value)=="31"): return "Barbaric – physical strength and combat prowess are highly valued in the culture. Travellers may be challenged to a fight, or dismissed if they seem incapable of defending themselves. Sports tend towards the bloody and violent." 
        elif(str(value)=="32"): return "Remnant – the culture is a surviving remnant of a once-great and vibrant civilisation, clinging to its former glory. The world is filled with crumbling ruins, and every story revolves around the good old days." 
        elif(str(value)=="33"): return "Degenerate – the culture is falling apart and is on the brink of war or economic collapse. Violent protests are common, and the social order is decaying." 
        elif(str(value)=="34"): return "Progressive – the culture is expanding and vibrant. Fortunes are being made in trade; science is forging bravely ahead." 
        elif(str(value)=="35"): return "Recovering – a recent trauma, such as a plague, war, disaster or despotic regime has left scars on the culture." 
        elif(str(value)=="36"): return "Nexus – members of many different cultures and species visit here" 
        elif(str(value)=="41"): return "Tourist Attraction – some aspect of the culture or the planet draws visitors from all over charted space." 
        elif(str(value)=="42"): return "Violent – physical conflict is common, taking the form of duels, brawls or other contests. Trial by combat is a part of their judicial system." 
        elif(str(value)=="43"): return "Peaceful – physical conflict is almost unheardof. The culture produces few soldiers, and diplomacy reigns supreme. Forceful Travellers will be ostracised." 
        elif(str(value)=="44"): return "Obsessed – everyone is obsessed with or addicted to a substance, personality, act or item. This monomania pervades every aspect of the culture." 
        elif(str(value)=="45"): return "Fashion - fine clothing and decoration are considered vitally important in the culture. Underdressed Travellers have no standing here." 
        elif(str(value)=="46"): return "At war – the culture is at war, either with another planet or polity, or is troubled by terrorists or rebels." 
        elif(str(value)=="51"): return "Unusual Custom: Offworlders – space travellers hold a unique position in the culture’s mythology or beliefs, and travellers will be expected to live up to these myths" 
        elif(str(value)=="52"): return "Unusual Custom: Starport – the planet’s starport is more than a commercial centre; it might be a religious temple, or be seen as highly controversial and surrounded by protestors." 
        elif(str(value)=="53"): return "Unusual Custom: Media – news agencies and telecommunications channels are especially strange here. Getting accurate information may be difficult." 
        elif(str(value)=="54"): return "Unusual Customs: Technology – the culture interacts with technology in an unusual way. Telecommunications might be banned, robots might have civil rights, or cyborgs might be property." 
        elif(str(value)=="55"): return "Unusual Customs: Lifecycle – there might be a mandatory age of termination, or anagathics might be widely used. Family units might be different, with children being raised by the state or banned in favour of cloning." 
        elif(str(value)=="56"): return "Unusual Customs: Social Standings – the culture has  a distinct caste system. Travellers of a low social standing who do not behave appropriately will face punishment." 
        elif(str(value)=="61"): return "Unusual Customs: Trade – the culture has an odd attitude towards some aspect of commerce, which may interfere with trade at the spaceport. For example, merchants might expect a gift as part of a deal, or some goods may only be handled by certain families." 
        elif(str(value)=="62"): return "Unusual Customs: Nobility – those of high social standing have a strange custom associated with them; perhaps nobles are blinded, or must live in gilded cages, or only serve for a single year before being exiled." 
        elif(str(value)=="63"): return "Unusual Customs: Sex – the culture has an unusual attitude towards intercourse and reproduction. Perhaps cloning is used instead, or sex is used to seal commercial deals." 
        elif(str(value)=="64"): return "Unusual Customs: Eating – food and drink occupies an unusual place in the culture. Perhaps eating is a private affair, or banquets and formal dinners are seen as the highest form of politeness." 
        elif(str(value)=="65"): return "Unusual Customs: Travel – travellers may be distrusted or feted, or perhaps the culture frowns on those who leave their homes." 
        elif(str(value)=="66"): return "Unusual Custom: Conspiracy – something strange is going on. The government is being subverted by another group or agency." 
        else: return "<CULTURAL DIFFERENCE ERROR: NOT IN SCOPE>"
    @staticmethod
    def getLawLevelDescription(value):
        if(value in [0, "0"]): return "No restrictions - Heavy armor and a handy weapon recommended."
        elif(value in [1, "1"]): return "Banned Weapons: Poison gas, explosives, undetectable weapons, WMDs.  Max armor permitted: Battle dress." 
        elif(value in [2, "2"]): return "Banned Weapons: Portable energy and laser weapons.  Max armor permitted: Combat Armor." 
        elif(value in [3, "3"]): return "Banned Weapons: Military grade weapons (automatics).  Max armor permitted: Flak armor." 
        elif(value in [4, "4"]): return "Banned Weapons: Light assault automatic weapons, submachine guns.  Max armor permitted: Cloth Armor." 
        elif(value in [5, "5"]): return "Banned Weapons: Personal Concealable weapons.  Max armor permitted: Mesh Armor." 
        elif(value in [6, "6"]): return "Banned Weapons: All firearms except Shotguns, Stunners; carrying weapons discouraged (by law).  Max armor permitted: Mesh Armor." 
        elif(value in [7, "7"]): return "Banned Weapons: Shotguns.  Max armor permitted: Mesh Armor." 
        elif(value in [8, "8"]): return "Banned Weapons: All bladed weapons, stunners.  Max armor permitted: All visible armor." 
        else: return "All weapons and armor banned." 
    @staticmethod
    def GetBaseDescription(value):
        bases = ["S","R","N"]
        if(value=="S"): return "Scout" 
        elif(value=="R"): return "Reserach" 
        elif(value=="N"): return "Naval" 
        elif(value=="T"): return "TAS" 
        else:  return "TAS & " +DescriptionGenerator.GetBaseDescription(bases[random.randint(0,len(bases)-1)]) + ""
    @staticmethod
    def getStarportClass(starport):
        if(starport in [11, 12, 13, 14, 15, 16, 17, 18, "A"]): return "A"
        elif(starport in [9, 10, "B"]): return "B"
        elif(starport in [7, 8, "C"]): return "C"
        elif(starport in [5, 6, "D"]): return "D"
        elif(starport in [3, 4, "E"]): return "E"
        else: return "X"
    @staticmethod
    def getStarportDescription(starport, berthing_cost=500):
        if(starport in [11, 12, 13, 14, 15, 16, 17, 18, "A"]): return "Excellent, "+str(berthing_cost)+"cr Berthing cost.  Refined fuel available. Shipyard (all) Repair facilities. "
        elif(starport in [9, 10, "B"]): return "Good, "+str(berthing_cost)+"cr Berthing cost.  Refined fuel available. Shipyard (spacecraft) Repair facilities. "
        elif(starport in [7, 8, "C"]): return "Routine, "+str(berthing_cost)+"cr Berthing cost.  Unrefined fuel available. Shipyard (small craft) Repair facilities. "
        elif(starport in [5, 6, "D"]): return "Poor, "+str(berthing_cost)+"cr Berthing cost.  Unrefined fuel available. Limited Repair facilities. "
        elif(starport in [3, 4, "E"]): return "Frontier, No Berthing cost.  No fuel available. No Repair facilities. "
        elif(starport in [-2, -1, 0, 1, 2, "X"]): return "No spaceport. "
    @staticmethod
    def GetTravelCodeDescription(value):
        if(value=="A"): return "*Amber Travel Zone* Exercise caution, danger exists within this system."
        elif(value=="R"): return "!Restricted Travel Zone! Major Danger within system. Disease or Ongoing War present or Protected space."
        else: return "System is safe for travellers."
    @staticmethod
    def GetTradeCodeDescription(value):
        if(value=="Ag"): return "Agricultural" 
        elif(value=="As"): return "Asteroid" 
        elif(value=="Ba"): return "Barren" 
        elif(value=="De"): return "Desert" 
        elif(value=="Fl"): return "Fluid Oceans" 
        elif(value=="Ga"): return "Garden" 
        elif(value=="Hi"): return "High Population" 
        elif(value=="Ht"): return "High Tech" 
        elif(value=="Ie"): return "Ice-capped" 
        elif(value=="In"): return "Industrial"
        elif(value=="Lo"): return "Low Population"
        elif(value=="Lt"): return "Low Tech"
        elif(value=="Na"): return "Non-Agricultural"
        elif(value=="NI"): return "Non-Industrial"
        elif(value=="Po"): return "Poor"
        elif(value=="Ri"): return "Rich"
        elif(value=="Va"): return "Vacuum"
        elif(value=="Wa"): return "Water World"
        else: return ""
    @staticmethod
    def getTechLevelDescription(value):
        if(value==0): return "TL 0 (Primitive): No technology. TL 0 species have only discovered the simplest tools and principles, and are on a par with Earth’s Stone Age." 
        elif(value in [1]): return "TL 1 (Primitive): Roughly on a par with Bronze or Iron age technology. TL 1 science is mostly superstition, but they can manufacture weapons and work metals." 
        elif(value in [2]): return "TL 2 (Primitive): Renaissance technology. TL 2 brings with it a greater understanding of chemistry, physics, biology and astronomy as well as the scientific method." 
        elif(value in [3]): return "TL 3 (Primitive): The advances of TL 2 are now applied, bringing the germ of industrial revolution and steam power. Primitive firearms now dominate the battlefield. This is roughly comparable to the early 19th century." 
        elif(value in [4]): return "TL 4 (Industrial): The transition to industrial revolution is complete, bringing plastics, radio and other such inventions. Roughly comparable to the late 19th/early 20th century." 
        elif(value in [5]): return "TL 5 (Industrial): TL 5 brings widespread electrification, tele-communications and internal combustion. At the high end of the TL, atomics and primitive computing appear. Roughly on a par with the mid–20th century. " 
        elif(value in [6]): return "TL 6 (Industrial): TL 6 brings the development of fission power and more advanced computing. Advances in materials technology and rocketry bring about the dawn of the space age." 
        elif(value in [7]): return "TL 7 (Pre-Stellar): A pre-stellar society can reach orbit reliably and has telecommunications satellites. Computers become common. At the time of writing, humanity is currently somewhere between TL 7 and TL 8." 
        elif(value in [8]): return "TL 8 (Pre-Stellar): At TL 8, it is possible to reach other worlds in the same system, although terraforming or full colonisation are not within the culture’s capacity. Permanent space habitats become possible. Fusion power becomes commercially viable." 
        elif(value in [9]): return "TL 9 (Pre-Stellar): The defining element of TL 9 is the development of gravity manipulation, which makes space travel vastly safer and faster. This research leads to development of the jump drive, which occurs near the end of this Tech Level. TL 9 cultures can colonise other worlds, although travelling to a colony is often a one-way trip." 
        elif(value in [10]): return "TL 10 (Early Stellar): With the advent of commonly available jump drives, nearby systems are opened up. Orbital habitats and factories become common. Interstellar travel and trade lead to an economic boom. Colonies become much more viable."
        elif(value in [11]): return "TL 11 (Early Stellar): The first true artificial intelligences become possible, as computers are able to model synaptic networks. Grav-supported structures reach to the heavens. Jump 2 travel becomes possible, allowing easier travel beyond the one jump stellar mains."
        elif(value in [12]): return "TL 12 (Average Stellar): Weather control revolutionises terraforming and agriculture. Man-portable plasma weapons and carrier-mounted fusion guns make the battlefield untenable for unarmoured combatants. Jump 3 travel is developed."
        elif(value in [13]): return "TL 13 (Average Stellar): The battle dress appears on the battlefield in response to the new weapons. Cloning of body parts becomes easy. Advances in hull design and thruster plates means that spacecraft can easily go underwater. Jump 4 travel."
        elif(value in [14]): return "TL 14 (Average Stellar): Fusion weapons become manportable. Flying cities appear. Jump 5 travel."
        elif(value in [15]): return "TL 15 (High Stellar): Black globe generators suggest a new direction for defensive technologies, while the development of synthetic anagathics means that the human lifespan is now vastly increased. Jump 6 travel."
        else: return "TL 16+ (Beyond Known Tech): Higher Technology Levels exist (indeed, there is no theoretical upper limit) and may appear in other settings or be discovered by pioneering scientists within the Third Imperium."
    @staticmethod
    def getTagEntityType(tag):
        tagEntry = DescriptionGenerator.tagData.get(tag, None)
        if tagEntry is not None:
            return tagEntry.get("Entity Type", None)
        return None
    @staticmethod
    def getTagDescription(tag):
        tagEntry = DescriptionGenerator.tagData.get(tag, None)
        if tagEntry is not None:
            return tagEntry.get("Description", None)
        return None
    @staticmethod
    def getTagEnemies(tag):
        tagEntry = DescriptionGenerator.tagData.get(tag, None)
        if tagEntry is not None:
            return tagEntry.get("Enemies", None)
        return None
    @staticmethod
    def getTagFriends(tag):
        tagEntry = DescriptionGenerator.tagData.get(tag, None)
        if tagEntry is not None:
            return tagEntry.get("Friends", None)
        return None
    @staticmethod
    def getTagComplications(tag):
        tagEntry = DescriptionGenerator.tagData.get(tag, None)
        if tagEntry is not None:
            return tagEntry.get("Complications", None)
        return None
    @staticmethod
    def getTagFriends(tag):
        tagEntry = DescriptionGenerator.tagData.get(tag, None)
        if tagEntry is not None:
            return tagEntry.get("Things", None)
        return None
    @staticmethod
    def getTagFriends(tag):
        tagEntry = DescriptionGenerator.tagData.get(tag, None)
        if tagEntry is not None:
            return tagEntry.get("Places", None)
        return None
# =====================================================================
class Settlement():
    def __init__(self, 
        name, 
        settlement_type, 
        population_size, 
        description, 
        population_demographics="Isolated",
        modes_of_transportation=[],
        parent_planet=None, 
        ):
        self.name = name
        self.settlement_type=settlement_type
        self.population_size = population_size
        self.parent_planet = parent_planet
        self.description = description
        self.population_demographics = population_demographics
    def get_settlement_classification(self):
        if self.population_size <= 80: return "Thorp"
        elif self.population_size <= 400: return "Hamlet"
        elif self.population_size <= 900: return "Village"
        elif self.population_size <= 2000: return "Small town"
        elif self.population_size <= 5000: return "Large town"
        elif self.population_size <= 12000: return "Small city"
        elif self.population_size <= 25000: return "Large city"
        else: return "Metropolis"
    def __str__(self):
        pass
        return "{}. pop {} [{}]".format(self.name, self.population_size, self.get_settlement_classification())
class AreaOfIntersest():
    def __init__(self, name, area_type, parent_planet, description, is_dungeon):
        self.name = name
        self.area_type = area_type
        self.parent_planet = parent_planet
        self.description = description
        self.is_dungeon = is_dungeon
    def __str__(self):
        pass
        return "{} {} [{}]".format(self.name, self.area_type, "Dungeon" if self.is_dungeon else "Location")

# =====================================================================
class Sector():
    def __init__(self, name="<Sector>", seed = 1234567890):
        self.seed = seed
        self.name=name
        self.subsectors = {
        "a":None, "b":None, "c":None, "d":None, 
        "e":None, "f":None, "g":None, "h":None, 
        "i":None, "j":None, "k":None, "l":None, 
        "m":None, "n":None, "o":None, "p":None, 
        }
        self.systems = {}
        self.description = []
        self.notes = []
        self.history = []
        self.borders = []
        self.tradeRoutes = []
        self.tags = []
    def addSubsector(self, letter, subsector):
        self.subsectors[letter] = subsector
        subsector.parent_sector=self
    def addSystem(self, system): 
        pass
        self.systems[system.hexCoord] = system
    def getSystemByName(self, name):  return self.systems.get(name)
    def generateBorders(self):
        pass
        pass
    def __str__(self): return "Sector {}".format(self.name)
    def save(self):
        SubsectorGenerator.writeSectorTextFile(self)
        SubsectorGenerator.writeSectorXmlFile(self)
        SubsectorGenerator.writeSectorToFile(self)
    @staticmethod
    def load(sector_name):
        filename = "{}-Sector.pickle".format(sector_name)
        if os.path.exists(filename):
            file = open(filename, 'rb')
            sector = pickle.load(file)
            file.close()
        return sector
class Subsector():
    def __init__(self, name, sector, sectorSection):
        self.name=name
        self.parent_sector=sector
        self.subsector_letter = sectorSection
        self.hexGrid = {} # 
        self.systems = {} # 
        self.description = []
        self.notes = []
        self.history = []
        self.tags = []
    def addSystem(self, hexCoord, system): 
        self.hexGrid[hexCoord] = system
        self.systems[system.name] = system
        system.subsectorParent = self
    def getSystemByHex(self, hexCoord): return self.hexGrid.get(hexCoord)
    def __str__(self): return "Subsector {} of the {} Sector".format(self.name, self.parent_sector.name)
class StarSystem():
    def __init__(self, systemDict):
        self.systemDict=systemDict
        self.subsectorParent = None
        self.name = systemDict.get("name")
        self.hexCoord = systemDict.get("system hex")
        self.star = systemDict.get("system star")
        self.systemLineup = systemDict.get("system lineup")
        self.habitableZone = systemDict.get("system habitable zone")
        self.primaryPlanet = self.systemLineup[self.habitableZone]

        self.alignment = systemDict.get("system alignment", "Im")
        self.nobleLeader = systemDict.get("system noble leader", "")

        self.uwp = self.primaryPlanet.uwp
        self.upp = self.primaryPlanet.upp
        self.travelCode = systemDict.get("system travel code", "-")
        self.travelCodeReason = systemDict.get("system travel code reason", [])
        self.tradeCodes = systemDict.get("system trade codes")
        self.gasGiants = systemDict.get("system gas giants")
        self.planetoidBelts = systemDict.get("system asteroid belts")
        self.populationModifier = systemDict.get("system population modifier")
        self.populatedWorlds = systemDict.get("system populated worlds")
        self.bases = systemDict.get("system bases")
        self.piracy_warning = systemDict.get("system piracy warning", False)

        self.description = []
        self.notes = []
        self.history = []
        self.megacorpsPresence=[]
        self.tags = []
    def displayUppCode(self):
        hex_key=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        return"{}{}{}{}{}{}{}-{}".format(
            Utils.hex_key[self.primaryPlanet.size],
            Utils.hex_key[self.primaryPlanet.atmosphere],
            Utils.hex_key[min(15, max(0, self.primaryPlanet.hydrographics))],
            Utils.hex_key[self.primaryPlanet.population],
            Utils.hex_key[self.primaryPlanet.government],
            Utils.hex_key[self.primaryPlanet.lawLevel],
            Utils.hex_key[min(15, max(0, self.primaryPlanet.techLevel))],
            SubsectorGenerator.getStarportClass(self.primaryPlanet.starport),
            )
    def displayUwpCode(self):
        hex_key=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        return"{}{}{}{}{}{}{}-{}".format(
            SubsectorGenerator.getStarportClass(self.primaryPlanet.starport),
            Utils.hex_key[self.primaryPlanet.size],
            Utils.hex_key[self.primaryPlanet.atmosphere],
            Utils.hex_key[min(15, max(0, self.primaryPlanet.hydrographics))],
            Utils.hex_key[self.primaryPlanet.population],
            Utils.hex_key[self.primaryPlanet.government],
            Utils.hex_key[self.primaryPlanet.lawLevel],
            Utils.hex_key[min(15, max(0, self.primaryPlanet.techLevel))]
            )
    def getStarportClass(self, starportLevel):
        if(starportLevel in [3, 4]): return "E"
        elif(starportLevel in [5, 6]): return "D"
        elif(starportLevel in [7, 8]): return "C"
        elif(starportLevel in [9, 10]): return "B"
        elif(starportLevel >= 11): return "A"
        else: return "X"
    def addPlanetaryBody(self, body, location):
        if (self.systemLineup[location] is None):
            self.systemLineup[location] = body
            body.systemParent = self
            return True
        return False
    def setPlanetaryBody(self, body, location):
        self.systemLineup[location] = body
        body.systemParent = self
    def getPlanetaryBody(self, index):
        if index < len(self.systemLineup[index]) and index >= 0:
            body = self.systemLineup[index]
            return body
        return None
    def __str__(self): "{} ({}) {}".format(self.name, self.hexCoord, self.primaryPlanet.displayUwpCode())
class PlantaryBody(object):
    def __init__(self, systemDict, name):
        self.name = name
        self.parent = None
        self.systemParent = None
        self.size = systemDict.get("{} size".format(self.name))
        self.atmosphere = systemDict.get("{} atmosphere".format(self.name))
        self.hydrographics = systemDict.get("{} hydrographics".format(self.name))
        self.population = systemDict.get("{} population".format(self.name))
        self.government = systemDict.get("{} government".format(self.name))
        self.lawLevel = systemDict.get("{} law level".format(self.name))
        self.starport = systemDict.get("{} starport".format(self.name))
        self.birthing_cost_per_week = systemDict.get("{} berthing cost".format(self.name), 500) 
        self.refined_fueling_cost = systemDict.get("{} refined fuel".format(self.name), 500) 
        self.unrefined_fueling_cost = systemDict.get("{} unrefined fuel".format(self.name), 100) 
        self.techLevel = systemDict.get("{} tech level".format(self.name))
        self.temperature = systemDict.get("{} temperature".format(self.name))
        self.uwp = self.displayUwpCode() if self.size else None
        self.upp = self.displayUppCode() if self.size else None
        self.moons = systemDict.get("{} moons".format(self.name), [])
        self.description = []
        self.notes = []
        self.history = []
        self.settlements = []
        self.areas_of_interest = []
        self.tags = []
    def __str__(self): return self.displayUwpCode()
    def add_orbiting_body(self, moon):
        moon.parent = self
        self.moons.append(moon)
    def displayUppCode(self):
        hex_key=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        return"{}{}{}{}{}{}{}-{}".format(
            Utils.hex_key[self.size],
            Utils.hex_key[self.atmosphere],
            Utils.hex_key[min(15, max(0, self.hydrographics))],
            Utils.hex_key[self.population],
            Utils.hex_key[self.government],
            Utils.hex_key[self.lawLevel],
            Utils.hex_key[min(15, max(0, self.techLevel))],
            SubsectorGenerator.getStarportClass(self.starport),
            )
    def displayUwpCode(self):
        hex_key=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        return"{}{}{}{}{}{}{}-{}".format(
            SubsectorGenerator.getStarportClass(self.starport),
            Utils.hex_key[self.size],
            Utils.hex_key[self.atmosphere],
            Utils.hex_key[min(15, max(0, self.hydrographics))],
            Utils.hex_key[self.population],
            Utils.hex_key[self.government],
            Utils.hex_key[self.lawLevel],
            Utils.hex_key[min(15, max(0, self.techLevel))]
            )
    def getStarportClass(self, starportLevel):
        if(starportLevel in [3, 4]): return "E"
        elif(starportLevel in [5, 6]): return "D"
        elif(starportLevel in [7, 8]): return "C"
        elif(starportLevel in [9, 10]): return "B"
        elif(starportLevel >= 11): return "A"
        else: return "X"
    def getPlanetType(self):
        if(self.size in [0, 1, 2] and self.atmosphere in [0, 1] and self.temperature > 9): 
            return "Rocky"
        elif(self.atmosphere in [10, 11, 12]): 
            return "Hellhole"
        elif(self.size in [0, 1, 2] and self.atmosphere in [0, 1] and self.temperature < 5): 
            return "Iceball"
        elif(self.size in [0, 1, 2] and self.atmosphere in [0, 1]): 
            return "Rocky"
        elif(self.atmosphere > 2 and self.hydrographics < 3): 
            return "Desert"
        elif(self.hydrographics == 10): 
            return "Waterworld"
        elif(self.atmosphere in [0]): 
            return "Rocky"
        else:
            return "Garden"
    def add_area_of_interest(self, area):
        self.areas_of_interest.append(area)
        area.parent_planet = self
    def add_settlement(self, settlement):
        self.settlements.append(settlement)
        settlement.parent_planet = self
    def get_upp_or_planet_type(self): return self.getPlanetType()
class Planet(PlantaryBody):
    def __init__(self, systemDict, name):
        PlantaryBody.__init__(self,systemDict, name)
    def __str__(self): return "{} ({})".format(self.name, self.displayUwpCode())
    def get_upp_or_planet_type(self): return self.displayUwpCode()
class GasGiant(PlantaryBody):
    def __init__(self, systemDict, name):
        PlantaryBody.__init__(self,systemDict, name)
        self.rings = systemDict.get("{} gas giant rings".format(name), False)
    def __str__(self): return "Gas Giant"
    def getPlanetType(self): 
        return "Jovian"
    def get_upp_or_planet_type(self): 
        if self.rings: return "Ringed"
        else: return "Gas Giant"
class AsteroidBelt(PlantaryBody):
    def __init__(self, systemDict, name):
        PlantaryBody.__init__(self,systemDict, name)
        self.primary=None
    def __str__(self): return "Asteroid"
    def getPlanetType(self): return "Belt"
    def add_primary(self, primary):
        self.add_orbiting_body(primary)
        self.primary=primary
    def get_upp_or_planet_type(self): return "Asteroid"
class PrimaryPlanet(Planet):
    def __init__(self, systemDict):
        Planet.__init__(self, systemDict, "primary")
        self.factions = systemDict.get("primary factions")
        self.culturals = systemDict.get("primary cultural diff")
        self.tradeCodes = systemDict.get("primary trade codes")
        self.moons = systemDict.get("primary moons")
        self.portsTypes = systemDict.get("primary starport types")
        self.portsTypesRoll = systemDict.get("primary starport types roll")
        self.portsTypesHighest = systemDict.get("primary starport types highest")   
    def __str__(self): return self.displayUwpCode()
    def make_non_primary(self):
        asNonPrimary = Planet({},self.name)
        asNonPrimary.name = self.name
        asNonPrimary.systemParent = self.systemParent
        asNonPrimary.size = self.size
        asNonPrimary.atmosphere = self.atmosphere
        asNonPrimary.hydrographics =self.hydrographics
        asNonPrimary.population = self.population
        asNonPrimary.government = self.government
        asNonPrimary.lawLevel = self.lawLevel
        asNonPrimary.starport = self.starport
        asNonPrimary.techLevel = self.techLevel
        asNonPrimary.temperature = self.temperature
        asNonPrimary.uwp = asNonPrimary.displayUwpCode()
        asNonPrimary.upp = asNonPrimary.displayUppCode()
        asNonPrimary.moons = self.moons 
        asNonPrimary.description = self.description
        asNonPrimary.notes = self.notes
        asNonPrimary.history = self.history
        return asNonPrimary
class Moon(PlantaryBody):
    def __init__(self, moonDict, name):
        PlantaryBody.__init__(self, moonDict, name)
    def __str__(self): return self.displayUwpCode()
class Star():
    ''' Star # Sol: G-type 2 V 
        Type    color Surface Temperature Average Mass Average Radius Average Luminosity
        O       Blue 2          5,000K or more 60   15      1,400,000
        B       Blue            11,000 – 25,000K    18      7 20,000
        A       Blue            7,500 – 11,000K     3.2     2.5 80
        F       Blue to White   6,000 – 7,500K      1.7     1.3 6
        G       White to Yellow 5,000 – 6,000K      1.1     1.1 1.2
        K       Orange to Red   3,500 – 5,000K      0.8     0.9 0.4
        M       Red Under 3,500K 0.3 0.4 0.04

        Type Description
        Ia Very Luminous Supergiants
        Ib Less Luminous Supergiants
        II Luminous Giants
        III Giants
        IV Subgiants
        V Main Sequence (Dwarf) Stars
        VI Subdwarfs
        VII White Dwarfs
        
        Stellar type distribution
        Ia0     16     0.03%    0003
        Ia     241     0.43%    0043
        Iab    191     0.34%    0034
        Ib     694     1.23%    0123
        I       17     0.03%    0003
        II    1627     2.89%    0289
        III  22026    39.13%    3913
        IV    6418    11.40%    1140
        V    24873    44.19%    4419
        VI      92     0.16%    0016
        VII     89     0.16%    0016
        '''
    star_type = {
        "O"     :  ["Blue 2",           "5,000K or more",       "60", "15",  "1,400,000"],
        "B"     :  ["Blue",             "11,000 – 25,000K",     "18", "7",   "20,000"],
        "A"     :  ["Blue",             "7,500 – 11,000K",      "3.2","2.5", "80"],
        "F"     :  ["Blue to White",    "6,000 – 7,500K",       "1.7","1.3", "6"],
        "G"     :  ["White to Yellow",  "5,000 – 6,000K",       "1.1","1.1", "1.2"],
        "K"     :  ["Orange to Red",    "3,500 – 5,000K",       "0.8","0.9", "0.4"],
        "M"     :  ["Red",              "Under 3,500K",         "0.3","0.4", "0.04"],
        }
    luminocity_type={
        "Ia" :"Very Luminous Supergiants",
        "Ib" :"Less Luminous Supergiants",
        "II" :"Luminous Giants",
        "III": "Giants",
        "IV" :"Subgiants",
        "V" :"Main Sequence (Dwarf) Stars",
        "VI" :"Subdwarfs",
        "VII" :"White Dwarfs",
        }
    @staticmethod
    def generate(name):
        s_classes=["O","B","B","A","A","F","F","F","G","G","G","K","K","M","M","M"]
        s_class = s_classes[random.randint(0,len(s_classes)-1)]
        roll = random.randint(1,10000)
        luminosity=""
        if(roll<=3): luminosity="Ia0"
        elif(roll<=46): luminosity="Ia"
        elif(roll<=80): luminosity="Iab"
        elif(roll<=203): luminosity="Ib"
        elif(roll<=206): luminosity="I"
        elif(roll<=495): luminosity="II"
        elif(roll<=4408): luminosity="III"
        elif(roll<=5548): luminosity="IV"
        elif(roll<=9967): luminosity="V"
        elif(roll<=9983): luminosity="VI"
        else: luminosity="VII"
        star = Star(name, s_class, random.randint(0,9), luminosity, binary_companion=None)
        return star
    @staticmethod
    def fromString(starStr):
        parts = starStr.split(" ")
        star = Star(name, starStr[0], int(starStr[1]), parts[1], binary_companion=None)
        return star
    def __init__(self, name, stellar_class, heat_rating, luminosity, binary_companion=None):
        self.name=name
        self.stellar_class=stellar_class
        self.heat_rating=heat_rating
        self.luminosity=luminosity
        self.binary_companion=binary_companion
    def __str__(self):
        return "{} ({}{}{})".format(self.name[0].upper()+self.name[1:].lower(), self.stellar_class, self.heat_rating, self.luminosity)
    def getStellarCode(self):
        return "{}{} {}".format(self.stellar_class, self.heat_rating, self.luminosity)
    def add_binary_companion(other_star):
        self.binary_companion=other_star
        other_star.binary_companion=self
        self.name+="-A"
        other_star.name+="-B"
    def make_triple_star(other_starA,other_starB):
        self.binary_companion=other_star
        other_star.binary_companion=self
        self.name+="-A"
        other_star.name+="-B"
class SubsectorGenerator(object):
    """Subsector generator: Generates subsector with a given seed and saves it to pickle file"""
    @staticmethod
    def getNeighboringSystems(hexcoord, sector, already_claimed):
        neighbors = []
        num1 = int(hexcoord[0:2])
        num1a = max(0, min(num1-1, 32))
        num1b = max(0, min(num1+1, 32))
        nums1 = list(set([
            hexcoord[:2],
            "0{}".format(num1a) if num1a < 9 else str(num1a),
            "0{}".format(num1b) if num1b < 9 else str(num1b)
            ]))
        num2 = int(hexcoord[2:4])
        num2a = max(0, min(num2-1, 40))
        num2b = max(0, min(num2+1, 40))
        nums2 = list(set([
            hexcoord[2:],
            "0{}".format(num2a) if num2a < 9 else str(num2a),
            "0{}".format(num2b) if num2b < 9 else str(num2b)
            ]))
        for x in nums1:
            for y in nums2:
                potential_neighbor = x+y
                if potential_neighbor in sector.systems.keys() and potential_neighbor not in neighbors and potential_neighbor not in already_claimed:
                    neighbors.append(potential_neighbor)
        neighbors.sort()
        return list(set(neighbors))
    @staticmethod
    def getNumberGasGiants(gasGiantChanceTestDM): 
        GasGiantTest = random.randint(2,12)
        
        if (GasGiantTest > gasGiantChanceTestDM):
            numOfGasGiants = random.randint(1,3)
            return numOfGasGiants
        return 0
    @staticmethod
    def getNumberPlanetoidBelts(planetoidBeltChanceTestDM): 
        planetoidBeltTest = random.randint(2,12)
        planetoidBelts=0
        if (planetoidBeltTest > planetoidBeltChanceTestDM):
            planetoidBelts = max(0, random.randint(1,6)-3)
            return planetoidBelts
        return 0
    @staticmethod
    def setBaseTypeMine(planetStarport, systemDictionary):
        if(planetStarport in [3,4]): # Frontier Base
            if(planetStarportTypes >= 12):
                systemDictionary["primary starport types"].append("Pirate")
                systemDictionary["primary starport types highest"] = "P"
        elif(planetStarport in [5, 6]): # D, Poor Base
            if(planetStarportTypes >= 7):
                systemDictionary["primary starport types"].append("Scout")
                systemDictionary["primary starport types highest"] = "S"
            if(planetStarportTypes >= 12):
                systemDictionary["primary starport types"].append("Pirate")
                systemDictionary["primary starport types highest"] = "P"
        elif(planetStarport in [7, 8]): # C, Routine Base
            if(planetStarportTypes >= 8):
                systemDictionary["primary starport types"].append("Scout")
                systemDictionary["primary starport types highest"] = "S"
            if(planetStarportTypes >= 10):
                systemDictionary["primary starport types"].append("Research")
                systemDictionary["primary starport types"].append("TAS")
                systemDictionary["primary starport types"].append("Consulate")
                systemDictionary["primary starport types"].append("Pirate")
                systemDictionary["primary starport types highest"] = "T"
        elif(planetStarport in [9, 10]): # B, Good Base
            if(planetStarportTypes >= 6):
                systemDictionary["primary starport types"].append("TAS")
                systemDictionary["primary starport types highest"] = "T"
            if(planetStarportTypes >= 8):
                systemDictionary["primary starport types"].append("Scout")
                systemDictionary["primary starport types"].append("Naval")
                systemDictionary["primary starport types"].append("Consulate")
                systemDictionary["primary starport types highest"] = "N"
            if(planetStarportTypes >= 10):
                systemDictionary["primary starport types"].append("Research")
                systemDictionary["primary starport types"].append("Pirate")
                systemDictionary["primary starport types highest"] = "R"
        elif(planetStarport >= 11): # A, Excellent Base
            if(planetStarportTypes >= 4):
                systemDictionary["primary starport types"].append("TAS")
                systemDictionary["primary starport types highest"] = "T"
            if(planetStarportTypes >= 6):
                systemDictionary["primary starport types"].append("Consulate")
                systemDictionary["primary starport types highest"] = "C"
            if(planetStarportTypes >= 8):
                systemDictionary["primary starport types"].append("Naval")
                systemDictionary["primary starport types"].append("Research")
                systemDictionary["primary starport types highest"] = "N"
            if(planetStarportTypes >= 12):
                systemDictionary["primary starport types"].append("Pirate")
                systemDictionary["primary starport types highest"] = "R"
        else:
            systemDictionary["primary starport types highest"] = "-"
            systemDictionary["primary starport types"].append("None")
    @staticmethod
    def setBaseType(systemDictionary):
        #roll = random.randint(2,12)
        systemDictionary["primary starport types highest"] = random.choice(["N","S","T","R"])
    @staticmethod
    def generateRandomPlanet( name, hexLoc, systemDictionary, planetHabitableZoneLocation=0, verbose=False): 
        # PRIMARY PLANET STATS
        # SIZE
        planetSize = random.randint(2,12)-2
        systemDictionary["{} size".format(name)] = planetSize

        # ATMOSPHERE
        planetAtmosphere = random.randint(2,12) + planetSize - 7
        systemDictionary["{} atmosphere".format(name)] = planetAtmosphere

        # HYDROGRAPHICS
        HydrographicsDM = 0
        if(planetAtmosphere in [0, 1, 10, 11, 13]):
            HydrographicsDM = -4
        if(planetAtmosphere in [0, 1, 10, 11, 13]):
            HydrographicsDM = -4
        planetHydrographics = random.randint(2,12)-7 + planetAtmosphere + HydrographicsDM
        
        if (planetSize in [0,1]):
            planetHydrographics = 0
        systemDictionary["{} hydrographics".format(name)] = max(0, min(10, planetHydrographics))

        # POPULATION
        planetPopulation = random.randint(2,12)-2
        systemDictionary["{} population".format(name)] = planetPopulation


        # TEMPERATURE
        temperatureDM = 0
        if(planetAtmosphere in [2, 3]):
            temperatureDM = -2
        elif(planetAtmosphere in [4, 5]):
            temperatureDM = -1
        elif(planetAtmosphere in [6, 7]):
            temperatureDM = 0
        elif(planetAtmosphere in [8, 9]):
            temperatureDM = 1
        elif(planetAtmosphere in [10, 13, 15]):
            temperatureDM = 2
        elif(planetAtmosphere in [11, 12]):
            temperatureDM = 6
        if(planetHabitableZoneLocation > 0):
            temperatureDM += 4
        elif(planetHabitableZoneLocation < 0):
            temperatureDM -= 4
        planetTemperature = random.randint(2,12) + temperatureDM

        systemDictionary["{} temperature".format(name)] = planetTemperature

        # GOVERNMENT
        planetGovernment = max(0, min(random.randint(2,12)-7 + planetPopulation, 15))
        if(planetPopulation == 0):
            planetGovernment = 0
        systemDictionary["{} government".format(name)] = planetGovernment
        PoliticalFactionsDM = 0
        if (planetGovernment in [0, 7]):
            PoliticalFactionsDM += 1
        elif (planetGovernment > 10):
            PoliticalFactionsDM -= 1
        planetPoliticalFactions = random.randint(1,3) + PoliticalFactionsDM
        systemDictionary["{} factions".format(name)] = planetPoliticalFactions

        # CULTURE
        culturalDifferences = random.randint(1,6)*10 + random.randint(1,6)
        systemDictionary["{} cultural diff".format(name)] = culturalDifferences

        # LAW
        planetLawLevel = random.randint(2,12)-7 + planetGovernment
        if(planetPopulation == 0):
            planetLawLevel = 0
        systemDictionary["{} law level".format(name)] = min(planetLawLevel, 15)

        # STARPORT
        starportDM = 0
        if(planetPopulation >= 10):
            starportDM+=2
        elif(planetPopulation >= 8):
            starportDM+=1
        elif(planetPopulation <= 4):
            starportDM-=2
        elif(planetPopulation <= 2):
            starportDM-=1
        planetStarport = random.randint(2,12) + starportDM
        if(planetPopulation == 0):
            planetStarport = 0
        systemDictionary["{} starport".format(name)] = planetStarport
        # if there is a planet, not just a large rock, then there is a down port and a star town
        # systemDictionary["primary downport"] = planetStarport
        # systemDictionary["primary startown"] = planetStarport
        berthingCost = 500
        if planetStarport < 5: berthingCost = 0
        elif planetStarport < 7: berthingCost = random.randint(1, 6)*10
        elif planetStarport < 9: berthingCost = random.randint(1, 6)*100
        elif planetStarport < 11: berthingCost = random.randint(1, 6)*500
        elif planetStarport > 10: berthingCost = random.randint(1, 6)*1000
        refiendFuelCost = 200+random.randint(1, 6)*50
        unrefiendFuelCost = 40+random.randint(1, 6)*10
        systemDictionary["{} berthing cost".format(name)] = berthingCost
        systemDictionary["{} refined fuel".format(name)] = refiendFuelCost
        systemDictionary["{} unrefined fuel".format(name)] = unrefiendFuelCost

        # TECH LEVEL
        minTechLevel = 3
        if(planetAtmosphere in [2, 3, 13, 14]): minTechLevel = 5
        elif(planetAtmosphere in [0, 1, 10, 15]): minTechLevel = 8
        elif(planetAtmosphere in [11]): minTechLevel = 9
        elif(planetAtmosphere in [12]): minTechLevel = 1
        techLevelDM = 0
        if (planetStarport in [10]):   techLevelDM +=6
        elif (planetStarport in [11]): techLevelDM +=4
        elif (planetStarport in [12]): techLevelDM +=2
        if (planetSize in [0, 1]): techLevelDM +=2
        elif (planetSize in [2, 3, 4]): techLevelDM +=1
        if (planetAtmosphere in [1, 2, 3, 4, 10, 11, 12, 13, 14, 15]): techLevelDM +=1
        if (planetHydrographics in [0, 1]): techLevelDM +=1
        elif (planetHydrographics in [10]): techLevelDM +=2
        if (planetPopulation in [1, 2, 3, 4, 5, 8]):   techLevelDM +=1
        elif (planetPopulation in [9]): techLevelDM +=2
        elif (planetPopulation in [10]): techLevelDM +=4
        if (planetGovernment in [0, 5]):   techLevelDM +=1
        elif (planetGovernment in [7]): techLevelDM +=2
        elif (planetGovernment in [13, 14]): techLevelDM -=2
        planetTechLevel = minTechLevel + random.randint(1,6) + techLevelDM
        if(planetPopulation == 0):
            planetTechLevel = 0
        systemDictionary["{} tech level".format(name)] = planetTechLevel
        systemDictionary["primary berthing cost"] = berthingCost
        systemDictionary["primary refined fuel"] = refiendFuelCost
        systemDictionary["primary unrefined fuel"] = unrefiendFuelCost

        planetStarportTypes = random.randint(2,12) + starportDM
        starport_bases = []
        if planetStarport >= 11:
            roll = random.randint(2,12) + starportDM
            if roll >= 8: starport_bases.append("Naval")
            roll = random.randint(2,12) + starportDM
            if roll >= 10: starport_bases.append("Scout")
            roll = random.randint(2,12) + starportDM
            if roll >= 8: starport_bases.append("Research")
            starport_bases.append("TAS")
        elif planetStarport >= 9:
            roll = random.randint(2,12) + starportDM
            if roll >= 8: starport_bases.append("Naval")
            roll = random.randint(2,12) + starportDM
            if roll >= 8: starport_bases.append("Scout")
            roll = random.randint(2,12) + starportDM
            if roll >= 10: starport_bases.append("Research")
            starport_bases.append("TAS")
        elif planetStarport >= 7:
            roll = random.randint(2,12) + starportDM
            if roll >= 8: starport_bases.append("Scout")
            roll = random.randint(2,12) + starportDM
            if roll >= 10: starport_bases.append("Research")
            roll = random.randint(2,12) + starportDM
            if roll >= 10: starport_bases.append("TAS")
        elif planetStarport >= 5:
            roll = random.randint(2,12) + starportDM
            if roll >= 7: starport_bases.append("TAS")
        piracy_warning_roll = random.randint(2,12)
        if (
            (piracy_warning_roll >= 12 and planetStarport >= 7) or 
            (piracy_warning_roll >= 11 and planetStarport <= 6)
            ):
            systemDictionary["system piracy warning"] = True
            starport_bases.append("Pirate")

        systemDictionary["primary starport types"] = starport_bases
        systemDictionary["system bases"] = starport_bases
        systemDictionary["primary starport types roll"] = planetStarportTypes
        # systemDictionary["primary starport types highest"] = ""
        # SubsectorGenerator.setBaseTypeMine(systemDictionary)
        if "Naval" in starport_bases:
            systemDictionary["primary starport types highest"] = "N"
        elif "Scout" in starport_bases:
            systemDictionary["primary starport types highest"] = "S"
        elif "Research" in starport_bases:
            systemDictionary["primary starport types highest"] = "R"
        elif "Research" in starport_bases:
            systemDictionary["primary starport types highest"] = "T"
        else:
            systemDictionary["primary starport types highest"] = "-"
        return systemDictionary
    @staticmethod
    def generateRandomPrimary( name, hexLoc, systemDictionary, planetHabitableZoneLocation=0, verbose=False): 
        # PRIMARY PLANET STATS
        # SIZE
        planetSize = random.randint(2,12)-2
        systemDictionary["primary size"] = planetSize

        # ATMOSPHERE
        planetAtmosphere = random.randint(2,12) + planetSize - 7
        systemDictionary["primary atmosphere"] = planetAtmosphere

        # HYDROGRAPHICS
        HydrographicsDM = 0
        if(planetAtmosphere in [0, 1, 10, 11, 13]):
            HydrographicsDM = -4
        if(planetAtmosphere in [0, 1, 10, 11, 13]):
            HydrographicsDM = -4
        planetHydrographics = random.randint(2,12)-7 + planetAtmosphere + HydrographicsDM
        
        if (planetSize in [0,1]):
            planetHydrographics = 0
        systemDictionary["primary hydrographics"] = max(0, min(10, planetHydrographics))

        # POPULATION
        planetPopulation = random.randint(2,12)-2
        systemDictionary["primary population"] = planetPopulation
        systemDictionary["system population modifier"] = min(9, systemDictionary["primary population"]) # STUB TODO FIX THIS
        if (systemDictionary["primary population"] == 0): 
            systemDictionary["system population modifier"]=0

        # TEMPERATURE
        temperatureDM = 0
        if(planetAtmosphere in [2, 3]):
            temperatureDM = -2
        elif(planetAtmosphere in [4, 5]):
            temperatureDM = -1
        elif(planetAtmosphere in [6, 7]):
            temperatureDM = 0
        elif(planetAtmosphere in [8, 9]):
            temperatureDM = 1
        elif(planetAtmosphere in [10, 13, 15]):
            temperatureDM = 2
        elif(planetAtmosphere in [11, 12]):
            temperatureDM = 6
        if(planetHabitableZoneLocation > 0):
            temperatureDM += 4
        elif(planetHabitableZoneLocation < 0):
            temperatureDM -= 4
        planetTemperature = random.randint(2,12) + temperatureDM

        systemDictionary["primary temperature"] = planetTemperature

        # GOVERNMENT
        planetGovernment = max(0, min(random.randint(2,12)-7 + planetPopulation, 15))
        if(planetPopulation == 0):
            planetGovernment = 0
        systemDictionary["primary government"] = planetGovernment
        PoliticalFactionsDM = 0
        if (planetGovernment in [0, 7]):
            PoliticalFactionsDM += 1
        elif (planetGovernment > 10):
            PoliticalFactionsDM -= 1
        planetPoliticalFactions = random.randint(1,3) + PoliticalFactionsDM
        systemDictionary["primary factions"] = planetPoliticalFactions

        # CULTURE
        culturalDifferences = random.randint(1,6)*10 + random.randint(1,6)
        systemDictionary["primary cultural diff"] = culturalDifferences

        # LAW
        planetLawLevel = random.randint(2,12)-7 + planetGovernment
        if(planetPopulation == 0):
            planetLawLevel = 0
        systemDictionary["primary law level"] = min(planetLawLevel, 15)

        # STARPORT
        starportDM = 0
        if(planetPopulation >= 10):
            starportDM+=2
        elif(planetPopulation >= 8):
            starportDM+=1
        elif(planetPopulation <= 4):
            starportDM-=2
        elif(planetPopulation <= 2):
            starportDM-=1
        planetStarport = random.randint(2,12) + starportDM
        if(planetPopulation == 0):
            planetStarport = 0
        systemDictionary["primary starport"] = planetStarport
        # if there is a planet, not just a large rock, then there is a down port and a star town
        # systemDictionary["primary downport"] = planetStarport
        # systemDictionary["primary startown"] = planetStarport
        berthingCost = 500
        if planetStarport < 5: berthingCost = 0
        elif planetStarport < 7: berthingCost = random.randint(1, 6)*10
        elif planetStarport < 9: berthingCost = random.randint(1, 6)*100
        elif planetStarport < 11: berthingCost = random.randint(1, 6)*500
        elif planetStarport > 10: berthingCost = random.randint(1, 6)*1000
        refiendFuelCost = 200+random.randint(1, 6)*50
        unrefiendFuelCost = 40+random.randint(1, 6)*10
        systemDictionary["primary berthing cost"] = berthingCost
        systemDictionary["primary refined fuel"] = refiendFuelCost
        systemDictionary["primary unrefined fuel"] = unrefiendFuelCost

        planetStarportTypes = random.randint(2,12) + starportDM
        starport_bases = []
        if planetStarport >= 11:
            roll = random.randint(2,12) + starportDM
            if roll >= 8: starport_bases.append("Naval")
            roll = random.randint(2,12) + starportDM
            if roll >= 10: starport_bases.append("Scout")
            roll = random.randint(2,12) + starportDM
            if roll >= 8: starport_bases.append("Research")
            starport_bases.append("TAS")
        elif planetStarport >= 9:
            roll = random.randint(2,12) + starportDM
            if roll >= 8: starport_bases.append("Naval")
            roll = random.randint(2,12) + starportDM
            if roll >= 8: starport_bases.append("Scout")
            roll = random.randint(2,12) + starportDM
            if roll >= 10: starport_bases.append("Research")
            starport_bases.append("TAS")
        elif planetStarport >= 7:
            roll = random.randint(2,12) + starportDM
            if roll >= 8: starport_bases.append("Scout")
            roll = random.randint(2,12) + starportDM
            if roll >= 10: starport_bases.append("Research")
            roll = random.randint(2,12) + starportDM
            if roll >= 10: starport_bases.append("TAS")
        elif planetStarport >= 5:
            roll = random.randint(2,12) + starportDM
            if roll >= 7: starport_bases.append("TAS")
        piracy_warning_roll = random.randint(2,12)
        systemDictionary["system piracy warning"] = False
        if (
            (piracy_warning_roll >= 12 and planetStarport >= 7) or 
            (piracy_warning_roll >= 11 and planetStarport <= 6)
            ):
            systemDictionary["system piracy warning"] = True
            starport_bases.append("Pirate")

        systemDictionary["primary starport types"] = starport_bases
        systemDictionary["system bases"] = starport_bases
        systemDictionary["primary starport types roll"] = planetStarportTypes
        # systemDictionary["primary starport types highest"] = ""
        # SubsectorGenerator.setBaseTypeMine(systemDictionary)
        if "Naval" in starport_bases:
            systemDictionary["primary starport types highest"] = "N"
        elif "Scout" in starport_bases:
            systemDictionary["primary starport types highest"] = "S"
        elif "Research" in starport_bases:
            systemDictionary["primary starport types highest"] = "R"
        elif "Research" in starport_bases:
            systemDictionary["primary starport types highest"] = "T"
        else:
            systemDictionary["primary starport types highest"] = "-"
        

        # TECH LEVEL
        minTechLevel = 3
        if(planetAtmosphere in [2, 3, 13, 14]): minTechLevel = 5
        elif(planetAtmosphere in [0, 1, 10, 15]): minTechLevel = 8
        elif(planetAtmosphere in [11]): minTechLevel = 9
        elif(planetAtmosphere in [12]): minTechLevel = 1
        techLevelDM = 0
        if (planetStarport in [10]):   techLevelDM +=6
        elif (planetStarport in [11]): techLevelDM +=4
        elif (planetStarport in [12]): techLevelDM +=2
        if (planetSize in [0, 1]): techLevelDM +=2
        elif (planetSize in [2, 3, 4]): techLevelDM +=1
        if (planetAtmosphere in [1, 2, 3, 4, 10, 11, 12, 13, 14, 15]): techLevelDM +=1
        if (planetHydrographics in [0, 1]): techLevelDM +=1
        elif (planetHydrographics in [10]): techLevelDM +=2
        if (planetPopulation in [1, 2, 3, 4, 5, 8]):   techLevelDM +=1
        elif (planetPopulation in [9]): techLevelDM +=2
        elif (planetPopulation in [10]): techLevelDM +=4
        if (planetGovernment in [0, 5]):   techLevelDM +=1
        elif (planetGovernment in [7]): techLevelDM +=2
        elif (planetGovernment in [13, 14]): techLevelDM -=2
        planetTechLevel = minTechLevel + random.randint(1,6) + techLevelDM
        if(planetPopulation == 0):
            planetTechLevel = 0
        systemDictionary["primary tech level"] = planetTechLevel
    @staticmethod
    def generateEarthlikePrimary( name, hexLoc, systemDictionary, planetHabitableZoneLocation=0, verbose=False): 
        # Earthlike PRIMARY PLANET STATS
        # SIZE
        planetSize = random.choice([7, 7, 8, 8, 8, 8, 9])
        systemDictionary["primary size"] = planetSize

        # ATMOSPHERE
        planetAtmosphere = random.choice([5, 6, 6, 6, 7])
        systemDictionary["primary atmosphere"] = planetAtmosphere

        # HYDROGRAPHICS
        planetHydrographics = random.randint(2,12)-7 + planetAtmosphere
        
        if (planetSize in [0,1]):
            planetHydrographics = 0
        systemDictionary["primary hydrographics"] = max(0, min(10, planetHydrographics))

        # POPULATION
        planetPopulation = random.randint(2,12)-2
        systemDictionary["primary population"] = planetPopulation
        systemDictionary["system population modifier"] = min(9, systemDictionary["primary population"]) # STUB TODO FIX THIS
        if (systemDictionary["primary population"] == 0): 
            systemDictionary["system population modifier"]=0

        # TEMPERATURE
        temperatureDM = 0
        if(planetAtmosphere in [2, 3]):
            temperatureDM = -2
        elif(planetAtmosphere in [4, 5]):
            temperatureDM = -1
        elif(planetAtmosphere in [6, 7]):
            temperatureDM = 0
        elif(planetAtmosphere in [8, 9]):
            temperatureDM = 1
        elif(planetAtmosphere in [10, 13, 15]):
            temperatureDM = 2
        elif(planetAtmosphere in [11, 12]):
            temperatureDM = 6
        if(planetHabitableZoneLocation > 0):
            temperatureDM += 4
        elif(planetHabitableZoneLocation < 0):
            temperatureDM -= 4
        planetTemperature = random.randint(2,12) + temperatureDM

        systemDictionary["primary temperature"] = planetTemperature

        # GOVERNMENT
        planetGovernment = max(0, min(random.randint(2,12)-7 + planetPopulation, 15))
        if(planetPopulation == 0):
            planetGovernment = 0
        systemDictionary["primary government"] = planetGovernment
        PoliticalFactionsDM = 0
        if (planetGovernment in [0, 7]):
            PoliticalFactionsDM += 1
        elif (planetGovernment > 10):
            PoliticalFactionsDM -= 1
        planetPoliticalFactions = random.randint(1,3) + PoliticalFactionsDM
        systemDictionary["primary factions"] = planetPoliticalFactions

        # CULTURE
        culturalDifferences = random.randint(1,6)*10 + random.randint(1,6)
        systemDictionary["primary cultural diff"] = culturalDifferences

        # LAW
        planetLawLevel = random.randint(2,12)-7 + planetGovernment
        if(planetPopulation == 0):
            planetLawLevel = 0
        systemDictionary["primary law level"] = min(planetLawLevel, 15)

        # STARPORT
        starportDM = 0
        if(planetPopulation >= 10):
            starportDM+=2
        elif(planetPopulation >= 8):
            starportDM+=1
        elif(planetPopulation <= 4):
            starportDM-=2
        elif(planetPopulation <= 2):
            starportDM-=1
        planetStarport = random.randint(2,12) + starportDM
        if(planetPopulation == 0):
            planetStarport = 0
        systemDictionary["primary starport"] = planetStarport
        # if there is a planet, not just a large rock, then there is a down port and a star town
        # systemDictionary["primary downport"] = planetStarport
        # systemDictionary["primary startown"] = planetStarport
        berthingCost = 500
        if planetStarport < 5: berthingCost = 0
        elif planetStarport < 7: berthingCost = random.randint(1, 6)*10
        elif planetStarport < 9: berthingCost = random.randint(1, 6)*100
        elif planetStarport < 11: berthingCost = random.randint(1, 6)*500
        elif planetStarport > 10: berthingCost = random.randint(1, 6)*1000
        refiendFuelCost = 200+random.randint(1, 6)*50
        unrefiendFuelCost = 40+random.randint(1, 6)*10
        systemDictionary["primary berthing cost"] = berthingCost
        systemDictionary["primary refined fuel"] = refiendFuelCost
        systemDictionary["primary unrefined fuel"] = unrefiendFuelCost

        planetStarportTypes = random.randint(2,12) + starportDM
        starport_bases = []
        if planetStarport >= 11:
            roll = random.randint(2,12) + starportDM
            if roll >= 8: starport_bases.append("Naval")
            roll = random.randint(2,12) + starportDM
            if roll >= 10: starport_bases.append("Scout")
            roll = random.randint(2,12) + starportDM
            if roll >= 8: starport_bases.append("Research")
            starport_bases.append("TAS")
        elif planetStarport >= 9:
            roll = random.randint(2,12) + starportDM
            if roll >= 8: starport_bases.append("Naval")
            roll = random.randint(2,12) + starportDM
            if roll >= 8: starport_bases.append("Scout")
            roll = random.randint(2,12) + starportDM
            if roll >= 10: starport_bases.append("Research")
            starport_bases.append("TAS")
        elif planetStarport >= 7:
            roll = random.randint(2,12) + starportDM
            if roll >= 8: starport_bases.append("Scout")
            roll = random.randint(2,12) + starportDM
            if roll >= 10: starport_bases.append("Research")
            roll = random.randint(2,12) + starportDM
            if roll >= 10: starport_bases.append("TAS")
        elif planetStarport >= 5:
            roll = random.randint(2,12) + starportDM
            if roll >= 7: starport_bases.append("TAS")
        piracy_warning_roll = random.randint(2,12)
        systemDictionary["system piracy warning"] = False
        if (
            (piracy_warning_roll >= 12 and planetStarport >= 7) or 
            (piracy_warning_roll >= 11 and planetStarport <= 6)
            ):
            systemDictionary["system piracy warning"] = True
            starport_bases.append("Pirate")

        systemDictionary["primary starport types"] = starport_bases
        systemDictionary["system bases"] = starport_bases
        systemDictionary["primary starport types roll"] = planetStarportTypes
        # systemDictionary["primary starport types highest"] = ""
        # SubsectorGenerator.setBaseTypeMine(systemDictionary)
        if "Naval" in starport_bases:
            systemDictionary["primary starport types highest"] = "N"
        elif "Scout" in starport_bases:
            systemDictionary["primary starport types highest"] = "S"
        elif "Research" in starport_bases:
            systemDictionary["primary starport types highest"] = "R"
        elif "Research" in starport_bases:
            systemDictionary["primary starport types highest"] = "T"
        else:
            systemDictionary["primary starport types highest"] = "-"

        # TECH LEVEL
        minTechLevel = 3
        if(planetAtmosphere in [2, 3, 13, 14]): minTechLevel = 5
        elif(planetAtmosphere in [0, 1, 10, 15]): minTechLevel = 8
        elif(planetAtmosphere in [11]): minTechLevel = 9
        elif(planetAtmosphere in [12]): minTechLevel = 1
        techLevelDM = 0
        if (planetStarport in [10]):   techLevelDM +=6
        elif (planetStarport in [11]): techLevelDM +=4
        elif (planetStarport in [12]): techLevelDM +=2
        if (planetSize in [0, 1]): techLevelDM +=2
        elif (planetSize in [2, 3, 4]): techLevelDM +=1
        if (planetAtmosphere in [1, 2, 3, 4, 10, 11, 12, 13, 14, 15]): techLevelDM +=1
        if (planetHydrographics in [0, 1]): techLevelDM +=1
        elif (planetHydrographics in [10]): techLevelDM +=2
        if (planetPopulation in [1, 2, 3, 4, 5, 8]):   techLevelDM +=1
        elif (planetPopulation in [9]): techLevelDM +=2
        elif (planetPopulation in [10]): techLevelDM +=4
        if (planetGovernment in [0, 5]):   techLevelDM +=1
        elif (planetGovernment in [7]): techLevelDM +=2
        elif (planetGovernment in [13, 14]): techLevelDM -=2
        planetTechLevel = minTechLevel + random.randint(1,6) + techLevelDM
        if(planetPopulation == 0):
            planetTechLevel = 0
        systemDictionary["primary tech level"] = planetTechLevel
    @staticmethod
    def determine_travel_codes(systemDictionary):
        # SYSTEM TRAVEL CODES
        systemDictionary["system travel code"] = "-"
        amber_travel_code_reasons = []
        if systemDictionary["system piracy warning"]:
            amber_travel_code_reasons.append("Pirate Presence")
        if systemDictionary["primary atmosphere"] >= 10: # Don't fix
            amber_travel_code_reasons.append("Harsh Atmosphere")
        if systemDictionary["primary government"] in [0,7,10] and systemDictionary["primary population"] > 0:

            if systemDictionary["primary government"] == 0:
                if (random.randint(1, 6) < 4): # fix this 1/2 the time
                    systemDictionary["primary government"] = random.randint(1, 3)
                else:
                    amber_travel_code_reasons.append("Government Strife: No Government")
            if systemDictionary["primary government"] == 10:
                if (random.randint(1, 6) < 4): # fix this 1/2 the time
                    systemDictionary["primary government"] = systemDictionary["primary government"] + random.choice([-1,1])
                else:
                    amber_travel_code_reasons.append("Government Strife: Unstable Government")
        if systemDictionary["primary law level"] == 0 and systemDictionary["primary population"] > 0:
            if (random.randint(1, 6) < 4): # fix this 1/2 the time
                systemDictionary["primary law level"] = 1
            else:
                amber_travel_code_reasons.append("No weapon restrictions (Wild West)")
        if systemDictionary["primary law level"] >= 9:
            if (random.randint(1, 6) < 4): # fix this 1/2 the time
                systemDictionary["primary law level"] = 8
            else:
                amber_travel_code_reasons.append("NO Weapons & Armor: All Weapons and Armor Banned") 
        if len(amber_travel_code_reasons) > 0: 
            systemDictionary["system travel code"] = "A"
            systemDictionary["system travel code reason"] = amber_travel_code_reasons
    @staticmethod
    def regenerate_existing_travel_codes(system):
        # SYSTEM TRAVEL CODES
        system.travelCode = "-"
        amber_travel_code_reasons = []
        if system.piracy_warning:
            amber_travel_code_reasons.append("Pirate Presence")
        if system.primaryPlanet.atmosphere >= 10: # Don't fix
            amber_travel_code_reasons.append("Harsh Atmosphere")
        if system.primaryPlanet.government in [0,7,10] and system.primaryPlanet.population > 0:

            if system.primaryPlanet.government == 0:
                if (random.randint(1, 6) < 4): # fix this 1/2 the time
                    system.primaryPlanet.government = random.randint(1, 3)
                else:
                    amber_travel_code_reasons.append("Government Strife: No Government")
            if system.primaryPlanet.government == 10:
                if (random.randint(1, 6) < 4): # fix this 1/2 the time
                    system.primaryPlanet.government +=  random.choice([-1,1])
                else:
                    amber_travel_code_reasons.append("Government Strife: Unstable Government")
        if system.primaryPlanet.lawLevel == 0 and system.primaryPlanet.population > 0:
            if (random.randint(1, 6) < 4): # fix this 1/2 the time
                system.primaryPlanet.lawLevel = 1
            else:
                amber_travel_code_reasons.append("No weapon restrictions (Wild West)")
        if system.primaryPlanet.lawLevel >= 9:
            if (random.randint(1, 6) < 4): # fix this 1/2 the time
                system.primaryPlanet.lawLevel = 8
            else:
                amber_travel_code_reasons.append("NO Weapons & Armor: All Weapons and Armor Banned") 
        if len(amber_travel_code_reasons) > 0: 
            system.primaryPlanet.travelCode = "A"
            system.travelCodeReason = amber_travel_code_reasons
    @staticmethod
    def generateLocalSystem( name, hexLoc, must_be_earthlike, verbose=False): 
        if (hexLoc is None): return None
        """
        -   systemChance: ranges from 1-5 and is used as a part of a range for world chance in a parsec hex
        """
        letters = ["Star","Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", 
            "Eta", "Theta", "Iota", "Kappa", "Lamda", "Mu", "Nu", "", 
            "Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Upsilon", "Phi", 
            "Chi", "Psi", "Omega"]
        planetHeatLevel = 0
        planetHabitableZoneLocation = 0
        systemDictionary = {}
        # GAS GIANT TEST
        gasGiantChanceTestDM = 8
        planetoidBeltChanceTestDM = 4
        systemDictionary["name"] = name
        systemDictionary["system hex"] = hexLoc
        systemDictionary["system alignment"] = "Im"
        systemDictionary["system noble leader"] = ""
        primary_in_belt = False

        star = Star.generate(name)
        if verbose: print(str(star))
        systemDictionary["system star"] = star

        # System Lineup and Habitable zone
        systemDictionary["system lineup"] = [star, None,None,None,None,None,None, None,None,None,None,None,None, None,None,None,None,None,None]
        systemDictionary["system habitable zone"] = random.randint(1,6)

        systemDictionary["system gas giants"] = SubsectorGenerator.getNumberGasGiants(gasGiantChanceTestDM)
        systemDictionary["system asteroid belts"] = SubsectorGenerator.getNumberPlanetoidBelts(planetoidBeltChanceTestDM)
        # STUB TODO FIX THIS: MW (1) + GasGiants (2) + Belts (4) + 2D
        systemDictionary["system populated worlds"] = 1 + systemDictionary["system gas giants"] + systemDictionary["system gas giants"] + random.randint(2,12) 
        # Generate Primary
        if must_be_earthlike:
            SubsectorGenerator.generateEarthlikePrimary( name, hexLoc, systemDictionary, planetHabitableZoneLocation, verbose)
        else:
            SubsectorGenerator.generateRandomPrimary( name, hexLoc, systemDictionary, planetHabitableZoneLocation, verbose)

        # Travel codes:
        SubsectorGenerator.determine_travel_codes(systemDictionary)
        

        # SYSTEM TRADE CODES
        planetSize=systemDictionary["primary size"]
        planetAtmosphere=systemDictionary["primary atmosphere"]
        planetHydrographics=systemDictionary["primary hydrographics"]
        planetPopulation=systemDictionary["primary population"]
        planetGovernment=systemDictionary["primary government"]
        planetLawLevel=systemDictionary["primary law level"]
        planetTechLevel=systemDictionary["primary tech level"]
        systemTradeCodes = []
        if( planetAtmosphere in [4, 5, 6, 7, 8, 9] and 
            planetHydrographics in [4, 5, 6, 7, 8] and 
            planetPopulation in [5, 6, 7]): 
            systemTradeCodes.append("Ag")
        if(planetPopulation == 0 and planetAtmosphere == 0 and planetHydrographics == 0): systemTradeCodes.append("As")
        if(planetPopulation == 0 and planetGovernment == 0 and planetLawLevel == 0): systemTradeCodes.append("Ba")
        if(planetHydrographics == 0 and planetAtmosphere >= 2): systemTradeCodes.append("De")
        if(planetAtmosphere >= 10 and planetTechLevel >= 1): systemTradeCodes.append("Fl")
        if(planetSize in [6, 7, 8] and planetAtmosphere in [5, 6, 8] and planetHydrographics in [5, 6, 7]): 
            systemTradeCodes.append("Ga")
        if(planetPopulation >= 9): systemTradeCodes.append("Hi")
        if(planetTechLevel >= 12): systemTradeCodes.append("Ht")
        if(planetHydrographics > 0 and planetAtmosphere in [0, 1]): systemTradeCodes.append("Ie")
        if(planetAtmosphere in [0, 1, 2, 4, 7, 9] and planetPopulation >= 9): systemTradeCodes.append("In")
        if(planetPopulation <= 3): systemTradeCodes.append("Lo")
        if(planetTechLevel <= 5): systemTradeCodes.append("Lt")
        if(planetAtmosphere in [0, 1, 2, 3] and planetHydrographics <= 3 and planetPopulation >= 6): systemTradeCodes.append("Na")
        if(planetPopulation in [0, 1, 2, 3, 4, 5, 6]): systemTradeCodes.append("Ni")
        if(planetHydrographics <= 3): systemTradeCodes.append("Po")
        if(planetAtmosphere in [6,8] and planetPopulation in [6, 7, 8] and planetGovernment in [4, 5, 6, 7, 8, 9]): 
            systemTradeCodes.append("Ri")
        if(planetAtmosphere == 0): systemTradeCodes.append("Va")
        if(planetHydrographics >= 10): systemTradeCodes.append("Wa")

        systemDictionary["system trade codes"] = systemTradeCodes

        

        # Get Broader system planets and Moons
        numberOfOtherPlanets = systemDictionary["system populated worlds"] - 1 # -1 for primary 
        primaryPlanet = PrimaryPlanet(systemDictionary)
        primaryPlanet.name = name
        if primaryPlanet.size < 2: # generate Belt as primary
            systemDictionary["system asteroid belts"] = 1
            primary_in_belt=True
            beltName = "{} {}".format(name, letters[systemDictionary["system habitable zone"]])
            population = primaryPlanet.population
            government = primaryPlanet.government
            tech = primaryPlanet.techLevel
            law = primaryPlanet.lawLevel
            starport = primaryPlanet.starport
            
            systemDictionary["primary size"] = 0
            primaryPlanet.size = 0
            systemDictionary["primary atmosphere"] = 0
            primaryPlanet.atmosphere = 0
            systemDictionary["primary hydrographics"] = 0
            primaryPlanet.hydrographics = 0
            systemDictionary["primary temperature"] = 0
            primaryPlanet.temperature = 0

            beltDict= {
                "{} size".format(beltName): 0, "{} atmosphere".format(beltName): 0, 
                "{} hydrographics".format(beltName):0, "{} temperature".format(beltName): 0, 
                "{} population".format(beltName): population, "{} government".format(beltName): government, 
                "{} law level".format(beltName): law, "{} tech level".format(beltName): tech,
                "{} starport".format(beltName): starport,  
                }
            belt = AsteroidBelt(beltDict, beltName)

            # Asteroid Ring Planetoids.
            numberAsteroidMoons = random.randint(population, population*5)
            if (belt.moons is None): 
                belt.moons = []
            belt.add_primary( primaryPlanet )
            assigned_population = 0
            asteroidMoonPopulation = population
            for i in range(numberAsteroidMoons):
                moonSize = 0
                if belt.size >= 4:
                    moonSize = random.randint(0, int(belt.size * 0.75) )
                moonAtmo = moonSize - 2
                moonTemp = 2
                if(moonSize in [0, 1, 2]): moonAtmo = 0
                elif(moonSize in [3, 4] and moonAtmo in [0, 1, 2]): moonAtmo = 0
                elif(moonSize in [3, 4] and moonAtmo in [3, 4, 5]): moonAtmo = 1
                elif(moonSize in [3, 4] and moonAtmo >= 6): moonAtmo = 10
                moonHydro = random.choice([0,0,0,0,0,1])
                if asteroidMoonPopulation > 1:
                    asteroidMoonPopulation = random.choice(range(asteroidMoonPopulation-assigned_population))
                if assigned_population == population:
                    asteroidMoonPopulation = 0
                else:
                    asteroidMoonPopulation = 1
                assigned_population += asteroidMoonPopulation
                asteroidMoonGovernment = government
                asteroidMoonLaw = law
                asteroidMoonTech = tech
                asteroidMoonStarport = starport
                if asteroidMoonPopulation < 1:
                    asteroidMoonGovernment = 0
                    asteroidMoonLaw = 0
                    asteroidMoonTech = 0
                    asteroidMoonStarport = 0
                moonDict = {
                        "{}-{} size".format(belt.name,i+1): moonSize, "{}-{} atmosphere".format(belt.name,i+1): moonAtmo, 
                        "{}-{} hydrographics".format(belt.name,i+1): moonHydro, "{}-{} temperature".format(belt.name,i+1): moonTemp, 
                        "{}-{} population".format(belt.name,i+1): asteroidMoonPopulation, "{}-{} government".format(belt.name,i+1): asteroidMoonGovernment, 
                        "{}-{} law level".format(belt.name,i+1): asteroidMoonLaw, "{}-{} tech level".format(belt.name,i+1): asteroidMoonTech,
                        "{}-{} starport".format(belt.name,i+1): asteroidMoonStarport,  
                        }
                belt.add_orbiting_body( Moon( moonDict, "{}-{}".format(belt.name,i+1) ) )
            
            primaryPlanet = belt
        else:
            # primary Moons.
            numberPrimaryMoons = random.choice([0,1,1,1,2,3])
            planetName = primaryPlanet.name
            if (primaryPlanet.moons is None): 
                primaryPlanet.moons = []
            for i in range(numberPrimaryMoons):
                moonSize = 0
                if primaryPlanet.size >= 4:
                    moonSize = random.randint(0, int(primaryPlanet.size * 0.75) )
                moonAtmo = moonSize - 2
                moonTemp = 2
                if(moonSize in [0, 1, 2]): moonAtmo = 0
                elif(moonSize in [3, 4] and moonAtmo in [0, 1, 2]): moonAtmo = 0
                elif(moonSize in [3, 4] and moonAtmo in [3, 4, 5]): moonAtmo = 1
                elif(moonSize in [3, 4] and moonAtmo >= 6): moonAtmo = 10
                moonHydro = random.choice([0,0,0,0,0,1])
                moonDict = {
                        "{}-{} size".format(planetName,i+1): moonSize, "{}-{} atmosphere".format(planetName,i+1): moonAtmo, 
                        "{}-{} hydrographics".format(planetName,i+1): moonHydro, "{}-{} temperature".format(planetName,i+1): moonTemp, 
                        "{}-{} population".format(planetName,i+1): 0, "{}-{} government".format(planetName,i+1): 0, 
                        "{}-{} law level".format(planetName,i+1): 0, "{}-{} tech level".format(planetName,i+1): 0,
                        "{}-{} starport".format(planetName,i+1): 0,  
                        }
                moon = Moon( moonDict, "{}-{}".format(planetName,i+1) )
                primaryPlanet.add_orbiting_body( moon )
                moon.parent = primaryPlanet
                if verbose: print("added Moon")
        if verbose: print(str(primaryPlanet))

        
        # Save primary.
        systemDictionary["system lineup"][systemDictionary["system habitable zone"]] = primaryPlanet

        # Other Bodies in this system
        # Gas Giants
        for i in range(systemDictionary["system gas giants"]):
            numberOfOtherPlanets -= 1
            loc = systemDictionary["system habitable zone"] + random.randint(1,6)
            while (systemDictionary["system lineup"][loc] is not None):
                loc += 1
            gasGiantName = "{} {}".format(name, letters[loc])
            gasGiantDict= {
                "{} size".format(gasGiantName): 0, "{} atmosphere".format(gasGiantName): 0, 
                "{} hydrographics".format(gasGiantName): 0, "{} temperature".format(gasGiantName): 0, 
                "{} population".format(gasGiantName): 0, "{} government".format(gasGiantName): 0, 
                "{} law level".format(gasGiantName): 0, "{} tech level".format(gasGiantName): 0,
                "{} starport".format(gasGiantName): 0,  
                }
            gas_giant = GasGiant(gasGiantDict, gasGiantName)
            systemDictionary["system lineup"][loc] = gas_giant
            # non prime Moons.
            numberJovianMoons = random.randint(6, 16)
            swapped_primary = False
            planetName = gas_giant.name
            if (gas_giant.moons is None): 
                gas_giant.moons = []
            for i in range(numberJovianMoons):
                moon = None
                swapped_primary = False
                roll = random.randint(1, 6)
                moon = None
                if roll == 6: # Planetoid moon!
                    moonDict = {}
                    moonName = PseudoMarkovNameGenerator.getName(PseudoMarkovNameGenerator.readLinesFromFile("surnames.txt"))
                    SubsectorGenerator.generateRandomPrimary( moonName, hexLoc, moonDict, loc, verbose=False)
                    planetoidMoon = PrimaryPlanet( moonDict )
                    # Planetoid Moons.
                    numberPlanetoidMoonMoons = random.choice([0,1,1,1,2,2,2,3,3,4])
                    planetoidMoon.name = moonName
                    if (planetoidMoon.moons is None): 
                        planetoidMoon.moons = []
                    for j in range(numberPlanetoidMoonMoons):
                        moonSize = 0
                        if planetoidMoon.size >= 4:
                            moonSize = random.randint(0, int(planetoidMoon.size * 0.75) )
                        moonAtmo = moonSize - 2
                        moonTemp = 2
                        if(moonSize in [0, 1, 2]): moonAtmo = 0
                        elif(moonSize in [3, 4] and moonAtmo in [0, 1, 2]): moonAtmo = 0
                        elif(moonSize in [3, 4] and moonAtmo in [3, 4, 5]): moonAtmo = 1
                        elif(moonSize in [3, 4] and moonAtmo >= 6): moonAtmo = 10
                        moonHydro = random.choice([0,0,0,0,0,1])
                        moonTechLevel = primaryPlanet.techLevel
                        moonDict = {
                                "{}-{} size".format(moonName,j+1): moonSize, "{}-{} atmosphere".format(moonName,j+1): moonAtmo, 
                                "{}-{} hydrographics".format(moonName,j+1): moonHydro, "{}-{} temperature".format(moonName,j+1): moonTemp, 
                                "{}-{} population".format(moonName,j+1): 0, "{}-{} government".format(moonName,j+1): 0, 
                                "{}-{} law level".format(moonName,j+1): 0, "{}-{} tech level".format(moonName,j+1): moonTechLevel,
                                "{}-{} starport".format(moonName,j+1): 0,  
                                }
                        
                        planetoidMoon.moons.append( Moon( moonDict, "{}-{}".format(moonName,j+1) ) )
                    # Is Planetoid new Prime?
                    if (primaryPlanet.techLevel > 0): 
                        planetoidMoon.techLevel = primaryPlanet.techLevel
                    if (primaryPlanet.starport > 0):# There is a space port here, and on the Primary, primary spaceport must be best
                        planetoidMoon.starport = random.choice(range(primaryPlanet.starport))
                        if verbose: print("{}'s starport is {} | primary is {}".format(planetoidMoon.name, planetoidMoon.starport, primaryPlanet.starport))
                        planetoidMoon = planetoidMoon.make_non_primary() # turn planetoid into Planet rather than prime 
                    else:# There is a space port here, but not on the "primary"
                        if verbose: print("***{} - Habitable Zone is: {}".format(name, systemDictionary["system habitable zone"]))
                        if verbose: print(str(systemDictionary["system lineup"][systemDictionary["system habitable zone"]]))
                        if verbose: 
                            print("Switching {} [{}] to {} [{}] orbiting {} (Jovian)".format(
                                primaryPlanet.name, 
                                primaryPlanet.uwp, 
                                planetoidMoon.name, 
                                planetoidMoon.uwp, 
                                gas_giant.name))
                            for body in systemDictionary["system lineup"]:
                                if verbose: print("{} [{}]".format(body.name if body else "-", str(body)))
                        old_primary = primaryPlanet
                        planetoidMoon.name = primaryPlanet.name
                        if old_primary in systemDictionary["system lineup"]:
                            old_primary.name = "{} {}".format(name, letters[systemDictionary["system lineup"].index(primaryPlanet)])
                        else:
                            old_primary.name = moonName
                        primaryPlanet = planetoidMoon
                        if verbose:print("Primary's Swapped! {} -> {}".format(old_primary.name, primaryPlanet.name))
                        swapped_primary = True
                    moon = planetoidMoon
                elif roll == 5 and not gas_giant.rings: # It has a ring of asteroids!
                    beltName = "{} {}".format(name, letters[loc])
                    population = random.randint(1,6)
                    government = systemDictionary["primary government"]
                    tech = systemDictionary["primary tech level"]
                    law_value = min(max(0,systemDictionary["primary law level"]), 9)
                    law = random.choice(range(law_value)) if law_value > 1 else 0
                    starport = systemDictionary["primary starport"]
                    beltDict= {
                        "{} size".format(beltName): 0, "{} atmosphere".format(beltName): 0, 
                        "{} hydrographics".format(beltName): 0, "{} temperature".format(beltName): 0, 
                        "{} population".format(beltName): population, "{} government".format(beltName): government, 
                        "{} law level".format(beltName): law, "{} tech level".format(beltName): tech,
                        "{} starport".format(beltName): starport,  
                        }
                    belt = AsteroidBelt(beltDict, beltName)
                    systemDictionary["system lineup"][loc] = belt
                    # Asteroid Ring Planetoids.
                    numberAsteroidMoons = random.randint(1, 5)
                    if (belt.moons is None): 
                        belt.moons = []
                    assigned_population = 0
                    asteroidMoonPopulation = population
                    for i in range(numberAsteroidMoons):
                        moonSize = 0
                        if belt.size >= 4:
                            moonSize = random.randint(0, int(belt.size * 0.75) )
                        moonAtmo = moonSize - 2
                        moonTemp = 2
                        if(moonSize in [0, 1, 2]): moonAtmo = 0
                        elif(moonSize in [3, 4] and moonAtmo in [0, 1, 2]): moonAtmo = 0
                        elif(moonSize in [3, 4] and moonAtmo in [3, 4, 5]): moonAtmo = 1
                        elif(moonSize in [3, 4] and moonAtmo >= 6): moonAtmo = 10
                        moonHydro = random.choice([0,0,0,0,0,1])
                        if asteroidMoonPopulation > 1:
                            asteroidMoonPopulation = random.choice(range(asteroidMoonPopulation-assigned_population))
                        if assigned_population == population:
                            asteroidMoonPopulation = 0
                        else:
                            asteroidMoonPopulation = 1
                        assigned_population += asteroidMoonPopulation
                        asteroidMoonGovernment = government
                        asteroidMoonLaw = law
                        asteroidMoonTech = tech
                        asteroidMoonStarport = starport
                        if asteroidMoonPopulation < 1:
                            asteroidMoonGovernment = 0
                            asteroidMoonLaw = 0
                            asteroidMoonTech = 0
                            asteroidMoonStarport = 0
                        moonDict = {
                                "{}-{} size".format(belt.name,i+1): moonSize, "{}-{} atmosphere".format(belt.name,i+1): moonAtmo, 
                                "{}-{} hydrographics".format(belt.name,i+1): moonHydro, "{}-{} temperature".format(belt.name,i+1): moonTemp, 
                                "{}-{} population".format(belt.name,i+1): asteroidMoonPopulation, "{}-{} government".format(belt.name,i+1): asteroidMoonGovernment, 
                                "{}-{} law level".format(belt.name,i+1): asteroidMoonLaw, "{}-{} tech level".format(belt.name,i+1): asteroidMoonTech,
                                "{}-{} starport".format(belt.name,i+1): asteroidMoonStarport,  
                                }
                        belt.add_orbiting_body( Moon( moonDict, "{}-{}".format(belt.name,i+1) ) )
                        moon = belt
                        gas_giant.rings = True
                        if verbose: print("added Asteroid Ring Planetoids")
                    moon = belt
                    if verbose: print("added Asteroid Ring")
                else: # Normal Moon
                    moonSize = 0
                    if gas_giant.size >= 4:
                        moonSize = random.randint(0, int(gas_giant.size * 0.75) )
                    moonAtmo = moonSize - 2
                    moonTemp = 2
                    if(moonSize in [0, 1, 2]): moonAtmo = 0
                    elif(moonSize in [3, 4] and moonAtmo in [0, 1, 2]): moonAtmo = 0
                    elif(moonSize in [3, 4] and moonAtmo in [3, 4, 5]): moonAtmo = 1
                    elif(moonSize in [3, 4] and moonAtmo >= 6): moonAtmo = 10
                    moonHydro = random.choice([0,0,0,0,0,1])
                    moonTechLevel = primaryPlanet.techLevel
                    moonDict = {
                            "{}-{} size".format(planetName,i+1): moonSize, "{}-{} atmosphere".format(planetName,i+1): moonAtmo, 
                            "{}-{} hydrographics".format(planetName,i+1): moonHydro, "{}-{} temperature".format(planetName,i+1): moonTemp, 

                            "{}-{} population".format(planetName,i+1): 0, "{}-{} government".format(planetName,i+1): 0, 
                            "{}-{} law level".format(planetName,i+1): 0, "{}-{} tech level".format(planetName,i+1): moonTechLevel,
                            "{}-{} starport".format(planetName,i+1): 0,  
                            }
                    moon = Moon( moonDict, "{}-{}".format(planetName,i+1) )
                gas_giant.add_orbiting_body( moon )
                if verbose or swapped_primary:
                    for body in systemDictionary["system lineup"]:
                        if body:
                            if verbose: print("{} [{}]".format(body.name if body else "-", str(body)))
                            if not isinstance(body, Star) and body.moons:
                                for m in body.moons:
                                    if m and verbose:
                                        print("  {} [{}]".format(m.name if m else "-", str(m)))
                if verbose: print("added Moon")
            if verbose: print(str(systemDictionary["system lineup"][loc]))
        # Asteroid Belts
        primary_in_belt
        num_asteroid_belts = systemDictionary["system asteroid belts"]
        if primary_in_belt:
            num_asteroid_belts = max(0,num_asteroid_belts)
        for i in range(num_asteroid_belts):
            numberOfOtherPlanets -= 1
            loc = systemDictionary["system habitable zone"] + random.randint(1,6)
            while (systemDictionary["system lineup"][loc] is not None):
                loc += 1
            beltName = "{} {}".format(name, letters[loc])
            population = random.randint(1,6)
            government = systemDictionary["primary government"]
            tech = systemDictionary["primary tech level"]
            law = systemDictionary["primary law level"]
            starport = systemDictionary["primary starport"]
            beltDict= {
                "{} size".format(beltName): 0, "{} atmosphere".format(beltName): 0, 
                "{} hydrographics".format(beltName): 0, "{} temperature".format(beltName): 0, 
                "{} population".format(beltName): population, "{} government".format(beltName): government, 
                "{} law level".format(beltName): law, "{} tech level".format(beltName): tech,
                "{} starport".format(beltName): starport,  
                }
            belt = AsteroidBelt(beltDict, beltName)
            systemDictionary["system lineup"][loc] = belt
            # non prime Moons.
            numberAsteroidMoons = random.randint(3, 10)
            planetName = belt.name
            if (belt.moons is None): 
                belt.moons = []
            for i in range(numberAsteroidMoons):
                moon = None
                moonSize = 0
                if belt.size >= 4:
                    moonSize = random.randint(0, int(belt.size * 0.75) )
                moonAtmo = moonSize - 2
                moonTemp = 2
                if(moonSize in [0, 1, 2]): moonAtmo = 0
                elif(moonSize in [3, 4] and moonAtmo in [0, 1, 2]): moonAtmo = 0
                elif(moonSize in [3, 4] and moonAtmo in [3, 4, 5]): moonAtmo = 1
                elif(moonSize in [3, 4] and moonAtmo >= 6): moonAtmo = 10
                moonHydro = random.choice([0,0,0,0,0,1])
                moonTechLevel = primaryPlanet.techLevel
                moonDict = {
                        "{}-{} size".format(planetName,i+1): moonSize, "{}-{} atmosphere".format(planetName,i+1): moonAtmo, 
                        "{}-{} hydrographics".format(planetName,i+1): moonHydro, "{}-{} temperature".format(planetName,i+1): moonTemp, 
                        "{}-{} population".format(planetName,i+1): 0, "{}-{} government".format(planetName,i+1): 0, 
                        "{}-{} law level".format(planetName,i+1): 0, "{}-{} tech level".format(planetName,i+1): moonTechLevel,
                        "{}-{} starport".format(planetName,i+1): 0,  
                        }
                
                moon = Moon( moonDict, "{}-{}".format(planetName,i+1) )
                belt.add_orbiting_body( moon )
                if verbose: print("added Moon")
            if verbose: print(str(systemDictionary["system lineup"][loc]))
        # Misc Planets
        for i in range(numberOfOtherPlanets):
            loc = 1+i
            if (systemDictionary["system lineup"][loc] is not None):
                continue
            if verbose: print("Planet {} of system {}".format(i, name))
            isInner = (loc < 8)
            planetName = "{} {}".format(name, letters[loc])
            if verbose: print(planetName)
            planetSize = (max(1, random.randint(2, 12) - 2) if isInner else max(1, random.randint(1,6) - 2))
            planetAtmo = planetSize - 2
            planetTemp = (12 if isInner else 2)
            if(planetSize in [0, 1, 2]): planetAtmo = 0
            elif(planetSize in [3, 4] and planetAtmo in [0, 1, 2]): planetAtmo = 0
            elif(planetSize in [3, 4] and planetAtmo in [3, 4, 5]): planetAtmo = 1
            elif(planetSize in [3, 4] and planetAtmo >= 6): planetAtmo = 10
            planetHydro = (0 if isInner else max(0,planetSize-6))

            if (planetSize in [7, 8, 9] and planetAtmo in [5, 6, 7]):
                planetHydroDM = 0
                planetHydro = random.randint(2,12)-7 + planetAtmo + planetHydroDM
                if isInner and i < systemDictionary["system habitable zone"]: planetTemp = 12
                elif isInner and i > systemDictionary["system habitable zone"]: planetTemp = 7
                else: planetTemp = 2
            planetDict = {
                "{} size".format(planetName): planetSize, "{} atmosphere".format(planetName): planetAtmo, 
                "{} hydrographics".format(planetName): planetHydro, "{} temperature".format(planetName): planetTemp, 
                "{} population".format(planetName): 0, "{} government".format(planetName): 0, 
                "{} law level".format(planetName): 0, "{} tech level".format(planetName): 0,
                "{} starport".format(planetName): 0,  
                "{} berthing cost".format(planetName):0,
                "{} refined fuel".format(planetName):0,
                "{} unrefined fuel".format(planetName):0
                }
            if verbose: print(str(planetDict))
            non_prime_planet = Planet(planetDict, planetName)
            systemDictionary["system lineup"][loc] = non_prime_planet
            # non prime Moons.
            numberNonPrimaryMoons = random.choice([0,1,1,1,2,2,2,3,3,4])
            planetName = non_prime_planet.name
            if (non_prime_planet.moons is None): 
                non_prime_planet.moons = []
            for i in range(numberNonPrimaryMoons):
                moon = None
                moonSize = 0
                if non_prime_planet.size >= 4:
                    moonSize = random.randint(0, int(non_prime_planet.size * 0.75) )
                moonAtmo = moonSize - 2
                moonTemp = 2
                if(moonSize in [0, 1, 2]): moonAtmo = 0
                elif(moonSize in [3, 4] and moonAtmo in [0, 1, 2]): moonAtmo = 0
                elif(moonSize in [3, 4] and moonAtmo in [3, 4, 5]): moonAtmo = 1
                elif(moonSize in [3, 4] and moonAtmo >= 6): moonAtmo = 10
                moonHydro = random.choice([0,0,0,0,0,1])
                moonTechLevel = primaryPlanet.techLevel
                moonDict = {
                        "{}-{} size".format(planetName,i+1): moonSize, "{}-{} atmosphere".format(planetName,i+1): moonAtmo, 
                        "{}-{} hydrographics".format(planetName,i+1): moonHydro, "{}-{} temperature".format(planetName,i+1): moonTemp, 
                        "{}-{} population".format(planetName,i+1): 0, "{}-{} government".format(planetName,i+1): 0, 
                        "{}-{} law level".format(planetName,i+1): 0, "{}-{} tech level".format(planetName,i+1): moonTechLevel,
                        "{}-{} starport".format(planetName,i+1): 0,  
                        }
                
                non_prime_planet.add_orbiting_body(  Moon( moonDict, "{}-{}".format(planetName,i+1) ) )
                if verbose: print("added Moon")
        if verbose: print("DONE")
        return systemDictionary
        #
    @staticmethod
    def getStarportClass(starportLevel):
        if(starportLevel is None): return "X"
        if(starportLevel in [3, 4]): return "E"
        elif(starportLevel in [5, 6]): return "D"
        elif(starportLevel in [7, 8]): return "C"
        elif(starportLevel in [9, 10]): return "B"
        elif(starportLevel >= 11): return "A"
        else: return "X"
    @staticmethod
    def getGetFullTradeCodes(tradeCode):
        if (tradeCode.lower() == "ag"): return "Agricultural"
        elif (tradeCode.lower() == "as"): return "Asteroid"
        elif (tradeCode.lower() == "ba"): return "Barren"
        elif (tradeCode.lower() == "de"): return "Desert"
        elif (tradeCode.lower() == "fl"): return "Fluid Oceans"
        elif (tradeCode.lower() == "ga"): return "Garden"
        elif (tradeCode.lower() == "hi"): return "High Population"
        elif (tradeCode.lower() == "ht"): return "High Tech"
        elif (tradeCode.lower() == "ie"): return "Ice-Capped"
        elif (tradeCode.lower() == "in"): return "Industrial"
        elif (tradeCode.lower() == "lo"): return "Low Population"
        elif (tradeCode.lower() == "lt"): return "Low Tech"
        elif (tradeCode.lower() == "na"): return "Non-Agricultural"
        elif (tradeCode.lower() == "ni"): return "Non-Industrial"
        elif (tradeCode.lower() == "po"): return "Poor"
        elif (tradeCode.lower() == "ri"): return "Rich"
        elif (tradeCode.lower() == "va"): return "Vacuum"
        elif (tradeCode.lower() == "wa"): return "Water World"
        elif (tradeCode.lower() == "oc"): return "Ocean World"
        elif (tradeCode.lower() == "co"): return "Cold World"
        elif (tradeCode.lower() == "tu"): return "Tundra World"
        elif (tradeCode.lower() == "fr"): return "Frozen World"
        elif (tradeCode.lower() == "ho"): return "Hot World"
        elif (tradeCode.lower() == "he"): return "Hell World"
        elif (tradeCode.lower() == "tr"): return "Tropical World"
        elif (tradeCode.lower() == "lk"): return "Locked World"
        elif (tradeCode.lower() == "cp"): return "Subsector Capital"
        elif (tradeCode.lower() == "cs"): return "Sector Capital"
        elif (tradeCode.lower() == "cy"): return "Colony World"
    @staticmethod
    def displayUppCode(system):
        hex_key=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        return"{}{}{}{}{}{}{}-{}".format(
            Utils.hex_key[system["primary size"]],
            Utils.hex_key[system["primary atmosphere"]],
            Utils.hex_key[min(15, max(0, system["primary hydrographics"]))],
            Utils.hex_key[system["primary population"]],
            Utils.hex_key[system["primary government"]],
            Utils.hex_key[system["primary law level"]],
            Utils.hex_key[min(15, max(0, system["primary tech level"]))],
            SubsectorGenerator.getStarportClass(system["primary starport"]),
            )
    @staticmethod
    def displayUwpCode(system):
        hex_key=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        return"{}{}{}{}{}{}{}-{}".format(
            SubsectorGenerator.getStarportClass(system["primary starport"]),
            Utils.hex_key[system["primary size"]],
            Utils.hex_key[system["primary atmosphere"]],
            Utils.hex_key[min(15, max(0, system["primary hydrographics"]))],
            Utils.hex_key[system["primary population"]],
            Utils.hex_key[system["primary government"]],
            Utils.hex_key[system["primary law level"]],
            Utils.hex_key[min(15, max(0, system["primary tech level"]))],
            )
    @staticmethod
    def getGenieSunbaneSystemCode(system):
        remarks = ""
        for tradeCode in system["system trade codes"]:
            remarks += "{} ".format(tradeCode)
        return "{0:<14}{1:<4} {2:<9} {3:<1} {4:<16} {5:1}  {6:<3} {7:2} {8:<15}".format(
            system["name"],
            system["system hex"],
            SubsectorGenerator.displayUppCode(system),
            system["primary starport types highest"],
            remarks[:16],
            " ", # ZONE: - A R
            "{}{}{}".format("P","B",system["system gas giants"]),
            "Im",
            system["system star"].getStellarCode(),
            )
    @staticmethod
    def getT5FormatSystemCode(systemDict):
        '''
        Hex  Name                 UWP       Remarks                     {Ix}   (Ex)    [Cx]   N     B  Z PBG W  A    Stellar              
        ---- -------------------- --------- --------------------------- ------ ------- ------ ----- -- - --- -- ---- ---------------------
        '''
        remarks = ""
        for tradeCode in systemDict["system trade codes"]:
            remarks += "{} ".format(tradeCode)
        return "{0:4} {1:<20} {2:9} {3:27} {4:6} {5:7} {6:6} {7:5} {8:2} {9:1} {10:3} {11:2} {12:4} {13:21}".format(
            systemDict["system hex"],
            systemDict["name"],
            SubsectorGenerator.displayUwpCode(systemDict),
            remarks[:16],
            "{  }",
            "(  )",
            "[ ]",
            systemDict.get("system noble leader", ""),
            systemDict["primary starport types highest"],
            systemDict["system travel code"], # ZONE: - A R
            "{}{}{}".format(systemDict["system population modifier"],systemDict["system asteroid belts"],systemDict["system gas giants"]),
            systemDict["system populated worlds"],
            systemDict.get("system alignment", "Im"),
            systemDict["system star"].getStellarCode(),
            )
    @staticmethod
    def getT5SystemCode(system):
        remarks = ""
        for tradeCode in system.tradeCodes:
            remarks += "{} ".format(tradeCode)
        return "{0:4} {1:<20} {2:9} {3:27} {4:6} {5:7} {6:6} {7:5} {8:2} {9:1} {10:3} {11:2} {12:4} {13:21}".format(
            system.hexCoord,
            str(system.name),
            system.displayUwpCode(),
            remarks[:16],
            "{  }",
            "(  )",
            "[ ]",
            system.nobleLeader,
            system.primaryPlanet.portsTypesHighest,
            system.travelCode, # ZONE: - A R
            "{}{}{}".format( system.populationModifier, system.planetoidBelts, system.gasGiants),
            system.populatedWorlds,
            "Im",
            system.star.getStellarCode()
            )
    @staticmethod
    def getTraderSystemCode(system):
        remarks = ""
        for tradeCode in system["system trade codes"]:
            remarks += "{} ".format(tradeCode)
        #Vittalikii    2534 B953101-A    Lo Po           A  224 Im# 
        return "{0:<14}{1:<4} {2:<9} {3:<1} {4:<14} {5:1} {6:<3}    ".format(
            system["name"],
            system["system hex"],
            SubsectorGenerator.displayUppCode(system),
            system["primary starport types highest"],
            remarks[:14],
            "Im",
            "A", # ZONE: - A R
            )
    @staticmethod
    def displayUwpStats(uwp):
        uwp = uwp.replace("-","")
        hex_key=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        print("")
        print("Primary Planet UWP")
        print("Primary Size: {} - {}".format(uwp[1], 
            DescriptionGenerator.getSizeDescription(Utils.hex_key.index(uwp[1]))))
        print("Primary Atmosphere: {} - {}".format(uwp[2], 
            DescriptionGenerator.getAtmosphereDescription(Utils.hex_key.index(uwp[2]))))
        print("Primary Hydrographics: {} - {}".format(uwp[3], 
            DescriptionGenerator.getHydrographicsDescription(Utils.hex_key.index(uwp[3]))))
        print("")
        print("Primary Population: {} - {} - x{}".format(
            uwp[4], 
            DescriptionGenerator.getPopulationDescription(  max(0,min(15,hex_key.index(uwp[4])))  ), 
            "-"))
        print("Primary Government: {} - {}".format(uwp[5], 
            DescriptionGenerator.getGovernmentDescription(Utils.hex_key.index(uwp[5]))))
        print("Primary Law Level: {} - {}".format(uwp[6], 
            DescriptionGenerator.getLawLevelDescription(Utils.hex_key.index(uwp[6]))))
        print("Primary Tech Level: {} - {}".format(uwp[7], 
            DescriptionGenerator.getTechLevelDescription(Utils.hex_key.index(uwp[7]))))
        print("")
        print("Primary Starport: {} - {}".format(uwp[0], 
            DescriptionGenerator.getStarportDescription(uwp[0])))
        print("")
    @staticmethod
    def displaySystemStats(system):
        hex_key=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        print("")
        print("System Name: {}".format(system["system name"]))
        print("System HEX: {}".format(system["system hex"]))
        print("System Travel Code: {}".format(system["system travel code"]))
        print("Gas Giant      #: {}".format(system["system gas giants"]))
        print("Asteroid Belts #: {}".format(system["system asteroid belts"]))
        print("")
        print("Primary Planet")
        print("Primary Size: {} - {}".format(Utils.hex_key[system["primary size"]], 
            DescriptionGenerator.getSizeDescription(system["primary size"])))
        print("Primary Atmosphere: {} - {}".format(Utils.hex_key[system["primary atmosphere"]], 
            DescriptionGenerator.getAtmosphereDescription(system["primary atmosphere"])))
        print("Primary Temp: {} - {}".format(system["primary temperature"], 
            DescriptionGenerator.getTemperatureDescription(system["primary temperature"])))
        print("Primary Hydrographics: {} - {}".format(Utils.hex_key[system["primary hydrographics"]], 
            DescriptionGenerator.getHydrographicsDescription(system["primary hydrographics"])))
        print("")
        print("Primary Population: {} - {} - x{}".format(Utils.hex_key[system["primary population"]], 
            DescriptionGenerator.getPopulationDescription(system["primary population"]), 
            system["system population modifier"]))
        print("Primary Government: {} - {}".format(Utils.hex_key[system["primary government"]], 
            DescriptionGenerator.getGovernmentDescription(system["primary government"])))
        print("Primary Law Level: {} - {}".format(Utils.hex_key[system["primary law level"]], 
            DescriptionGenerator.getLawLevelDescription(system["primary law level"])))
        print("Primary Tech Level: {} - {}".format(system["primary tech level"], 
            DescriptionGenerator.getTechLevelDescription(system["primary tech level"])))
        print("")
        print("Primary Starport: {} - {}".format(SubsectorGenerator.getStarportClass(system["primary starport"]), 
            DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(system["primary starport"]))))
        starports = ""
        for port in system["primary starport types"]:
            starports += "{}, ".format(port)
        starports = starports[:-2]
        print("Starports: [{}] {} - {}".format(system["primary starport types roll"], system["primary starport types highest"], starports))
        print("")
        print("System Trade Codes: ")
        for tradeCode in system["system trade codes"]:
            print("{} - {}".format(tradeCode, SubsectorGenerator.getGetFullTradeCodes(tradeCode)))
        print("")
    @staticmethod
    def hexTransform(systemIndex):
        sectorWidth = 10*4
        sectorHeight = 10*4
        hexCoord = "{0}{1}{2}{3}".format(
            "0" if (systemIndex // sectorWidth)+1 < 10 else "",
            (systemIndex // sectorWidth)+1,
            "0" if (systemIndex % sectorHeight)+1 < 10 else "",
            (systemIndex % sectorHeight)+1
            )
        if(int(hexCoord) <= 3240):
            return hexCoord
        return None
    @staticmethod
    def getSubsectorFromHexCoord(hexCoord):
        # print(hexCoord)
        hexInt = int(hexCoord)
        # print(hexInt)
        # print(hexInt)
        subsectorLetter = "A"
        if (hexInt >= 901 and hexInt <= 910 or hexInt >= 1001 and hexInt <= 1010 or 
            hexInt >= 1101 and hexInt <= 1110 or hexInt >= 1201 and hexInt <= 1210 or 
            hexInt >= 1301 and hexInt <= 1310 or hexInt >= 1401 and hexInt <= 1410 or 
            hexInt >= 1501 and hexInt <= 1510 or hexInt >= 1601 and hexInt <= 1610): subsectorLetter = "B"
        elif (hexInt >= 1701 and hexInt <= 1710 or hexInt >= 1801 and hexInt <= 1810 or 
            hexInt >= 1901 and hexInt <= 1910 or hexInt >= 2001 and hexInt <= 2010 or 
            hexInt >= 2101 and hexInt <= 2110 or hexInt >= 2201 and hexInt <= 2210 or 
            hexInt >= 2301 and hexInt <= 2310 or hexInt >= 2401 and hexInt <= 2410): subsectorLetter = "C"
        elif (hexInt >= 2501 and hexInt <= 2510 or hexInt >= 2601 and hexInt <= 2610 or 
            hexInt >= 2701 and hexInt <= 2710 or hexInt >= 2801 and hexInt <= 2810 or 
            hexInt >= 2901 and hexInt <= 2910 or hexInt >= 3001 and hexInt <= 3010 or 
            hexInt >= 3101 and hexInt <= 3110 or hexInt >= 3201 and hexInt <= 3210 ): subsectorLetter = "D"
        
        elif (hexInt >= 111 and hexInt <= 120 or hexInt >= 211 and hexInt <= 220 or 
            hexInt >= 311 and hexInt <= 320 or hexInt >= 411 and hexInt <= 420 or 
            hexInt >= 511 and hexInt <= 520 or hexInt >= 611 and hexInt <= 620 or 
            hexInt >= 711 and hexInt <= 720 or hexInt >= 811 and hexInt <= 820): subsectorLetter = "E"
        elif (hexInt >= 911 and hexInt <= 920 or hexInt >= 1011 and hexInt <= 1010 or 
            hexInt >= 1111 and hexInt <= 1120 or hexInt >= 1211 and hexInt <= 1220 or 
            hexInt >= 1311 and hexInt <= 1320 or hexInt >= 1411 and hexInt <= 1420 or 
            hexInt >= 1511 and hexInt <= 1520 or hexInt >= 1611 and hexInt <= 1620): subsectorLetter = "F"
        elif (hexInt >= 1711 and hexInt <= 1720 or hexInt >= 1811 and hexInt <= 1820 or 
            hexInt >= 1911 and hexInt <= 1920 or hexInt >= 2011 and hexInt <= 2020 or 
            hexInt >= 2111 and hexInt <= 2120 or hexInt >= 2211 and hexInt <= 2220 or 
            hexInt >= 2311 and hexInt <= 2320 or hexInt >= 2411 and hexInt <= 2420): subsectorLetter = "G"
        elif (hexInt >= 2511 and hexInt <= 2520 or hexInt >= 2611 and hexInt <= 2620 or 
            hexInt >= 2711 and hexInt <= 2720 or hexInt >= 2811 and hexInt <= 2820 or 
            hexInt >= 2911 and hexInt <= 2920 or hexInt >= 3011 and hexInt <= 3020 or 
            hexInt >= 3111 and hexInt <= 3120 or hexInt >= 3211 and hexInt <= 3220 ): subsectorLetter = "H"
        
        elif (hexInt >= 121 and hexInt <= 130 or hexInt >= 221 and hexInt <= 230 or 
            hexInt >= 321 and hexInt <= 330 or hexInt >= 421 and hexInt <= 430 or 
            hexInt >= 521 and hexInt <= 530 or hexInt >= 621 and hexInt <= 630 or 
            hexInt >= 721 and hexInt <= 730 or hexInt >= 821 and hexInt <= 820): subsectorLetter = "I"
        elif (hexInt >= 921 and hexInt <= 930 or hexInt >= 1021 and hexInt <= 1030 or 
            hexInt >= 1121 and hexInt <= 1130 or hexInt >= 1221 and hexInt <= 1230 or 
            hexInt >= 1321 and hexInt <= 1330 or hexInt >= 1421 and hexInt <= 1430 or 
            hexInt >= 1521 and hexInt <= 1530 or hexInt >= 1621 and hexInt <= 1630 ): subsectorLetter = "J"
        elif (hexInt >= 1721 and hexInt <= 1730 or hexInt >= 1821 and hexInt <= 1830 or 
            hexInt >= 1921 and hexInt <= 1930 or hexInt >= 2021 and hexInt <= 2030 or 
            hexInt >= 2121 and hexInt <= 2130 or hexInt >= 2221 and hexInt <= 2230 or 
            hexInt >= 2321 and hexInt <= 2330 or hexInt >= 2421 and hexInt <= 2430 ): subsectorLetter = "K"
        elif (hexInt >= 2521 and hexInt <= 2530 or hexInt >= 2621 and hexInt <= 2630 or 
            hexInt >= 2721 and hexInt <= 2730 or hexInt >= 2821 and hexInt <= 2830 or 
            hexInt >= 2921 and hexInt <= 2930 or hexInt >= 3021 and hexInt <= 3030 or 
            hexInt >= 3121 and hexInt <= 3130 or hexInt >= 3221 and hexInt <= 3230 ): subsectorLetter = "L"
        
        elif (hexInt >= 131 and hexInt <= 140 or hexInt >= 231 and hexInt <= 240 or 
            hexInt >= 331 and hexInt <= 340 or hexInt >= 431 and hexInt <= 440 or 
            hexInt >= 531 and hexInt <= 540 or hexInt >= 631 and hexInt <= 640 or 
            hexInt >= 731 and hexInt <= 740 or hexInt >= 831 and hexInt <= 840 ): subsectorLetter = "M"
        elif (hexInt >= 931 and hexInt <= 940 or hexInt >= 1031 and hexInt <= 1040 or 
            hexInt >= 1131 and hexInt <= 1140 or hexInt >= 1231 and hexInt <= 1240 or 
            hexInt >= 1331 and hexInt <= 1340 or hexInt >= 1431 and hexInt <= 1440 or 
            hexInt >= 1531 and hexInt <= 1540 or hexInt >= 1631 and hexInt <= 1640 ): subsectorLetter = "N"
        elif (hexInt >= 1731 and hexInt <= 1740 or hexInt >= 1831 and hexInt <= 1840 or 
            hexInt >= 1931 and hexInt <= 1940 or hexInt >= 2031 and hexInt <= 2040 or 
            hexInt >= 2131 and hexInt <= 2140 or hexInt >= 2231 and hexInt <= 2240 or 
            hexInt >= 2331 and hexInt <= 2340 or hexInt >= 2431 and hexInt <= 2440 ): subsectorLetter = "O"
        elif (hexInt >= 2531 and hexInt <= 2540 or hexInt >= 2631 and hexInt <= 2640 or 
            hexInt >= 2731 and hexInt <= 2740 or hexInt >= 2831 and hexInt <= 2840 or 
            hexInt >= 2931 and hexInt <= 2940 or hexInt >= 3031 and hexInt <= 3040 or 
            hexInt >= 3131 and hexInt <= 3140 or hexInt >= 3231 and hexInt <= 3240 ): subsectorLetter = "P"
        # print(subsectorLetter)
        # input("Press Enter")
        return subsectorLetter
    @staticmethod
    def generateSubsector(rand_seed, name, verbose):
        if rand_seed:
            random.seed(rand_seed)
        subsector = Subsector("<Sector>", name)
        i = 0
        sectorSize=3240
        systemCodeList = []
        # for i in range(sectorSize):
        system = SubsectorGenerator.generateLocalSystem( "System-{}".format(str(i+1)), SubsectorGenerator.hexTransform(i))
        if (system is None):
            print("System was NONE. probably due too bad HEX coord")
        else:
            if verbose: print("System created")
        # systemCodeList.append(SubsectorGenerator.getGenieSunbaneSystemCode(system))

        
        SubsectorGenerator.displaySystemStats(system)
        if verbose: print("")
        if verbose: print(SubsectorGenerator.getGenieSunbaneSystemCode(system))
        # if (system is not None):
        #     subsector.addSystem(system.getSystemCode(), system)
    @staticmethod
    def createFileHeader(systemCodeList, sector):
        systemCodeList.append("# <TIMESTAMP>")
        systemCodeList.append("")
        systemCodeList.append("# {}".format(sector.name))
        systemCodeList.append("# {},{} (Spacial Grid)".format("XXX","YYY"))
        systemCodeList.append("")
        systemCodeList.append("# Name: {}".format(sector.name))
        systemCodeList.append("")
        systemCodeList.append("# Abbreviation: {}".format(sector.name[:4]))
        systemCodeList.append("")
        systemCodeList.append("# {}: {}".format("", ""))
        systemCodeList.append("")
        systemCodeList.append("# Credits: {}".format("Stefan DeWolfe"))
        systemCodeList.append("")
        systemCodeList.append("# Subsector A: {}".format(sector.subsectors["a"].name ))
        systemCodeList.append("# Subsector B: {}".format(sector.subsectors["b"].name ))
        systemCodeList.append("# Subsector C: {}".format(sector.subsectors["c"].name ))
        systemCodeList.append("# Subsector D: {}".format(sector.subsectors["d"].name ))
        systemCodeList.append("# Subsector E: {}".format(sector.subsectors["e"].name ))
        systemCodeList.append("# Subsector F: {}".format(sector.subsectors["f"].name ))
        systemCodeList.append("# Subsector G: {}".format(sector.subsectors["g"].name ))
        systemCodeList.append("# Subsector H: {}".format(sector.subsectors["h"].name ))
        systemCodeList.append("# Subsector I: {}".format(sector.subsectors["i"].name ))
        systemCodeList.append("# Subsector J: {}".format(sector.subsectors["j"].name ))
        systemCodeList.append("# Subsector K: {}".format(sector.subsectors["k"].name ))
        systemCodeList.append("# Subsector L: {}".format(sector.subsectors["l"].name ))
        systemCodeList.append("# Subsector M: {}".format(sector.subsectors["m"].name ))
        systemCodeList.append("# Subsector N: {}".format(sector.subsectors["n"].name ))
        systemCodeList.append("# Subsector O: {}".format(sector.subsectors["o"].name ))
        systemCodeList.append("# Subsector P: {}".format(sector.subsectors["p"].name ))
        systemCodeList.append("")
        politicalPowers = [("Im", "3rd Imperium"), ("NaHu", "Non-Aligned, Human-dominated"), ("NaXX", "Non-Aligned, unclaimed")]
        for politicalPower in politicalPowers:
            systemCodeList.append("# Alleg: {}: \"{}\"".format(politicalPower[0], politicalPower[1]))
        systemCodeList.append("Hex  Name                 UWP       Remarks                     {Ix}   (Ex)    [Cx]   N     B  Z PBG W  A    Stellar              ")
        systemCodeList.append("---- -------------------- --------- --------------------------- ------ ------- ------ ----- -- - --- -- ---- ---------------------")
    @staticmethod
    def createXmlFile(systemXmlData, sector):
        colors = ["Maroon", "Red", "Orange", "Yellow", "Green", "Cyan", "Blue", "Indigo", "Purple", "Violet"]
        systemXmlData.append("<?xml version=\"1.0\"?>")
        systemXmlData.append("<Sector xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" "
            + "xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" Selected=\"true\" Tags=\"InReview OTU\" "
            + "Abbreviation=\"{}\">".format(
            sector.name[:4]
            ))
        systemXmlData.append("  <Name Lang=\"as\">{}</Name>")
        systemXmlData.append("  <Credits>")
        systemXmlData.append("             &lt;b&gt;{}&lt;/b&gt; sector was designed by a random engine by Stefan DeWolfe")
        systemXmlData.append("             with further refinement by Stefan DeWolfe.")
        systemXmlData.append("    </Credits>")
        systemXmlData.append("  <X>{}</X>".format(0))
        systemXmlData.append("  <Y>{}</Y>".format(0))
        systemXmlData.append("  <Product Author=\"Stefan DeWolfe\" Title=\"\" Publisher=\"Stefan DeWolfe\" Ref=\"https://www.mongoosepublishing.com\" />")
        systemXmlData.append("  <DataFile Source=\"{}\" Milieu=\"{}\" Ref=\"{}\" />".format("SubsectorGenerator", "101", "-None-"))
        systemXmlData.append("  <Subsectors>")
        systemXmlData.append("    <Subsector Index=\"A\">{}</Subsector>".format(sector.subsectors["a"].name ))
        systemXmlData.append("    <Subsector Index=\"B\">{}</Subsector>".format(sector.subsectors["b"].name ))
        systemXmlData.append("    <Subsector Index=\"C\">{}</Subsector>".format(sector.subsectors["c"].name ))
        systemXmlData.append("    <Subsector Index=\"D\">{}</Subsector>".format(sector.subsectors["d"].name ))
        systemXmlData.append("    <Subsector Index=\"E\">{}</Subsector>".format(sector.subsectors["e"].name ))
        systemXmlData.append("    <Subsector Index=\"F\">{}</Subsector>".format(sector.subsectors["f"].name ))
        systemXmlData.append("    <Subsector Index=\"G\">{}</Subsector>".format(sector.subsectors["g"].name ))
        systemXmlData.append("    <Subsector Index=\"H\">{}</Subsector>".format(sector.subsectors["h"].name ))
        systemXmlData.append("    <Subsector Index=\"I\">{}</Subsector>".format(sector.subsectors["i"].name ))
        systemXmlData.append("    <Subsector Index=\"J\">{}</Subsector>".format(sector.subsectors["j"].name ))
        systemXmlData.append("    <Subsector Index=\"K\">{}</Subsector>".format(sector.subsectors["k"].name ))
        systemXmlData.append("    <Subsector Index=\"L\">{}</Subsector>".format(sector.subsectors["l"].name ))
        systemXmlData.append("    <Subsector Index=\"M\">{}</Subsector>".format(sector.subsectors["m"].name ))
        systemXmlData.append("    <Subsector Index=\"N\">{}</Subsector>".format(sector.subsectors["n"].name ))
        systemXmlData.append("    <Subsector Index=\"O\">{}</Subsector>".format(sector.subsectors["o"].name ))
        systemXmlData.append("    <Subsector Index=\"P\">{}</Subsector>".format(sector.subsectors["p"].name ))
        systemXmlData.append("  </Subsectors>")
        systemXmlData.append("  <Allegiances>")
        # systemXmlData.append("    <Allegiance Code=\"{}\" Base=\"{}\">{}</Allegiance>".format("NaXX", "Na", "Non-Aligned, unclaimed"))
            # <Allegiance Code="NaXX" Base="Na">Non-Aligned, unclaimed</Allegiance>
            # <Allegiance Code="AsTv" Base="As">Aslan Hierate, Tlaukhu vassal clan dominates</Allegiance>
            # <Allegiance Code="AsT1" Base="As">Aslan Hierate, Tlaukhu control, Khauleairl (2), Estoieie' (16), Toaseilwi (22)</Allegiance>
            # <Allegiance Code="AsMw" Base="As">Aslan Hierate, single multiple-world clan dominates</Allegiance>
            # <Allegiance Code="AsSc" Base="As">Aslan Hierate, multiple clans split control</Allegiance>
            # <Allegiance Code="AsVc" Base="As">Aslan Hierate, vassal clan dominates</Allegiance>
            # <Allegiance Code="AsT9" Base="As">Aslan Hierate, Tlaukhu control, Aokhalte (10), Sahao' (21), Ouokhoi (26)</Allegiance>
            # <Allegiance Code="AsWc" Base="As">Aslan Hierate, single one-world clan dominates</Allegiance>
            # <Allegiance Code="AsT2" Base="As">Aslan Hierate, Tlaukhu control, Syoisuis (3)</Allegiance>
            # <Allegiance Code="AsT3" Base="As">Aslan Hierate, Tlaukhu control, Tralyeaeawi (4), Yulraleh (12), Aiheilar (25), Riyhalaei (28)</Allegiance>
            # <Allegiance Code="AsT0" Base="As">Aslan Hierate, Tlaukhu control, Yerlyaruiwo (1), Hrawoao (13), Eisohiyw (14), Ferekhearl (19)</Allegiance>
            # <Allegiance Code="AsT5" Base="As">Aslan Hierate, Tlaukhu control, Hlyueawi (6), Isoitiyro (15)</Allegiance>
            # <Allegiance Code="AsT8" Base="As">Aslan Hierate, Tlaukhu control, Seieakh (9), Akatoiloh (18), We'okunir (29)</Allegiance>
            # <Allegiance Code="AsXX" Base="As">Aslan Hierate, unknown</Allegiance>
            # <Allegiance Code="AsT7" Base="As">Aslan Hierate, Tlaukhu control, Ikhtealyo (8), Tlerfearlyo (20), Yehtahikh (24)</Allegiance>
            # <Allegiance Code="AsT6" Base="As">Aslan Hierate, Tlaukhu control, Uiktawa (7), Iykyasea (17), Faowaou (27)</Allegiance>
            # <Allegiance Code="AsTz" Base="As">Aslan Hierate, Zodia clan</Allegiance>
            # <Allegiance Code="AsT4" Base="As">Aslan Hierate, Tlaukhu control, Eakhtiyho (5), Eteawyolei' (11), Fteweyeakh (23)</Allegiance>
        systemXmlData.append("  </Allegiances>")
        systemXmlData.append("  <Borders>")

        # systemXmlData.append("  <Border Allegiance=\"{}\" LabelPosition=\"{}\">".format()
        #      + "0031 0131 0230 0331 0430 0530 0629 0729 0728 0828 0928 1027 1128 1228 1329 1428 1528 1628 1728 "
        #      + "1827 1928 2027 2127 2226 2326 2425 2525 2524 2624 2724 2823 2923 3022 3122 3121 3120 3119 3218 "
        #      + "3217 3216 3316 3317 3318 3319 3320 3321 3322 3323 3324 3325 3326 3327 3328 3329 3330 3331 3332 "
        #      + "3333 3334 3335 3336 3337 3338 3339 3340 3341 3241 3141 3041 2941 2841 2741 2641 2541 2441 2341 "
        #      + "2241 2141 2041 1941 1841 1741 1641 1541 1441 1341 1241 1141 1041 0941 0841 0741 0641 0541 0441 "
        #      + "0341 0241 0141 0041 0040 0039 0038 0037 0036 0035 0034 0033 0032 0031</Border>".format())
        systemXmlData.append("  </Borders>")
        systemXmlData.append("  <Regions>")
        # already_claimed = []
        # for hexCoord in sector.systems.keys():
        #     starSystem = sector.systems[hexCoord]
        #     if SubsectorGenerator.is_earthlike_cradle_of_civ(starSystem) and hexCoord not in already_claimed:
        #         print("Found earthlike cradle for Civilization: {} {} {}".format(hexCoord, starSystem.name, starSystem.uwp))
        #         color = random.choice(colors)
        #         region_text = "      <Region Color=\"{}\" LabelPosition=\"{}\" Label=\"{}\">".format(color, hexCoord, starSystem.name)
        #         already_present = []
        #         hexes = SubsectorGenerator.getNeighboringSystems(hexCoord, sector, already_claimed) + [hexCoord]
        #         hexes.sort()
        #         for neighbor in hexes:
        #             if neighbor not in already_present:
        #                 region_text += neighbor + " "
        #                 already_present.append(neighbor)
        #                 already_claimed.append(neighbor)
        #         region_text = region_text[:-1]
        #         region_text += "</Region><!-- -->"
        #         systemXmlData.append(region_text) 
        #     elif SubsectorGenerator.is_earthlike_cradle_of_civ(starSystem) and hexCoord in already_claimed:
        #         print("This Hex {} has already been claimed".format(hexCoord))

        # systemXmlData.append("      <Region Color=\"{}\" LabelPosition=\"{}\" Label=\"{}\">".format("Indigo", "0308", "Rinean Shoal")
        #     +"0110 0209 0309 0308 0407 0406 0405 0506 0507 0407 0408 0309 0310 0210 0110</Region>".format())
        systemXmlData.append("  </Regions>")
        systemXmlData.append("  <Routes>")
            # <Route Start="3219" End="0117" EndOffsetX="1" Allegiance="As" />
            # <Route Start="1340" End="1040" Allegiance="As" />
        systemXmlData.append("  </Routes>")
        systemXmlData.append("</Sector>")
    @staticmethod
    def writeSectorToFile(sector):
        print("Writing to File: \"{}\"".format("{}-Sector.pickle".format(sector.name)))
        pickle.dump( sector, open( "{}-Sector.pickle".format(sector.name), "wb" ) )
    @staticmethod
    def writeSectorTextFile(sector):
        print("Writing to File: \"{}\"".format("{}-Sector.txt".format(sector.name)))
        systemCodeList = []
        SubsectorGenerator.createFileHeader(systemCodeList, sector)
        for hexcoord in sector.systems.keys():
            systemCodeList.append(SubsectorGenerator.getT5FormatSystemCode(sector.systems[hexcoord].systemDict))
        with open("{}-Sector.txt".format(sector.name), 'w') as f:
            for item in systemCodeList:
                f.write("%s\n" % item)
    @staticmethod
    def writeSectorXmlFile(sector):
        print("Writing to File: \"{}\"".format("{}-Sector.xml".format(sector.name)))
        systemXmlData = []
        SubsectorGenerator.createXmlFile(systemXmlData, sector)
        with open("{}-Sector.xml".format(sector.name), 'w') as f:
            for item in systemXmlData:
                f.write("%s\n" % item)
    @staticmethod
    def generateFullSector(rand_seed, sectorName, density, sprinkle_in_earthlikes, verbose=False, 
        # naming_type="sw"
        naming_type="traveller"
        ):
        if rand_seed:
            random.seed(rand_seed)

        sector = Sector(sectorName, rand_seed)

        namesLines = PseudoMarkovNameGenerator.readLinesFromFile("surnames.txt")
        used_names = []
        for letter in sector.subsectors.keys():
            if verbose: print(letter)
            name = PseudoMarkovNameGenerator.getName(namesLines)

            subsector = Subsector(name, sector, letter)
            sector.addSubsector(letter, subsector)
        i = 0
        sectorSize=3240
        systemCodeList = []
        SubsectorGenerator.createFileHeader(systemCodeList, sector)
        densityModifier = 4# Standard
        if density.lower() in ["all"]:
            densityModifier = 1
        elif density.lower() in ["super-dense"]:
            densityModifier = 2
        elif density.lower() in ["dense"]:
            densityModifier = 3
        elif density.lower() in ["sparce"]:
            densityModifier = 5
        elif density.lower() in ["rift"]:
            densityModifier = 6
        
        for i in range(sectorSize):
            if verbose: print(i)
            hexCoord = SubsectorGenerator.hexTransform(i)
            if verbose:  print(hexCoord)
            if (hexCoord is not None):
                currentSubsector = SubsectorGenerator.getSubsectorFromHexCoord(hexCoord)
                if (random.randint(1,6) >= densityModifier):
                    name = None
                    while not name or name in used_names:
                        if naming_type.lower() in ["star wars", "starwars", "star-wars", "sw"]:
                            name = StarWarsPlanetNameGenerator.getName()
                        else:
                            name = PseudoMarkovNameGenerator.getName(namesLines)
                    used_names.append(name)
                    must_be_earthlike = random.randint(1, 20) == 20
                    if must_be_earthlike: 
                        print("Forcing an Earthlike at {}".format(hexCoord))

                    systemDict = SubsectorGenerator.generateLocalSystem(name, hexCoord, must_be_earthlike, verbose)
                    
                    starSystem =  StarSystem(systemDict)
                    starSystem.subsectorParent = currentSubsector.lower()
                    
                    if (systemDict is not None):
                        sector.subsectors[currentSubsector.lower()].addSystem(hexCoord, starSystem)
                        sector.addSystem(starSystem)
                    else:
                        if verbose: print("System Dictionary was NONE. probably due too bad HEX coord")
                else:
                    if verbose: print("No system in this Hex: {}".format(hexCoord))

        SubsectorGenerator.writeSectorTextFile(sector)
        SubsectorGenerator.writeSectorXmlFile(sector)
        SubsectorGenerator.writeSectorToFile(sector)
    @staticmethod
    def is_earthlike_cradle_of_civ(starSystem):
        return ( 
            starSystem.primaryPlanet.size in [7, 8, 9] and 
            starSystem.primaryPlanet.atmosphere in [5, 6, 7, 8] and # could add 4, 9
            starSystem.primaryPlanet.techLevel >= 8
            )
    @staticmethod
    def getHumanHabitableSystems(sector, verbose=False):
        print('''Humans prefer: 
        Size: 6-9      - 0.7g to 1.25g
        Atmo: 5, 6, 7, - thin-standard-dense
        Hydro: 3-9     - 26% to 95% water
        first establisted areas are starport A, highest Text
        Starport|Size|Atmo|Hydro|Pop|Gov|Law - Tech 
        Highest|6-9|5, 6, 7|3-9|Highest|Varies|Varies - Highest''')
        systems = []
        for systemHexCoord in sector.systems.keys():
            if(verbose): print(systemHexCoord)
            system = sector.systems[systemHexCoord]
            uwp = system.displayUwpCode()
            if(uwp[1] in ["6", "7", "8", "9"] 
                and uwp[2] in ["6", "8", "5"] 
                and uwp[3] in ["3", "4", "5", "6", "7", "8", "9"]
                and uwp[4] not in ["0", "1", "2", "3", "4", "5", "6"]
                and system.primaryPlanet.temperature in ["5", "6", "7", "8", "9"]
                ):
                systems.append(system)
            else:
                if(verbose): print("    Fail Size, Atmo, Hydro, Pop, or Temp")
        if len(systems) < 1:
            print("No optimal Human Systems")
        else:
            for system in systems:
                print(SubsectorGenerator.getT5FormatSystemCode(system.systemDict)[:-1])
        return systems
    @staticmethod
    def getCloseToHumanHabitableSystems(sector, verbose=False):
        ''' Humans prefer: 
                Size: 6-9      - 0.7g to 1.25g
                Atmo: 5, 6, 7, - thin-standard-dense
                Hydro: 3-9     - 26% to 95% water
                first establisted areas are starport A, highest Text
            Starport|Size|Atmo|Hydro|Pop|Gov|Law - Tech 
            Highest|6-9|5, 6, 7|3-9|Highest|Varies|Varies - Highest 
            '''
        systems = []
        for systemHexCoord in sector.systems.keys():
            if(verbose): print(systemHexCoord)
            system = sector.systems[systemHexCoord]
            uwp = system.displayUwpCode()
            if(uwp[1] in ["6", "7", "8", "9"] 
                and uwp[2] in ["6", "7", "5"] 
                and uwp[3] in ["3", "4", "5", "6", "7", "8", "9"]
                and uwp[4] not in ["0", "1", "2", "3", "4", "5", "6"]
                # and system.primaryPlanet.temperature in ["5", "6", "7", "8", "9"]
                ):
                systems.append(system)
            else:
                if(verbose): print("    Fail Size, Atmo, Hydro, Pop, or Temp")
        if len(systems) < 1:
            print("No Suboptimal Human Systems")
        else:
            for system in systems:
                print(SubsectorGenerator.getT5FormatSystemCode(system.systemDict)[:-1])
        return systems
    @staticmethod
    def getHotAlienHabitableSystems(sector, verbose=False):
        systems = []
        for systemHexCoord in sector.systems.keys():
            if(verbose): print(systemHexCoord)
            system = sector.systems[systemHexCoord]
            uwp = system.displayUwpCode()
            if(uwp[1] in ["6", "7", "8", "9"] 
                and uwp[2] in ["6", "7", "5"] 
                and uwp[3] in ["3", "4", "5", "6", "7", "8", "9"]
                and uwp[4] not in ["0", "1", "2", "3", "4", "5", "6"]
                and system.primaryPlanet.temperature in ["10", "11", "12"]
                ):
                systems.append(system)
            else:
                if(verbose): print("    Fail Size, Atmo, Hydro, Pop, or Temp")
        if len(systems) < 1:
            print("No optimal Hot Alien Systems")
        else:
            for system in humanPreferedSystems:
                print(SubsectorGenerator.getT5FormatSystemCode(system.systemDict)[:-1])
        return systems
    @staticmethod
    def getColdAlienHabitableSystems(sector, verbose=False):
        systems = []
        for systemHexCoord in sector.systems.keys():
            if(verbose): print(systemHexCoord)
            system = sector.systems[systemHexCoord]
            uwp = system.displayUwpCode()
            if(uwp[1] in ["6", "7", "8", "9"] 
                and uwp[2] in ["6", "7", "5"] 
                and uwp[3] in ["3", "4", "5", "6", "7", "8", "9"]
                and uwp[4] not in ["0", "1", "2", "3", "4", "5", "6"]
                and system.primaryPlanet.temperature in ["0", "1", "2", "3", "4"]
                ):
                systems.append(system)
            else:
                if(verbose): print("    Fail Size, Atmo, Hydro, Pop, or Temp")
        if len(systems) < 1:
            print("No optimal Hot Alien Systems")
        else:
            for system in humanPreferedSystems:
                print(SubsectorGenerator.getT5FormatSystemCode(system.systemDict)[:-1])
        return systems
    @staticmethod
    def getUninhabittedSystems(sector, verbose=False):
        systems = []
        for systemHexCoord in sector.systems.keys():
            if(verbose): print(systemHexCoord)
            system = sector.systems[systemHexCoord]
            uwp = system.displayUwpCode()
            if(uwp[4] not in ["0"]
                ):
                systems.append(system)
            else:
                if(verbose): print("    Fail Size, Atmo, Hydro, Pop, or Temp")
        if len(humanPreferedSystems) < 1:
            print("No unpopulated Systems")
        else:
            for system in humanPreferedSystems:
                print(SubsectorGenerator.getT5FormatSystemCode(system.systemDict)[:-1])
        return systems
class XmlModifierForSector():
    @staticmethod
    def alterXmlForSector(sector, verbose=False):
        pass   
class SectorViewer():
    def __init__(self, sector):
        self.sector = sector
    def getSubsectorFromHexCoord(self, hexCoord):
        hexInt = int(hexCoord)
        hexInt = int(hexInt/100)
        subsectorLetter = "A"
        if (hexInt >= 901 and hexInt <= 910 or hexInt >= 1001 and hexInt <= 1010 or 
            hexInt >= 1101 and hexInt <= 1110 or hexInt >= 1201 and hexInt <= 1210 or 
            hexInt >= 1301 and hexInt <= 1310 or hexInt >= 1401 and hexInt <= 1410 or 
            hexInt >= 1501 and hexInt <= 1510 or hexInt >= 1601 and hexInt <= 1610): subsectorLetter = "B"
        elif (hexInt >= 1701 and hexInt <= 1710 or hexInt >= 1801 and hexInt <= 1810 or 
            hexInt >= 1901 and hexInt <= 1910 or hexInt >= 2001 and hexInt <= 2010 or 
            hexInt >= 2101 and hexInt <= 2110 or hexInt >= 2201 and hexInt <= 2210 or 
            hexInt >= 2301 and hexInt <= 2310 or hexInt >= 2401 and hexInt <= 2410): subsectorLetter = "C"
        elif (hexInt >= 2501 and hexInt <= 2510 or hexInt >= 2601 and hexInt <= 2610 or 
            hexInt >= 2701 and hexInt <= 2710 or hexInt >= 2801 and hexInt <= 2810 or 
            hexInt >= 2901 and hexInt <= 2910 or hexInt >= 3001 and hexInt <= 3010 or 
            hexInt >= 3101 and hexInt <= 3110 or hexInt >= 3201 and hexInt <= 3210 ): subsectorLetter = "D"
        
        elif (hexInt >= 111 and hexInt <= 120 or hexInt >= 211 and hexInt <= 220 or 
            hexInt >= 311 and hexInt <= 320 or hexInt >= 411 and hexInt <= 420 or 
            hexInt >= 511 and hexInt <= 520 or hexInt >= 611 and hexInt <= 620 or 
            hexInt >= 711 and hexInt <= 720 or hexInt >= 811 and hexInt <= 820): subsectorLetter = "E"
        elif (hexInt >= 911 and hexInt <= 920 or hexInt >= 1011 and hexInt <= 1010 or 
            hexInt >= 1111 and hexInt <= 1120 or hexInt >= 1211 and hexInt <= 1220 or 
            hexInt >= 1311 and hexInt <= 1320 or hexInt >= 1411 and hexInt <= 1420 or 
            hexInt >= 1511 and hexInt <= 1520 or hexInt >= 1611 and hexInt <= 1620): subsectorLetter = "F"
        elif (hexInt >= 1711 and hexInt <= 1720 or hexInt >= 1811 and hexInt <= 1820 or 
            hexInt >= 1911 and hexInt <= 1920 or hexInt >= 2011 and hexInt <= 2020 or 
            hexInt >= 2111 and hexInt <= 2120 or hexInt >= 2211 and hexInt <= 2220 or 
            hexInt >= 2311 and hexInt <= 2320 or hexInt >= 2411 and hexInt <= 2420): subsectorLetter = "G"
        elif (hexInt >= 2511 and hexInt <= 2520 or hexInt >= 2611 and hexInt <= 2620 or 
            hexInt >= 2711 and hexInt <= 2720 or hexInt >= 2811 and hexInt <= 2820 or 
            hexInt >= 2911 and hexInt <= 2920 or hexInt >= 3011 and hexInt <= 3020 or 
            hexInt >= 3111 and hexInt <= 3120 or hexInt >= 3211 and hexInt <= 3220 ): subsectorLetter = "H"
        
        elif (hexInt >= 121 and hexInt <= 130 or hexInt >= 221 and hexInt <= 230 or 
            hexInt >= 321 and hexInt <= 330 or hexInt >= 421 and hexInt <= 430 or 
            hexInt >= 521 and hexInt <= 530 or hexInt >= 621 and hexInt <= 630 or 
            hexInt >= 721 and hexInt <= 730 or hexInt >= 821 and hexInt <= 820): subsectorLetter = "I"
        elif (hexInt >= 921 and hexInt <= 930 or hexInt >= 1021 and hexInt <= 1030 or 
            hexInt >= 1121 and hexInt <= 1130 or hexInt >= 1221 and hexInt <= 1230 or 
            hexInt >= 1321 and hexInt <= 1330 or hexInt >= 1421 and hexInt <= 1430 or 
            hexInt >= 1521 and hexInt <= 1530 or hexInt >= 1621 and hexInt <= 1630 ): subsectorLetter = "J"
        elif (hexInt >= 1721 and hexInt <= 1730 or hexInt >= 1821 and hexInt <= 1830 or 
            hexInt >= 1921 and hexInt <= 1930 or hexInt >= 2021 and hexInt <= 2030 or 
            hexInt >= 2121 and hexInt <= 2130 or hexInt >= 2221 and hexInt <= 2230 or 
            hexInt >= 2321 and hexInt <= 2330 or hexInt >= 2421 and hexInt <= 2430 ): subsectorLetter = "K"
        elif (hexInt >= 2521 and hexInt <= 2530 or hexInt >= 2621 and hexInt <= 2630 or 
            hexInt >= 2721 and hexInt <= 2730 or hexInt >= 2821 and hexInt <= 2830 or 
            hexInt >= 2921 and hexInt <= 2930 or hexInt >= 3021 and hexInt <= 3030 or 
            hexInt >= 3121 and hexInt <= 3130 or hexInt >= 3221 and hexInt <= 3230 ): subsectorLetter = "L"
        
        elif (hexInt >= 131 and hexInt <= 140 or hexInt >= 231 and hexInt <= 240 or 
            hexInt >= 331 and hexInt <= 340 or hexInt >= 431 and hexInt <= 440 or 
            hexInt >= 531 and hexInt <= 540 or hexInt >= 631 and hexInt <= 640 or 
            hexInt >= 731 and hexInt <= 740 or hexInt >= 831 and hexInt <= 840 ): subsectorLetter = "M"
        elif (hexInt >= 931 and hexInt <= 940 or hexInt >= 1031 and hexInt <= 1040 or 
            hexInt >= 1131 and hexInt <= 1140 or hexInt >= 1231 and hexInt <= 1240 or 
            hexInt >= 1331 and hexInt <= 1340 or hexInt >= 1431 and hexInt <= 1440 or 
            hexInt >= 1531 and hexInt <= 1540 or hexInt >= 1631 and hexInt <= 1640 ): subsectorLetter = "N"
        elif (hexInt >= 1731 and hexInt <= 1740 or hexInt >= 1831 and hexInt <= 1840 or 
            hexInt >= 1931 and hexInt <= 1940 or hexInt >= 2031 and hexInt <= 2040 or 
            hexInt >= 2131 and hexInt <= 2140 or hexInt >= 2231 and hexInt <= 2240 or 
            hexInt >= 2331 and hexInt <= 2340 or hexInt >= 2431 and hexInt <= 2440 ): subsectorLetter = "O"
        elif (hexInt >= 2531 and hexInt <= 2540 or hexInt >= 2631 and hexInt <= 2640 or 
            hexInt >= 2731 and hexInt <= 2740 or hexInt >= 2831 and hexInt <= 2840 or 
            hexInt >= 2931 and hexInt <= 2940 or hexInt >= 3031 and hexInt <= 3040 or 
            hexInt >= 3131 and hexInt <= 3140 or hexInt >= 3231 and hexInt <= 3240 ): subsectorLetter = "P"
        return subsectorLetter
    def getSystemByHex(self, hexCoord):
        subsectorLetter = self.getSubsectorFromHexCoord(hexCoord)
        return self.sector.subsectors[subsectorLetter.lower()].getSystemByHex(hexCoord)
    def getSystemByName(self, systemName):
        pass
        return self.sector.systems.get(systemName)
    @staticmethod
    def getPlanetDrawing(planet):
        if planet is None: return "   "
        elif isinstance(planet, Moon): return " * "
        elif isinstance(planet, PrimaryPlanet): 
            if len(planet.moons) > 1:
                return "*O*"
            elif len(planet.moons) == 1:
                return " O*"
            else:
                return " O "
        elif isinstance(planet, GasGiant): 
            if planet.rings is not None and planet.rings:
                return "-G-"
            else:
                return " G "
        elif isinstance(planet, AsteroidBelt): return ":::"
        elif isinstance(planet, Planet): 
            if len(planet.moons) > 1:
                return "*o*"
            elif len(planet.moons) == 1:
                return " o*"
            else:
                return " o "
    def getInhabitedAreas(self, system):
        for body in system.systemLineup:
            if body is not None and not isinstance(body, Star):
                if body.population > 0:
                    print("  {} {}".format(body.name.upper() if isinstance(body, PrimaryPlanet) else body.name, body.upp if body.upp  is not None else ""))
                for moon in body.moons:
                    if moon.population > 0:
                        print("  {} -> {} {}".format(body.name, moon.name.upper() if isinstance(moon, PrimaryPlanet) else moon.name, moon.upp if moon.upp  is not None else ""))
                    if moon.moons is not None:
                        for moonMoon in moon.moons:
                            if moon.population > 0:
                                print("  {} -> {} -> {} {}".format(body.name, moon.name, moonMoon.name.upper() if isinstance(moonMoon, PrimaryPlanet) else moonMoon.name, moonMoon.upp if moonMoon.upp is not None else ""))
    def displaySystemStats(self, system):
        print("System Name: {} ( {} ) [{}]. {} {}-{}.".format(system.name, system.hexCoord, system.travelCode, 
            system.subsectorParent.name, 
            system.subsectorParent.subsector_letter.upper(), 
            system.subsectorParent.parent_sector.name
            ))
        print("")
        if system.travelCode != "-":
            print("Travel Code {} : {}".format(
                system.travelCode,
                system.travelCodeReason,
                ))
        else:
            print("Travel Code - : Safe")
        print("")
        print("Gas Giant      #: {}".format(system.gasGiants))
        print("Asteroid Belts #: {}".format(system.planetoidBelts))
        print("")
        print("Star: {} {}".format(str(system.star), Star.star_type[system.star.stellar_class][0]))
        print("'.")
        print("  \\ Inner System")
        print("SUN: {0:^9} {1:^9} {2:^9} {3:^9} {4:^9} {5:^9}".format(
            "" if system.systemLineup[1] is None else SectorViewer.getPlanetDrawing(system.systemLineup[1]), 
            "" if system.systemLineup[2] is None else SectorViewer.getPlanetDrawing(system.systemLineup[2]), 
            "" if system.systemLineup[3] is None else SectorViewer.getPlanetDrawing(system.systemLineup[3]), 
            "" if system.systemLineup[4] is None else SectorViewer.getPlanetDrawing(system.systemLineup[4]), 
            "" if system.systemLineup[5] is None else SectorViewer.getPlanetDrawing(system.systemLineup[5]), 
            "" if system.systemLineup[6] is None else SectorViewer.getPlanetDrawing(system.systemLineup[6]), 
            ))
        print("  /  {0:^9} {1:^9} {2:^9} {3:^9} {4:^9} {5:^9}".format(
            "-" if system.systemLineup[1] is None else str(system.systemLineup[1].get_upp_or_planet_type()), 
            "-" if system.systemLineup[2] is None else str(system.systemLineup[2].get_upp_or_planet_type()), 
            "-" if system.systemLineup[3] is None else str(system.systemLineup[3].get_upp_or_planet_type()), 
            "-" if system.systemLineup[4] is None else str(system.systemLineup[4].get_upp_or_planet_type()),
            "-" if system.systemLineup[5] is None else str(system.systemLineup[5].get_upp_or_planet_type()), 
            "-" if system.systemLineup[6] is None else str(system.systemLineup[6].get_upp_or_planet_type()), 
            ))
        print(".'   {0:^9} {1:^9} {2:^9} {3:^9} {4:^9} {5:^9}".format(
            "" if system.systemLineup[1] is None else str(system.systemLineup[1].getPlanetType()), 
            "" if system.systemLineup[2] is None else str(system.systemLineup[2].getPlanetType()), 
            "" if system.systemLineup[3] is None else str(system.systemLineup[3].getPlanetType()), 
            "" if system.systemLineup[4] is None else str(system.systemLineup[4].getPlanetType()),
            "" if system.systemLineup[5] is None else str(system.systemLineup[5].getPlanetType()), 
            "" if system.systemLineup[6] is None else str(system.systemLineup[6].getPlanetType()), 
            ))
        print("")
        print("    Mid System")
        print(" ->  {0:^9} {1:^9} {2:^9} {3:^9} {4:^9} {5:^9}".format(
            "" if system.systemLineup[7] is None else SectorViewer.getPlanetDrawing(system.systemLineup[7]), 
            "" if system.systemLineup[8] is None else SectorViewer.getPlanetDrawing(system.systemLineup[8]), 
            "" if system.systemLineup[9] is None else SectorViewer.getPlanetDrawing(system.systemLineup[9]),
            "" if system.systemLineup[10] is None else SectorViewer.getPlanetDrawing(system.systemLineup[10]), 
            "" if system.systemLineup[11] is None else SectorViewer.getPlanetDrawing(system.systemLineup[11]), 
            "" if system.systemLineup[12] is None else SectorViewer.getPlanetDrawing(system.systemLineup[12]), 

            ))
        print("     {0:^9} {1:^9} {2:^9} {3:^9} {4:^9} {5:^9}".format(
            "-" if system.systemLineup[7] is None else str(system.systemLineup[7].get_upp_or_planet_type()), 
            "-" if system.systemLineup[8] is None else str(system.systemLineup[8].get_upp_or_planet_type()), 
            "-" if system.systemLineup[9] is None else str(system.systemLineup[9].get_upp_or_planet_type()),
            "-" if system.systemLineup[10] is None else str(system.systemLineup[10].get_upp_or_planet_type()), 
            "-" if system.systemLineup[11] is None else str(system.systemLineup[11].get_upp_or_planet_type()), 
            "-" if system.systemLineup[12] is None else str(system.systemLineup[12].get_upp_or_planet_type()), 

            ))
        print("     {0:^9} {1:^9} {2:^9} {3:^9} {4:^9} {5:^9}".format(
            "" if system.systemLineup[7] is None else str(system.systemLineup[7].getPlanetType()), 
            "" if system.systemLineup[8] is None else str(system.systemLineup[8].getPlanetType()), 
            "" if system.systemLineup[9] is None else str(system.systemLineup[9].getPlanetType()),
            "" if system.systemLineup[10] is None else str(system.systemLineup[10].getPlanetType()), 
            "" if system.systemLineup[11] is None else str(system.systemLineup[11].getPlanetType()), 
            "" if system.systemLineup[12] is None else str(system.systemLineup[12].getPlanetType()), 

            ))
        print("")
        print("    Outer System")
        print(" --> {0:^9} {1:^9} {2:^9} {3:^9} {4:^9}".format(
            "" if system.systemLineup[13] is None else SectorViewer.getPlanetDrawing(system.systemLineup[13]), 
            "" if system.systemLineup[14] is None else SectorViewer.getPlanetDrawing(system.systemLineup[14]), 
            "" if system.systemLineup[15] is None else SectorViewer.getPlanetDrawing(system.systemLineup[15]), 
            "" if system.systemLineup[16] is None else SectorViewer.getPlanetDrawing(system.systemLineup[16]), 
            "" if system.systemLineup[17] is None else SectorViewer.getPlanetDrawing(system.systemLineup[17])
            ))
        print("     {0:^9} {1:^9} {2:^9} {3:^9} {4:^9}".format(
            "-" if system.systemLineup[13] is None else str(system.systemLineup[13].get_upp_or_planet_type()), 
            "-" if system.systemLineup[14] is None else str(system.systemLineup[14].get_upp_or_planet_type()),
            "-" if system.systemLineup[15] is None else str(system.systemLineup[15].get_upp_or_planet_type()), 
            "-" if system.systemLineup[16] is None else str(system.systemLineup[16].get_upp_or_planet_type()), 
            "-" if system.systemLineup[17] is None else str(system.systemLineup[17].get_upp_or_planet_type())
            ))
        print("     {0:^9} {1:^9} {2:^9} {3:^9} {4:^9}".format(
            "" if system.systemLineup[13] is None else str(system.systemLineup[13].getPlanetType()), 
            "" if system.systemLineup[14] is None else str(system.systemLineup[14].getPlanetType()),
            "" if system.systemLineup[15] is None else str(system.systemLineup[15].getPlanetType()), 
            "" if system.systemLineup[16] is None else str(system.systemLineup[16].getPlanetType()), 
            "" if system.systemLineup[17] is None else str(system.systemLineup[17].getPlanetType())
            ))
        print("")
        print("Inhabited Areas:")
        self.getInhabitedAreas(system)
        
        print("")
        print("Primary {}: {}".format("Planet" if system.primaryPlanet.size > 3 else "Dwarf-Planet", system.primaryPlanet.name))
        TerminalUtils.pprint("Size: {0:2} - {1}".format(Utils.hex_key[system.primaryPlanet.size], 
            DescriptionGenerator.getSizeDescription(system.primaryPlanet.size)))
        TerminalUtils.pprint("Atmo: {0:2} - {1}".format(Utils.hex_key[system.primaryPlanet.atmosphere], 
            DescriptionGenerator.getAtmosphereDescription(system.primaryPlanet.atmosphere)), indent=11)
        TerminalUtils.pprint("Temp: {0:<2} - {1}".format(system.primaryPlanet.temperature, 
            DescriptionGenerator.getTemperatureDescription(system.primaryPlanet.temperature)), indent=11)
        TerminalUtils.pprint("Hydr: {0:2} - {1}".format(Utils.hex_key[system.primaryPlanet.hydrographics], 
            DescriptionGenerator.getHydrographicsDescription(system.primaryPlanet.hydrographics)), indent=11)
        print("")
        print("Pop.: {0:2} - {1} - x{2}".format(Utils.hex_key[system.primaryPlanet.population], 
            DescriptionGenerator.getPopulationDescription(system.primaryPlanet.population), 
            system.populationModifier))
        TerminalUtils.pprint("Gov.: {0:2} - {1}".format(Utils.hex_key[system.primaryPlanet.government], 
            DescriptionGenerator.getGovernmentDescription(system.primaryPlanet.government)), indent=11)
        TerminalUtils.pprint("Law : {0:2} - {1}".format(Utils.hex_key[system.primaryPlanet.lawLevel], 
            DescriptionGenerator.getLawLevelDescription(system.primaryPlanet.lawLevel)), indent=11)
        TerminalUtils.pprint("Tech: {0:2} - {1}".format(system.primaryPlanet.techLevel, 
            DescriptionGenerator.getTechLevelDescription(system.primaryPlanet.techLevel)), indent=11)
        print("")
        TerminalUtils.pprint("Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(system.primaryPlanet.starport), 
            DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(system.primaryPlanet.starport))), indent=11)
        starports = ""
        if isinstance(system.primaryPlanet, PrimaryPlanet):
            for port in system.primaryPlanet.portsTypes:
                starports += "{}, ".format(port)
            starports = starports[:-2]
            TerminalUtils.pprint("Starports: [{}] {} - {}".format(system.primaryPlanet.portsTypesRoll, system.primaryPlanet.portsTypesHighest, starports))
        else:
            for port in system.primaryPlanet.primary.portsTypes:
                starports += "{}, ".format(port)
            starports = starports[:-2]
            TerminalUtils.pprint("Starports: [{}] {} - {}".format(system.primaryPlanet.primary.portsTypesRoll, system.primaryPlanet.primary.portsTypesHighest, starports))
        print("")
        print("Trade Codes: ")
        for tradeCode in system.tradeCodes:
            print("{} - {}".format(tradeCode, SubsectorGenerator.getGetFullTradeCodes(tradeCode)))
        print("")
        print("Moons:")
        if(system.primaryPlanet.moons is not None):
            for moon in system.primaryPlanet.moons:
                print("- {} - {}".format(moon.name, moon.displayUwpCode())) 
        print("=========================================================")
        for body in system.systemLineup:
            if ( body is not None and (body is system.star) ): 
                continue
            if isinstance(body, GasGiant):
                print("{}: {} | {} moons".format(body.name, body.getPlanetType(), len(body.moons) if body.moons is not None else "0"))
                notable_moons = []
                if(body.moons is not None):
                    print("Moons:")
                    for moon in body.moons:
                        print("{} {} - {}".format(body.moons.index(moon)+1,moon.name, moon.displayUwpCode()))
                        if isinstance(moon, Planet) or isinstance(moon, AsteroidBelt): 
                            notable_moons.append(moon)
                    if len(notable_moons) > 0: 
                        print("Notable Moons: ")
                        for moon in notable_moons:
                            print("{} {}: {} ({})".format(
                                body.moons.index(moon)+1,
                                moon.name.upper() if moon is system.primaryPlanet else moon.name, 
                                moon.displayUwpCode(), 
                                moon.getPlanetType()
                                )
                            )
                            TerminalUtils.pprint("  Size: {0:2} - {1}".format(Utils.hex_key[moon.size], 
                                DescriptionGenerator.getSizeDescription(moon.size)), indent=4)
                            TerminalUtils.pprint("  Atmo: {0:2} - {1}".format(Utils.hex_key[moon.atmosphere], 
                                DescriptionGenerator.getAtmosphereDescription(moon.atmosphere)), indent=13)
                            TerminalUtils.pprint("  Temp: {0:2} - {1}".format(moon.temperature, 
                                DescriptionGenerator.getTemperatureDescription(moon.temperature)), indent=13)
                            TerminalUtils.pprint("  Hydr: {0:2} - {1}".format(Utils.hex_key[moon.hydrographics], 
                                DescriptionGenerator.getHydrographicsDescription(moon.hydrographics)), indent=13)
                            print("")
                            if moon.population > 0:
                                TerminalUtils.pprint("  Pop.: {0:2} - {1}".format(Utils.hex_key[moon.population], 
                                    DescriptionGenerator.getPopulationDescription(moon.population)), indent=13)
                                TerminalUtils.pprint("  Gov.: {0:2} - {1}".format(Utils.hex_key[moon.government], 
                                    DescriptionGenerator.getGovernmentDescription(moon.government)), indent=13)
                                TerminalUtils.pprint("  Law : {0:2} - {1}".format(Utils.hex_key[moon.lawLevel], 
                                    DescriptionGenerator.getLawLevelDescription(moon.lawLevel)), indent=13)
                                TerminalUtils.pprint("  Tech: {0:2} - {1}".format(moon.techLevel, 
                                    DescriptionGenerator.getTechLevelDescription(moon.techLevel)), indent=13)
                                print("")
                                TerminalUtils.pprint("  Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(moon.starport), 
                                    DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(moon.starport))), indent=4)
                                print("")
                            # Notes
                            if moon is not None:
                                print("Settlements:")
                                if len(moon.settlements) > 0:
                                    for settlement in moon.settlements:
                                        print("- {}: {} [{}-{}]".format(settlement.name, settlement.settlement_type, settlement.population_size,  settlement.get_settlement_classification() ))
                                        TerminalUtils.pprint("    "+settlement.description if settlement.description != "" else "-Empty Description-", indent=4)
                                print("\nAreas of Interest:")
                                if len(moon.areas_of_interest) > 0:
                                    for area in moon.areas_of_interest:
                                        print("- {} {} [{}]".format(area.name, area.area_type, "Dungeon" if area.is_dungeon else "Location"))
                                        TerminalUtils.pprint("    "+area.description if area.description != "" else "-Empty Description-", indent=4)
                                print("{} NOTES:".format(moon.name))
                                for entry in moon.description:
                                    TerminalUtils.pprint("{}:\n{}\n".format(entry[0], entry[1]), width=100, indent=4)
                                for entry in moon.history:
                                    TerminalUtils.pprint("{}:\n{}\n".format(entry[0], entry[1]), width=100, indent=4)
                                for entry in moon.notes:
                                    TerminalUtils.pprint("{}:\n{}\n".format(entry[0], entry[1]), width=100, indent=4)
                                print("")
                            
                            if(moon.moons is not None):
                                print("  Moons: {}".format(len(moon.moons)))
                                for moonsMoon in moon.moons:
                                    print("  - {} - {}".format(moonsMoon.name, moonsMoon.displayUwpCode()))
                                print("")
                print("")
                # for each moon
                # list moon name <name>-<x>
            elif isinstance(body, AsteroidBelt):
                print("{0}: {1} ({2})".format(body.name, body.displayUwpCode(), body.getPlanetType()))
                TerminalUtils.pprint("  Size: {0:2} - {1}".format(Utils.hex_key[body.size], 
                    DescriptionGenerator.getSizeDescription(body.size)), indent=4)
                TerminalUtils.pprint("  Atmo: {0:2} - {1}".format(Utils.hex_key[body.atmosphere], 
                    DescriptionGenerator.getAtmosphereDescription(body.atmosphere)), indent=13)
                TerminalUtils.pprint("  Temp: {0:2} - {1}".format(body.temperature, 
                    DescriptionGenerator.getTemperatureDescription(body.temperature)), indent=13)
                TerminalUtils.pprint("  Hydr: {0:2} - {1}".format(Utils.hex_key[body.hydrographics], 
                    DescriptionGenerator.getHydrographicsDescription(body.hydrographics)), indent=13)
                print("")
                if body.population > 0:
                    TerminalUtils.pprint("  Pop.: {0:2} - {1}".format(Utils.hex_key[body.population], 
                        DescriptionGenerator.getPopulationDescription(body.population)), indent=13)
                    TerminalUtils.pprint("  Gov.: {0:2} - {1}".format(Utils.hex_key[body.government], 
                        DescriptionGenerator.getGovernmentDescription(body.government)), indent=13)
                    TerminalUtils.pprint("  Law : {0:2} - {1}".format(Utils.hex_key[body.lawLevel], 
                        DescriptionGenerator.getLawLevelDescription(body.lawLevel)), indent=13)
                    TerminalUtils.pprint("  Tech: {0:2} - {1}".format(body.techLevel, 
                        DescriptionGenerator.getTechLevelDescription(body.techLevel)), indent=13)
                    print("")
                    TerminalUtils.pprint("  Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(body.starport), 
                        DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(body.starport))), indent=4)
                    print("")
                if(body.moons is not None):
                    print("  Dwarf Planets: {}".format(len(body.moons)))
                    for dp in body.moons:
                        print("  - {} - {}".format(dp.name, dp.displayUwpCode()))
                    print("")
                print("")
            elif body is not None:
                print("{0}: {1} ({2})".format(body.name.upper() if body is system.primaryPlanet else body.name, body.displayUwpCode(), body.getPlanetType()))
                TerminalUtils.pprint("  Size: {0:2} - {1}".format(Utils.hex_key[body.size], 
                    DescriptionGenerator.getSizeDescription(body.size)), indent=13)
                TerminalUtils.pprint("  Atmo: {0:2} - {1}".format(Utils.hex_key[body.atmosphere], 
                    DescriptionGenerator.getAtmosphereDescription(body.atmosphere)), indent=13)
                TerminalUtils.pprint("  Temp: {0:2} - {1}".format(body.temperature, 
                    DescriptionGenerator.getTemperatureDescription(body.temperature)), indent=13)
                TerminalUtils.pprint("  Hydr: {0:2} - {1}".format(Utils.hex_key[body.hydrographics], 
                    DescriptionGenerator.getHydrographicsDescription(body.hydrographics)), indent=13)
                print("")
                if body.population > 0:
                    TerminalUtils.pprint("  Pop.: {0:2} - {1}".format(Utils.hex_key[body.population], 
                        DescriptionGenerator.getPopulationDescription(body.population)), indent=13)
                    TerminalUtils.pprint("  Gov.: {0:2} - {1}".format(Utils.hex_key[body.government], 
                        DescriptionGenerator.getGovernmentDescription(body.government)), indent=13)
                    TerminalUtils.pprint("  Law : {0:2} - {1}".format(Utils.hex_key[body.lawLevel], 
                        DescriptionGenerator.getLawLevelDescription(body.lawLevel)), indent=13)
                    TerminalUtils.pprint("  Tech: {0:2} - {1}".format(body.techLevel, 
                        DescriptionGenerator.getTechLevelDescription(body.techLevel)), indent=13)
                    print("")
                    TerminalUtils.pprint("  Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(system.primaryPlanet.starport), 
                        DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(system.primaryPlanet.starport))))
                    print("")
                if(body.moons is not None):
                    print("Moons:")
                    for moon in body.moons:
                        print("- {} - {}".format(moon.name, moon.displayUwpCode())) 
                print("")
            # Notes
            if body is not None:
                print("Settlements:")
                if len(body.settlements) > 0:
                    for settlement in body.settlements:
                        print("- {}: {} [{}-{}]".format(settlement.name, settlement.settlement_type, settlement.population_size,  settlement.get_settlement_classification() ))
                        TerminalUtils.pprint("    "+settlement.description if settlement.description != "" else "    -Empty Description-", indent=4)
                print("\nAreas of Interest:")
                if len(body.areas_of_interest) > 0:
                    for area in body.areas_of_interest:
                        print("- {} {} [{}]".format(area.name, area.area_type, "Dungeon" if area.is_dungeon else "Location"))
                        TerminalUtils.pprint("    "+ area.description if area.description != "" else "    -Empty Description-", indent=4)
                print("")
                print("{} NOTES:".format(body.name))
                for entry in body.description:
                    TerminalUtils.pprint("{}:\n{}\n".format(entry[0], entry[1]), width=100, indent=4)
                for entry in body.history:
                    TerminalUtils.pprint("{}:\n{}\n".format(entry[0], entry[1]), width=100, indent=4)
                for entry in body.notes:
                    TerminalUtils.pprint("{}:\n{}\n".format(entry[0], entry[1]), width=100, indent=4)
            print("")
        print("SYSTEM NOTES:")
        for entry in system.description:
            TerminalUtils.pprint("{}:\n{}".format(entry[0], entry[1]), width=100, indent=4)
        for entry in system.history:
            TerminalUtils.pprint("{}:\n{}".format(entry[0], entry[1]), width=100, indent=4)
        for entry in system.megacorpsPresence:
            TerminalUtils.pprint("{}:\n{}".format(entry[0], entry[1]), width=100, indent=4)
    def displaySystemLocationStats(self, system, location_index):
        location = system.systemLineup[location_index]
        print("System Name: {} ( {} ) [{}]. {} {}-{}.".format(system.name, system.hexCoord, system.travelCode, 
            system.subsectorParent.name, 
            system.subsectorParent.subsector_letter.upper(), 
            system.subsectorParent.parent_sector.name
            ))
        print("")
        if system.travelCode != "-":
            print("Travel Code {} : {}".format(
                system.travelCode,
                system.travelCodeReason,
                ))
        else:
            print("Travel Code - : Safe")
            print("{} {}: {} ({})".format(
                location.moons.index(location)+1,
                location.name.upper() if location is system.primaryPlanet else location.name, 
                location.displayUwpCode(), 
                location.getPlanetType()
                )
            )
        TerminalUtils.pprint("  Size: {0:2} - {1}".format(Utils.hex_key[location.size], 
            DescriptionGenerator.getSizeDescription(location.size)), indent=4)
        TerminalUtils.pprint("  Atmo: {0:2} - {1}".format(Utils.hex_key[location.atmosphere], 
            DescriptionGenerator.getAtmosphereDescription(location.atmosphere)), indent=4)
        TerminalUtils.pprint("  Temp: {0:2} - {1}".format(location.temperature, 
            DescriptionGenerator.getTemperatureDescription(location.temperature)), indent=4)
        TerminalUtils.pprint("  Hydr: {0:2} - {1}".format(Utils.hex_key[location.hydrographics], 
            DescriptionGenerator.getHydrographicsDescription(location.hydrographics)), indent=4)
        print("")
        if location.population > 0:
            TerminalUtils.pprint("  Pop.: {0:2} - {1}".format(Utils.hex_key[location.population], 
                DescriptionGenerator.getPopulationDescription(location.population)), indent=4)
            TerminalUtils.pprint("  Gov.: {0:2} - {1}".format(Utils.hex_key[location.government], 
                DescriptionGenerator.getGovernmentDescription(location.government)), indent=4)
            TerminalUtils.pprint("  Law : {0:2} - {1}".format(Utils.hex_key[location.lawLevel], 
                DescriptionGenerator.getLawLevelDescription(location.lawLevel)), indent=4)
            TerminalUtils.pprint("  Tech: {0:2} - {1}".format(location.techLevel, 
                DescriptionGenerator.getTechLevelDescription(location.techLevel)), indent=4)
            print("")
            TerminalUtils.pprint("  Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(location.starport), 
                DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(location.starport))), indent=4)
            print("")
        
        if(location.moons is not None):
            print("  Moons: {}".format(len(location.moons)))
            for moon in location.moons:
                print("  - {} - {}".format(moon.name, moon.displayUwpCode()))
            print("")
        print("Settlements:")
        if len(location.settlements) > 0:
            for settlement in location.settlements:
                print("- {}: {} [{}-{}]".format(settlement.name, settlement.settlement_type, settlement.population_size, settlement.get_settlement_classification() ))
                TerminalUtils.pprint("    "+ settlement.description if settlement.description != "" else "    -Empty Description-", indent=4)
        print("\nAreas of Interest:")
        if len(location.areas_of_interest) > 0:
            for area in location.areas_of_interest:
                print("- {} {} [{}]".format(area.name, area.area_type, "Dungeon" if area.is_dungeon else "Location"))
                TerminalUtils.pprint("    "+ area.description if area.description != "" else "    -Empty Description-", indent=4)
        print("")
        print("NOTES:")
        for entry in location.description:
            TerminalUtils.pprint("{}:\n{}\n".format(entry[0], entry[1]), width=100)
        for entry in location.history:
            TerminalUtils.pprint("{}:\n{}\n".format(entry[0], entry[1]), width=100)
        for entry in location.notes:
            TerminalUtils.pprint("{}:\n{}\n".format(entry[0], entry[1]), width=100)
        for entry in location.megacorpsPresence:
            TerminalUtils.pprint("{}:\n{}\n".format(entry[0], entry[1]), width=100)
        for entry in location.primaryPlanet.description:
            TerminalUtils.pprint("{}:\n{}\n".format(entry[0], entry[1]), width=100)
        for entry in location.primaryPlanet.history:
            TerminalUtils.pprint("{}:\n{}\n".format(entry[0], entry[1]), width=100)
class SectorEditor():
    @staticmethod
    def performSystemEdit(sector, system, viewer):
        input("\nPress Enter to Edit System...")
        done=False
        MainMenu = [
        "System Symmary", "Change System Name", "Edit System Leadership", 
        "Edit Primary", "Edit Planet", 
        "Add Planet to System", "Remove Planet from System",
        "System Description", "System History", "System MegaCorp Entries", "System Notes Entries", 
        "Planet Description", "Planet History",  "Planet Notes Entries", 
        "Swap Planets", 
        "Exit"]
        while(not done):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Edit system: {} {}".format(system.name, system.displayUwpCode()))
            selection = TerminalUtils.selectMenuItem(MainMenu, "Select an option. >")
            if(selection == "Exit"):  done=True
            elif(selection == "System Symmary"):  
                os.system('cls' if os.name == 'nt' else 'clear')
                viewer.displaySystemStats(system)
                input("Press enter to continue...")
            elif(selection == "Change System Name"): 
                new_name = input("What is the new name of the {} system and its primary?: $>".format(system.name))
                if "Yes" == TerminalUtils.selectMenuItem(["Yes", "No"], "Are you sure you want to change {} to \"{}\"? $>".format(system.name, new_name)):
                    performSystemRename(new_name, sector, system, viewer)
            elif(selection == "Edit System Leadership"):  
                pass
                SectorEditor.editSystemLeadership(system)
            elif(selection == "Edit Primary"): 
                pass 
                SectorEditor.editPrimary(system)
            elif(selection == "Edit Planet"):  
                planet = None
                orbiting_bodies = []
                orbiting_body_names = []
                for body in system.systemLineup:
                    if body is not None and not isinstance(body, Star):
                        print("- {}: {}".format(body.name, body.displayUwpCode() ))
                        orbiting_bodies.append(body)
                        orbiting_body_names.append(body.name)
                orbiting_body_name = TerminalUtils.selectMenuItem(options=orbiting_body_names+["Back"], prompt="Select a body to edit. $>")
                if orbiting_body_name.lower() not in ["back", "exit", "cancel"]:
                    planet = orbiting_bodies[orbiting_body_names.index(orbiting_body_name)]
                    SectorEditor.editPlanet(system, planet)
            elif(selection == "Add Planet to System"):  SectorEditor.addPlanetToSystem(system)
            elif(selection == "Remove Planet to System"):  SectorEditor.addPlanetToSystem(system)
            elif(selection == "System Description"):  SectorEditor.editTextField(system, system.description, "System Description")
            elif(selection == "System History"):  SectorEditor.editTextField(system, system.history, "System History")
            elif(selection == "System MegaCorp Entries"):  SectorEditor.editTextField(system, system.megacorpsPresence, "MegaCorps")
            elif(selection == "System Notes Entries"):  SectorEditor.editTextField(system, system.notes, "System Notes")
            elif(selection == "Planet Description"):  
                names = []
                for body in system.systemLineup:
                    names.append(body.name)
                name = TerminalUtils.selectMenuItem(names+["Back"], "Select a planet to view. >")
                if(name == "Exit"):  done=True
                planet = system.systemLineup[names.index(name)]
                SectorEditor.editTextField(planet, planet.description, "Planet Description")
            elif(selection == "Planet History"):  
                names = []
                for body in system.systemLineup:
                    names.append(body.name)
                name = TerminalUtils.selectMenuItem(names+["Back"], "Select a planet to view. >")
                if(name == "Exit"):  done=True
                planet = system.systemLineup[names.index(name)]
                SectorEditor.editTextField(planet, planet.history, "Planet History")
            elif(selection == "Planet Notes Entries"):  
                names = []
                for body in system.systemLineup:
                    names.append(body.name)
                name = TerminalUtils.selectMenuItem(names+["Back"], "Select a planet to view. >")
                if(name == "Exit"):  done=True
                planet = system.systemLineup[names.index(name)]
                SectorEditor.editTextField(planet, planet.notes, "Planet Notes")
            elif(selection == "Swap Planets"): 
                pass
                SectorEditor.swapSystemBodies(system)
            else:
                pass
                print("I don't think {} is an option... yet.".format(selection))   
        return True  
    @staticmethod
    def setPrimaryAttributeValue(valueName, currentValue, earthValue, minValue, maxValue, descriptorMethod, derivation="2D"):
        doneWithQuestion = False
        while(not doneWithQuestion):
            value=0
            print("Current {0}: [{1}] | Earth is {0} [{2}] | Range is [{3}-{4}] derived from {5}".format(valueName, currentValue, earthValue, minValue, maxValue, derivation))
            print("{0}: {1:2} - {2}".format(valueName, Utils.hex_key[currentValue], 
                descriptorMethod(currentValue)))
            value = int(input("Enter a value between {} and {} >".format(minValue, maxValue)))
            if(value <= minValue or value >= maxValue):
                print("Invalid {} value: {}. needs to be from [{}-{}]".format(valueName, currentValue, minValue, maxValue,))
                continue
            print("{0}: {1:2} - {2}".format(valueName, Utils.hex_key[value], 
                descriptorMethod(value)))
            if(TerminalUtils.selectMenuItem(prompt="Is this alright? >").lower() == "yes"):
                doneWithQuestion=True
        return value
    @staticmethod
    def editPrimary(system):
        primaryPlanet = system.primaryPlanet
        # EDIT STARTS HERE
        # primaryPlanet.name = input()
        done=False
        doneWithQuestion = False
        while (not done):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Editing Primary Planet ({}) UWP".format(system.name))
            size = setPrimaryAttributeValue("Size", primaryPlanet.size, 8, 0, 12, DescriptionGenerator.getSizeDescription, "2D-2")
            atmosphere = setPrimaryAttributeValue("Atmosphere", primaryPlanet.atmosphere, 6, 0, 15, DescriptionGenerator.getAtmosphereDescription, derivation="2D-7+size")
            hydrographics = setPrimaryAttributeValue("Hydrographics", primaryPlanet.hydrographics, 8, 0, 10, DescriptionGenerator.getHydrographicsDescription, derivation="2D-7+Modifiers")
            temperature = setPrimaryAttributeValue("Temperature", primaryPlanet.temperature, 7, 0, 15, DescriptionGenerator.getTemperatureDescription, derivation="2D+Modifiers")

            population = setPrimaryAttributeValue("Population", primaryPlanet.population, 9, 0, 12, DescriptionGenerator.getPopulationDescription, derivation="2D-2")
            government = setPrimaryAttributeValue("Government", primaryPlanet.government, 7, 0, 15, DescriptionGenerator.getGovernmentDescription, derivation="2D-7")
            lawLevel = setPrimaryAttributeValue("Law Level", primaryPlanet.lawLevel, 4, 0, 15, DescriptionGenerator.getLawLevelDescription, derivation="2D-7+GovernmentCharacteristic")
            # STARPORT
            doneWithQuestion = False
            while(not doneWithQuestion):
                print("Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(primaryPlanet.starport), 
                    DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(primaryPlanet.starport), primaryPlanet.birthing_cost_per_week)))
                starportDM = 0
                if(population >= 10): starportDM+=2
                elif(population >= 8): starportDM+=1
                elif(population <= 4): starportDM-=2
                elif(population <= 2): starportDM-=1
                portsTypesRoll = 1
                roll = int(input("Enter a value between 2 and 12 to be added to {} for starport Class >".format(starportDM)))
                planetStarport = roll + starportDM
                if(population == 0): planetStarport = 0
                birthing_cost_per_week=0
                refiendFuelCost=500
                unrefiendFuelCost=100
                if(population > 0): 
                    print("1D x Cr1000 for class A, 1D x Cr500 for class B, 1D x Cr100 for class C,  1D x Cr10 for class D, ocr for E and X")
                    value = input("Enter a credit cost for berthing a starship in this system (default {}cr). >".format(starportDM, planetStarport*100))
                    if value == "": value = planetStarport*100
                    birthing_cost_per_week = int(value)
                    print("Typical Refined fuel costs 500cr, (default 200+1D*50")
                    value = input("Enter Refined Fuel cost. >")
                    if value == "": value = 200+random.randint(1, 6)*50
                    refiendFuelCost = int(value)
                    print("Typical Unrefined fuel costs 100cr, (default 40+1D*10)")
                    value = input("Enter a Unrefined Fuel cost. >")
                    if value == "": value = 40+random.randint(1, 6)*10
                    unrefiendFuelCost = int(value)

                print("Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(planetStarport), 
                    DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(planetStarport), birthing_cost_per_week)))
                if(TerminalUtils.selectMenuItem(prompt="Is this alright? >").lower() == "yes"):
                    doneWithQuestion=True

            # TECH LEVEL
            minTechLevel = 3
            if(atmosphere in [2, 3, 13, 14]): minTechLevel = 5
            elif(atmosphere in [0, 1, 10, 15]): minTechLevel = 8
            elif(atmosphere in [11]): minTechLevel = 9
            elif(atmosphere in [12]): minTechLevel = 1
            techLevelDM = 0
            if (planetStarport in [10]):   techLevelDM +=6
            elif (planetStarport in [11]): techLevelDM +=4
            elif (planetStarport in [12]): techLevelDM +=2
            if (size in [0, 1]): techLevelDM +=2
            elif (size in [2, 3, 4]): techLevelDM +=1
            if (atmosphere in [1, 2, 3, 4, 10, 11, 12, 13, 14, 15]): techLevelDM +=1
            if (hydrographics in [0, 1]): techLevelDM +=1
            elif (hydrographics in [10]): techLevelDM +=2
            if (population in [1, 2, 3, 4, 5, 8]):   techLevelDM +=1
            elif (population in [9]): techLevelDM +=2
            elif (population in [10]): techLevelDM +=4
            if (government in [0, 5]):   techLevelDM +=1
            elif (government in [7]): techLevelDM +=2
            elif (government in [13, 14]): techLevelDM -=2
            doneWithQuestion = False
            while(not doneWithQuestion):
                TerminalUtils.pprint("Tech Level: {0:2} - {1}".format(primaryPlanet.techLevel, 
                    DescriptionGenerator.getTechLevelDescription(primaryPlanet.techLevel)))
                TerminalUtils.pprint("BASE NEW TL: {0:2} - {1}".format(minTechLevel + techLevelDM, 
                    DescriptionGenerator.getTechLevelDescription(minTechLevel + techLevelDM)))
                roll = int(input("Enter a value between 1 and 6 to be added to {} for Tech Level >".format(minTechLevel + techLevelDM)))
                techLevel = minTechLevel + techLevelDM + roll
                if(population == 0): techLevel = 0
                TerminalUtils.pprint("Tech Level: {0:2} - {1}".format(techLevel, 
                    DescriptionGenerator.getTechLevelDescription(techLevel)))
                if(TerminalUtils.selectMenuItem(prompt="Is this alright? >").lower() == "yes"):
                        doneWithQuestion=True
            systemTradeCodes = []
            if(atmosphere in [4, 5, 6, 7, 8, 9] and hydrographics in [4, 5, 6, 7, 8] and population in [5, 6, 7]): systemTradeCodes.append("Ag")
            if(population == 0 and atmosphere == 0 and hydrographics == 0): systemTradeCodes.append("As")
            if(population == 0 and government == 0 and lawLevel == 0): systemTradeCodes.append("Ba")
            if(hydrographics == 0 and atmosphere >= 2): systemTradeCodes.append("De")
            if(atmosphere >= 10 and techLevel >= 1): systemTradeCodes.append("Fl")
            if(size in [6, 7, 8] and atmosphere in [5, 6, 8] and hydrographics in [5, 6, 7]): systemTradeCodes.append("Ga")
            if(population >= 9): systemTradeCodes.append("Hi")
            if(techLevel >= 12): systemTradeCodes.append("Ht")
            if(hydrographics > 0 and atmosphere in [0, 1]): systemTradeCodes.append("Ie")
            if(atmosphere in [0, 1, 2, 4, 7, 9] and population >= 9): systemTradeCodes.append("In")
            if(population <= 3): systemTradeCodes.append("Lo")
            if(techLevel <= 5): systemTradeCodes.append("Lt")
            if(atmosphere in [0, 1, 2, 3] and hydrographics <= 3 and population >= 6): systemTradeCodes.append("Na")
            if(population in [0, 1, 2, 3, 4, 5, 6]): systemTradeCodes.append("Ni")
            if(hydrographics <= 3): systemTradeCodes.append("Po")
            if(atmosphere in [6,8] and population in [6, 7, 8] and government in [4, 5, 6, 7, 8, 9]): systemTradeCodes.append("Ri")
            if(atmosphere == 0): systemTradeCodes.append("Va")
            if(hydrographics >= 10): systemTradeCodes.append("Wa")

            portsTypesRoll = int(input("Enter a value between 2 and 12 to be added to {} for starport Types Roll >".format(starportDM)))
            portsTypes = []
            portsTypesHighest = random.choice(["N","S","T","R"])
            portsTypes.append(portsTypesHighest)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Presenting the NEW Primary Planet in the {} system".format(system.name))
            print("Size: {0:2} - {1}".format(Utils.hex_key[size], 
                DescriptionGenerator.getSizeDescription(size)))
            print("Atmo: {0:2} - {1}".format(Utils.hex_key[atmosphere], 
                DescriptionGenerator.getAtmosphereDescription(atmosphere)))
            print("Temp: {0:<2} - {1}".format(temperature, 
                DescriptionGenerator.getTemperatureDescription(temperature)))
            print("Hydr: {0:2} - {1}".format(Utils.hex_key[hydrographics], 
                DescriptionGenerator.getHydrographicsDescription(hydrographics)))
            print("")
            print("Pop.: {0:2} - {1} - x{2}".format(Utils.hex_key[population], 
                DescriptionGenerator.getPopulationDescription(population), 
                system.populationModifier))
            TerminalUtils.pprint("Gov.: {0:2} - {1}".format(Utils.hex_key[government], 
                DescriptionGenerator.getGovernmentDescription(government)))
            TerminalUtils.pprint("Law : {0:2} - {1}".format(Utils.hex_key[lawLevel], 
                DescriptionGenerator.getLawLevelDescription(lawLevel)))
            TerminalUtils.pprint("Tech: {0:2} - {1}".format(techLevel, 
                DescriptionGenerator.getTechLevelDescription(techLevel)))
            print("")
            print("Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(planetStarport), 
                DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(planetStarport), birthing_cost_per_week)))
            starports = ""
            for port in portsTypes:
                starports += "{}, ".format(port)
            starports = starports[:-2]
            print("Starports: [{}] {} - {}".format(portsTypesRoll, portsTypesHighest, starports))
            print("")
            print("Trade Codes: ")
            for tradeCode in systemTradeCodes:
                print("{} - {}".format(tradeCode, SubsectorGenerator.getGetFullTradeCodes(tradeCode)))
            if(TerminalUtils.selectMenuItem(options=["No", "Yes"],prompt="About to overwrite. Is this alright? >").lower() == "yes"):
                done=True
        # SAVE TO SYSTEM
        primaryPlanet.size = size
        primaryPlanet.atmosphere = atmosphere
        primaryPlanet.hydrographics = hydrographics
        primaryPlanet.temperature = temperature
        primaryPlanet.population = population
        primaryPlanet.government = government
        primaryPlanet.lawLevel = lawLevel
        primaryPlanet.starport = planetStarport
        primaryPlanet.birthing_cost_per_week = birthing_cost_per_week
        primaryPlanet.refiendFuelCost = refiendFuelCost
        primaryPlanet.unrefiendFuelCost = unrefiendFuelCost
        primaryPlanet.techLevel = techLevel
        primaryPlanet.portsTypes = portsTypes
        primaryPlanet.portsTypesRoll = portsTypesRoll
        primaryPlanet.portsTypesHighest = random.choice(["N","S","T","R"])
        system.primaryPlanet = primaryPlanet
        system.systemLineup[system.habitableZone] = primaryPlanet
        system.tradeCodes = systemTradeCodes
        updateSystemDictionary(system)
        # Display Results
        print("Primary Planet: {} system".format(system.primaryPlanet.name))
        print("Size: {0:2} - {1}".format(Utils.hex_key[system.primaryPlanet.size], 
            DescriptionGenerator.getSizeDescription(system.primaryPlanet.size)))
        print("Atmo: {0:2} - {1}".format(Utils.hex_key[system.primaryPlanet.atmosphere], 
            DescriptionGenerator.getAtmosphereDescription(system.primaryPlanet.atmosphere)))
        print("Temp: {0:<2} - {1}".format(system.primaryPlanet.temperature, 
            DescriptionGenerator.getTemperatureDescription(system.primaryPlanet.temperature)))
        print("Hydr: {0:2} - {1}".format(Utils.hex_key[system.primaryPlanet.hydrographics], 
            DescriptionGenerator.getHydrographicsDescription(system.primaryPlanet.hydrographics)))
        print("")
        print("Pop.: {0:2} - {1} - x{2}".format(Utils.hex_key[system.primaryPlanet.population], 
            DescriptionGenerator.getPopulationDescription(system.primaryPlanet.population), 
            system.populationModifier))
        TerminalUtils.pprint("Gov.: {0:2} - {1}".format(Utils.hex_key[system.primaryPlanet.government], 
            DescriptionGenerator.getGovernmentDescription(system.primaryPlanet.government)))
        TerminalUtils.pprint("Law : {0:2} - {1}".format(Utils.hex_key[system.primaryPlanet.lawLevel], 
            DescriptionGenerator.getLawLevelDescription(system.primaryPlanet.lawLevel)))
        TerminalUtils.pprint("Tech: {0:2} - {1}".format(system.primaryPlanet.techLevel, 
            DescriptionGenerator.getTechLevelDescription(system.primaryPlanet.techLevel)))
        print("")
        print("Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(system.primaryPlanet.starport), 
            DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(system.primaryPlanet.starport))))
        starports = ""
        for port in system.primaryPlanet.portsTypes:
            starports += "{}, ".format(port)
        starports = starports[:-2]
        print("Starports: [{}] {} - {}".format(system.primaryPlanet.portsTypesRoll, system.primaryPlanet.portsTypesHighest, starports))
        print("")
        print("Trade Codes: ")
        for tradeCode in system.tradeCodes:
            print("{} - {}".format(tradeCode, SubsectorGenerator.getGetFullTradeCodes(tradeCode)))
    @staticmethod
    def editPlanet(system, planet):
        done=False
        doneWithQuestion = False
        if isinstance(planet, PrimaryPlanet): 
            editPrimary(system)
        elif isinstance(planet, GasGiant): 
            return None
        elif isinstance(planet, AsteroidBelt): 
            while (not done):
                # os.system('cls' if os.name == 'nt' else 'clear')
                print("Editing Asteroid Belt ({}) UWP".format(planet.name))
                print("")
                size = 0
                atmosphere = 0
                hydrographics = 0
                temperature = 0

                population = SectorEditor.setPrimaryAttributeValue("Population", planet.population, 9, 0, 12, DescriptionGenerator.getPopulationDescription, derivation="2D-2")
                government = SectorEditor.setPrimaryAttributeValue("Government", planet.government, 7, 0, 15, DescriptionGenerator.getGovernmentDescription, derivation="2D-7")
                lawLevel = SectorEditor.setPrimaryAttributeValue("Law Level", planet.lawLevel, 4, 0, 15, DescriptionGenerator.getLawLevelDescription, derivation="2D-7+GovernmentCharacteristic")
                # STARPORT
                doneWithQuestion = False
                while(not doneWithQuestion):
                    print("Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(planet.starport), 
                        DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(planet.starport), planet.birthing_cost_per_week)))
                    starportDM = 0
                    if(population >= 10): starportDM+=2
                    elif(population >= 8): starportDM+=1
                    elif(population <= 4): starportDM-=2
                    elif(population <= 2): starportDM-=1
                    portsTypesRoll = 1
                    roll = int(input("Enter a value between 1 and 6 to be added to 6+{} for starport Class (C class or better) $>".format(starportDM)))
                    roll = min(max(0, roll),6)
                    planetStarport = 6 + roll + starportDM
                    if(population == 0): planetStarport = 0
                    birthing_cost_per_week=100
                    refiendFuelCost=500
                    unrefiendFuelCost=100
                    if(population > 0): 
                        print("\nStarport class is {}: {}\n".format(planetStarport, DescriptionGenerator.getStarportClass(planetStarport)))
                        print("1D x Cr1000 for class A, 1D x Cr500 for class B, 1D x Cr100 for class C,  1D x Cr10 for class D, or Cr0 for E and X")
                        value = input("Enter a credit cost for berthing a starship in this system (default {}cr). >".format(starportDM, planetStarport*100))
                        if value in ["", "random"]: 
                            value = planetStarport*100
                        birthing_cost_per_week = int(value)
                        print("Typical Refined fuel costs 500cr, (default 200+1D*50")
                        value = input("Enter Refined Fuel cost. >")
                        if value in ["", "random"]: 
                            value = 200+random.randint(1, 6)*50
                        refiendFuelCost = int(value)
                        print("Typical Unrefined fuel costs 100cr, (default 40+1D*10)")
                        value = input("Enter a Unrefined Fuel cost. >")
                        if value in ["", "random"]: 
                            value = 40+random.randint(1, 6)*10
                        unrefiendFuelCost = int(value)

                    print("Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(planetStarport), 
                        DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(planetStarport), birthing_cost_per_week)))
                    if(TerminalUtils.selectMenuItem(prompt="Is this alright? >").lower() == "yes"):
                        doneWithQuestion=True

                # TECH LEVEL
                minTechLevel = 3
                if(atmosphere in [2, 3, 13, 14]): minTechLevel = 5
                elif(atmosphere in [0, 1, 10, 15]): minTechLevel = 8
                elif(atmosphere in [11]): minTechLevel = 9
                elif(atmosphere in [12]): minTechLevel = 1
                techLevelDM = 0
                if (planetStarport in [10]):   techLevelDM +=6
                elif (planetStarport in [11]): techLevelDM +=4
                elif (planetStarport in [12]): techLevelDM +=2
                if (size in [0, 1]): techLevelDM +=2
                elif (size in [2, 3, 4]): techLevelDM +=1
                if (atmosphere in [1, 2, 3, 4, 10, 11, 12, 13, 14, 15]): techLevelDM +=1
                if (hydrographics in [0, 1]): techLevelDM +=1
                elif (hydrographics in [10]): techLevelDM +=2
                if (population in [1, 2, 3, 4, 5, 8]):   techLevelDM +=1
                elif (population in [9]): techLevelDM +=2
                elif (population in [10]): techLevelDM +=4
                if (government in [0, 5]):   techLevelDM +=1
                elif (government in [7]): techLevelDM +=2
                elif (government in [13, 14]): techLevelDM -=2
                doneWithQuestion = False
                while(not doneWithQuestion):
                    TerminalUtils.pprint("Tech Level: {0:2} - {1}".format(planet.techLevel, 
                        DescriptionGenerator.getTechLevelDescription(planet.techLevel)))
                    TerminalUtils.pprint("BASE NEW TL: {0:2} - {1}".format(minTechLevel + techLevelDM, 
                        DescriptionGenerator.getTechLevelDescription(minTechLevel + techLevelDM)))
                    roll = int(input("Enter a value between 1 and 6 to be added to {} for Tech Level >".format(minTechLevel + techLevelDM)))
                    techLevel = minTechLevel + techLevelDM + roll
                    if(population == 0): techLevel = 0
                    TerminalUtils.pprint("Tech Level: {0:2} - {1}".format(techLevel, 
                        DescriptionGenerator.getTechLevelDescription(techLevel)))
                    if(TerminalUtils.selectMenuItem(prompt="Is this alright? >").lower() == "yes"):
                            doneWithQuestion=True
                systemTradeCodes = []
                if(atmosphere in [4, 5, 6, 7, 8, 9] and hydrographics in [4, 5, 6, 7, 8] and population in [5, 6, 7]): systemTradeCodes.append("Ag")
                if(population == 0 and atmosphere == 0 and hydrographics == 0): systemTradeCodes.append("As")
                if(population == 0 and government == 0 and lawLevel == 0): systemTradeCodes.append("Ba")
                if(hydrographics == 0 and atmosphere >= 2): systemTradeCodes.append("De")
                if(atmosphere >= 10 and techLevel >= 1): systemTradeCodes.append("Fl")
                if(size in [6, 7, 8] and atmosphere in [5, 6, 8] and hydrographics in [5, 6, 7]): systemTradeCodes.append("Ga")
                if(population >= 9): systemTradeCodes.append("Hi")
                if(techLevel >= 12): systemTradeCodes.append("Ht")
                if(hydrographics > 0 and atmosphere in [0, 1]): systemTradeCodes.append("Ie")
                if(atmosphere in [0, 1, 2, 4, 7, 9] and population >= 9): systemTradeCodes.append("In")
                if(population <= 3): systemTradeCodes.append("Lo")
                if(techLevel <= 5): systemTradeCodes.append("Lt")
                if(atmosphere in [0, 1, 2, 3] and hydrographics <= 3 and population >= 6): systemTradeCodes.append("Na")
                if(population in [0, 1, 2, 3, 4, 5, 6]): systemTradeCodes.append("Ni")
                if(hydrographics <= 3): systemTradeCodes.append("Po")
                if(atmosphere in [6,8] and population in [6, 7, 8] and government in [4, 5, 6, 7, 8, 9]): systemTradeCodes.append("Ri")
                if(atmosphere == 0): systemTradeCodes.append("Va")
                if(hydrographics >= 10): systemTradeCodes.append("Wa")

                portsTypesRoll = int(input("Enter a value between 2 and 12 to be added to {} for starport Types Roll >".format(starportDM)))
                portsTypes = []
                portsTypesHighest = random.choice(["N","S","T","R"])
                portsTypes.append(portsTypesHighest)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Presenting the NEW Planet in the {} system".format(system.name))
                print("Size: {0:2} - {1}".format(Utils.hex_key[size], 
                    DescriptionGenerator.getSizeDescription(size)))
                print("Atmo: {0:2} - {1}".format(Utils.hex_key[atmosphere], 
                    DescriptionGenerator.getAtmosphereDescription(atmosphere)))
                print("Temp: {0:<2} - {1}".format(temperature, 
                    DescriptionGenerator.getTemperatureDescription(temperature)))
                print("Hydr: {0:2} - {1}".format(Utils.hex_key[hydrographics], 
                    DescriptionGenerator.getHydrographicsDescription(hydrographics)))
                print("")
                print("Pop.: {0:2} - {1} - x{2}".format(Utils.hex_key[population], 
                    DescriptionGenerator.getPopulationDescription(population), 
                    system.populationModifier))
                TerminalUtils.pprint("Gov.: {0:2} - {1}".format(Utils.hex_key[government], 
                    DescriptionGenerator.getGovernmentDescription(government)))
                TerminalUtils.pprint("Law : {0:2} - {1}".format(Utils.hex_key[lawLevel], 
                    DescriptionGenerator.getLawLevelDescription(lawLevel)))
                TerminalUtils.pprint("Tech: {0:2} - {1}".format(techLevel, 
                    DescriptionGenerator.getTechLevelDescription(techLevel)))
                print("")
                print("Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(planetStarport), 
                    DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(planetStarport), birthing_cost_per_week)))
                starports = ""
                for port in portsTypes:
                    starports += "{}, ".format(port)
                starports = starports[:-2]
                print("Starports: [{}] {} - {}".format(portsTypesRoll, portsTypesHighest, starports))
                print("")
                print("Trade Codes: ")
                for tradeCode in systemTradeCodes:
                    print("{} - {}".format(tradeCode, SubsectorGenerator.getGetFullTradeCodes(tradeCode)))
                if(TerminalUtils.selectMenuItem(options=["No", "Yes"],prompt="About to overwrite. Is this alright? >").lower() == "yes"):
                    done=True
        elif isinstance(planet, Planet): 
            # EDIT STARTS HERE
            # planet.name = input()
            while (not done):
                # os.system('cls' if os.name == 'nt' else 'clear')
                print("Editing Planet ({}) UWP".format(system.name))
                size = SectorEditor.setPrimaryAttributeValue("Size", planet.size, 8, 0, 12, DescriptionGenerator.getSizeDescription, "2D-2")
                atmosphere = SectorEditor.setPrimaryAttributeValue("Atmosphere", planet.atmosphere, 6, 0, 15, DescriptionGenerator.getAtmosphereDescription, derivation="2D-7+size")
                hydrographics = SectorEditor.setPrimaryAttributeValue("Hydrographics", planet.hydrographics, 8, 0, 10, DescriptionGenerator.getHydrographicsDescription, derivation="2D-7+Modifiers")
                temperature = SectorEditor.setPrimaryAttributeValue("Temperature", planet.temperature, 7, 0, 15, DescriptionGenerator.getTemperatureDescription, derivation="2D+Modifiers")

                population = SectorEditor.setPrimaryAttributeValue("Population", planet.population, 9, 0, 12, DescriptionGenerator.getPopulationDescription, derivation="2D-2")
                government = SectorEditor.setPrimaryAttributeValue("Government", planet.government, 7, 0, 15, DescriptionGenerator.getGovernmentDescription, derivation="2D-7")
                lawLevel = SectorEditor.setPrimaryAttributeValue("Law Level", planet.lawLevel, 4, 0, 15, DescriptionGenerator.getLawLevelDescription, derivation="2D-7+GovernmentCharacteristic")
                # STARPORT
                doneWithQuestion = False
                while(not doneWithQuestion):
                    print("Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(planet.starport), 
                        DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(planet.starport), planet.birthing_cost_per_week)))
                    starportDM = 0
                    if(population >= 10): starportDM+=2
                    elif(population >= 8): starportDM+=1
                    elif(population <= 4): starportDM-=2
                    elif(population <= 2): starportDM-=1
                    portsTypesRoll = 1
                    roll = int(input("Enter a value between 2 and 12 to be added to {} for starport Class >".format(starportDM)))
                    planetStarport = roll + starportDM
                    if(population == 0): planetStarport = 0
                    birthing_cost_per_week=0
                    refiendFuelCost=500
                    unrefiendFuelCost=100
                    if(population > 0): 
                        print("\nStarport class is {}: {}\n".format(planetStarport, DescriptionGenerator.getStarportClass(planetStarport)))
                        print("1D x Cr1000 for class A, 1D x Cr500 for class B, 1D x Cr100 for class C,  1D x Cr10 for class D, or Cr0 for E and X")
                        value = input("Enter a credit cost for berthing a starship in this system (default {}cr). >".format(starportDM, planetStarport*100))
                        if value in ["", "random"]: 
                            value = planetStarport*100
                        birthing_cost_per_week = int(value)
                        print("Typical Refined fuel costs 500cr, (default 200+1D*50")
                        value = input("Enter Refined Fuel cost. >")
                        if value in ["", "random"]: 
                            value = 200+random.randint(1, 6)*50
                        refiendFuelCost = int(value)
                        print("Typical Unrefined fuel costs 100cr, (default 40+1D*10)")
                        value = input("Enter a Unrefined Fuel cost. >")
                        if value in ["", "random"]: 
                            value = 40+random.randint(1, 6)*10
                        unrefiendFuelCost = int(value)

                    print("Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(planetStarport), 
                        DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(planetStarport), birthing_cost_per_week)))
                    if(TerminalUtils.selectMenuItem(prompt="Is this alright? >").lower() == "yes"):
                        doneWithQuestion=True

                # TECH LEVEL
                minTechLevel = 3
                if(atmosphere in [2, 3, 13, 14]): minTechLevel = 5
                elif(atmosphere in [0, 1, 10, 15]): minTechLevel = 8
                elif(atmosphere in [11]): minTechLevel = 9
                elif(atmosphere in [12]): minTechLevel = 1
                techLevelDM = 0
                if (planetStarport in [10]):   techLevelDM +=6
                elif (planetStarport in [11]): techLevelDM +=4
                elif (planetStarport in [12]): techLevelDM +=2
                if (size in [0, 1]): techLevelDM +=2
                elif (size in [2, 3, 4]): techLevelDM +=1
                if (atmosphere in [1, 2, 3, 4, 10, 11, 12, 13, 14, 15]): techLevelDM +=1
                if (hydrographics in [0, 1]): techLevelDM +=1
                elif (hydrographics in [10]): techLevelDM +=2
                if (population in [1, 2, 3, 4, 5, 8]):   techLevelDM +=1
                elif (population in [9]): techLevelDM +=2
                elif (population in [10]): techLevelDM +=4
                if (government in [0, 5]):   techLevelDM +=1
                elif (government in [7]): techLevelDM +=2
                elif (government in [13, 14]): techLevelDM -=2
                doneWithQuestion = False
                while(not doneWithQuestion):
                    TerminalUtils.pprint("Tech Level: {0:2} - {1}".format(planet.techLevel, 
                        DescriptionGenerator.getTechLevelDescription(planet.techLevel)))
                    TerminalUtils.pprint("BASE NEW TL: {0:2} - {1}".format(minTechLevel + techLevelDM, 
                        DescriptionGenerator.getTechLevelDescription(minTechLevel + techLevelDM)))
                    roll = int(input("Enter a value between 1 and 6 to be added to {} for Tech Level >".format(minTechLevel + techLevelDM)))
                    techLevel = minTechLevel + techLevelDM + roll
                    if(population == 0): techLevel = 0
                    TerminalUtils.pprint("Tech Level: {0:2} - {1}".format(techLevel, 
                        DescriptionGenerator.getTechLevelDescription(techLevel)))
                    if(TerminalUtils.selectMenuItem(prompt="Is this alright? >").lower() == "yes"):
                            doneWithQuestion=True
                systemTradeCodes = []
                if(atmosphere in [4, 5, 6, 7, 8, 9] and hydrographics in [4, 5, 6, 7, 8] and population in [5, 6, 7]): systemTradeCodes.append("Ag")
                if(population == 0 and atmosphere == 0 and hydrographics == 0): systemTradeCodes.append("As")
                if(population == 0 and government == 0 and lawLevel == 0): systemTradeCodes.append("Ba")
                if(hydrographics == 0 and atmosphere >= 2): systemTradeCodes.append("De")
                if(atmosphere >= 10 and techLevel >= 1): systemTradeCodes.append("Fl")
                if(size in [6, 7, 8] and atmosphere in [5, 6, 8] and hydrographics in [5, 6, 7]): systemTradeCodes.append("Ga")
                if(population >= 9): systemTradeCodes.append("Hi")
                if(techLevel >= 12): systemTradeCodes.append("Ht")
                if(hydrographics > 0 and atmosphere in [0, 1]): systemTradeCodes.append("Ie")
                if(atmosphere in [0, 1, 2, 4, 7, 9] and population >= 9): systemTradeCodes.append("In")
                if(population <= 3): systemTradeCodes.append("Lo")
                if(techLevel <= 5): systemTradeCodes.append("Lt")
                if(atmosphere in [0, 1, 2, 3] and hydrographics <= 3 and population >= 6): systemTradeCodes.append("Na")
                if(population in [0, 1, 2, 3, 4, 5, 6]): systemTradeCodes.append("Ni")
                if(hydrographics <= 3): systemTradeCodes.append("Po")
                if(atmosphere in [6,8] and population in [6, 7, 8] and government in [4, 5, 6, 7, 8, 9]): systemTradeCodes.append("Ri")
                if(atmosphere == 0): systemTradeCodes.append("Va")
                if(hydrographics >= 10): systemTradeCodes.append("Wa")

                portsTypesRoll = int(input("Enter a value between 2 and 12 to be added to {} for starport Types Roll >".format(starportDM)))
                portsTypes = []
                portsTypesHighest = random.choice(["N","S","T","R"])
                portsTypes.append(portsTypesHighest)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Presenting the NEW Primary Planet in the {} system".format(system.name))
                print("Size: {0:2} - {1}".format(Utils.hex_key[size], 
                    DescriptionGenerator.getSizeDescription(size)))
                print("Atmo: {0:2} - {1}".format(Utils.hex_key[atmosphere], 
                    DescriptionGenerator.getAtmosphereDescription(atmosphere)))
                print("Temp: {0:<2} - {1}".format(temperature, 
                    DescriptionGenerator.getTemperatureDescription(temperature)))
                print("Hydr: {0:2} - {1}".format(Utils.hex_key[hydrographics], 
                    DescriptionGenerator.getHydrographicsDescription(hydrographics)))
                print("")
                print("Pop.: {0:2} - {1} - x{2}".format(Utils.hex_key[population], 
                    DescriptionGenerator.getPopulationDescription(population), 
                    system.populationModifier))
                TerminalUtils.pprint("Gov.: {0:2} - {1}".format(Utils.hex_key[government], 
                    DescriptionGenerator.getGovernmentDescription(government)))
                TerminalUtils.pprint("Law : {0:2} - {1}".format(Utils.hex_key[lawLevel], 
                    DescriptionGenerator.getLawLevelDescription(lawLevel)))
                TerminalUtils.pprint("Tech: {0:2} - {1}".format(techLevel, 
                    DescriptionGenerator.getTechLevelDescription(techLevel)))
                print("")
                print("Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(planetStarport), 
                    DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(planetStarport), birthing_cost_per_week)))
                starports = ""
                for port in portsTypes:
                    starports += "{}, ".format(port)
                starports = starports[:-2]
                print("Starports: [{}] {} - {}".format(portsTypesRoll, portsTypesHighest, starports))
                print("")
                print("Trade Codes: ")
                for tradeCode in systemTradeCodes:
                    print("{} - {}".format(tradeCode, SubsectorGenerator.getGetFullTradeCodes(tradeCode)))
                if(TerminalUtils.selectMenuItem(options=["No", "Yes"],prompt="About to overwrite. Is this alright? >").lower() == "yes"):
                    done=True
            # SAVE TO SYSTEM
        planet.size = size
        planet.atmosphere = atmosphere
        planet.hydrographics = hydrographics
        planet.temperature = temperature
        planet.population = population
        planet.government = government
        planet.lawLevel = lawLevel
        planet.starport = planetStarport
        planet.birthing_cost_per_week = birthing_cost_per_week
        planet.refiendFuelCost = refiendFuelCost
        planet.unrefiendFuelCost = unrefiendFuelCost
        planet.techLevel = techLevel
        system.systemTradeCodes = list(set(system.systemTradeCodes+systemTradeCodes))
        system.systemTradeCodes.sort()
        if isinstance(planet, AsteroidBelt):
            for moon in planet.moons: 
                asteroidMoonPopulation = planet.population
                if asteroidMoonPopulation > 1:
                    asteroidMoonPopulation = random.choice(range(asteroidMoonPopulation-assigned_population))
                if assigned_population == planet.population and planet.population < 1:
                    asteroidMoonPopulation = 0
                else:
                    asteroidMoonPopulation = 1
                assigned_population += asteroidMoonPopulation

            moon.government = government
            moon.lawLevel = lawLevel
            moon.starport = planetStarport
            moon.birthing_cost_per_week = birthing_cost_per_week
            moon.refiendFuelCost = refiendFuelCost
            moon.unrefiendFuelCost = unrefiendFuelCost
            moon.techLevel = techLevel

        # Display Results
        print("Planet: {}, {} system ".format(planet.name, system.name))
        print("Size: {0:2} - {1}".format(Utils.hex_key[planet.size], 
            DescriptionGenerator.getSizeDescription(planet.size)))
        print("Atmo: {0:2} - {1}".format(Utils.hex_key[planet.atmosphere], 
            DescriptionGenerator.getAtmosphereDescription(planet.atmosphere)))
        print("Temp: {0:<2} - {1}".format(planet.temperature, 
            DescriptionGenerator.getTemperatureDescription(planet.temperature)))
        print("Hydr: {0:2} - {1}".format(Utils.hex_key[planet.hydrographics], 
            DescriptionGenerator.getHydrographicsDescription(planet.hydrographics)))
        print("")
        print("Pop.: {0:2} - {1} - x{2}".format(Utils.hex_key[planet.population], 
            DescriptionGenerator.getPopulationDescription(planet.population), 
            system.populationModifier))
        TerminalUtils.pprint("Gov.: {0:2} - {1}".format(Utils.hex_key[planet.government], 
            DescriptionGenerator.getGovernmentDescription(planet.government)))
        TerminalUtils.pprint("Law : {0:2} - {1}".format(Utils.hex_key[planet.lawLevel], 
            DescriptionGenerator.getLawLevelDescription(planet.lawLevel)))
        TerminalUtils.pprint("Tech: {0:2} - {1}".format(planet.techLevel, 
            DescriptionGenerator.getTechLevelDescription(planet.techLevel)))
        print("")
        print("Starport: {0} - {1}".format(SubsectorGenerator.getStarportClass(planet.starport), 
            DescriptionGenerator.getStarportDescription(SubsectorGenerator.getStarportClass(planet.starport))))
    @staticmethod
    def editSystemLeadership(system):
        hex_key=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        done=False
        doneWithQuestion = False
        while (not done):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Editing Primary Planet ({}) Leadership".format(system.name))


            alignment = TerminalUtils.selectMenuItem(options=["3rd Imperium", "Non-Aligned, Human-dominated", "Non-Aligned", "Other"], prompt="Select an option. >")
            alignmentShort = "Im"
            if alignment == "Non-Aligned, Human-dominated": alignmentShort = "NaHu"
            elif alignment == "Non-Aligned": alignmentShort = "NaXX"


            print("System Noble House:")

            system.nobleLeader = input("Enter 5 character Noble Extention")
            system.alignment = alignmentShort
            travelcode = TerminalUtils.selectMenuItem(options=["Amber", "Restricted", "Open"], prompt="Select an option. >")[0]
            system.travelCode =  travelcode if travelcode in ["A", "R"] else ""
            system.systemDict["system travel code"] = system.travelCode
            system.systemDict["system alignment"] = system.alignment
            system.systemDict["system noble leader"] = system.nobleLeader
            if(TerminalUtils.selectMenuItem(prompt="Is this alright? >").lower() == "yes"):
                done=True
    @staticmethod
    def updateSystemDictionary(system):
        system.systemDict["system trade codes"] = system.tradeCodes

        system.systemDict["primary size"] = system.primaryPlanet.size 
        system.systemDict["primary atmosphere"] = system.primaryPlanet.atmosphere 
        system.systemDict["primary hydrographics"] = system.primaryPlanet.hydrographics 
        system.systemDict["primary temperature"] = system.primaryPlanet.temperature
        system.systemDict["primary population"] = system.primaryPlanet.population 
        system.systemDict["primary government"] = system.primaryPlanet.government
        system.systemDict["primary law level"] = system.primaryPlanet.lawLevel
        system.systemDict["primary starport"] = system.primaryPlanet.starport 
        system.systemDict["primary tech level"] = system.primaryPlanet.techLevel 
    @staticmethod
    def swapSystemBodies(system):
        print("stubbed")
        input("Press any key to continue...")
    @staticmethod
    def editTextField(obj, editableObject, title):
        done=False
        editDescriptionMenu = [
            "View {}".format(title), 
            "Add {} Entry".format(title), 
            "Edit {} Entry".format(title), 
            "Remove {} Entry".format(title), 
            "Back"]
        while(not done):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(title)
            selection = TerminalUtils.selectMenuItem(editDescriptionMenu, "Select an option. >")
            if(selection == "Back"):  
                pass 
                done=True
            elif(selection == editDescriptionMenu[0]): 
                os.system('cls' if os.name == 'nt' else 'clear')
                print(title)
                for entry in editableObject:
                    TerminalUtils.pprint("{}:\n{}".format(entry[0], entry[1]), width=100)
                input("Press enter to continue...")
            elif(selection == editDescriptionMenu[1]): 
                os.system('cls' if os.name == 'nt' else 'clear')
                print(editableObject)
                entryName = input("New Entry Name? >")
                entryText = input("Write or Paste text for entry: >")
                entry = [entryName,entryText]
                editableObject.append(entry)
                print("Entry {} Added".format(entryName))
            elif(selection == editDescriptionMenu[2]): 
                os.system('cls' if os.name == 'nt' else 'clear')
                print(str(editableObject))
                entryNames=[]
                entries=[]
                for entry in editableObject:
                    entryNames.append(entry[0])
                    entries.append(entry[1])
                entryName = selectMenuItem(options=entryNames+["Back"], prompt="Select an Entry. >")
                if(selection == "Back"): continue
                entryIndex = entryNames.index(entryName)
                editableObject[entryIndex][1] = input("Write or Paste text for entry: >")
                print("Entry {} Edit Complete".format(entryName))
            elif(selection == editDescriptionMenu[3]): 
                os.system('cls' if os.name == 'nt' else 'clear')
                entryNames=[]
                entries=[]
                for entry in editableObject:
                    entryNames.append(entry[0])
                    entries.append(entry[1])
                entryName = TerminalUtils.selectMenuItem(options=entryNames+["Back"], prompt="Select an Entry. >")
                if(selection == "Back"): continue
                entryIndex = entryNames.index(entryName)
                editableObject.remove(entryIndex)
                print("Entry {} Removed".format(entryName))
    @staticmethod
    def performSystemRename(new_name, sector, system, viewer):
        old_name = system.name
        subsector = system.subsectorParent
        if old_name in subsector.systems.keys():
            subsector.systems[new_name] = subsector.systems[old_name]
        system.star.name = new_name
        system.name = new_name
        system.primaryPlanet.name = new_name
        if system.primaryPlanet.moons is not None:
            for moon in system.primaryPlanet.moons:
                if old_name in moon.name:
                    if " " in moon.name:
                        parts = moon.name.split(" ")
                        moon.name = new_name + " " + parts[1]
                    else:
                        moon.name = new_name
        system.systemDict["name"] = new_name
        for body in system.systemLineup:
            if body is not None and body is not system.star and body is not system.primaryPlanet:
                parts = body.name.split(" ")
                body.name = new_name + " " + parts[1]
                if body.moons is not None:
                    for moon in body.moons:
                        if old_name in moon.name:
                            # print(new_name)
                            # print(moon.name)
                            parts = moon.name.split(" ")
                            # print(parts)
                            moon.name = new_name + " " + parts[1]
                            # print(moon.name)
                            # input("")
    @staticmethod
    def addPlanetToSystem(system):
        planet_type = TerminalUtils.selectMenuItem(options=["Planet", "Asteroid Belt", "Jovian", "random", "Nevermind"], prompt="Select an option. $>")
        if planet_type == "Nevermind": 
            return None
        if planet_type == "Jovian":
            done = False
            while planet_type.lower() == "random":
                planet_type = random.choice(["Planet", "Asteroid Belt", "Jovian"])
                print("Random Selection: {}".format(planet_type))
                if selectMenuItem(options=["Yes", "No"], prompt="Is it Okay to add a {}? $>".format(planet_type)) =="No":
                    planet_type = "random"
        if planet_type == "Jovian":
            pass
        elif planet_type == "Asteroid Belt":
            pass
        elif planet_type == "Planet": 
            planet_name = input("What is the planet Name? $>")
            planet_size = int(input("What is the planet's size? (0-10) $>"))
            planet_atmosphere = int(input("What is the planet's atmosphere? (0-15) $>"))
            planet_hydrographics = int(input("What is the planet's hydrographics? (0-10) $>"))
            planet_temperature = int(input("What is the planet's temperature? (2-12) $>"))
            planet_population = int(input("What is the planet's population? (0-12) $>"))
            if planet_population > 0:
                planet_government = int(input("What is the planet's government? (0-15) $>"))
                planet_law = int(input("What is the planet's law level? (0-9) $>"))
                min_tech_level = 3
                if planet_atmosphere in [0, 1, 10, 15]: min_tech_level = 8
                elif planet_atmosphere in [2, 5, 13, 14]: min_tech_level = 5
                elif planet_atmosphere in [11]: min_tech_level = 9
                elif planet_atmosphere in [12]: min_tech_level = 10
                value = int(input("What is the planet's tech level (min {})? (0-10) $>".format(min_tech_level)))
                planet_tech = max(0, min(value, min_tech_level3))
                planet_starport = int(input("What is the planet's starport rating? (0-10) $>"))
                if planet_starport > 4:
                    planet_berthing = int(input("What is the planet's berthing cost? $>"))
                    if value == "": value = planetStarport*100
                    value = input("What is the planet's refined fuel cost? $>")
                    if value == "": value = 200+random.randint(1, 6)*50
                    planet_refined_fuel_cost = int(value)
                    value = input("What is the planet's unrefined fuel cos? $>")
                    if value == "": value = 40+random.randint(1, 6)*10
                    planet_unrefined_fuel_cost = int(value)
            plnaet_dict = {
                            "{} size".format(planet_name): planet_size, "{} atmosphere".format(planet_name): planet_atmosphere, 
                            "{} hydrographics".format(planet_name): planet_hydrographics, "{} temperature".format(planet_name): planet_temperature, 
                            "{} population".format(planet_name): planet_population, "{} government".format(planet_name): planet_government, 
                            "{} law level".format(planet_name): planet_law, "{} tech level".format(planet_name): planet_tech,
                            "{} starport".format(planet_name): planet_starport,  
                            "{} berthing cost".format(planet_name):planet_berthing,
                            "{} refined fuel".format(planet_name):planet_refined_fuel_cost,
                            "{} unrefined fuel".format(planet_name):planet_unrefined_fuel_cost
                            }
            planet = Planet(plnaet_dict, planet_name)
            # non prime Moons.
            numberNonPrimaryMoons = int(input("How manu moons does this planet have? (1-4) $>"))
            if (non_prime_planet.moons is None): 
                non_prime_planet.moons = []
            for i in range(numberNonPrimaryMoons):
                moon = None
                moonSize = 0
                if non_prime_planet.size >= 4:
                    moonSize = random.randint(0, int(non_prime_planet.size * 0.75) )
                moonAtmo = moonSize - 2
                moonTemp = 2
                if(moonSize in [0, 1, 2]): moonAtmo = 0
                elif(moonSize in [3, 4] and moonAtmo in [0, 1, 2]): moonAtmo = 0
                elif(moonSize in [3, 4] and moonAtmo in [3, 4, 5]): moonAtmo = 1
                elif(moonSize in [3, 4] and moonAtmo >= 6): moonAtmo = 10
                moonHydro = random.choice([0,0,0,0,0,1])
                moonTechLevel = primaryPlanet.techLevel
                moonDict = {
                        "{}-{} size".format(planet_name,i+1): moonSize, "{}-{} atmosphere".format(planet_name,i+1): moonAtmo, 
                        "{}-{} hydrographics".format(planet_name,i+1): moonHydro, "{}-{} temperature".format(planet_name,i+1): moonTemp, 
                        "{}-{} population".format(planet_name,i+1): 0, "{}-{} government".format(planet_name,i+1): 0, 
                        "{}-{} law level".format(planet_name,i+1): 0, "{}-{} tech level".format(planet_name,i+1): moonTechLevel,
                        "{}-{} starport".format(planet_name,i+1): 0,  
                        "{}-{} berthing cost".format(planet_name,i+1):planet_berthing,
                        "{}-{} refined fuel".format(planet_name,i+1):planet_refined_fuel_cost,
                        "{}-{} unrefined fuel".format(planet_name,i+1):planet_unrefined_fuel_cost
                        }
                
                planet.add_orbiting_body(  Moon( moonDict, "{}-{}".format(planet_name,i+1) ) )
            print(system.systemLineup)
            available_slots = []
            for i in range(len(system.systemLineup)):
                if system.systemLineup[i] is None:
                    available_slots.append(i)
            planet_loc = TerminalUtils.selectMenuItem(options=available_slots+["Nevermind"], prompt="Select an option. $>")
            if planet_loc == "Nevermind": return None
            system.systemLineup[planet_loc] = planet
    @staticmethod
    def add_system(sector):
        pass
        pass
    @staticmethod
    def set_primary_planet(
            system, 
            name, 
            size, 
            atmosphere, 
            hydrographics, 
            temperature, 
            population, 
            government, 
            lawLevel, 
            starports, birthing_cost_per_week, refined_fueling_cost, unrefined_fueling_cost,
            techLevel,
            moons=[], 
            keep_moons=False
    ):
        loc = system.systemLineup.index(system.primaryPlanet)
        system.name = name
        system.star.name = name
        system.systemDict["name"] = name
        system.systemDict["primary size"] = size
        system.systemDict["primary atmosphere"] = atmosphere
        system.systemDict["primary hydrographics"] = hydrographics
        system.systemDict["primary temperature"] = temperature
        system.systemDict["primary population"] = population 
        system.systemDict["primary government"] = government 
        system.systemDict["primary law level"] = lawLevel
        system.systemDict["primary starport"] = starports
        system.systemDict["primary berthing cost"] = birthing_cost_per_week
        system.systemDict["primary refined fuel"] = refined_fueling_cost
        system.systemDict["primary unrefined fuel"] = unrefined_fueling_cost
        system.systemDict["primary tech level"] = techLevel
        if keep_moons:
            system.systemDict["primary moons"] = system.primaryPlanet.moons
        else:
            system.systemDict["primary moons"] = moons
        SubsectorGenerator.determine_travel_codes(system.systemDict)
        SubsectorGenerator.regenerate_existing_travel_codes(system)

        system.primaryPlanet = PrimaryPlanet(system.systemDict)
        system.systemLineup[loc] = system.primaryPlanet
        system.primaryPlanet.name = name
        system.primaryPlanet.size = size
        system.primaryPlanet.atmosphere = atmosphere
        system.primaryPlanet.hydrographics = hydrographics
        system.primaryPlanet.temperature = temperature
        system.primaryPlanet.population = population
        system.primaryPlanet.government = government
        system.primaryPlanet.lawLevel = lawLevel
        system.primaryPlanet.techLevel = techLevel
        system.primaryPlanet.starports = starports
        system.primaryPlanet.birthing_cost_per_week = birthing_cost_per_week
        system.primaryPlanet.refined_fueling_cost = refined_fueling_cost
        system.primaryPlanet.unrefined_fueling_cost = unrefined_fueling_cost
        system.primaryPlanet.uwp = system.primaryPlanet.displayUwpCode()
        system.primaryPlanet.upp = system.primaryPlanet.displayUppCode()
        system.uwp = system.primaryPlanet.uwp
        system.upp = system.primaryPlanet.upp
    @staticmethod
    def transformPrimaryInSystemToPreset(planet_to_be_changed, sector, system, viewer):
        if (planet_to_be_changed.lower() in ["thalassa"]): # B88A889-8
            new_name = "Thalassa"
            keep_moons=len(system.primaryPlanet.moons) > 0
            SectorEditor.performSystemRename(new_name, sector, system, viewer)
            SectorEditor.set_primary_planet(
                system, 
                name = new_name, 
                size = 8, # Earth-like
                atmosphere = 8, # Dense. breathable
                hydrographics = 10, # 76%-85% Water world
                temperature = 8, # Temperate 0-30
                population = 8, # Hundreds of millions
                government = 8, # Civil Service Bureaucracy
                lawLevel = 8,  # All bladed weapons, stunners
                starports = 9,  # B class. Good. 1D x Cr500. Refined Fuel. Shipyard (spacecraft) Repair
                birthing_cost_per_week = 1000, 
                refined_fueling_cost = 500, 
                unrefined_fueling_cost = 100,
                techLevel = 9, # TL 9 (Pre-Stellar)
                moons=[], keep_moons=keep_moons,
                ) 
            wanted_moons = 1
            if not keep_moons:
                for i in range(wanted_moons):
                    moonSize = random.choice([0, 0, 1, 1, 1, 2, 2, 3, 3, 3])
                    moonAtmo = max(0, min(moonSize-2, 2))
                    moonHydro =  random.choice([0, 0, 1, 1, 1, 2, 2])
                    moonTemp = 0
                    moonPopulation = 0
                    moonGovernment = 0
                    moonLaw = 0
                    moonTech = 0
                    moonStarport = 0
                    moonDict = {
                                "{}-{} size".format(system.primaryPlanet.name,i+1): moonSize, "{}-{} atmosphere".format(system.primaryPlanet.name,i+1): moonAtmo, 
                                "{}-{} hydrographics".format(system.primaryPlanet.name,i+1): moonHydro, "{}-{} temperature".format(system.primaryPlanet.name,i+1): moonTemp, 
                                "{}-{} population".format(system.primaryPlanet.name,i+1): moonPopulation, "{}-{} government".format(system.primaryPlanet.name,i+1): moonGovernment, 
                                "{}-{} law level".format(system.primaryPlanet.name,i+1): moonLaw, "{}-{} tech level".format(system.primaryPlanet.name,i+1): moonTech,
                                "{}-{} starport".format(system.primaryPlanet.name,i+1): moonStarport,  
                                }
                    system.primaryPlanet.add_orbiting_body( Moon( moonDict, "{}-{}".format(system.primaryPlanet.name,i+1) ) )
            system.primaryPlanet.description = [
                ("Overview","Thalassa (TR 1613) is a rich water world with a moderate population over a hundred million, but not yet at a billion sophonts in population size."),
                ("World-outlook", "This is a rich world with a prosperous and thriving world economy. "+
                    "This world has high-grade living conditions with a good climate and a non-harmful environment. "+
                    "As such, this world is much sought after with large queues for immigration here. "+
                    "Most observers think that the planet's economy and population will prosper in the near future barring outside forces.")
                ]
            system.primaryPlanet.notes = [

                ]
            system.primaryPlanet.history = [

                ]
            system.megacorpsPresence = [
                ("GeDeCo", "The General Development Corperation maintains a presence on Thalassa. "+
                    "They trade with and employ the inhabitants."),
                ]
            system.primaryPlanet.add_settlement(Settlement(  
                "Thalassa", 
                "Startown-Capital", 
                int(3*0.4*DescriptionGenerator.getPopulationTotal(system.primaryPlanet.population)), 
                "The downport is in a flat suburb of the Capital city on an Island around the equatorial region of the planet.", 
                "Integrated",
                ["Auto-vehicles", "Aircraft", "Gravcraft", "Powered Ships/Submarines", "Spacecraft"]
                ))
            # system.primaryPlanet.add_area_of_interest(AreaOfIntersest(
            #     name, 
            #     area_type, 
            #     system.primaryPlanet, 
            #     description, 
            #     is_dungeon
            #     ))
        elif (planet_to_be_changed.lower() in ["homestead"]): # D560250-6 -> D761351-6
            new_name = "Homestead"
            keep_moons=len(system.primaryPlanet.moons) > 0
            SectorEditor.performSystemRename(new_name, sector, system, viewer)
            SectorEditor.set_primary_planet(
                system, 
                name = new_name, 
                size = 7, # .9 g
                atmosphere = 6, # Standard
                hydrographics = 1, # Desert world / 3 Small seas and oceans.
                temperature = 9, # 7 Temperate 0-30
                population = 2, # 2 / 3 Hundreds -> Thousands
                government = 5, # 5 / 5 Feudal TechnocracyRuling functions are performed by specific individuals for persons who agree to be ruled by them. 
                                # Relationships are based on the performance of technical activities which are mutually beneficial
                lawLevel = 1, # No restrictions – heavy armour and a handy weapon recommended…
                starports = 6, # D class. Poor. 1D x Cr10. Unrefined Fuel. Limited Repair
                birthing_cost_per_week = 30, # 1D x Cr500 # Open air Starport
                refined_fueling_cost = None, # Unavailable
                unrefined_fueling_cost = 100, # 100
                techLevel = 6, # TL 6 (Industrial)
                moons=[], keep_moons=keep_moons,
                )
            if not keep_moons:
                for i in range(wanted_moons):
                    moonSize = random.choice([0, 0, 1, 1, 1, 2, 2, 3, 3, 3])
                    moonAtmo = max(0, min(moonSize-2, 2))
                    moonHydro =  random.choice([0, 0, 1, 1, 1, 2, 2])
                    moonTemp = 0
                    moonPopulation = 0
                    moonGovernment = 0
                    moonLaw = 0
                    moonTech = 0
                    moonStarport = 0
                    moonDict = {
                                "{}-{} size".format(system.primaryPlanet.name,i+1): moonSize, "{}-{} atmosphere".format(system.primaryPlanet.name,i+1): moonAtmo, 
                                "{}-{} hydrographics".format(system.primaryPlanet.name,i+1): moonHydro, "{}-{} temperature".format(system.primaryPlanet.name,i+1): moonTemp, 
                                "{}-{} population".format(system.primaryPlanet.name,i+1): moonPopulation, "{}-{} government".format(system.primaryPlanet.name,i+1): moonGovernment, 
                                "{}-{} law level".format(system.primaryPlanet.name,i+1): moonLaw, "{}-{} tech level".format(system.primaryPlanet.name,i+1): moonTech,
                                "{}-{} starport".format(system.primaryPlanet.name,i+1): moonStarport,  
                                }
                    system.primaryPlanet.add_orbiting_body( Moon( moonDict, "{}-{}".format(system.primaryPlanet.name,i+1) ) )
            system.primaryPlanet.description = [
                ("Book Summary", "In the days of the previous Empire, Homestead was a garden world named Synre and had a population in the billions. "+
                "Now, it is a blasted ruin filled desert, testament to the carnage of the fall of the previous empire. It was recently " +
                "recolonized by a few hardy settlers from the quadrant, who survive by mining metals from the ruined cities. "+
                "The night skies of Homestead are beautiful - shot through by thousands of shooting stars from the ring of debris that still surrounds the planet."),
                ] 
            system.primaryPlanet.notes = [
                ("Mining Operation", "There is a mining operation staffed by locals that they use to barter for goods with GeDeCo."),
                ("Bandits", "There are bandits that are made up of those banished by the town and they may work with pirates to raid the local towns and villages."),
                ]
            system.primaryPlanet.history = [
                ("Past", "In the days of the previous Empire, Homestead was a garden world named Synre and had a population in the billions. "),
                ("Recent", "Now, it is a blasted ruin filled desert, testament to the carnage of the fall of the previous empire. It was recently " +
                "recolonized by a few hardy settlers from the quadrant, who survive by mining metals from the ruined cities. "),
                ]
            system.megacorpsPresence = [
                ("GeDeCo", "The General Development Corperation maintains a presence on Homestead. "+
                    "They trade with the miners for ore and in exchange bring technology."),
                ]
            system.primaryPlanet.add_settlement(Settlement( 
                "Downport", 
                "Downport", 
                int(2*0.2*DescriptionGenerator.getPopulationTotal(system.primaryPlanet.population)),
                "", 
                "Isolated",
                ["Riding beasts", "Mag-lev Train", "Spacecraft", "Aircraft", "Auto-vehicles"]
                ))
            system.primaryPlanet.add_settlement(Settlement( 
                "Binyamin", 
                "Mining", 
                int(5*0.6*DescriptionGenerator.getPopulationTotal(system.primaryPlanet.population)),
                "", 
                "Isolated",
                ["Riding beasts", "Mag-lev Train", "Spacecraft", "Aircraft", "Auto-vehicles"]
                ))
            # system.primaryPlanet.add_area_of_interest(AreaOfIntersest(
            #     name, 
            #     area_type, 
            #     system.primaryPlanet, 
            #     description, 
            #     is_dungeon
            #     ))
        elif (planet_to_be_changed.lower() in ["bt-sht 365", "vamarda", "vamarda-0"]): # B773566-C / 0770000-0
            new_name = "BT-SHT 365"
            keep_moons=len(system.primaryPlanet.moons) > 0
            SectorEditor.performSystemRename(new_name, sector, system, viewer)
            SectorEditor.set_primary_planet(
                system, 
                name = new_name, 
                size = 7, # .9 g
                atmosphere = 7, # Standard, Tainted
                hydrographics = 0, # Desert world / 3 Small seas and oceans.
                temperature = 7, # 7 Temperate 0-30
                population = 0, # 0 / Millions
                government = 0, # 0 / 11 Non-Charismatic Leader: hereditary king/queen-ship
                lawLevel = 0,  # All firearms except shotguns & stunners; carrying weapons discouraged
                starports = 0,  # No port / B class. Good. 1D x Cr500. Refined Fuel. Shipyard (spacecraft) Repair
                birthing_cost_per_week = 0, # 1D x Cr500
                refined_fueling_cost = 0, # 500
                unrefined_fueling_cost = 0, # 100
                techLevel = 0, # TL 0 (Primitive): No technology / TL 12 (Average Stellar)
                moons=[], keep_moons=keep_moons,
                ) 
            wanted_moons = 1
            if not keep_moons:
                for i in range(wanted_moons):
                    moonSize = random.choice([0, 0, 1, 1, 1, 2, 2, 3, 3, 3])
                    moonAtmo = max(0, min(moonSize-2, 2))
                    moonHydro =  random.choice([0, 0, 1, 1, 1, 2, 2])
                    moonTemp = 0
                    moonPopulation = 0
                    moonGovernment = 0
                    moonLaw = 0
                    moonTech = 0
                    moonStarport = 0
                    moonDict = {
                                "{}-{} size".format(system.primaryPlanet.name,i+1): moonSize, "{}-{} atmosphere".format(system.primaryPlanet.name,i+1): moonAtmo, 
                                "{}-{} hydrographics".format(system.primaryPlanet.name,i+1): moonHydro, "{}-{} temperature".format(system.primaryPlanet.name,i+1): moonTemp, 
                                "{}-{} population".format(system.primaryPlanet.name,i+1): moonPopulation, "{}-{} government".format(system.primaryPlanet.name,i+1): moonGovernment, 
                                "{}-{} law level".format(system.primaryPlanet.name,i+1): moonLaw, "{}-{} tech level".format(system.primaryPlanet.name,i+1): moonTech,
                                "{}-{} starport".format(system.primaryPlanet.name,i+1): moonStarport,  
                                }
                    system.primaryPlanet.add_orbiting_body( Moon( moonDict, "{}-{}".format(system.primaryPlanet.name,i+1) ) )
            for body in system.systemLineup:
                if body is not None and not isinstance(body, Star) and not isinstance(body, GasGiant):
                    body.population = 0
                    body.government = 0
                    body.lawLevel = 0
                    body.starports = 0
            system.primaryPlanet.description = [
                ("Summary", "Now the planet is mostly a blasted moonscape with tainted atmosphere."),
                ] 
            system.primaryPlanet.notes = [
                ("Former Glory", "In the days of the previous Empire, BT-SHT 365 was a garden world named Vamarda and had a population in the billions with high technology."),
                ]
            system.primaryPlanet.history = [
                ("Past", "In the days of the previous Empire, BT-SHT 365 was a garden world named Vamarda and had a population in the billions with high technology. "),
                ("Recent", "Now the planet is mostly a blasted moonscape with tainted atmosphere. "),
                ]
            system.megacorpsPresence = [
                ("GeDeCo", "The General Development Corperation maintains a presence on BT-SHT 365. "+
                    "They occupy the capital of Carellon for some purpose."),
                ]
            system.primaryPlanet.add_settlement(Settlement( 
                "Carellon", 
                "Capital", 
                0,
                "", 
                "Isolated",
                []
                ))
            # system.primaryPlanet.add_area_of_interest(AreaOfIntersest(
            #     name, 
            #     area_type, 
            #     system.primaryPlanet, 
            #     description, 
            #     is_dungeon
            #     ))
        elif (planet_to_be_changed.lower() in ["vamarda-1"]): # B773566-C / 0770000-0
            new_name = "Vamarda"
            keep_moons=len(system.primaryPlanet.moons) > 0
            SectorEditor.performSystemRename(new_name, sector, system, viewer)
            SectorEditor.set_primary_planet(
                system, 
                name = new_name, 
                size = 7, # .9 g
                atmosphere = 7, # Standard, Tainted
                hydrographics = 1, # Desert world / 3 Small seas and oceans.
                temperature = 7, # 7 Temperate 0-30
                population = 1, # 0 / Millions
                government = 11, # 0 / 11 Non-Charismatic Leader: hereditary king/queen-ship
                lawLevel = 1,  # Poison gas, explosives, undetectable weapons, WMD
                starports = 7,  # No port / B class. Good. 1D x Cr500. Refined Fuel. Shipyard (spacecraft) Repair
                birthing_cost_per_week = 0, # 1D x Cr500
                refined_fueling_cost = 500, # 500
                unrefined_fueling_cost = 100, # 100
                techLevel = 12, # TL 0 (Primitive): No technology / TL 12 (Average Stellar)
                moons=[],keep_moons=keep_moons,
                ) 
            system.primaryPlanet.description = [

                ]
            system.primaryPlanet.notes = [

                ]
            system.primaryPlanet.history = [

                ]
            system.primaryPlanet.add_settlement(Settlement( 
                name, 
                settlement_type, 
                population_size, 
                description, 
                population_demographics
                ))
            system.primaryPlanet.add_area_of_interest(AreaOfIntersest(
                name, 
                area_type, 
                system.primaryPlanet, 
                description, 
                is_dungeon
                ))
        elif (planet_to_be_changed.lower() in ["vamarda-2"]): # B773566-D / 0770000-0
            new_name = "Vamarda"
            keep_moons=len(system.primaryPlanet.moons) > 0
            SectorEditor.performSystemRename(new_name, sector, system, viewer)
            SectorEditor.set_primary_planet(
                system, 
                name = new_name, 
                size = 7, # .9 g
                atmosphere = 7, # Standard, Tainted
                hydrographics = 2, # Desert world / 3 Small seas and oceans.
                temperature = 7, # 7 Temperate 0-30
                population = 2, # 0 / Millions
                government = 11, # 0 / 11 Non-Charismatic Leader: hereditary king/queen-ship
                lawLevel = 3,  # Military weapons
                starports = 9,  # No port / B class. Good. 1D x Cr500. Refined Fuel. Shipyard (spacecraft) Repair
                birthing_cost_per_week = 100, # 1D x Cr500
                refined_fueling_cost = 500, # 500
                unrefined_fueling_cost = 100, # 100
                techLevel = 13, # TL 0 (Primitive): No technology / TL 12 (Average Stellar)
                moons=[],keep_moons=keep_moons,
                ) 
            system.primaryPlanet.description = [

                ]
            system.primaryPlanet.notes = [

                ]
            system.primaryPlanet.history = [

                ]
            system.primaryPlanet.add_settlement(Settlement( 
                name, 
                settlement_type, 
                population_size, 
                description, 
                population_demographics
                ))
            system.primaryPlanet.add_area_of_interest(AreaOfIntersest(
                name, 
                area_type, 
                system.primaryPlanet, 
                description, 
                is_dungeon
                ))
        elif (planet_to_be_changed.lower() in ["vamarda-3"]): # B773566-D / 0770000-0
            new_name = "Vamarda"
            keep_moons=len(system.primaryPlanet.moons) > 0
            SectorEditor.performSystemRename(new_name, sector, system, viewer)
            SectorEditor.set_primary_planet(
                system, 
                name = new_name, 
                size = 7, # .9 g
                atmosphere = 7, # Standard, Tainted
                hydrographics = 3, # Desert world / 3 Small seas and oceans.
                temperature = 7, # 7 Temperate 0-30
                population = 3, # 0 / Millions
                government = 11, # 0 / 11 Non-Charismatic Leader: hereditary king/queen-ship
                lawLevel = 1,  # Poison gas, explosives, undetectable weapons, WMD
                starports = 9,  # No port / B class. Good. 1D x Cr500. Refined Fuel. Shipyard (spacecraft) Repair
                birthing_cost_per_week = 100, # 1D x Cr500
                refined_fueling_cost = 500, # 500
                unrefined_fueling_cost = 100, # 100
                techLevel = 13, # TL 0 (Primitive): No technology / TL 12 (Average Stellar)
                moons=[],keep_moons=keep_moons,
                ) 
            system.primaryPlanet.description = [

                ]
            system.primaryPlanet.notes = [

                ]
            system.primaryPlanet.history = [

                ]
            system.primaryPlanet.add_settlement(Settlement( 
                name, 
                settlement_type, 
                population_size, 
                description, 
                population_demographics
                ))
            system.primaryPlanet.add_area_of_interest(AreaOfIntersest(
                name, 
                area_type, 
                system.primaryPlanet, 
                description, 
                is_dungeon
                ))
        elif (planet_to_be_changed.lower() in ["vamarda-4"]): # B773566-E / 0770000-0
            new_name = "Vamarda"
            keep_moons=len(system.primaryPlanet.moons) > 0
            SectorEditor.performSystemRename(new_name, sector, system, viewer)
            SectorEditor.set_primary_planet(
                system, 
                name = new_name, 
                size = 7, # .9 g
                atmosphere = 6, # Standard
                hydrographics = 4, # Desert world / 3 Small seas and oceans.
                temperature = 7, # 7 Temperate 0-30
                population = 6, # 0 / Millions
                government = 11, # 0 / 5 Non-Charismatic Leader: hereditary king/queen-ship
                lawLevel = 6,  # All firearms except shotguns & stunners; carrying weapons discouraged
                starports = 11,  # No port / B class. Good. 1D x Cr500. Refined Fuel. Shipyard (spacecraft) Repair
                birthing_cost_per_week = 1000, # 1D x Cr500
                refined_fueling_cost = 500, # 500
                unrefined_fueling_cost = 100, # 100
                techLevel = 14, # TL 0 (Primitive): No technology / TL 12 (Average Stellar)
                moons=[],keep_moons=keep_moons,
                ) 
            system.primaryPlanet.description = [

                ]
            system.primaryPlanet.notes = [

                ]
            system.primaryPlanet.history = [

                ]
            system.primaryPlanet.add_settlement(Settlement( 
                name, 
                settlement_type, 
                population_size, 
                description, 
                population_demographics
                ))
            system.primaryPlanet.add_area_of_interest(AreaOfIntersest(
                name, 
                area_type, 
                system.primaryPlanet, 
                description, 
                is_dungeon
                ))
        elif (planet_to_be_changed.lower() in ["vamarda-5"]): # B773566-F / 0770000-0
            new_name = "Vamarda"
            keep_moons=len(system.primaryPlanet.moons) > 0
            SectorEditor.performSystemRename(new_name, sector, system, viewer)
            SectorEditor.set_primary_planet(
                system, 
                name = new_name, 
                size = 7, # .9 g
                atmosphere = 6, # Standard, Tainted
                hydrographics = 5, # Desert world / 3 Small seas and oceans.
                temperature = 7, # 7 Temperate 0-30
                population = 9, # 0 / Millions
                government = 11, # 0 / 5 Non-Charismatic Leader: hereditary king/queen-ship
                lawLevel = 6,  # All firearms except shotguns & stunners; carrying weapons discouraged
                starports = 11,  # No port / B class. Good. 1D x Cr500. Refined Fuel. Shipyard (spacecraft) Repair
                birthing_cost_per_week = 1000, # 1D x Cr500
                refined_fueling_cost = 500, # 500
                unrefined_fueling_cost = 100, # 100
                techLevel = 15, # TL 0 (Primitive): No technology / TL 12 (Average Stellar)
                moons=[],keep_moons=keep_moons,
                ) 
            system.primaryPlanet.description = [

                ]
            system.primaryPlanet.notes = [

                ]
            system.primaryPlanet.history = [

                ]
            system.primaryPlanet.add_settlement(Settlement( 
                name, 
                settlement_type, 
                population_size, 
                description, 
                population_demographics
                ))
            system.primaryPlanet.add_area_of_interest(AreaOfIntersest(
                name, 
                area_type, 
                system.primaryPlanet, 
                description, 
                is_dungeon
                ))
        elif (planet_to_be_changed.lower() in ["ogmha", "pirate world"]): # D560250-6 -> D761351-6
            new_name = "Oghma"
            keep_moons=len(system.primaryPlanet.moons) > 0
            SectorEditor.performSystemRename(new_name, sector, system, viewer)
            system.piracy_warning=True
            SectorEditor.set_primary_planet(
                system, 
                name = new_name, 
                size = 7, # .9 g
                atmosphere = 5, # Standard, thin
                hydrographics = 3, # 3 Small seas and oceans.
                temperature = 4, # 4 cold
                population = 7, # 2 / 3 Hundreds -> Thousands
                government = 5, # 5 / 5 Feudal Technocracy: Ruling functions are performed by specific individuals for persons who agree to be ruled by them. 
                                # Relationships are based on the performance of technical activities which are mutually beneficial
                lawLevel = 4, # No restrictions – heavy armour and a handy weapon recommended…
                starports = 9, # D class. Poor. 1D x Cr10. Unrefined Fuel. Limited Repair
                birthing_cost_per_week = 2000, # 1D x Cr500 # Open air Starport
                refined_fueling_cost = 500, # available
                unrefined_fueling_cost = 100, # 100 available
                techLevel = 9, # TL 6 (Industrial)
                moons=[], keep_moons=keep_moons,
                )
            
            system.travelCode = "A"
            system.bases.append("Pirate")
            if not keep_moons:
                for i in range(wanted_moons):
                    moonSize = random.choice([0, 0, 1, 1, 1, 2, 2, 3, 3, 3])
                    moonAtmo = max(0, min(moonSize-2, 2))
                    moonHydro =  random.choice([0, 0, 1, 1, 1, 2, 2])
                    moonTemp = 0
                    moonPopulation = 0
                    moonGovernment = 0
                    moonLaw = 0
                    moonTech = 0
                    moonStarport = 0
                    moonDict = {
                                "{}-{} size".format(system.primaryPlanet.name,i+1): moonSize, "{}-{} atmosphere".format(system.primaryPlanet.name,i+1): moonAtmo, 
                                "{}-{} hydrographics".format(system.primaryPlanet.name,i+1): moonHydro, "{}-{} temperature".format(system.primaryPlanet.name,i+1): moonTemp, 
                                "{}-{} population".format(system.primaryPlanet.name,i+1): moonPopulation, "{}-{} government".format(system.primaryPlanet.name,i+1): moonGovernment, 
                                "{}-{} law level".format(system.primaryPlanet.name,i+1): moonLaw, "{}-{} tech level".format(system.primaryPlanet.name,i+1): moonTech,
                                "{}-{} starport".format(system.primaryPlanet.name,i+1): moonStarport,  
                                }
                    system.primaryPlanet.add_orbiting_body( Moon( moonDict, "{}-{}".format(system.primaryPlanet.name,i+1) ) )
            system.primaryPlanet.description = [

                ] 
            system.primaryPlanet.notes = [

                ]
            system.primaryPlanet.history = [

                ]
            system.megacorpsPresence = [
 
                ]
            # system.primaryPlanet.add_settlement(Settlement( 
            #     "Downport", 
            #     "Downport", 
            #     int(2*0.2*DescriptionGenerator.getPopulationTotal(system.primaryPlanet.population)),
            #     "", 
            #     "Isolated",
            #     ["Riding beasts", "Mag-lev Train", "Spacecraft", "Aircraft", "Auto-vehicles"]
            #     ))
            # system.primaryPlanet.add_area_of_interest(AreaOfIntersest(
            #     name, 
            #     area_type, 
            #     system.primaryPlanet, 
            #     description, 
            #     is_dungeon
            #     ))
        elif (planet_to_be_changed.lower() in ["marduk", "murdok"]): # C377436-5 -> C767436-5
            new_name = "Marduk"
            keep_moons=len(system.primaryPlanet.moons) > 0
            SectorEditor.performSystemRename(new_name, sector, system, viewer)
            SectorEditor.set_primary_planet(
                system, 
                name = new_name, 
                size = 7, # .9 g
                atmosphere = 6, # Standard
                hydrographics = 7, # Desert world / 3 Small seas and oceans.
                temperature = 9, # 7 Temperate 0-30
                population = 4, # 4 Tens of thousands
                government = 3, # 3 Self-Perpetuating Oligarchy - Ruling functions are performed by a restricted minority, 
                                # with little or no input from the mass of citizenry
                lawLevel = 6, # All firearms except shotguns & stunners; carrying weapons discouraged
                starports = 7, # C class. Routine. 1D x Cr100. Refined Fuel. Small Craft Repair
                birthing_cost_per_week = 400, # 1D x Cr100
                refined_fueling_cost = None, # Unavailable
                unrefined_fueling_cost = 100, # 100
                techLevel = 5, # TL 5 (Industrial) Roughly on a par with the mid–20th century.
                moons=[], keep_moons=keep_moons,
                )
            if not keep_moons:
                for i in range(wanted_moons):
                    moonSize = random.choice([0, 0, 1, 1, 1, 2, 2, 3, 3, 3])
                    moonAtmo = max(0, min(moonSize-2, 2))
                    moonHydro =  random.choice([0, 0, 1, 1, 1, 2, 2])
                    moonTemp = 0
                    moonPopulation = 0
                    moonGovernment = 0
                    moonLaw = 0
                    moonTech = 0
                    moonStarport = 0
                    moonDict = {
                                "{}-{} size".format(system.primaryPlanet.name,i+1): moonSize, "{}-{} atmosphere".format(system.primaryPlanet.name,i+1): moonAtmo, 
                                "{}-{} hydrographics".format(system.primaryPlanet.name,i+1): moonHydro, "{}-{} temperature".format(system.primaryPlanet.name,i+1): moonTemp, 
                                "{}-{} population".format(system.primaryPlanet.name,i+1): moonPopulation, "{}-{} government".format(system.primaryPlanet.name,i+1): moonGovernment, 
                                "{}-{} law level".format(system.primaryPlanet.name,i+1): moonLaw, "{}-{} tech level".format(system.primaryPlanet.name,i+1): moonTech,
                                "{}-{} starport".format(system.primaryPlanet.name,i+1): moonStarport,  
                                }
                    system.primaryPlanet.add_orbiting_body( Moon( moonDict, "{}-{}".format(system.primaryPlanet.name,i+1) ) )
            system.primaryPlanet.description = [

                ] 
            system.primaryPlanet.notes = [

                ]
            system.primaryPlanet.history = [

                ]
            system.megacorpsPresence = [
 
                ]
            system.primaryPlanet.add_settlement(Settlement( 
                "Marduk Downport", 
                "Downport", 
                int(2*0.2*DescriptionGenerator.getPopulationTotal(system.primaryPlanet.population)),
                "", 
                "Isolated",
                ["Riding beasts", "Spacecraft", "Aircraft", "Auto-vehicles"]
                ))
            # system.primaryPlanet.add_area_of_interest(AreaOfIntersest(
            #     name, 
            #     area_type, 
            #     system.primaryPlanet, 
            #     description, 
            #     is_dungeon
            #     ))
    @staticmethod
    def get_planetary_body_from_system(sector, system, viewer):
        available_indeces = []
        for p in system.systemLineup:
            if isinstance(p, GasGiant):
                print("{} {}".format(system.systemLineup.index(p), p.name))
                for m in p.moons: 
                    if not isinstance(p, Sun) and not isinstance(p, AsteroidBelt) and not isinstance(p, GasGiant):
                        print("  {} {}".format(p.moons.index(m), m.name))
                        available_indeces.append( (system.systemLineup.index(p), p.moons.index(m)) )
            if not isinstance(p, Sun) and not isinstance(p, AsteroidBelt) and not isinstance(p, GasGiant):
                print("{} {}".format(system.systemLineup.index(p), p.name))
                available_indeces.append( (system.systemLineup.index(p),None) )

        parent_planet = TerminalUtils.selectMenuItem(options=available_indeces+["Nevermind"], 
            prompt="Select a Location in the system. $>")
        if parent_planet == "Nevermind":
            return None
        elif type(parent_planet) is tuple and parent_planet[1] is None:
            parent_planet = system.systemLineup[parent_planet[0]]
        elif type(parent_planet) is tuple and parent_planet[1] is not None: 
            parent_planet = system.systemLineup[parent_planet[0]].moons[parent_planet[1]]
        return parent_planet
    @staticmethod
    def add_area_of_interest(sector, system, viewer):
        print("Add Area of Interest to a planet in the {} system...".format(system.name))
        parent_planet = get_planetary_body_from_system(sector, system, viewer) #(Planet, None) or (GasGiant, Planet/Moon) or (AsteroidBelt, Planet/Moon)
        if parent_planet is None:
            return False
        elif type(parent_planet) is tuple: #(Planet, None) or (GasGiant, Planet/Moon) or (AsteroidBelt, Planet/Moon)
            area_type = TerminalUtils.selectMenuItem(options=[
                "Industrial Site", "Research Lab", 
                "Natural Wonder", "Landmark",
                "Deserted Island", "Crater", "Abandoned City", "Abandoned Town", "Ancient Ruins",
                ], prompt="Select an Area Type. $>")

            name = input("What is the area's name? (its a(n) {}): $>".format(area_type))
            description = input("Add the area description: $>")
            is_dungeon = TerminalUtils.selectMenuItem(options=["Yes", "No"], prompt="Select an option. $>") == "Yes"
            area = AreaOfIntersest(name, area_type, parent_planet, description, is_dungeon)
            if parent_planet[1] is not None:
                parent_planet[1].add_area_of_interest(area)
            else:
                parent_planet[0].add_area_of_interest(area)
            return True
        else:
            print("parent_planet is not a tuple: is {} : {}".format( type(parent_planet), str(parent_planet) ))
            return False
    @staticmethod
    def edit_area_of_interest(sector, system, viewer):
        print("Edit Area of Interest to a planet in the {} system...".format(system.name))
        parent_planet = get_planetary_body_from_system(sector, system, viewer) #(Planet, None) or (GasGiant, Planet/Moon) or (AsteroidBelt, Planet/Moon)
        if parent_planet is None:
            return False
        elif type(parent_planet) is tuple: #(Planet, None) or (GasGiant, Planet/Moon) or (AsteroidBelt, Planet/Moon)
            area_names = []
            for area in parent_planet.areas_of_interest:
                if (TerminalUtils.selectMenuItem(options=["Yes", "No"], 
                    prompt="Edit this Area ({} {} {})? $>".format(
                        area.name, 
                        area.area_type, 
                        "Dungeon" if area.is_dungeon else "Location"
                        )
                    ) == "Yes"
                ):
                    if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Edit the Area Type ()? $>".format(area.name)) == "Yes":
                        area.area_type = TerminalUtils.selectMenuItem(options=[
                            "Industrial Site", "Research Lab", 
                            "Natural Wonder", "Landmark",
                            "Deserted Island", "Crater", "Empty City", "Abandoned Town", "Ancient Ruins",
                            ], prompt="Select an Area Type. $>")
                    if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Edit the Area Name ({})? $>".format()) == "Yes":
                        area.name = input("What is the area's name ({})? (its a(n) {}): $>".format(area.name, area.area_type))
                    area.is_dungeon = TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Is the Area a Dungeon? ({})? $>".format(area.is_dungeon)) == "Yes"
                    TerminalUtils.pprint(area.description if len(area.description) < 20 else area.description[:20] )
                    if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Change the Area Description ({})? $>".format()) == "Yes":
                        area.description = input("Add the area description: $>")
            return True
        else:
            print("parent_planet is not a tuple: is {} : {}".format( type(parent_planet), str(parent_planet) ))
            return False
    @staticmethod
    def add_area_of_settlement(sector, system, viewer):
        print("Add Settlement to a planet in the {} system...".format(system.name))
        parent_planet = get_planetary_body_from_system(sector, system, viewer) #(Planet, None) or (GasGiant, Planet/Moon) or (AsteroidBelt, Planet/Moon)
        if parent_planet is None:
            return False
        elif type(parent_planet) is tuple: #(Planet, None) or (GasGiant, Planet/Moon) or (AsteroidBelt, Planet/Moon)
            pp = parent_planet[1]
            if pp is None:
                pp = parent_planet[0]
            print("Population of Planet {} is in the {} [{}]".format(pp.name, DescriptionGenerator.getPopulationTotal(pp.population), pp.population))
            settlement_type = TerminalUtils.selectMenuItem(options=[
                "Star Town", "Capital", "Sea Port", 
                "Agricultural", "Mining", "Industrial", "Scientific", "Wonder Location"
                ], prompt="Select a Settlement Type. $>")
            name = input("What the settlement name? $>")
            modifier = 0.4
            print("Population presets: {} at 20.%, {} at 20.%, {} at 30.%, {} at 40.%, {} at 50.%,".format(
                DescriptionGenerator.getPopulationTotal(pp.population) * 0.1,
                DescriptionGenerator.getPopulationTotal(pp.population) * 0.2,
                DescriptionGenerator.getPopulationTotal(pp.population) * 0.3,
                DescriptionGenerator.getPopulationTotal(pp.population) * 0.4,
                DescriptionGenerator.getPopulationTotal(pp.population) * 0.5,
                ))
            value = input("What {}'s population? (leave empty or type \"random\" to generate the town size ({}% of total pop))$>".format(name, int(modifier*10)))
            if value.lower() in ["", "random"]:
                value = DescriptionGenerator.getPopulationTotal(pp.population) * modifier * random.randint(1, 6)
            else:
                value = int(value)
            population_size = value
            description = ""
            if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Enter a description of {} at this time? $>".format(name)) == "Yes":
                description = input("Enter {} description: $>".format(name))
            population_demographics="Isolated"
            if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Enter a population demographics of {} at this time? $>".format(name)) == "Yes":
                print("Isolated: 97% is main population demographic, ")
                print("Semi-Isolated: 79% is main population demographic, less variety")
                print("Mixed: 79% is main population demographic, more variety")
                
                print("Integrated: 37% is main population demographic, ")
                population_demographics=TerminalUtils.selectMenuItem(options=["Isolated", "Semi-Isolated", "Mixed", "Integrated"], 
                    prompt="Enter a population demographics for {}. $>".format(name))
            modes_of_transportation = []
            done=False
            while not done:
                print("Modes of mass transportation:\nRiding beast -> Auto-bus/Auto-car, Grav-vehicles,\n"+
                    "Steam engine -> Mag-lev Train -> Vacuum Train,\nSailing Ship -> Powered Ships -> Aircraft,\n"+
                    "Aircraft -> Gravcraft -> Spacecraft,\netc")
                if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Enter a modes of transportation available? $>".format(name)) == "Yes":
                    mode_of_transportation = input("Transportation type: $>")
                    if mode_of_transportation.lower() not in ["", "cancel", "exit", "back", "quit", "nevermind"]:
                        modes_of_transportation.append(mode_of_transportation)
                    else:
                        done = True
                else:
                    done = True



            settlement = Settlement( name, settlement_type, population_size, description, population_demographics, modes_of_transportation)
            if parent_planet[1] is not None:
                parent_planet[1].add_settlement(settlement)
            else:
                parent_planet[0].add_settlement(settlement)
            return True
        else:
            print("parent_planet is not a tuple: is {} : {}".format( type(parent_planet), str(parent_planet) ))
            return False
    @staticmethod
    def edit_area_of_settlement(sector, system, viewer):
        print("Edit Area of Interest to a planet in the {} system...".format(system.name))
        parent_planet = get_planetary_body_from_system(sector, system, viewer)
        if parent_planet is None:
            return False
        elif type(parent_planet) is tuple:
            pp = parent_planet[1]
            if pp is None:
                pp = parent_planet[0]
            area_names = []
            for settlement in pp.settlements:
                if (TerminalUtils.selectMenuItem(options=["Yes", "No"], 
                    prompt="Edit this Settlement ({} {} {} {})? $>".format(
                        settlement.name, 
                        settlement.settlement_type, 
                        settlement.population_size,
                        settlement.get_settlement_classification(),
                        )
                    ) == "Yes"
                ):
                    
                    print("Population of Planet {} is in the {} [{}]".format(pp.name, DescriptionGenerator.getPopulationTotal(pp.population), pp.population))
                    settlement_type = TerminalUtils.selectMenuItem(options=[
                        "Star Town", "Capital", "Sea Port", 
                        "Agricultural", "Mining", "Industrial", "Scientific", "Wonder Location"
                        ], prompt="Select a Settlement Type. $>")
                    name = input("What the settlement name? $>")
                    modifier = 0.4
                    print("Population presets: {} at 20.%, {} at 20.%, {} at 30.%, {} at 40.%, {} at 50.%,".format(
                        DescriptionGenerator.getPopulationTotal(pp.population) * 0.1,
                        DescriptionGenerator.getPopulationTotal(pp.population) * 0.2,
                        DescriptionGenerator.getPopulationTotal(pp.population) * 0.3,
                        DescriptionGenerator.getPopulationTotal(pp.population) * 0.4,
                        DescriptionGenerator.getPopulationTotal(pp.population) * 0.5,
                        ))
                    value = input("What {}'s population? (leave empty or type \"random\" to generate the town size ({}% of total pop))$>".format(name, int(modifier*10)))
                    if value.lower() in ["", "random"]:
                        value = DescriptionGenerator.getPopulationTotal(pp.population) * modifier * random.randint(1, 6)
                    else:
                        value = int(value)
                    population_size = value
                    description = ""
                    if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Enter a description of {} at this time? $>".format(name)) == "Yes":
                        description = input("Enter {} description: $>".format(name))
                    population_demographics="Isolated"
                    if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Enter a population demographics of {} at this time? $>".format(name)) == "Yes":
                        print("Isolated: 97% is main population demographic, ")
                        print("Semi-Isolated: 79% is main population demographic, less variety")
                        print("Mixed: 79% is main population demographic, more variety")
                        
                        print("Integrated: 37% is main population demographic, ")
                        population_demographics=TerminalUtils.selectMenuItem(options=["Isolated", "Semi-Isolated", "Mixed", "Integrated"], 
                            prompt="Enter a population demographics for {}. $>".format(name))
                    modes_of_transportation = []
                    done=False
                    while not done:
                        print("Modes of mass transportation:\nRiding beast -> Auto-bus/Auto-car, Grav-vehicles,\n"+
                            "Steam engine -> Mag-lev Train -> Vacuum Train,\nSailing Ship -> Powered Ships -> Aircraft,\n"+
                            "Aircraft -> Gravcraft -> Spacecraft,\netc")
                        if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Enter a modes of transportation available? $>".format(name)) == "Yes":
                            mode_of_transportation = input("Transportation type: $>")
                            if mode_of_transportation.lower() not in ["", "cancel", "exit", "back", "quit", "nevermind"]:
                                modes_of_transportation.append(mode_of_transportation)
                            else:
                                done = True
                        else:
                            done = True
                    
            return True
        else:
            print("parent_planet is not a tuple: is {} : {}".format( type(parent_planet), str(parent_planet) ))
            return False
# =====================================================================
class Character(object):
    uppValues = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    fitness_levels=["feeble", "lean", "athletic", "fit", "average", "pudgy", "fat", "obese"]
    mass_descriptions = ["Gaunt", "Skinny", "Average", "Overweight", "Obese"]
    height_descriptions = ["Very Short", "Short", "Average","Tall","Very Tall"]
    sizes = [0.25,0.50,1.01,1.52,2.03,2.54,3.04,3.55,4.06,4.56, 5.07,5.58,6.08,6.60,7.10,7.60,8.1,8.6,9.1,9.6,10.1,
        10.6,11.1,11.6,12.1, 12.6, 13.1, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 19.0, 19.5, 20.0, 
        20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5
        ]
    cups  = ["AA","A","B","C","D","DD","E","F","FF","G","GG",
        "H","HH","J","JJ","K","KK","L","LL","M","MM",
        "N","NN","O","OO", "P", "PP", "Q", "QQ", "R", "RR", "S", "SS", "T", "TT", "UU", "U", "V", "VV", "W", "WW", "X", "XX", "Y","YY", "Z", "ZZ"
        ]
    cupInches  = [0.5,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
        21,22,23,24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46
        ]
    def __init__(self, initDict):
        super().__init__()
        self.name = initDict.get("name", "FName")
        self.surname = initDict.get("surname", "LName")
        self.species = initDict.get("species", "Human") # Human
        self.subspecies = initDict.get("subspecies",None) # Sol, Imperial, special
        self.sex = initDict.get("sex", "Female")
        self.age = initDict.get("age", 20)
        self.weight = initDict.get("weight", 170.6)
        self.base_weight = self.weight
        self.height = initDict.get("height", 63.7)
        
        self.fitness = initDict.get("fitness", "average")

        self.height_description = self.get_height_map() # (for race)  Average
        self.mass_description = self.get_weight_map() # (for race)  Overweight

        self.character_notes = initDict.get("character notes", "")
        self.muscle_percent = 0
        self.fat_percent = 0
        self.water_percent = 0
        self.other_percent = 0
        self._determine_base_percents()
        self.parts_weight = initDict.get("parts_weight", {"breast":1.5, "belly":0, "butt":0, "body":0})
        self.setup_progress = 0
        self.relations = {}
    def _determine_base_percents(self):
        self.fat_percent = 0.18 # base human male body fat %
        self.muscle_percent = 0.24 # base human female body fat %
        self.water_percent=0.5 # base human body is about 50-65% water
        self.other_percent=0 # non-digestable mass
        if(self.species.lower() in ["human", "base"] and self.sex.lower() in ["female"]):
            if(self.fitness.lower() in ["athletic"]):
                self.fat_percent = 0.17
                self.muscle_percent = 0.4
            elif(self.fitness.lower() in ["fit"]):
                self.fat_percent = 0.23
                self.muscle_percent = 0.33
            elif(self.fitness.lower() in ["average"]):
                self.fat_percent = 0.29
                self.muscle_percent = 0.27
            elif(self.fitness.lower() in ["pudgy"]):
                self.fat_percent = 0.33
                self.muscle_percent = 0.27
            elif(self.fitness.lower() in ["fat"]):
                self.fat_percent = 0.4
                self.muscle_percent = 0.27
            elif(self.fitness.lower() in ["obese"]):
                self.fat_percent = 0.4
                self.muscle_percent = 0.27
            elif(self.fitness.lower() in ["lean"]):
                self.fat_percent = 0.15
                self.muscle_percent = 0.35
        elif(self.species.lower() in ["human", "base"] and self.sex.lower() in ["male"]):
            if(self.fitness.lower() in ["athletic"]):
                self.fat_percent = 0.18
                self.muscle_percent = 0.4
            elif(self.fitness.lower() in ["fit"]):
                self.fat_percent = 0.23
                self.muscle_percent = 0.38
            elif(self.fitness.lower() in ["average"]):
                self.fat_percent = 0.28
                self.muscle_percent = 0.36
            elif(self.fitness.lower() in ["pudgy"]):
                self.fat_percent = 0.32
                self.muscle_percent = 0.32
            elif(self.fitness.lower() in ["fat"]):
                self.fat_percent = 0.4
                self.muscle_percent = 0.20
            elif(self.fitness.lower() in ["obese"]):
                self.fat_percent = 0.4
                self.muscle_percent = 0.20
            elif(self.fitness.lower() in ["lean"]):
                self.fat_percent = 0.16
                self.muscle_percent = 0.35
        self.water_percent = round(0.95 - self.muscle_percent - self.fat_percent, 3)
        self.other_percent = (1 - self.fat_percent - self.muscle_percent  - self.water_percent)
    def get_weight_map(self):
        if self.fitness in ["lean", "feeble"]: return Character.mass_descriptions[0]
        elif self.fitness in [ "athletic", "fit"]: return Character.mass_descriptions[1]
        elif self.fitness in [ "average" ]: return Character.mass_descriptions[2]
        elif self.fitness in [ "pudgy", "fat"]: return Character.mass_descriptions[3]
        elif self.fitness in [ "obese" ]: return Character.mass_descriptions[4]
    def get_height_map(self):
        #if self.species in ["Human"]:
        if self.height <= 40.0: return Character.height_descriptions[0]
        elif 40.0 <= self.height and  self.height < 48.0: return Character.height_descriptions[1]
        elif 48.0 <= self.height and  self.height < 60.0: return Character.height_descriptions[2]
        elif 60.0 <= self.height and  self.height < 72.0: return Character.height_descriptions[3]
        elif 72.0 <= self.height: return Character.height_descriptions[4]
    def save(self, verbose=True):
        file = open("{}-{}.pickle".format(self.name, self.surname), 'wb')
        pickle.dump(self, file)
        if verbose: print("Saving file: {}-{}.pickle".format(self.name, self.surname))
        file.close()
    @staticmethod
    def load(fname, lname):
        character=None
        filename = "{}-{}.pickle".format(fname, lname)
        if os.path.exists(filename):
            file = open(filename, 'rb')
            character = pickle.load(file)
            file.close()
        return character
    @staticmethod
    def adjust_vitals():
        #         0                      1             2     3      4     5    6
        # python ./conversion_tracker.py adjust-vitals Andromeda Antari age   
        #usage()
        name = sys.argv[2] 
        surname = sys.argv[3] 
        predpreg = PregPred.load(name, surname)
        predpreg.age = max(0, min(int(sys.argv[4]), 60))
        print("Age set to: {}".format(predpreg.age))
        predpreg.save()
    @staticmethod
    def getCupSizeFromWeight(weight):
        '''# base 0.5
            A Cups Breasts  =  230 g (.50 lbs)
            B Cups Breasts  =  460 g (1.01 lbs) + .51 lbs / 230 g
            C Cups Breasts  =  690 g (1.52 lbs) + .51 lbs / 230 g
            D Cups Breasts  =  920 g (2.03 lbs) + .51 lbs / 130 g
            DD Cups Breasts = 1150 g (2.54 lbs) + .51 lbs / 
            E Cups Breasts  = 1380 g (3.04 lbs) + .50 lbs / 
            F Cups Breasts  = 1610 g (3.55 lbs) + .55 lbs / 
            FF Cups Breasts = 1840 g (4.06 lbs) + .51 lbs / 
            G Cups Breasts  = 2070 g (4.56 lbs) + .50 lbs / 
            GG Cups         = 2300 g (5.07 lbs) + .51 lbs / 
            H Cups Breasts  = 2530 g (5.58 lbs) + .51 lbs / 
            HH Cups Breasts = 2760 g (6.08 lbs) + .50 lbs / 
            J Cups Breasts  = 2990 g (6.60 lbs) + .52 lbs / 
            JJ Cups Breasts = 3220 g (7.10 lbs) + .50 lbs / 
            K Cups Breasts  = 3450 g (7.60 lbs) + .50 lbs / 
            '''
        for size in Character.sizes:
            if (weight-size <= 0.01):
                return Character.cups[Character.sizes.index(size)]
        return "-A"
    @staticmethod
    def getCupInchesFromWeight(weight):
        for size in Character.sizes:
            if (weight-size <= 0.01):
                return Character.cupInches[Character.sizes.index(size)]
        return -1
    @staticmethod
    def getCupSizeFromInches(inches):
        for size in Character.cupInches:
            if (inches-size <= 0.01):
                return Character.cups[Character.sizes.index(size)]
        return "-A"
class Item():
    def __init__(self, initDict):
        self.name = initDict.get("name", "Item Name")
        self.description = initDict.get("description", "<Description>")
        self.weight = initDict.get("weight", 0)
        self.size = initDict.get("size", 0)
        self.tech_level = initDict.get("tech level", 1)
        self.traits = initDict.get("traits", [])
        self.features = initDict.get("features", [])
    def get_traits_as_str(self):
        text = ""
        if len(self.traits) > 0:
            for trait in self.traits:
                text += "{}, ".format(trait)
            text = text[:-2]
        return text
    def get_features_as_str(self):
        text = ""
        if len(self.features) > 0:
            for feature in self.features:
                text += "{}, ".format(feature)
            text = text[:-2]
        return text
    def __str__(self): return "{} {} kg [{}]".format(self.name, self.weight, self.get_traits_as_str())
class Weapon(Item):
    def __init__(self, initDict):
        super().__init__(initDict)
        self.range = initDict.get("range", "Melee")
        self.damage = initDict.get("damage", "1D + STR DM")
        self.magazine = initDict.get("magazine", "N/A")
    def __str__(self): return "{} {} TL, {} meters, {} dmg, {} kg {} mag, traits: {}".format(
        self.name, 
        self.tech_level, 
        self.range, 
        self.damage, 
        self.weight, 
        self.magazine, 
        self.get_traits_as_str()
        )
class Armor(Item):
    def __init__(self, initDict):
        super().__init__(initDict)
        self.protection = initDict.get("protection", 0)
        self.radiation_protection = initDict.get("radiation protection", 0)
    def __str__(self): return "{} {} TL, +{} protection, {} Rad, {} kg  traits: {}".format(
        self.name, 
        self.tech_level, 
        self.protection, 
        self.radiation_protection, 
        self.weight, 
        self.get_traits_as_str()
        )
class Wound():
    def __init__(self, table_index, title, effect, cost_to_cure):
        self.table_index = table_index
        self.title = title
        self.effect = effect
        self.cost_to_cure = cost_to_cure
    def __str__(self):
        return "[{}] {}. Effect: ({}) {}cr ti cure.".format(
            self.table_index,
            self.title,
            self.effect,
            self.cost_to_cure,
            )
class Traveller(Character):
    stat_based_fitness_levels=["feeble", "lean", "average", "fit", "athletic"]
    STR="Strength"
    DEX="Dexterity"
    END="Endurance"
    INT="Intellect"
    EDU="Education"
    SOC="Social"

    MOR="Morale"
    LCK="Luck"
    SAN="Sanity"
    CHM="Charm"
    PSI="Psionic"
    OTR="Other"
    @staticmethod
    def get_skill_map():
        return {
            "Admin":-3, "Advocate":-3, "Animals: Handling":-3, "Animals: Training":-3, "Animals: Veterinary":-3,
            "Art":-3, "Astrogation":-3, "Athletics: Dexterity":-3, "Athletics: Endurance":-3, "Athletics: Strength":-3,
            "Broker":-3, "Carouse":-3, "Deception":-3, "Diplomat":-3, "Drive: Hovercraft":-3,
            "Drive: Mole":-3, "Drive: Tracked":-3, "Drive: Walker":-3, "Drive: Wheeled":-3, "Electronics: Comms":-3,
            "Electronics: Computers":-3, "Electronics: Remote Ops.":-3, "Electronics: Sensors":-3, "Engineer: J-Drive":-3, "Engineer: Life Support":-3,
            "Engineer: M-Drive":-3, "Engineer: Power Plant":-3, "Explosives":-3, "Flyer: Airship":-3, "Flyer: Grav":-3,
            "Flyer: Ornithopter":-3, "Flyer: Rotor":-3, "Flyer: Wing":-3, "Gambler":-3, "Gunner: Capital":-3,
            "Gunner: Ortillery":-3, "Gunner: Screen":-3, "Gunner: Turret":-3, "Gun Combat: Archaic":-3, "Gun Combat: Energy":-3,
            "Gun Combat: Slug":-3, "Heavy Weapons: Artillery":-3, "Heavy Weapons: Man-Portable":-3, "Heavy Weapons: Vehicle":-3, "Investigate":-3,
            "Jack-of-All-Trades":-3, "Leadership":-3, "Mechanic":-3, "Medic":-3, "Melee: Blade":-3,
            "Melee: Bludgeon":-3, "Melee: Natural":-3, "Melee: Unarmed":-3, "Navigation":-3, "Persuade":-3,
            "Pilot: Capital Ships":-3, "Pilot: Small Craft":-3, "Pilot: Spacecraft":-3, 
            "Profession: Belter": -3, "Profession: Biologicals": -3, "Profession: Civil Engineering": -3, 
            "Profession: Construction": -3, "Profession: Hydroponics": -3, "Profession: Polymers": -3,
            "Recon":-3, 
            "Science: Archaeology":-3, "Science: Astronomy":-3, "Science: Biology":-3, "Science: Chemistry":-3, "Science: Cosmology":-3,
            "Science: Cybernetics":-3, "Science: Economics":-3, "Science: Genetics":-3, "Science: History":-3, "Science: Linguistics":-3,
            "Science: Philosophy":-3, "Science: Physics":-3, "Science: Planetology":-3, "Science: Psionicology":-3, "Science: Psychology":-3,
            "Science: Robotics":-3, "Science: Sophontology":-3, "Science: Xenology":-3, 
            "Seafarer: Ocean Ships":-3,
            "Seafarer: Personal":-3, "Seafarer: Sail":-3, "Seafarer: Submarine":-3, "Stealth":-3, "Steward":-3,
            "Streetwise":-3, "Survival":-3, "Tactics: Military":-3, "Tactics: Naval":-3, "Vacc Suit":-3,
            # "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3,
            # "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3,
            # "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3,
            # "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3,
            }
    @staticmethod
    def get_skill_training_map():
        return {
            "Admin":[0,0], "Advocate":[0,0], "Animals: Handling":[0,0], "Animals: Training":[0,0], "Animals: Veterinary":[0,0],
            "Art":[0,0], "Astrogation":[0,0], "Athletics: Dexterity":[0,0], "Athletics: Endurance":[0,0], "Athletics: Strength":[0,0],
            "Broker":[0,0], "Carouse":[0,0], "Deception":[0,0], "Diplomat":[0,0], "Drive: Hovercraft":[0,0],
            "Drive: Mole":[0,0], "Drive: Tracked":[0,0], "Drive: Walker":[0,0], "Drive: Wheeled":[0,0], "Electronics: Comms":[0,0],
            "Electronics: Computers":[0,0], "Electronics: Remote Ops.":[0,0], "Electronics: Sensors":[0,0], "Engineer: J-Drive":[0,0], "Engineer: Life Support":[0,0],
            "Engineer: M-Drive":[0,0], "Engineer: Power Plant":[0,0], "Explosives":[0,0], "Flyer: Airship":[0,0], "Flyer: Grav":[0,0],
            "Flyer: Ornithopter":[0,0], "Flyer: Rotor":[0,0], "Flyer: Wing":[0,0], "Gambler":[0,0], "Gunner: Capital":[0,0],
            "Gunner: Ortillery":[0,0], "Gunner: Screen":[0,0], "Gunner: Turret":[0,0], "Gun Combat: Archaic":[0,0], "Gun Combat: Energy":[0,0],
            "Gun Combat: Slug":[0,0], "Heavy Weapons: Artillery":[0,0], "Heavy Weapons: Man-Portable":[0,0], "Heavy Weapons: Vehicle":[0,0], "Investigate":[0,0],
            "Jack-of-All-Trades":[0,0], "Leadership":[0,0], "Mechanic":[0,0], "Medic":[0,0], "Melee: Blade":[0,0],
            "Melee: Bludgeon":[0,0], "Melee: Natural":[0,0], "Melee: Unarmed":[0,0], "Navigation":[0,0], "Persuade":[0,0],
            "Pilot: Capital Ships":[0,0], "Pilot: Small Craft":[0,0], "Pilot: Spacecraft":[0,0], 
            "Profession: Belter": [0,0], "Profession: Biologicals": [0,0], "Profession: Civil Engineering": [0,0], 
            "Profession: Construction": [0,0], "Profession: Hydroponics": [0,0], "Profession: Polymers": [0,0],

            "Recon":[0,0], 
            "Science: Archaeology":[0,0], "Science: Astronomy":[0,0], "Science: Biology":[0,0], "Science: Chemistry":[0,0], "Science: Cosmology":[0,0],
            "Science: Cybernetics":[0,0], "Science: Economics":[0,0], "Science: Genetics":[0,0], "Science: History":[0,0], "Science: Linguistics":[0,0],
            "Science: Philosophy":[0,0], "Science: Physics":[0,0], "Science: Planetology":[0,0], "Science: Psionicology":[0,0], "Science: Psychology":[0,0],
            "Science: Robotics":[0,0], "Science: Sophontology":[0,0], "Science: Xenology":[0,0], 
            "Seafarer: Ocean Ships":[0,0],
            "Seafarer: Personal":[0,0], "Seafarer: Sail":[0,0], "Seafarer: Submarine":[0,0], "Stealth":[0,0], "Steward":[0,0],
            "Streetwise":[0,0], "Survival":[0,0], "Tactics: Military":[0,0], "Tactics: Naval":[0,0], "Vacc Suit":[0,0],
            # "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3,
            # "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3,
            # "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3,
            # "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3, "Admin":-3,
            }
    @staticmethod
    def get_characteristics_map():
        return {
            Traveller.STR:0, Traveller.DEX:0, Traveller.END:0, Traveller.INT:0, Traveller.EDU:0, Traveller.SOC:0, 
            Traveller.MOR:0, Traveller.LCK:0, Traveller.SAN:0, Traveller.CHM:0, Traveller.PSI:0, Traveller.OTR:0
        }
    @staticmethod
    def get_characteristics_training_map():
        return {
            Traveller.STR:[0,0], Traveller.DEX:[0,0], Traveller.END:[0,0], Traveller.INT:[0,0], Traveller.EDU:[0,0], Traveller.SOC:[0,0], 
            Traveller.MOR:[0,0], Traveller.LCK:[0,0], Traveller.SAN:[0,0], Traveller.CHM:[0,0], Traveller.PSI:[0,0], Traveller.OTR:[0,0],
        }
    def get_total_skill_ranks(self):
        current_total_ranks = 0
        for skill in self.skills.keys():
            if self.skills[skill] > 0:
                current_total_ranks += self.skills[skill]
        return current_total_ranks
    def get_max_skill_ranks(self): return (self.characteristics[Traveller.EDU] + self.characteristics[Traveller.INT]) * 3
    def can_rank_up_in_skill(self): return self.get_total_skill_ranks() < self.get_max_skill_ranks()
    def __init__(self, initDict):
        super().__init__(initDict)
        self.skills = initDict.get("skills", Traveller.get_skill_map())
        self.skill_training = Traveller.get_skill_training_map()
        self.characteristics = initDict.get("characteristics", Traveller.get_characteristics_map())
        self.current_characteristics = dict(self.characteristics)
        self.characteristics_training = Traveller.get_characteristics_training_map()

        self._determind_fitness_based_on_stats()

        self.homeworld = initDict.get("homeworld", None)
        self.traits = initDict.get("traits", [])
        self.rads = 0

        self.pension = initDict.get("pension", None)
        self.debt = initDict.get("debt", None)
        self.cash = initDict.get("cash", None)
        self.assets = initDict.get("assets", [])
        self.living_cost = self.get_living_cost_based_on_social_score()
        self.equipped_armor = []
        self.equipped_weapons = []
        self.equipped_augments = []
        self.equipment = []

        self.allies = initDict.get("allies", [])
        self.contacts = initDict.get("contacts", [])
        self.rivals = initDict.get("rivals", [])
        self.enemies = initDict.get("enemies", [])

        self.wounds = []

        self.term_history = initDict.get("term history", [])
        self.description = initDict.get("description", [])
        self.bio_summary = initDict.get("bio", "")
        self.reputation = {"Law Enforcement": 0, "Order-Politics":0, "Politics":[{"Order"}], "Science":0, "Guilds": [
            {"name":"Merchant", "value": 0}, 
            {"name":"Travellers Aid Society", "value": 100},
            ]}
    def _determind_fitness_based_on_stats(self):
        if self.characteristics.get(Traveller.STR) :
            if self.characteristics.get(Traveller.STR) in [5, 4, 3]: self.fitness = "lean"
            elif self.characteristics.get(Traveller.STR) < 3: self.fitness = "feeble"
            elif self.characteristics.get(Traveller.STR) in [9, 10, 11]: self.fitness = "fit"
            elif self.characteristics.get(Traveller.STR) >= 12: self.fitness = "athletic"
            else: self.fitness = "average"
        else:
            self.fitness = "average"            
    def apply_wound(self, wound, debug=False):
        self.wounds.append(wound)
        damage = wound.effect.split(" ")
        for d in damage:
            for c in self.current_characteristics.keys():
                split = d.split("-")
                if split[0] in c[:3].upper():
                    self.current_characteristics[c] -= int(split[1])
                    if debug: print("Taking {} damage to {}".format(int(split[1]), c))
    def remove_wound(self, wound, debug=False):
        self.wounds.remove(wound)
        damage = wound.effect.split(" ")
        for d in damage:
            for c in self.current_characteristics.keys():
                split = d.split("-")
                if split[0] in c[:3].upper():
                    self.current_characteristics[c] += int(split[1])
                    if debug: print("Taking {} damage to {}".format(int(split[1]), c))
    def get_mass_carried(self):
        total = 0
        for item in self.equipped_armor:
            total += item.weight
        for item in self.equipped_weapons:
            total += item.weight
        for item in self.equipment:
            total += item.weight
        return total
    def get_upp(self):
        return "{}{}{}{}{}{}".format(
            Utils.get_hex_from_decimal(self.characteristics[Traveller.STR]),
            Utils.get_hex_from_decimal(self.characteristics[Traveller.DEX]),
            Utils.get_hex_from_decimal(self.characteristics[Traveller.END]),
            Utils.get_hex_from_decimal(self.characteristics[Traveller.INT]),
            Utils.get_hex_from_decimal(self.characteristics[Traveller.EDU]),
            Utils.get_hex_from_decimal(self.characteristics[Traveller.SOC]),
            )
    def get_upp_plus_6(self):
        return "{}{}{}{}{}{}-{}{}{}{}{}{}".format(
            Utils.get_hex_from_decimal(self.characteristics[Traveller.STR]),
            Utils.get_hex_from_decimal(self.characteristics[Traveller.DEX]),
            Utils.get_hex_from_decimal(self.characteristics[Traveller.END]),
            Utils.get_hex_from_decimal(self.characteristics[Traveller.INT]),
            Utils.get_hex_from_decimal(self.characteristics[Traveller.EDU]),
            Utils.get_hex_from_decimal(self.characteristics[Traveller.SOC]),

            Utils.get_hex_from_decimal(self.characteristics[Traveller.MOR]),
            Utils.get_hex_from_decimal(self.characteristics[Traveller.LCK]),
            Utils.get_hex_from_decimal(self.characteristics[Traveller.SAN]),
            Utils.get_hex_from_decimal(self.characteristics[Traveller.CHM]),
            Utils.get_hex_from_decimal(self.characteristics[Traveller.PSI]),
            Utils.get_hex_from_decimal(self.characteristics[Traveller.OTR]),
            )
    def get_dice_modifier(self, value):
        if value < 1: return -3
        elif value in [1, 2]: return -2
        elif value in [3, 5]: return -1
        elif value in [9, 11]: return 1
        elif value in [12, 14]: return 2
        elif value > 15: return 3
        else: return 0
    def __str__(self): return "{} {}, {} y/o {} {}.".format( self.name, self.surname, self.age, self.sex, self.species )
    def increase_skill(self, skill, level):
        if skill in self.skills.keys():
            self.skills[skill]+=level
            Utils.set_experience_levels_for_skill(traveller, skill)
            return True
        return False
    def increase_skill_exp(self, skill, exp=1):
        if skill in self.skill_training.keys():
            self.skill_training[skill][0]+=exp
            return True
        return False
    def increase_characteristic(self, characteristic, value, is_temporary=False):
        result = False
        if characteristic in self.characteristics.keys() and not is_temporary:
            self.characteristics[characteristic] += value
            result = True
            Utils.set_experience_levels_for_characteristic(traveller, characteristic)
        if characteristic in self.current_characteristics.keys():
            self.current_characteristics[characteristic] += value
            result = True
        return result
    def increase_characteristic_exp(self, characteristic, exp=1):
        if characteristic in self.characteristics_training.keys():
            self.characteristics_training[characteristic][0] += exp
            return True
        return False
    def become_trained_in_skill(self, general_skill):
        skill_list = self.skills.keys()
        if general_skill not in skill_list:
            self.skills[general_skill] = 0
        for skill in skill_list:
            if general_skill in skill:
                self.skills[skill] = 0
                return True
        return False
    def reset_characteristics(self):
        for c in self.characteristics.keys():
            self.current_characteristics[c] = self.characteristics[c]
    def get_skills_as_string(self):
        text = ""
        for skill in self.skills.keys():
            if self.skills[skill] >= 0:
                text += "{} {}, ".format(skill, self.skills[skill])
        if len(text) > 0:
            text = text[:-2]
        return text
    def get_living_cost_based_on_social_score(self):
        print(self.characteristics[Traveller.SOC])
        if self.characteristics[Traveller.SOC] == 4: return 800
        elif self.characteristics[Traveller.SOC] == 5: return 1000
        elif self.characteristics[Traveller.SOC] == 6: return 1200
        elif self.characteristics[Traveller.SOC] == 7: return 1500
        elif self.characteristics[Traveller.SOC] in [8, 9]: return 2000
        elif self.characteristics[Traveller.SOC] in [10,11]: return 2500
        elif self.characteristics[Traveller.SOC] in [12, 13]: return 5000
        elif self.characteristics[Traveller.SOC] in [14]: return 12000
        elif self.characteristics[Traveller.SOC] >= 15: return 20000
        else:
            return 400

class CreateTraveller():
    @staticmethod
    def new_traveller(): #
        #                               For Traveller creation, age starts at 18.
        #         0                     1             2         3      4      5        6      7      
        # python ./character_manager.py new-traveller Fname     Lname  sex    species  height weight 
        # python ./character_manager.py new-traveller Andromeda Antari Female Human
        # python ./character_manager.py new-traveller Andromeda Antari Female Human 68 169
        #usage()
        
        init_dict={}
        init_dict["name"] = sys.argv[2] 
        
        init_dict["surname"] = sys.argv[3] 

        name = sys.argv[2] 
        surname = sys.argv[3] 
        traveller = Traveller.load(init_dict["name"], init_dict["surname"])
        if traveller is None:
            init_dict["sex"] = sys.argv[4] 
            init_dict["age"] = 18
            init_dict["species"] = sys.argv[5] 
            init_dict["subspecies"] = DescriptionGenerator.species.get(init_dict["species"], "Standard")
            init_dict["traits"] = CharacterUtils.get_species_traits(init_dict["species"])

            init_dict["height"] = float(sys.argv[6]) # height in inches
            if init_dict["height"] < 1.0:
                print("Not an accepted height level: \"{}\"".format(init_dict["height"]))
                exit(6) 
            init_dict["weight"] = float(sys.argv[7]) # weight in lbs
            if init_dict["weight"] < 1.0:
                print("Not an accepted weight level: \"{}\"".format(init_dict["weight"]))
                exit(7)
            init_dict["fitness"] = "average"
            # Character Creation
            traveller = Traveller(init_dict)
            print(str(traveller))
            print("Let's make a Traveller!")
            print("\nHello Traveller!")
            traveller.homeworld = input("What is your Home planet? $>")
        if traveller.setup_progress < 1:
            CreateTraveller.setup_characteristics(traveller)
            if traveller.characteristics[Traveller.STR] > 7:
                traveller.fitness = Character.fitness_levels[2]
            elif traveller.characteristics[Traveller.STR] > 9:
                traveller.fitness = Character.fitness_levels[1]
            elif traveller.characteristics[Traveller.STR] < 5:
                traveller.fitness = Character.fitness_levels[4]
            traveller.save()
        if traveller.setup_progress < 2:
            CreateTraveller.setup_skills(traveller)
            traveller.save()
        if traveller.setup_progress < 3:
            CreateTraveller.setup_weapons(traveller)
            traveller.save()
        if traveller.setup_progress < 4:
            CreateTraveller.setup_armor(traveller)
            traveller.save()
        #CreateTraveller.setup_augments(traveller)
        if traveller.setup_progress < 5:
            CreateTraveller.setup_finances(traveller)
            traveller.save()
        if traveller.setup_progress < 6:
            CreateTraveller.setup_lifepaths(traveller)
            traveller.save()
        return traveller
    @staticmethod
    def setup_characteristics(traveller):
        done=False
        while not done:
            for c in traveller.characteristics.keys():
                if c == Traveller.PSI:
                    TerminalUtils.pprint("Psionics are usualy outlawed and Travellers start with it at 0. There are life events that grant Psionics \"naturally\" if you want to let the dice fall where they may. But if you want, you can start with it as non-zero. ")
                    value = input("What is your *{}* characteristic? (roll yourself, or enter #d# or #D to roll here. Empty is 0) $>".format(c))
                else:
                    value = input("What is your *{}* characteristic? (roll yourself, or enter #d# or #D to roll here. Empty is 8) $>".format(c))
                if "d" in value:
                    roll_values = value.split("d")
                    v1 = int(roll_values[0])
                    v2 = int(roll_values[1])
                    total = 0
                    for i in range(v1):
                        total += random.randint(1,v2)
                    value = total
                elif "D" in value:
                    total = 0
                    for i in range(int(value[0])):
                        total += random.randint(1, 6)
                    value = total
                elif value == "":
                    if c == Traveller.PSI:
                        value = 0
                    else:
                        value = 8
                traveller.characteristics[c] = int(value)
                traveller.current_characteristics[c] = traveller.characteristics[c]
                print("{0:10}: {1:2} | {2:2} [{3:2}]".format(
                    c, 
                    traveller.characteristics[c], 
                    traveller.current_characteristics[c],
                    traveller.get_dice_modifier(traveller.current_characteristics[c])
                    ))
              
            traveller.reset_characteristics()
            print("Characteristics:")
            for key in traveller.characteristics.keys():
                print("{0:<10}: {1:>2} | {2:>2} [{3:>2}]".format(
                    key, 
                    traveller.characteristics[key], 
                    traveller.current_characteristics[key],
                    traveller.get_dice_modifier(traveller.current_characteristics[key])
                    ))
            if input("This Okay? $>").lower() in ["y", "yes", "ye"]:
                done = True
            print("")
        CharacterUtils.set_experience_levels_for_characteristics(traveller)
        traveller.setup_progress = 1
    @staticmethod
    def setup_skills(traveller):
        done=False
        while not done:
            for s in traveller.skills.keys():
                value = input("What is your *{}* skill rank? (Empty is -3 or untrained) $>".format(s))
                if value == "":
                    value = -3
                else:
                    value = int(value)
                if value >= 0:
                    traveller.skills[s] = value
            print("Skills:")
            for key in traveller.skills.keys():
                if traveller.skills[key] >= 0 :
                    print("{}: {}".format(key, traveller.skills[key]))
            if input("This Okay? $>").lower() in ["y", "yes", "ye"]:
                done = True
            print("")
        CharacterUtils.set_experience_levels_for_skills(traveller)
        traveller.setup_progress = 2
    @staticmethod
    def setup_weapons(traveller):
        done=False
        while not done:
            number_of_weapons = int(input("How many weapons do you have? $>"))
            if (number_of_weapons < 0):
                print("Number of weapons needs to be 0 or higher.")
                continue
            for i in range(number_of_weapons):
                name = input("Weapon name: $>")
                description = input("Weapon description: $>")
                weight = input("Weapon weight: $>")
                size = input("Weapon size: $>")
                tech_level = int(input("Weapon Tech Level: $>"))
                traits = input("Weapon traits (split by \"|\"): $>")
                traits = traits.split("|")
                features = input("Weapon features (split by \", \"): $>")
                features = features.split(", ")
                weapon_range = input("Weapon Range: $>")
                weapon_damage = input("Weapon Damage (2D + 2): $>")
                weapon_magazine_size = "N/A"
                if weapon_range != "melee":
                    weapon_magazine_size = int(input("Weapon magazine size : $>"))
                    if weapon_magazine_size < 0:
                        weapon_magazine_size = 1
                weapon_dict={
                    "name":name, "description":description,
                    "weight":weight, "size":size,
                    "tech level":tech_level, "traits":traits,
                    "features":features,
                    "range": weapon_range, "damage": weapon_damage, "magazine": weapon_magazine_size,

                }
                weapon = Weapon(weapon_dict)
                print(weapon)
                traveller.equipped_weapons.append(weapon)
            if input("This Okay? $>").lower() in ["y", "yes", "ye"]:
                done = True
            print("")
        traveller.setup_progress = 3
    @staticmethod
    def edit_weapons(traveller):
        done=False
        while not done:
            for item in traveller.equipped_weapons:
                print(str(item))
            opt = input("add or remove Weapons? $>")
            if opt == "add":
                name = input("Weapon name: $>")
                description = input("Weapon description: $>")
                weight = input("Weapon weight: $>")
                size = input("Weapon size: $>")
                tech_level = int(input("Weapon Tech Level: $>"))
                traits = input("Weapon traits (split by \"|\"): $>")
                traits = traits.split("|")
                features = input("Weapon features (split by \", \"): $>")
                features = features.split(", ")
                weapon_range = input("Weapon Range: $>")
                weapon_damage = input("Weapon Damage (2D + 2): $>")
                weapon_magazine_size = "N/A"
                if weapon_range != "melee":
                    weapon_magazine_size = int(input("Weapon magazine size : $>"))
                    if weapon_magazine_size < 0:
                        weapon_magazine_size = 1
                weapon_dict={
                    "name":name, "description":description,
                    "weight":weight, "size":size,
                    "tech level":tech_level, "traits":traits,
                    "features":features,
                    "range": weapon_range, "damage": weapon_damage, "magazine": weapon_magazine_size,

                }
                weapon = Weapon(weapon_dict)
                print(weapon)
                traveller.equipped_weapons.append(weapon)
            elif opt == "remove":
                for item in traveller.equipped_weapons:
                    print(str(item))
                weapon_name = input("which Weapon? $>")
                weapon = None
                for weap in traveller.equipped_weapons:
                    if weapon_name == weap.name:
                        weapon = weap
                traveller.equipped_weapons.remove(weapon)
            
            if input("This Okay? $>").lower() in ["y", "yes", "ye"]:
                done = True
            print("")
        traveller.save()
    @staticmethod
    def setup_armor(traveller):
        done=False
        while not done:
            number_of_armors = int(input("How many Armor suits do you have? $>"))
            if (number_of_armors < 0):
                print("Number of weapons needs to be 0 or higher.")
                continue
            for i in range(number_of_armors):
                name = input("Armor name: $>")
                description = input("Armor description: $>")
                weight = input("Armor weight: $>")
                size = input("Armor size: $>")
                tech_level = int(input("Armor Tech Level: $>"))
                traits = input("Armor traits (split by \"|\"): $>")
                traits = traits.split("|")
                features = input("Armor features (split by \", \"): $>")
                features = features.split(", ")
                protection = int(input("Armor protection: $>"))
                rad_protection = int(input("Armor radiation protection: $>"))
                armor_dict={
                    "name":name, "description":description,
                    "weight":weight, "size":size,
                    "tech level":tech_level, 
                    "traits":traits,
                    "features":features,
                    "protection": protection,
                    "radiation protection": rad_protection
                }
                armor = Armor(armor_dict)
                print(armor)
                traveller.equipped_armor.append(armor)
            if input("This Okay? $>").lower() in ["y", "yes", "ye"]:
                done = True
            print("")
        traveller.setup_progress = 4
    @staticmethod
    def edit_armor(traveller):
        done=False
        while not done:
            opt = input("add or remove Armor? $>")
            for item in traveller.equipped_armor:
                print(str(item))
            if opt == "add":
                name = input("Armor name: $>")
                description = input("Armor description: $>")
                weight = input("Armor weight: $>")
                size = input("Armor size: $>")
                tech_level = int(input("Armor Tech Level: $>"))
                traits = input("Armor traits (split by \"|\"): $>")
                traits = traits.split("|")
                features = input("Armor features (split by \", \"): $>")
                features = features.split(", ")
                protection = int(input("Armor protection: $>"))
                rad_protection = int(input("Armor radiation protection: $>"))
                armor_dict={
                    "name":name, "description":description,
                    "weight":weight, "size":size,
                    "tech level":tech_level, 
                    "traits":traits,
                    "features":features,
                    "protection": protection,
                    "radiation protection": rad_protection
                }
                armor = Armor(armor_dict)
                print(armor)
                traveller.equipped_armor.append(armor)
            elif opt == "remove":
                for item in traveller.equipped_armor:
                    print(str(item))
                armor_name = input("which Armor? $>")
                armor = None
                for a in traveller.equipped_armor:
                    if armor_name == a.name:
                        armor = a
                traveller.equipped_armor.remove(armor)
            if input("This Okay? $>").lower() in ["y", "yes", "ye"]:
                done = True
            print("")
        traveller.save()
    @staticmethod
    def edit_equipment(traveller):
        done=False
        while not done:
            opt = input("add or remove Equipment? $>")
            for item in traveller.equipment:
                print(str(item))
            if opt == "add":
                name = input("Item name: $>")
                description = input("Item description: $>")
                weight = input("Item weight: $>")
                size = input("Item size: $>")
                tech_level = int(input("Item Tech Level: $>"))
                traits = input("Item traits (split by \"|\"): $>")
                traits = traits.split("|")
                item_dict={
                    "name":name, "description":description,
                    "weight":weight, "size":size,
                    "tech level":tech_level, "traits":traits,
                }
                item = item(item_dict)
                print(item)
                traveller.equipment.append(item)
            elif opt == "remove":
                for item in traveller.equipment:
                    print(str(item))
                item_name = input("which Equipment? $>")
                item = None
                for i in traveller.equipment:
                    if item_name == i.name:
                        item = i
                traveller.equipment.remove(armor)
            if input("This Okay? $>").lower() in ["y", "yes", "ye"]:
                done = True
            print("")
        traveller.save()
    @staticmethod
    def edit_cash(traveller):
        done=False
        value=None
        while not done:
            value = input("{} has Cr{}. What do they have now? $>".format(traveller.name, traveller.cash))
            if value == "":
                print("An empty string is not a value cash amount.")
                continue
            else:
                print("{} had Cr{}, but now has Cr{}.".format(traveller.name, traveller.cash, int(value)))
                if input("This Okay? $>").lower() in ["y", "yes", "ye"]:
                    done = True
                    traveller.cash = int(value)
            print("")
        traveller.save()
    # @staticmethod def setup_augments(traveller):  
    # @staticmethod def edit_augments(traveller):   
    @staticmethod
    def setup_finances(traveller):
        done=False
        while not done:
            has_ship_shares = input("Do you have ship shares? $>") in ["y", "ye", "yes"]
            if has_ship_shares:
                traveller.assets.append({"ship shares":int(input("How may have ship shares do you have? $>"))})
            traveller.cash = int(input("How any credits do you have? $>"))
            traveller.debt = int(input("How much debt do you have? $>"))
            if (TerminalUtils.selectMenuItem(options=["Yes", "No"], prompt="Traveller Living cost based on SOCIAL [{}] = {}.\nIs this Okay? (Yes/No) $>".format(
                traveller.characteristics[Traveller.SOC], traveller.living_cost
                )) =="No"):
                traveller.living_cost = int(input("What is your Living Cost? $>"))
            traveller.pension = int(input("What is your Pension? $>"))
            if input("This Okay? $>").lower() in ["y", "yes", "ye"]:
                done = True
            print("")
        traveller.setup_progress = 5
    @staticmethod
    def setup_lifepaths(traveller):
        done=False
        term = {"term:":None, "career/assignment":None, "survived":None, "commission":None, "advancement":None, "rank":None, "notes":None}
        planned_terms = 0
        terms=[]
        current_career = None
        current_rank = None
        while not done:
            planned_terms = int(input("How many terms do you have? $>"))
            for i in range(planned_terms):
                career_and_assignment = input("What was the term {} Career/Assignment (Agent/Law Enforcement)? $>".format(i+1))
                did_survive = input("Did you survive? $>").lower() in ["y", "yes", "ye"]
                did_get_comission = input("Did you get comission? $>").lower() in ["y", "yes", "ye"]
                did_advance = input("Did you advance in career rank? $>").lower() in ["y", "yes", "ye"]
                rank = int(input("What is your rank? $>"))
                notes = input("Enter events, connections & Notes? $>")
                term = {
                    "term:":i+1, 
                    "career/assignment":career_and_assignment, 
                    "survived":did_survive, 
                    "commission":did_get_comission, 
                    "advancement":did_advance, 
                    "rank":rank, 
                    "notes":notes
                    }
                terms.append(term)
            if input("This Okay? $>").lower() in ["y", "yes", "ye"]:
                done = True
            else:
                planned_terms = 0
                terms=[]
                current_career = None
                current_rank = None
            print("")
        traveller.term_history = terms
        traveller.setup_progress = 6
    @staticmethod
    def add_contact_character():
        character_type = sys.argv[1]
        init_dict={}
        name = sys.argv[2] 
        surname = sys.argv[3] 
        traveller = Traveller.load(name, surname)
        
        npc_name = sys.argv[4] 
        npc_surname = sys.argv[5]
        other_traveller = None
        npc = None
        if "relation" in character_type.lower():
            relation = sys.argv[6]
            relationship = sys.argv[7]
            other_traveller = Traveller.load(npc_name, npc_surname)
            if other_traveller is None:
                raise Exception("Traveller File Does Not Exist, please make a new Traveller.")
            # python ./character_manager.py add-relation Andromeda Antari Kayla Wu sibling "Life-long friend"

            traveller.relations["{}-{}".format(other_traveller.name, other_traveller.surname)] = {
            "character": "{}-{}".format(other_traveller.name, other_traveller.surname), 
            "relation" : relation, 
            "relationship": [relationship], 
            }
            other_traveller.relations["{}-{}".format(traveller.name, traveller.surname)] = {
            "character": "{}-{}".format(traveller.name, traveller.surname), 
            "relation" : relation, 
            "relationship": [relationship], 
            }
            other_traveller.save()
        else:
            # python ./character_manager.py add-relation Andromeda Antari firstname lastname reaction species-subspecies occupation system hex age sex-gender height weight
            reaction = sys.argv[6]
            reaction = reaction[0].upper() + reaction[1:].lower()
            species = sys.argv[7] 
            subspecies = "random"
            if "-" in species:
                parts = species.split("-")
                species = parts[0]
                subspecies = parts[1]

            occupation = sys.argv[8]

            system_name = sys.argv[9]

            hex_coord = sys.argv[10]

            
            age="random-adult"
            terms = "random"
            if len(sys.argv) > 11:
                if sys.argv[11].lower() not in ["random", "random-adult", "random-longlife"]:
                    age = int(sys.argv[11])
                    if age-18 > 0:
                        terms = int((age-18)//4)
            sex="random"
            gender="random"
            if len(sys.argv) > 12:
                sex_and_gender = sys.argv[12]
                if "-" in sex_and_gender:
                    sex_and_gender=sex_and_gender.split("-")
                    sex = sex_and_gender[0]
                    gender = sex_and_gender[1]
                    if gender.lower() in ["s","same"]:
                        print("Same")
                        gender = "Same as sex"
                    elif gender.lower() in ["o","opposite"]:
                        print("Opposite")
                        gender = "Opposite of sex"
                    elif gender.lower() in ["nb","nonbinary"]:
                        print("Non-binary")
                        gender = "Non-binary"
                else:
                    sex = sex_and_gender
            height = "random"
            weight="random"
            if len(sys.argv) > 13: 
                if sys.argv[13] not in ["random"]:
                    height = float(sys.argv[13])
            if len(sys.argv) > 14: 
                if sys.argv[14] not in ["random"]:
                    weight = float(sys.argv[14])
            npc = Npc(Npc.generate(
                npc_name, npc_surname, 
                age=age, terms=terms,
                sex=sex, apparent_gender=gender,
                species=species, subspecies=subspecies, 
                height=height, weight=weight, 
                fitness="random",
                upp="random", career=occupation,
                hair={"length":None, "style":None, "color":None, "beard":None},
                origin=None, 
                disposition="random", 
                motivation1="random", motivation1_value="random", 
                motivation2="random", motivation2_value="random", 
                quirk1="random", quirk2="random",
                hex_location=hex_coord,
                system_location=system_name,
                local_location="Downport",
                reaction=reaction,
                ))
            print(str(npc))
        
            if "ally" in character_type.lower():
                traveller.allies.append(npc)
            elif "contact" in character_type.lower():
                traveller.contacts.append(npc)
            elif "rival" in character_type.lower():
                traveller.rivals.append(npc)
            elif "enemy" in character_type.lower():
                traveller.enemies.append(npc)
        traveller.save()
    @staticmethod
    def edit_contact(npc):
        dispositions = ["Happy", "Sad", "Angry", "Nervous", 
            "Cool", "Sinister", 
            "Frightened", "Annoyed", "Businesslike", "Very friendly","Amorous/Flirtatious"]
        motivations = ["Fame","Career","Respect","Love & Romance", "Wealth & Money",
            "Helping Others", "Helping Self", "Helping Family/Nepotism","Greed", "Pain & Suffering",
            "Control", "Safety & Security", "Protecting Family","Honor/Loyalty","Discovering","Knowledge",
            "Health","Power","Creating/Creativity","Contributing","Approval/Acceptance","Curiosity","Idealism",
            "Justice","Independence","Equality","Order","Lust","Social Interaction","Status","Tranquility",
            "Vengeance", "Violence", "Stubbornness", "Leadership", "Generosity", "Cowardice", "Fellowship", 
            "Wisdom","Honesty", "Pomposity/Arrogance", "Ruthless", "Liar", "Harmless Eccentric", "Insane"]
        quirks = ["Facial tick", "Artificial arm", "Cyber-eye", "Cyber-visor", 
            "Unpleasant odor", "Cough", "Sneezing", "Boils/warts", "Burns", "Scars", 
            "Bandaged arm", "Limp", "Leg Brace", "Very smart", "Very unkempt", 
            "Too many clothes", "Too few clothes", "Open weapon", "Drunk", "Dark glasses", 
            "Breathing mask", "Large bag", "Notable headgear", "Notable gloves", 
            "Notable clothes", "Pet/Familiar", "Personal bot","Obsessive note-taking", 
            "Wants to come along","Hums","Whistles", "Accomplice","Strong accent",
            "Long fingernails", "Notable hair","Very formal language","Poor Language",
            "Psionic","Wears a Psionic Helmet","Constantly on phone","Constantly on net", 
            "Eschews technology","Has baby with them", "Bare feet", "Notable footwear", 
            "Swears constantly", "Uses long words/old-fashioned speech", "Pious religious", 
            "Evangelical religious", "Constantly eating","Darting eyes"]
        hairLengths = ["Bald", "Buzz-cut", "Short", "Average","Long"]
        hairColors = ["Grey/White", "Blonde", "Brown","Black","Colored"]
        hairStyles = ["Fanned", "Tiered", "Straight","Curly","Asymmetric"]
        beardChoices = ["None", "Goatee", "Big scraggy beard", "Neat beard","Mustache", "Handlebar Mustache"]
        if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Edit NPC Name? ({} {}). $>".format(npc.name, npc.surname)) == "Yes":
            npc.name = input("What is their new name? ({}). $>".format(npc.name))
            npc.surname = input("What is their new surname? ({}). $>".format(npc.surname))
        if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Edit NPC species? ({} {}). $>".format(npc.species, npc.subspecies)) == "Yes":
            npc.species = input("What is their new species? ({}). $>".format(npc.species))
            npc.subspecies = input("What is their new subspecies? ({}). $>".format(npc.subspecies))
        if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Edit NPC reaction? ({}). $>".format(npc.reaction)) == "Yes":
            npc.reaction = TerminalUtils.selectMenuItem(options=["Allied", "Friendly", "Neutral", "Guarded", "Hostile"], prompt="What is their new reaction? ({}). $>".format(npc.reaction))
        if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Edit NPC occupation, age, and terms? ({} {} terms, {} y/o). $>".format(npc.career, npc.terms, npc.age)) == "Yes":
            npc.career = input("What is their new occupation? ({}). $>".format(npc.career))
            npc.terms = int(input("What is their new terms? ({}). $>".format(npc.terms)))
            npc.age = int(input("What is their new age? ({}). $>".format(npc.age)))
        if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Edit NPC UPP? ({}). $>".format(npc.upp)) == "Yes":
            npc.upp = input("What is their new UPP? ({}). $>".format(npc.upp))
        if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Edit NPC Hair? ({} {} {} {}). $>".format(npc.hair["length"], npc.hair["style"], npc.hair["color"], 
            npc.hair.get("beard", "-") if npc.hair.get("beard") else "-"
            )) == "Yes":
            npc.hair["length"] = TerminalUtils.selectMenuItem(options=hairLengths, prompt="What is their new hair length? ({}). $>".format(npc.hair["length"]))
            npc.hair["style"] = TerminalUtils.selectMenuItem(options=hairColors, prompt="What is their new hair style? ({}). $>".format( npc.hair["style"] ))
            npc.hair["color"] = TerminalUtils.selectMenuItem(options=hairStyles, prompt="What is their new hair color? ({}). $>".format(npc.hair["color"] ))
            beard = TerminalUtils.selectMenuItem(options=beardChoices, prompt="What is their new beard style? ({}). $>".format(npc.hair.get("beard", "-")))
            npc.hair["beard"] = beard if beard != "None" else None
        if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Edit NPC disposition? ({}). $>".format(npc.disposition)) == "Yes":
            print("Possible dispositions:")
            text = ""
            for disposition in dispositions:
                text += disposition + ", "
            text = text[:-2]
            TerminalUtils.pprint(text)
            npc.disposition = input("What is their new disposition? ({}). $>".format(npc.disposition))
        if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Edit NPC motivations? ({} {}). $>".format(npc.motivation1, npc.motivation2)) == "Yes":
            print("Possible motivations:")
            text = ""
            for motivation in motivations:
                text += motivation + ", "
            text = text[:-2]
            TerminalUtils.pprint(text)
            npc.motivation1 = input("What is their new motivation 1? ({}). $>".format(npc.motivation1))
            npc.motivation2 = input("What is their new motivation 2? ({}). $>".format(npc.motivation2))
        if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Edit NPC quirks? ({} {}). $>".format(npc.quirk1, npc.quirk2)) == "Yes":
            print("Possible quirks:")
            text = ""
            for quirk in quirks:
                text += quirk + ", "
            text = text[:-2]
            TerminalUtils.pprint(text)
            npc.quirk1 = input("What is their new quirk 1? ({}). $>".format(npc.quirk1))
            npc.quirk2 = input("What is their new quirk 2? ({}). $>".format(npc.quirk2))
        print(str(npc))
    @staticmethod
    def remove_contact_character():
        character_type = sys.argv[1].split("-")[1]
        init_dict={}
        name = sys.argv[2] 
        surname = sys.argv[3] 
        traveller = Traveller.load(name, surname)
        
        npc_name = sys.argv[4] 
        npc_surname = sys.argv[5]
        if character_type.lower() == "ally":
            for ally in traveller.allies:
                if ally.surname == npc_surname and ally.name == npc_name:
                    traveller.allies.remove(ally)

        elif character_type.lower() == "contact":
            for contact in traveller.contacts:
                if contact.surname == npc_surname and contact.name == npc_name:
                    traveller.contacts.remove(contact)

        elif character_type.lower() == "rival":
            for rival in traveller.rivals:
                if rival.surname == npc_surname and rival.name == npc_name:
                    traveller.rivals.remove(rival)

        elif character_type.lower() == "enemy":
            for enemy in traveller.enemies:
                if enemy.surname == npc_surname and enemy.name == npc_name:
                    traveller.enemies.remove(enemy)
        elif "relation" in character_type.lower():
            for relation_name in traveller.relations.keys():
                if "{}-{}".format(relation.surname,relation.name).lower() == relation_name.lower():
                    traveller.relations.pop(relation_name)
        else:
            print(sys.argv)
            print("{} {}".format(npc_name, npc_surname))
            raise Exception("Not recognized. {}".format(character_type))
        traveller.save()
    @staticmethod
    def edit_contact_character():
        character_type = sys.argv[1].split("-")[1]
        init_dict={}
        name = sys.argv[2] 
        surname = sys.argv[3] 
        traveller = Traveller.load(name, surname)
        
        npc_name = sys.argv[4] 
        npc_surname = sys.argv[5]
        if character_type.lower() == "ally":
            for ally in traveller.allies:
                if ally.surname == npc_surname and ally.name == npc_name:
                    CreateTraveller.edit_contact(ally)

        elif character_type.lower() == "contact":
            for contact in traveller.contacts:
                if contact.surname == npc_surname and contact.name == npc_name:
                    CreateTraveller.edit_contact(contact)

        elif character_type.lower() == "rival":
            for rival in traveller.rivals:
                if rival.surname == npc_surname and rival.name == npc_name:
                    CreateTraveller.edit_contact(rival)

        elif character_type.lower() == "enemy":
            for enemy in traveller.enemies:
                if enemy.surname == npc_surname and enemy.name == npc_name:
                    CreateTraveller.edit_contact(enemy)
        elif "relation" in character_type.lower():
            print(sys.argv)
            print("{} {}".format(npc_name, npc_surname))
            raise Exception("Not allowed to edit Traveller Relation here. They should have their own file you can edit.\nUse \"python ./character_manager.py <option> {} {} <args>\" to edit this character.".format(npc_name, npc_surname))
        else:
            print(sys.argv)
            print("{} {}".format(npc_name, npc_surname))
            raise Exception("Not recognized. {}".format(character_type))
        traveller.save()
    @staticmethod
    def edit_text_field():
        edit_text_type = sys.argv[1].split("-")[0]
        init_dict={}
        name = sys.argv[2] 
        surname = sys.argv[3] 
        traveller = Traveller.load(name, surname)
        if edit_text_type == "notes":
            for text in traveller.notes:
                TerminalUtils.pprint("{}: {}\n".format(traveller.notes.index(text)+1, text))
            opt = input("add, edit, remove? $>")
            if opt.lower() =="add":
                new_text = input("Add notes: $>")
            elif opt.lower() =="edit":
                index = int(input("Which entry?"))-1
                index = max(min(index, len(traveller.notes)-1), 0)
                print(traveller.notes[index])
                traveller.notes[index] = input("Edit notes: $>")
            elif opt.lower() =="remove":
                index = int(input("Which entry?"))-1
                index = max(min(index, len(traveller.notes)-1), 0)
                traveller.notes.remove(traveller.notes[index])
        elif edit_text_type == "description":
            for text in traveller.description:
                TerminalUtils.pprint("{}: {}\n".format(traveller.description.index(text)+1, text))
            opt = input("add, edit, remove? $>")
            if opt.lower() =="add":
                new_text = input("Add description: $>")
            elif opt.lower() =="edit":
                index = int(input("Which entry?"))-1
                index = max(min(index, len(traveller.description)-1), 0)
                print(traveller.description[index])
                traveller.description[index] = input("Edit description: $>")
            elif opt.lower() =="remove":
                index = int(input("Which entry?"))-1
                index = max(min(index, len(traveller.description)-1), 0)
                traveller.description.remove(traveller.description[index])
        traveller.save()
    @staticmethod
    def traveller_characteristic_exp_gain():
         #         0                     1         2     3     4     5
        # python ./character_manager.py exp-skill Fname Lname skill exp-value
        #usage()
        name = sys.argv[2] 
        surname = sys.argv[3] 
        traveller = Traveller.load(name, surname)
        characteristic = sys.argv[4]
        for c in traveller.characteristics.keys():
            if characteristic.lower() in c.lower() or c.lower() in characteristic.lower():
                characteristic = c
        value = 1
        if len(sys.argv) > 4:
            value = sys.argv[5]
            value = int(value)
        traveller.increase_characteristic_exp(characteristic, value)
        print("{} {} raised their {} characteristic by {} exp, putting it at [{}/{}]".format(
            traveller.name, traveller.surname,
            characteristic,
            value,
            traveller.characteristics_training[characteristic][0],
            traveller.characteristics_training[characteristic][1],
            )
            )
        if traveller.characteristics_training[characteristic][0] >= traveller.characteristics_training[characteristic][1]:
            traveller.characteristics[characteristic] += 1
            traveller.current_characteristics[characteristic] += 1
            traveller.characteristics_training[characteristic][0] -= traveller.characteristics_training[characteristic][1]
            CharacterUtils.set_experience_levels_for_characteristic(traveller, characteristic)
            print("{} {} ranked up their {} characteristic to {} [{}]. Next rank requires [{}/{}] Experience.".format(
            traveller.name, traveller.surname,
            characteristic,
            traveller.characteristics[characteristic],
            traveller.get_dice_modifier(traveller.characteristics[key]),
            traveller.characteristics_training[characteristic][0],
            traveller.characteristics_training[characteristic][1],
            )
            )
        traveller.save()
    @staticmethod
    def traveller_skill_exp_gain():
        #         0                     1         2     3     4     5
        # python ./character_manager.py exp-skill Fname Lname skill exp_value
        #usage()
        name = sys.argv[2] 
        surname = sys.argv[3] 
        traveller = Traveller.load(name, surname)
        skill = sys.argv[4]
        for s in traveller.skills.keys():
            if skill.lower() in s.lower() or s.lower() in skill.lower():
                skill = s
        value = 1
        if len(sys.argv) > 4:
            value = sys.argv[5]
            value = int(value)
        traveller.increase_skill_exp(skill, value)
        print("{} {} raised their {} skill by {} exp, putting it at [{}/{}]".format(
            traveller.name, traveller.surname,
            skill,
            value,
            traveller.skill_training[skill][0],
            traveller.skill_training[skill][1],
            )
            )
        if traveller.skill_training[skill][0] >= traveller.skill_training[skill][1]:
            if traveller.skills[skill] < 0:
                traveller.skills[skill] = 0
            else:
                traveller.skills[skill] += 1
            traveller.skill_training[skill][0] -= traveller.skill_training[skill][1]
            CharacterUtils.set_experience_levels_for_skills(traveller)
            print("{} {} ranked up their {} skill to {} [{}]. Next rank requires [{}/{}] Experience.".format(
            traveller.name, traveller.surname,
            skill,
            traveller.skills[skill],
            traveller.get_dice_modifier(traveller.skills[skill]),
            traveller.skill_training[skill][0],
            traveller.skill_training[skill][1],
            )
            )
        traveller.save()
    @staticmethod
    def add_traits(traveller):
        # python ./character_manager.py add-traits <name> <surname> "<trait: trait effect>"
        new_trait = ""
        if len(sys.argv) > 4: 
            new_trait = sys.argv[4] 
        else:
            new_trait = input("Enter the trait: (trait: trait effect)\n$>")
            print("")
        if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Is this the trait you want?. $>"):
            traveller.traits.append(new_trait)
    @staticmethod
    def edit_traits(traveller):
        # python ./character_manager.py edit-traits <name> <surname>
        # pick a trait, re-enter trait information
        done=False
        if len(traveller.traits) > 0:
            print("{} {}'s Traits:".format(traveller.name, traveller.surname))
            trait_names = []
            for trait in traveller.traits:
                trait_name = trait_names.split(":")[0]
                trait_names.append(trait_name)
                TerminalUtils.pprint("-   {}".format(trait), indent=4)
            while not done:
                selection = TerminalUtils.selectMenuItem(options=trait_names+["Cancel"], prompt="Select a Trait to EDIT. $>")
                if selection != "Cancel":
                    index = trait_names.index(selection)
                    print("")
                    TerminalUtils.pprint("{}".format(trait_names[index]))
                    print("")
                    new_trait = input("Enter the Trait to replace the one above (trait: trait effects).\n$>")
                    print("")
                    TerminalUtils.pprint("OLD: {}".format(trait_names[index]))
                    print("")
                    TerminalUtils.pprint("NEW: {}".format(new_trait))
                    print("")
                    if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Are you sure you want to overwrite?. $>"):
                        trait_names[index] = new_trait
                else:
                    done = True
    @staticmethod
    def remove_traits(traveller):
        # python ./character_manager.py remove-traits <name> <surname>
        # pick a trait, re-enter trait information
        done=False
        if len(traveller.traits) > 0:
            print("{} {}'s Traits:".format(traveller.name, traveller.surname))
            trait_names = []
            for trait in traveller.traits:
                trait_name = trait_names.split(":")[0]
                trait_names.append(trait_name)
                TerminalUtils.pprint("-   {}".format(trait), indent=4)
            while not done:
                selection = TerminalUtils.selectMenuItem(options=trait_names+["Cancel"], prompt="Select a Trait to REMOVE. $>")
                if selection != "Cancel":
                    index = trait_names.index(selection)
                    print("")
                    TerminalUtils.pprint("{}".format(trait_names[index]))
                    print("")
                    if TerminalUtils.selectMenuItem(options=["No", "Yes"], prompt="Are you sure you want to REMOVE this trait?. $>"):
                        trait_names.remove(trait_names[index])
                else:
                    done = True
    @staticmethod
    def view():
        #         0                     1    2     3     
        # python ./character_manager.py view Fname Lname
        #usage()
        name = sys.argv[2] 
        surname = sys.argv[3] 
        traveller = Traveller.load(name, surname)
        view_with_all_skills = False
        view_pred = True
        view_preg = True
        view_args = None
        if len(sys.argv) > 4:
            view_args = sys.argv[4].lower()
            if "all-skills" in sys.argv[4].lower():
                view_with_all_skills = True
            if "xpred" in sys.argv[4].lower():
                view_pred = False
            if "xpreg" in sys.argv[4].lower():
                view_preg = False
        CreateTraveller.display_traveller(traveller, view_args)
        if isinstance(traveller, Predator) and view_pred: Predator.display_pred(traveller)
        if isinstance(traveller, Incubator) and view_preg: Incubator.display_incubator(traveller)
    @staticmethod
    def display_character(character): 
        pass
        print("{} {}, {} y/o {} {}.".format( character.name, character.surname, character.age, character.sex, character.species ) )
    @staticmethod
    def display_traveller(traveller, view_args=None):
        view_with_all_skills = False
        hide_all_contacts=False
        clear_before_display = False
        if view_args is not None:
            if "all-skills" in view_args.lower():
                view_with_all_skills = True
            if "hide-all-contacts" in view_args.lower() or "hide-contacts" in view_args.lower():
                hide_all_contacts = True
            if "clear" in view_args.lower():
                clear_before_display = True
        if clear_before_display:
            os.system('cls' if os.name == 'nt' else 'clear')
        print("========================================================")
        print("{} {}, {} y/o {} {}.".format( traveller.name, traveller.surname, traveller.age, traveller.sex, traveller.species ) )
        if len(traveller.traits) > 0:
            print("Traits:")
            for trait in traveller.traits:
                TerminalUtils.pprint("-   {}".format(trait), indent=4)
        print("Characteristics: ")
        for key in traveller.characteristics.keys():
            print("  {0:<10}: {1:>2} | {2:>2} [{3:>2}] EXP: {4}/{5}".format(
                key, 
                traveller.characteristics[key], 
                traveller.current_characteristics[key],
                traveller.get_dice_modifier(traveller.current_characteristics[key]),
                traveller.characteristics_training[key][0],
                traveller.characteristics_training[key][1],
                )
            )
        # Skills, Only show trained ones.  
        print("Skills: [{} / {}]".format(traveller.get_total_skill_ranks(), traveller.get_max_skill_ranks()))
        column_size = 17
        skill_list = []# list(traveller.skills.keys())
        for key in traveller.skills.keys():
            if traveller.skills[key] >= 0 or view_with_all_skills:
                skill_list.append(key)
        if len(skill_list) > 10:
            split_listA = skill_list[:len(skill_list)//2]
            split_listB = skill_list[len(skill_list)//2:]
            for key in split_listA:
                if split_listA.index(key) < len(split_listB):
                    second_key = split_listB[split_listA.index(key)]
                else:
                    second_key = None
                text = "  {0:17}: {1:2}  EXP: {2}/{3} |  {4:17}: {5:2}  EXP: {6}/{7}".format(
                    key[:column_size], 
                    traveller.skills[key], 
                    traveller.skill_training[key][0], 
                    traveller.skill_training[key][1],

                    second_key[:column_size] if second_key else "", 
                    traveller.skills[second_key] if second_key else "", 
                    traveller.skill_training[second_key][0] if second_key else "", 
                    traveller.skill_training[second_key][1] if second_key else "",
                    )
                print(text)
        else:
            for key in skill_list:
                print( "  {0:17}: {1:2}  EXP: {2}/{3}".format(
                    key[:column_size] if len(key) > column_size else key, 
                    traveller.skills[key], 
                    traveller.skill_training[key][0], 
                    traveller.skill_training[key][1],
                    )
                )
        print("========================================================")
        print("Equipment: Cr{}".format(traveller.cash))
        for item in traveller.equipped_weapons:
            print("  "+str(item))
        for item in traveller.equipped_armor:
            print("  "+str(item))
        for item in traveller.equipped_augments:
            print("  "+str(item))
        for item in traveller.equipment:
            print("  "+str(item))
        print("========================================================")
        print("Terms")
        for term in traveller.term_history:
            # {"term:":None, "career/assignment":None, "survived":None, "commission":None, "advancement":None, "rank":None, "notes":None}
            TerminalUtils.pprint("  Term: {}. {} [{}] [{}] [{}] Rank: {}. {}".format(
                traveller.term_history.index(term)+1,#term["term"],#
                term["career/assignment"],
                "Sur" if term["survived"] else " - ",
                "Com" if term["commission"] else " - ",
                "Adv" if term["advancement"] else " - ",
                term["rank"],
                term["notes"],
                ), indent=4)
        if len(traveller.wounds) > 0:
            print("========================================================")
            print("Wounds:")
            for wound in traveller.wounds:
                print("  {}".format(str(wound)))
        if len(traveller.relations.keys()) > 0 and not hide_all_contacts:
            print("========================================================")
            print("Relations:")
            for relation in traveller.relations.keys():
                relationship_text = ""
                parts = relation.split("-")
                relation_name = parts[0]
                if len(parts) > 1:
                    relation_name += " "+ parts[1]
                for r in traveller.relations[relation]["relationship"]:
                    relationship_text += r + ", "
                if len(relationship_text) > 0: relationship_text = relationship_text[:-2]
                TerminalUtils.pprint("  {}: {} [{}]".format(relation_name, traveller.relations[relation]["relation"], relationship_text), width=100, indent=6)
                print("")
        if len(traveller.allies) > 0 and not hide_all_contacts:
            print("========================================================")
            print("Allies:")
            for ally in traveller.allies:
                TerminalUtils.pprint("  {}".format(ally.get_description()), width=100, indent=6)
                print("")
        if len(traveller.contacts) > 0 and not hide_all_contacts:
            print("========================================================")
            print("Contacts:")
            for contact in traveller.contacts:
                TerminalUtils.pprint("  {}".format(contact.get_description()), width=100, indent=6)
                print("")
        if len(traveller.rivals) > 0 and not hide_all_contacts:
            print("========================================================")
            print("Rivals:")
            for rival in traveller.rivals:
                TerminalUtils.pprint("  {}".format(rival.get_description()), width=100, indent=6)
                print("")
        if len(traveller.enemies) > 0 and not hide_all_contacts:
            print("========================================================")
            print("Enemies:")
            for enemy in traveller.enemies:
                TerminalUtils.pprint("  {}".format(enemy.get_description()), width=100, indent=6)
                print("")

        print("========================================================")
# =====================================================================
class Ship():
    def __init__(self, initDict):
        self.name = initDict.get("name","Centurian Hawk")
        self.is_standard_ship = initDict.get("is standard",True)
        self.age = initDict.get("age",0)
        self.ship_class = initDict.get("ship-class","Free Trader Type-A")
        self.tech_level = initDict.get("tech level",12)
        self.description = initDict.get("description","Using a 200-ton hull, the free trader "+
            "is an elementary interstellar merchant ship designed to ply the space lanes while "+
            "carrying a mixture of cargo and passengers. It is the archetypal tramp freighter "+
            "and common among adventuring groups and mercenary bands, often retrofitted with "+
            "turrets, weapons and other \"special\" modifications. As such, actual specifications "+
            "can vary wildly, often being proportional to the age of the ship, but the free trader "+
            "presented here is typical of a vessel fresh out of the shipyard.")
        self.crew = initDict.get("ship-crew", ["Pilot", "Astrogator", "Engineer", "Medic", "Steward"])
        self.hull = initDict.get("hull",{"tons":200,"configuration":"streamlined", "cost": 12000000})
        self.hull_points = self.get_hull_points()
        self.armor = initDict.get("armor",{"tons":5, "type":"Crystalion", "armor":2, "cost": 1200000})
        self.m_drive = initDict.get("m-drive",{"tons":2, "thrust":1 ,"power":20, "cost": 4000000})
        self.j_drive = initDict.get("j-drive",{"tons":10, "jump":1, "power":20, "cost": 15000000})
        self.power_plant = initDict.get("power-plant",{"tons":4, "type":"Fusion", "power":60, "cost": 4000000})
        self.fuel_tanks = initDict.get("fuel tanks",{"tons":21, "jump-steps":1, "tons-per-jump-step":20, "tons-per-month":1, "cost": 4000000})
        self.current_fuel = self.fuel_tanks["tons"]
        self.bridge = initDict.get("bridge",{"tons":10, "cost": 1000000, "modifications":[]})
        self.computer = initDict.get("computer",{"tons":10, "computer-level":5, "modifications":[ ], "cost": 30000})
        self.sensors = initDict.get("sensors",{"tons":10, "grade":"Civilian", "power":1, "cost": 3000000})
        self.weapons = initDict.get("weapons",[]) 
        self.hidden_weapons = []
        self.systems = initDict.get("systems",[
            {"name": "Fuel Scoop", "tons":0, "cost": 0},
            {"name": "Fuel Processors", "tons-per-day":20, "tons":1, "cost": 50000},
            {"name": "Cargo Crane", "tons":3, "cost": 3000000},
            ])
        self.staterooms = initDict.get("staterooms", [
            {"type":"Standard", "number":10, "cost":5000000},
            {"type":"Low Berths", "number":20, "cost":1000000},
            ])
        self.software = initDict.get("software",[
            {"type": "Jump Control", "value": 2, "cost": 200000},
            {"type": "Library", "cost": 0},
            {"type": "Maneuver", "value": 0, "cost": 0},
            ])
        self.common_areas = initDict.get("common-areas",{"tons":11, "cost": 1100000, "modifications":[]})
        self.cargo_space = initDict.get("cargo-space",{"tons":82, "modifications":[]})
        self.cargo_space_used = 0
        self.cargo = []
        self.craft_bay = initDict.get("craft-bay",[]) 
        self.hidden_cargo_space =  initDict.get("hidden-cargo-space",{"tons":0, "modifications":[]})
        self.hidden_cargo_space_used = 0
        self.hidden_cargo = []
        self.ships_locker = []
        self.standard_passangers = []
        self.low_berth_passangers = []
        self.damage = []
        self.reputation = 0
        self.maintentance_cost_per_month = self.maintentance_cost_per_month()
        self.purchase_price = self.get_full_cost()
    def has_system(self, system):
        for s in self.systems:
            if system.lower() in s["name"].lower():
                return True
        return False
    def get_system(self, system):
        for s in self.systems:
            if system.lower() in s["name"].lower():
                return s
        return None
    def has_software(self, software):
        for s in self.software:
            if software.lower() in s["name"].lower():
                return True
        return False
    def get_software(self, software):
        for s in self.software:
            if software.lower() in s["name"].lower():
                return s
        return None
    def get_full_cost(self):
        total = 0
        total += self.hull["cost"]
        total += self.armor["cost"]
        total += self.m_drive["cost"]
        total += self.j_drive["cost"]
        total += self.power_plant["cost"]
        total += self.bridge["cost"]
        total += self.computer["cost"]
        total += self.sensors["cost"]
        for s in self.systems:
            total += s.get("cost", 0)
        for s in self.staterooms:
            total += s.get("cost", 0)
        for s in self.software:
            total += s.get("cost", 0)
        if self.is_standard_ship:
            total = int(total * 0.9)
        return total
    def get_ship_age_discount(self):
        if 1 <= self.age and self.age <= 5: return 0.05
        elif 6 <= self.age and self.age <= 10: return 0.1
        elif 11 <= self.age and self.age <= 20: return 0.15
        elif 21 <= self.age and self.age <= 30: return 0.2
        elif 31 <= self.age and self.age <= 40: return 0.25
        elif 41 <= self.age and self.age <= 50: return 0.3
        elif 51 <= self.age and self.age <= 75: return 0.35
        elif 76 <= self.age and self.age <= 100: return 0.4
        elif 100 <= self.age: return 0.5
        else: return 0
    def get_used_cost(self): return int(self.get_full_cost() * float(1.0 - self.get_ship_age_discount()))
    def maintentance_cost_per_month(self): return round(float(self.get_full_cost()) / 12000.0)
    def get_power_plant_power(self): return self.power_plant["power"]
    def get_basic_ship_systems_power(self): return int(float(self.hull["tons"]) * 0.2)
    def get_manoeuver_drive_power(self): 
        drive_multiplier = self.m_drive["thrust"]
        if self.m_drive["thrust"] < 1:
            drive_multiplier = 0.25
        return int(float(self.hull["tons"]) * 0.1 * drive_multiplier)
    def get_jump_drive_power(self): return int(float(self.hull["tons"]) * 0.1 * self.j_drive["jump"])
    def get_ship_weapon_systems_power(self): 
        total_power = 0
        for mount in self.weapons:
            total_power += mount["power"]
            for weapon in mount["weapons"]:
                total_power += weapon["power"]
        return total_power
    def get_hull_points(self): return int(float(self.hull["tons"]) / 2.5)
    def get_bridge_tons(self):
        if self.hull_tons <= 50: return 3
        elif self.hull_tons > 50 and self.hull_tons < 100: return 6
        elif self.hull_tons >= 100 and self.hull_tons <= 200: return 10
        elif self.hull_tons > 200 and self.hull_tons <= 1000: return 20
        elif self.hull_tons > 1000 and self.hull_tons <= 2000: return 40
        else: return 60
    def get_small_bridge_tons(self):
        if self.hull_tons < 100: return 3
        elif self.hull_tons >= 100 and self.hull_tons <= 200: return 6
        elif self.hull_tons > 200 and self.hull_tons <= 1000: return 10
        elif self.hull_tons > 1000 and self.hull_tons <= 2000: return 20
        else: return 40
    def display_ship_sheet(ship):
        print("\"{}\" {}. TL {}".format(ship.name, ship.ship_class, ship.tech_level))
        print("Hull        | {} tons. {}. [{}/{}]".format( ship.hull["tons"], ship.hull["configuration"], ship.hull_points, ship.get_hull_points()))
        print("Armor       | {}. Armor: {}".format(ship.armor["type"], ship.armor["armor"]))
        print("M-Drive     | Thrust {}".format(ship.m_drive["thrust"]))
        print("J-Drive     | Jump {}".format(ship.j_drive["jump"]))
        print("Power Plant | {}. Armor: {}".format(ship.power_plant["type"], ship.power_plant["power"]))
        print("Fuel Tanks  | {} jump-{}, {} weeks of operation".format(
            ship.fuel_tanks["jump-steps"], 
            ship.j_drive["jump"], 
            4*ship.fuel_tanks["tons-per-month"]))
        print("Bridge")
        for mount in ship.weapons:
            if mount["mount"] in ["single", "double", "triple", "pop-up"]:
                descriptor = "turret"
            elif mount["mount"] in ["fixed"]:
                descriptor = "mount"
            elif mount["mount"] in ["barbette"]:
                descriptor = "barbette"
                
            weapon_text = ""
            for weap in mount["weapons"]:
                weapon_text += "{}, ".format(weap["name"])
            weapon_text = weapon_text[:-2]
            print("{} {}. {}".format(mount["mount"], descriptor, weapon_text))
        if len(ship.craft_bay) > 0:
            print("Craft Bay   | {} ton {}".format(ship.craft_bay["tons"], ship.craft_bay["craft"]))
        for s in ship.systems:
            text = ""
            if s["name"] == "Fuel Processors":
                text = "{}".format(s["name"], s["tons-per-day"])
            else:
                text = "{}".format(s["name"])
            print("System: {}".format(text))
        for stateroom in ship.staterooms:
            print("{} x{}".format(stateroom["type"], stateroom["number"]))
        for software in ship.software:
            print("{}{}".format(
                software["type"], 
                "/{}".format(software["value"]) if "value" in software.keys() else "" 
                )
            )
        common_area_text = ""
        if len(ship.common_areas["modifications"]) > 0:
            for ca in ship.common_areas["modifications"]:
                common_area_text += ca + ", "
            common_area_text = common_area_text[:-2]
        print("Common Areas: {}".format(common_area_text))
        cargo_text = ""
        if len(ship.cargo_space["modifications"]) > 0:
            for cs in ship.cargo_space["modifications"]:
                cargo_text += cs + ", "
            cargo_text = cargo_text[:-2]
        print("Cargo       | {} / {} {}".format(ship.cargo_space_used, ship.cargo_space["tons"], cargo_text))
        if ship.hidden_cargo_space["tons"] > 0:
            print("Concealed   | {} / {}".format(ship.hidden_cargo_space_used, ship.hidden_cargo_space["tons"]))
        crew_text = ""
        for crew in ship.crew:
            crew_text += crew + ", "
        crew_text = crew_text[:-2]
        print("Crew: {}".format(crew_text))
        print("Maintenance Cost: {}cr / Month".format(ship.maintentance_cost_per_month))
        print("Purchase Price: {}cr. used: {}cr".format(ship.get_full_cost(), ship.get_used_cost()))
        print("Power requirements: {}".format(ship.get_power_plant_power()))
        print("  Basic:   {}".format(ship.get_basic_ship_systems_power()))
        print("  M-drive: {}  |  J-drive: {}".format(ship.get_manoeuver_drive_power(), ship.get_jump_drive_power()))
        print("  Sensors: {}".format(ship.sensors["power"]))
        print("  Weapons: {}".format(ship.get_ship_weapon_systems_power()))
        print("Passangers:")
        for passanger in ship.standard_passangers:
            print("  STD | {} {}: {} y/o {} {}".format(passanger.name, passanger.surname, passanger.age, passanger.sex, passanger.species))
        for passanger in ship.low_berth_passangers:
            print("  LB  | {} {}: {} y/o {} {}".format(passanger.name, passanger.surname, passanger.age, passanger.sex, passanger.species))
        if ship.description != "":
            print("")
            print(ship.description)
    def add_passager_to_low_berth(self, passanger):
        for stateroom in self.staterooms:
            if stateroom["type"] in ["Low Berths"]:
                if self.low_berth_passangers is not None and len(self.low_berth_passangers) < stateroom["number"]:
                    self.low_berth_passangers.append(passanger)
                    return True
        return False
    def add_passager_to_stateroom(self, passanger):
        for stateroom in self.staterooms:
            if stateroom["type"] in ["Standard"]:
                if self.standard_passangers is not None and len(self.standard_passangers) < stateroom["number"]:
                    self.standard_passangers.append(passanger)
                    return True
        return False
    def remove_passanger_from_low_berth(self, passanger):
        for stateroom in self.staterooms:
            if stateroom["type"] in ["Low Berths"]:
                if self.low_berth_passangers is not None and passanger in self.low_berth_passangers:
                    self.low_berth_passangers.remove(passanger)
                    return True
        return False
    def remove_passanger_from_stateroom(self, passanger):
        for stateroom in self.staterooms:
            if stateroom["type"] in ["Standard"]:
                if self.standard_passangers is not None and passanger in self.standard_passangers:
                    self.standard_passangers.remove(passanger)
                    return True
        return False
    def get_passanger_by_names(self, name, surname):
        for passanger in self.standard_passangers: 
            if passanger.name == name and passanger.surname == surname:
                return passanger
        for passanger in self.low_berth_passangers: 
            if passanger.name == name and passanger.surname == surname:
                return passanger
        return None
    def save(self):
        file = open("{}-{}.pickle".format(self.name, self.ship_class.replace(" ","-")), 'wb')
        pickle.dump(self, file)
        file.close()
    @staticmethod
    def load(ship_name):
        ship=None
        filename = "{}.pickle".format(ship_name)
        if os.path.exists(filename):
            file = open(filename, 'rb')
            ship = pickle.load(file)
            file.close()
        return ship
class FreeTraderTypeA(Ship):
    def __init__(self):
        super().__init__({
            "is standard":True,
            "description":"Using a 200-ton hull, the free trader " +
                        "is an elementary interstellar merchant ship designed to ply the space lanes while " +
                        "carrying a mixture of cargo and passengers. It is the archetypal tramp freighter " +
                        "and common among adventuring groups and mercenary bands, often retrofitted with " +
                        "turrets, weapons and other ‘special’ modifications. As such, actual specifications " +
                        "can vary wildly, often being proportional to the age of the ship, but the free trader " +
                        "presented here is typical of a vessel fresh out of the shipyard.",
            "ship-class":"Free Trader Type-A", "tech level":12,"ship-crew": ["Pilot", "Astrogator", "Engineer", "Medic", "Steward"],
            "hull":{"tons":200,"configuration":"streamlined", "cost": 12000000, "modifications":[]},
            "armor":{"tons":5, "type":"Crystalion", "armor":2, "cost": 1200000},
            "m-drive":{"tons":2, "thrust":1 ,"power":20, "cost": 4000000},
            "j-drive":{"tons":10, "jump":1, "power":40, "cost": 15000000},
            "power-plant":{"tons":4, "type":"Fusion", "power":60, "cost": 4000000},
            "fuel tanks":{"tons":21, "jump-steps":1, "tons-per-jump-step":20, "tons-per-month":1, "cost": 0},
            "bridge":{"tons":10, "cost": 1000000, "modifications":[]},
            "computer":{"tons":0, "computer-level":5, "modifications":[ ], "cost": 30000},
            "sensors":{"tons":10, "grade":"Civilian", "power":1, "cost": 3000000},
            "systems":[
                {"name": "Fuel Scoop", "tons":0, "cost": 0},
                {"name": "Fuel Processors", "tons-per-day":20, "power":2, "tons":1, "cost": 50000},
                {"name": "Cargo Crane", "tons":3, "cost": 3000000},
                ],
            "staterooms": [
                {"type":"Standard", "number":10, "cost":5000000},
                {"type":"Low Berths", "number":20, "cost":1000000},
                ],
            "software":[
                {"type": "Jump Control", "value": 2, "cost": 200000},
                {"type": "Library", "cost": 0},
                {"type": "Maneuver", "value": 0, "cost": 0},
                ],
            "common-areas":{"tons":11, "cost": 1100000, "modifications":[]},
            "cargo-space":{"tons":82, "modifications":[]}
            })
class FarTraderTypeA2(Ship):
    def __init__(self):
        super().__init__({
            "is standard":True,
            "description":"While nominally a modified free trader, the "+
                "far trader has a series of modifications that "+
                "have become accepted as standard, and "+
                "many free traders are either modified to "+
                "this specification or are built this way from "+
                "new. The far trader swaps cargo space and "+
                "low berths for a larger jump drive and fuel "+
                "tank, allowing it to reach systems a basic "+
                "free trader cannot travel to. While less "+
                "cargo can mean less profits, the ability to "+
                "reach further systems or to travel between "+
                "stars at a faster rate can more than make "+
                "up for this in the hands of a clever captain.",
            "ship-class":"Far Trader Type-A2", "tech level":12,"ship-crew": ["Pilot", "Astrogator", "Engineer", "Medic", "Steward"],
            "hull":{"tons":200,"configuration":"streamlined", "cost": 12000000, "modifications":[]},
            "armor":{"tons":5, "type":"Crystalion", "armor":2, "cost": 1200000},
            "m-drive":{"tons":2, "thrust":1 ,"power":40, "cost": 4000000},
            "j-drive":{"tons":15, "jump":2, "power":40, "cost": 22500000},
            "power-plant":{"tons":4, "type":"Fusion", "power":75, "cost": 5000000},
            "fuel tanks":{"tons":41, "jump-steps":1, "tons-per-jump-step":20, "tons-per-month":1, "cost": 0},
            "bridge":{"tons":10, "cost": 1000000, "modifications":[]},
            "computer":{"tons":0, "computer-level":5, "modifications":["/bis"], "cost": 30000},
            "sensors":{"tons":10, "grade":"Civilian", "power":1, "cost": 3000000},
            "systems":[
                {"name": "Fuel Scoop", "tons":0, "cost": 0},
                {"name": "Fuel Processors", "tons-per-day":20, "power":2, "tons":1, "cost": 50000},
                {"name": "Cargo Crane", "tons":3, "cost": 3000000},
                ],
            "staterooms": [
                {"type":"Standard", "number":10, "cost":5000000},
                {"type":"Low Berths", "number":6, "cost":1000000},
                ],
            "software":[
                {"type": "Jump Control", "value": 1, "cost": 100000},
                {"type": "Library", "cost": 0},
                {"type": "Maneuver", "value": 0, "cost": 0},
                ],
            "common-areas":{"tons":11, "cost": 900000, "modifications":[]},
            "cargo-space":{"tons":64, "modifications":[]}
            })
class ScoutCourierTypeS(Ship):
    def __init__(self):
        super().__init__({
            "is standard":True,
            "description":"The scout ship is built for exploration, " +
                "survey, and courier duties, with many " +
                "thousands in service throughout Charted " +
                "Space. Despite the small 100 ton hull, the " +
                "scout is faster than most merchant ships " +
                "and can jump further too. While multiple " +
                "crew positions are technically required, it is " +
                "standard practice for a scout to be crewed " +
                "by just one or two highly skilled individuals " +
                "who understand the requirements needed " +
                "for self-sufficiency.",
            "ship-class":"Scout/Courier Type-S", 
            "tech level":12,
            "ship-crew": ["Pilot", "Astrogator", "Engineer"],
            "hull":{"tons":200,"configuration":"streamlined", "cost": 6000000, "modifications":[]},
            "armor":{"tons":5, "type":"Crystalion", "armor":4, "cost": 1200000},
            "m-drive":{"tons":4, "thrust":2 ,"power":20, "cost": 4000000},
            "j-drive":{"tons":15, "jump":2, "power":20, "cost": 15000000},
            "power-plant":{"tons":4, "type":"Fusion", "power":75, "cost": 5000000},
            "fuel tanks":{"tons":23, "jump-steps":1, "tons-per-jump-step":20, "tons-per-month":1, "cost": 0},
            "bridge":{"tons":10, "cost": 500000, "modifications":[]},
            "computer":{"tons":0, "computer-level":5, "modifications":["/bis"], "cost": 30000},
            "weapons": [
                {"mount": "double", "tech level":8, "tons": 1, "power": 1, "cost":500000, "weapons": [
                    {"name": "Beam Laser", "tech level":10, "range":"medium", "power": 4, "damage": "1D", "cost":500000, "traits":[]},
                    {"name": "Beam Laser", "tech level":10, "range":"medium", "power": 4, "damage": "1D", "cost":500000, "traits":[]},
                    # {"name": "Sandcaster", "tech level":9, "range":"special", "power": 0, "damage": "special", "cost":250000, "traits":[]},
                    ]},
                ],
            "sensors":{"tons":10, "grade":"Military", "power":2, "cost": 4100000},
            "craft-bay": {"tons":4, "craft":"Air/Raft", "cost": 1500000},
            "systems":[
                {"name": "Fuel Scoop", "tons":0, "cost": 0},
                {"name": "Fuel Processors", "tons-per-day":40, "power":2, "tons":1, "cost": 50000},
                {"name": "Probe Drones x10", "tons":2, "cost": 1000000},
                {"name": "Workshop", "tons":6, "cost": 900000},
                ],
            "staterooms": [
                {"type":"Standard", "number":4, "cost":2000000},
                # {"type":"Low Berths", "number":6, "cost":1000000},
                ],
            "software":[
                {"type": "Jump Control", "value": 2, "cost": 200000},
                {"type": "Library", "cost": 0},
                {"type": "Maneuver", "value": 0, "cost": 0},
                ],
            # "common-areas":{"tons":11, "cost": 900000, "modifications":[]},
            "cargo-space":{"tons":12, "modifications":[]}
            })
class FarTraderEmpressMaravaClass(Ship):
    def __init__(self):
        super().__init__({
            "is standard":True,
            "ship-class":"Far Trader Empress Marava-Class", "tech level":12,
            "description":"The far trader can be encountered anywhere " +
                            "in the Imperium. It ranges far and wide, and "+
                            "deals with every world it finds. Even amber "+
                            "zones and red zones are not considered off "+
                            "limits by its captains, provided there is profit "+
                            "to be made and the risk of being caught is slight.",
            "ship-crew": ["Pilot/Astrogator", "Engineer", "Medic", "Steward", "Gunner", "Gunner"],
            "hull":{"tons":200,"configuration":"streamlined", "cost": 12000000, "modifications":[]},
            "armor":{"tons":5, "type":"Crystalion", "armor":0, "cost": 1200000},
            "m-drive":{"tons":2, "thrust":1 ,"power":20, "cost": 4000000},
            "j-drive":{"tons":15, "jump":2, "power":40, "cost": 15000000},
            "power-plant":{"tons":6, "type":"Fusion", "power":90, "cost": 6000000},
            "fuel tanks":{"tons":41, "jump-steps":2, "tons-per-jump-step":20, "tons-per-month":1, "cost": 0},
            "bridge":{"tons":10, "cost": 1000000, "modifications":[]},
            "computer":{"tons":0, "computer-level":5, "modifications":["/bis"], "cost": 30000},
            "sensors":{"tons":10, "grade":"Civilian", "power":1, "cost": 3000000, "modifications":[]},
            "weapons": [
                {"mount": "double", "tech level":8, "tons": 1, "power": 1, "cost":500000, "weapons": [
                    {"name": "Beam Laser", "tech level":10, "range":"medium", "power": 4, "damage": "1D", "cost":500000, "traits":[]},
                    {"name": "Beam Laser", "tech level":10, "range":"medium", "power": 4, "damage": "1D", "cost":500000, "traits":[]},
                    ]},
                {"mount": "double", "tech level":8, "tons": 1, "power": 1, "cost":500000, "weapons": [
                    {"name": "Beam Laser", "tech level":10, "range":"medium", "power": 4, "damage": "1D", "cost":500000, "traits":[]},
                    {"name": "Beam Laser", "tech level":10, "range":"medium", "power": 4, "damage": "1D", "cost":500000, "traits":[]},
                    ]},
                ],
            "craft-bay": {"tons":5, "craft":"Air/Raft", "cost": 1500000, "modifications":[]},
            "systems":[
                {"name": "Fuel Scoop", "tons":0, "cost": 0},
                {"name": "Fuel Processors", "tons-per-day":40, "tons":1, "power":2, "cost": 50000},
                {"name": "Loading Belt", "tons":1, "cost": 3000},
                {"name": "Cargo Airlock", "tons":3, "cost": 300000},
                {"name": "Cargo Airlock", "tons":3, "cost": 300000},
                ],
            "staterooms": [
                {"type":"Standard", "number":10, "cost":5000000},
                {"type":"Low Berths", "number":4, "cost":1000000},
                ],
            "software":[
                {"type": "Jump Control", "value": 2, "cost": 200000},
                {"type": "Library", "cost": 0},
                {"type": "Maneuver", "value": 0, "cost": 0},
                ],
            "common-areas":{"tons":10, "cost": 1000000, "modifications":[]},
            "cargo-space":{"tons":57, "modifications":[]}
            })
class FarTraderA3LCalypsoClass(Ship):
    def __init__(self):
        super().__init__({
            "is standard":True,
            "ship-class":"Far Trader A3L Calypso-Class", "tech level":12,
            "description":"The far trader can be encountered anywhere " +
                            "in the Imperium. It ranges far and wide, and "+
                            "deals with every world it finds. Even amber "+
                            "zones and red zones are not considered off "+
                            "limits by its captains, provided there is profit "+
                            "to be made and the risk of being caught is slight.",
            "ship-crew": ["Pilot/Astrogator", "Engineer", "Medic", "Steward", "Gunner", "Gunner"],
            "hull":{"tons":200,"configuration":"streamlined", "modifications":[], "cost": 12000000},
            "armor":{"tons":5, "type":"Crystalion", "armor":0, "cost": 1200000},
            "m-drive":{"tons":2, "thrust":1 ,"power":20, "cost": 4000000},
            "j-drive":{"tons":15, "jump":2, "power":40, "cost": 15000000},
            "power-plant":{"tons":6, "type":"Fusion", "power":90, "cost": 6000000},
            "fuel tanks":{"tons":41, "jump-steps":2, "tons-per-jump-step":20, "tons-per-month":1, "cost": 0},
            "bridge":{"tons":10, "cost": 1000000, "modifications":[]},
            "computer":{"tons":0, "computer-level":5, "modifications":["/bis"], "cost": 30000},
            "sensors":{"tons":10, "grade":"Civilian", "power":1, "cost": 3000000},
            "weapons": [
                {"mount": "double", "tech level":8, "tons": 1, "power": 1, "cost":500000, "weapons": [
                    {"name": "Beam Laser", "tech level":10, "range":"medium", "power": 4, "damage": "1D", "cost":500000, "traits":[]},
                    {"name": "Beam Laser", "tech level":10, "range":"medium", "power": 4, "damage": "1D", "cost":500000, "traits":[]},
                    ]},
                {"mount": "double", "tech level":8, "tons": 1, "power": 1, "cost":500000, "weapons": [
                    {"name": "Missile Rack", "tech level":7, "range":"special", "power": 0, "damage": "4D", "cost":750000, "traits":["Smart"]},
                    {"name": "Sandcaster", "tech level":9, "range":"special", "power": 0, "damage": "special", "cost":250000, "traits":[]},
                    ]},
                ],
            "craft-bay": {"tons":5, "craft":"Air/Raft", "cost": 1500000},
            "systems":[
                {"name": "Fuel Scoop", "tons":0, "cost": 0},
                {"name": "Fuel Processors", "tons-per-day":40, "tons":1, "power":2, "cost": 50000},
                {"name": "Loading Belt", "tons":1, "cost": 3000},
                {"name": "Cargo Airlock", "tons":3, "cost": 300000},
                {"name": "Cargo Airlock", "tons":3, "cost": 300000},
                ],
            "staterooms": [
                {"type":"Standard", "number":9,   "cost":5000000},
                {"type":"Low Berths", "number":4, "cost":1000000},
                ],
            "software":[
                {"type": "Jump Control", "value": 2, "cost": 200000},
                {"type": "Library", "cost": 0},
                {"type": "Maneuver", "value": 0, "cost": 0},
                ],
            "common-areas":{"tons":10, "cost": 1000000, "modifications":["Medical Bay"] },
            "cargo-space":{"tons":57}
            })
# =====================================================================
class Job():
    job_types = [
        "Delivery", # Select Cargo, amount of cargo, view locations that are needing it, and plot a destination to go sell it (Free trading)
        "Frieght", # Select a shipment within your cargo capacity, plot course and deliver it to the star port (local shipping handles the rest).
        "Escort", # Passanger(s) have paid for you to take them to a destination system. Landing fees are added to payment as well as refuel
        "Explore", # generally means on an uninhabited planet. maybe a new system! go to the planet, do a survey. maybe explore some locations. scan for metals or biologicals.
        "Investigate", # Go to a place on a known planet and look around a bit. Might be rebels, an illegal operation (mining, drug, medical, slave colony).
        "Rescue", # go to a hostile place and rescue a person or group from a bad situation.
        "Kidnap", # meet someone, gain their trust, then take them to your patron
        ]
    ["Explore","Courier","Investigate", "Penetrate", "Protect",
            "Liberate", "Rescue", "Seize", "Kidnap", "Destroy","Military"]
    @staticmethod
    def generate( name, 
        job_type, legality, payout, 
        patron, 
        origin, destination, origin_hex, destination_hex, 
        support, opposition, 
        description, ):
        initDict = {}
        initDict["name"] = name
        initDict["description"] = description
        initDict["patron"] = job_type
        initDict["job type"] = legality
        initDict["payout"] = payout
        initDict["legality"] = legality
        initDict["support"] = support
        initDict["opposition"] = opposition
        initDict["origin"] = origin
        initDict["destination"] = destination
        initDict["origin hex"] = origin_hex
        initDict["destination hex"] = destination_hex
    def __init__(self, initDict):
        self.name = initDict.get("name", "<JOB>")
        self.description = initDict.get("description", "<DESCRIPTION>")
        self.patron = initDict.get("patron", None)
        self.job_type = initDict.get("job_type", "Delivery")
        self.payout_bonus_percent = initDict.get("payout", 1.0)
        self.payout = initDict.get("payout", 3500)
        self.legality = initDict.get("legality", "Legal")
        self.support = initDict.get("support", None)
        self.opposition = initDict.get("opposition", None)
        self.origin = initDict.get("origin", None)
        self.destination = initDict.get("destination", None)
        self.origin_hex = initDict.get("origin", None)
        self.destination_hex = initDict.get("destination", None)
        self.difficulty = initDict.get("difficulty") # Difficult
class HunterJob(Job):
    secondQuirkChance = 0.9
    facialHairChange = 0.2
    chanceextracbtskill = 0.5
    chanceextrabusskill = 0.4
    def __init__(self, initDict):
        self.wantedFor = initDict["wantedFor"]
        self.targetDescription = initDict["missionTarget"]
        self.bounty = initDict["bounty"]
        self.difficulty = initDict["difficulty"] # Difficult
        self.relativeReward = initDict["relativeReward"] # 0%
        self.rewardCredits = initDict["rewardCredits"] # (875)
    @staticmethod
    def generate(systemStance, patron=None):
        initDict = Job.generate(systemStance, patron)
        wantedFor = [
            "Assault and Battery", "Assault, Larceny", "Corruption", "Espionage", 
            "Grand Larceny", "Kidnapping", "Murder", "Piracy", "Racketeering", 
            "Smuggling", "Terrorism", "Trafficking", "Treason, Sedition"

            ]
        targetDescription = ["Brawler", "Thug", "Security Specialist", "Data Slicer", "Charlatan", 
            "Bounty Hunter", "Assassin", "Blockade Runner", "Crime Lord", "Space Transport Pilot", "Notorious Outlaw", "Fixer", 
            "Traveller (Pilot)", "Traveller (Steward)", "Traveller (Gunslinger)", "Traveller (Dealer)", "Traveller (Captain)", 
            "Political Figure", "Military Figure"]
        initDict["wantedFor"] = random.choice(wantedFor)
        initDict["missionTarget"] = random.choice(targetDescription)
        bounty = Bounty(Bounty.generate("<Bounty Name>", initDict["missionTarget"], initDict["wantedFor"]))
        initDict["bounty"] = bounty
        reward = 1000
        if (initDict["difficulty"] == "Milk Run"):
            reward = 100
        elif (initDict["difficulty"] == "Easy"):
            reward = 1000
        elif (initDict["difficulty"] == "Average"):
            reward = 10000
        elif (initDict["difficulty"] == "Difficult" and 
            ("Traveller" in initDict["missionTarget"] or "Figure" in initDict["missionTarget"]) 
            ):
            reward = 100000
        elif (initDict["difficulty"] == "Formidable" and 
            ("Traveller" in initDict["missionTarget"] or "Figure" in initDict["missionTarget"]) 
            ):
            reward = 1000000
        elif (initDict["difficulty"] == "Impossible" and 
            ("Traveller" in initDict["missionTarget"] or "Figure" in initDict["missionTarget"]) 
            ):
            reward = 10000000
        
        initDict["relativeReward"] = random.randint(0,1000)/10
        initDict["rewardCredits"] = int((initDict["relativeReward"]/100) * reward) # 0% (875)

        return initDict
class SWHuntingJob(object):
    @staticmethod
    def generate():
        initDict = {}
        wantedFor = [
            "Assault and Battery", "Assault and Battery", "Assault, Larceny", "Assault, Larceny", "Assault, Larceny", 
            "Corruption", "Espionage", "Espionage", "Grand Larceny", "Grand Larceny", 
            "Kidnapping", "Murder", "Murder", "Piracy", "Racketeering", 
            "Smuggling", "Terrorism", "Trafficking", "Trafficking", "Treason, Sedition", 
            ]
        targetDescription = [
            "Brawler", "Brawler", "Thug", "Thug", "Thug", 
            "Security Specialist", "Data Slicer", "Data Slicer", "Charlatan", "Charlatan", 
            "Bounty Hunter", "Assassin", "Assassin", "Blockade Runner", "Crime Lord", 
            "Space Transport Pilot", "Notorious Outlaw", "Fixer", "Fixer", "Famous Person Of Interest", 
            ]
        reward = [
            5000, 5000, 1000, 1000, 1000, 
            5000, 7000, 7000, 8000, 8000,
            7000, 5000, 8000, 8000, 8000,
            7000, 8000, 7000, 7000, "Special",
            ]
        initDict["wantedFor"] = random.choice(wantedFor) # 
        initDict["targetDescription"] = random.choice(targetDescription) #
        initDict["rewardCredits"] = random.choice(reward)

        return initDict
    def __init__(self, initDict):
        self.initDict = initDict
        self.wantedFor = initDict["wantedFor"] 
        self.targetDescription = initDict["targetDescription"] 
        self.rewardCredits = initDict["rewardCredits"] 
class HunterFlavor(object):
    @staticmethod
    def generate():
        initDict = {}
        demeanour = [
            "All business, no nonsense.", "Extreme aggression, easily provoked.", "Boring and plain.", 
            "Cheerful, bordering on saccharine.", "Melancholic and fatalist.", "Showy and narcissistic.", 
            ]
        weaponPreference = [
            "Explosives and heavy weapons", "Long range weapons, sniping",
            "Automated drones", "Stealth and melee weapons", "Hired help",
            "Heavy armour and close range weapons", "Combat vehicles", "All-rounder weapons and gear" 
            ]
        specialistGear = [
            "A jetpack, reliable but easily damaged.",
            "Ancient weaponry that ignores armour.",
            'A heavily upgraded, combat-specialized starship.',
            "Power armour and energy shields.",
            "Combat drugs.",
            "High tech tracking and scanning devices.",
            "A cloaking field.",
            "A bioengineered combat/tracking pet.",
            "Nanotech weapons, easily concealed.",
            "Multiple cybernetic augmentations."
            ]
        description = [
            "Nondescript, easily blending into crowds.",
            "Military surplus everything, trying a little too hard.",
            "Elegant and elaborate clothes and gear, like a fashionista.",
            "Practical equipment, worn by years of use.",
            "Punk fashion with tons of accessories.",
            "One colour all over, lots of fabric and plastic.",
            "Robes and masks, mystical in nature.",
            "Revealing clothes, covered in tattoos and cosmetic implants.",
            "Stylish clothes, suits and ties, dark and sleek.",
            "Brand new everything, most of it never used before."
            ]
        species = [
            "Human, +2 to their lowest stat,",
            "Vatborn, +2 STR,",
            "Mentat, +2 CHA,",
            "Spacer, +2 DEX,",
            "Lizard, +1 DEX and immune to heat,",
            "Feline, always acts before enemies/traps,",
            "Hound, preternatural sense of smell,",
            "Mantis, D8 unarmed damage,",
            "Rabbit, outrun anyone, even some vehicles,",
            "Yeti, +1 STR and immune to cold,",
            "Assassin Robot, closely resembles an organic,",
            "Combat Robot, +1 Armour at all times,"
            ]
        gimmick = [
            "They warn all their targets in advance.",
            "There's two of them: twins, friends, lovers, clones, etc.",
            "They're actually several people working in turns. Kill one and another comes back.",
            "They take great care to avoid any collateral damage.",
            "They try to make each kill slow and painful.",
            "They have branded corporate gear and try to show it off.",
            "They're exceptionally young or old, but no less effective for it.",
            "They offer to fake the party's deaths in return for a bribe.",
            "They carry incendiary grenades and are a pyromaniac.",
            "They have limited psychic ability. One power, always the CHA drawback.",
            "They are followed by a documentary crew.",
            "Their will places a large bounty on whoever kills them, larger than any existing ones.",
            "They are being hunted by another bounty hunter themselves.",
            "They dual wield their weapons. It looks cool but provides no benefit.",
            "They use only sidearms, daggers, and other \"light\" weapons and gear.",
            "They revel in causing unnecessary collateral damage.",
            "They are exceptionally skilled: +2 HP and +1 damage.",
            "They are particularly inept: -2 HP and -1 damage.",
            "They throw sonic devices which emit loud, piercing screeches they are immune to.",
            "They talk to their quarry constantly throughout the fight." 
            ]
        
        initDict["demeanour"] = random.choice(demeanour) # 
        initDict["weaponPreference"] = random.choice(weaponPreference) #
        initDict["specialistGear"] = random.choice(specialistGear)
        initDict["description"] = random.choice(description) # 
        initDict["species"] = random.choice(species) #
        initDict["gimmick"] = random.choice(gimmick)

        return initDict
    def __init__(self, initDict):
        self.initDict = initDict
        self.demeanour = initDict["demeanour"] 
        self.weaponPreference = initDict["weaponPreference"] 
        self.specialistGear = initDict["specialistGear"] 
        self.description = initDict["description"] 
        self.species = initDict["species"] 
        self.gimmick = initDict["gimmick"] 
    def getBlurb(self):
        text="This bounty hunter's demeanour is {} ".format(self.demeanour.lower())
        text+="They primarily attack using {}, with the assistance of their {} ".format(
            self.weaponPreference.lower(), self.specialistGear.lower())
        text+="They are a {} dressed in {} ".format(self.species.lower(), self.description.lower())
        text+="Their gimmick is that their {}".format(self.gimmick.lower())
        return text
class HunterSpaceShipFlavor(object):
    @staticmethod
    def generate():
        initDict = {}
        
        shipSize = [
            "Smaller than normal. (-2 HUL, fast)",
            "Of average size.",
            "Larger than normal. (+4 HP, +2 HUL, slow)",
            "Much larger than normal. (+8 HP, +4 HUL, very slow)"
            ]
        shipType = [
            "Military: For combat or troop/starfighter transport. (+1 Armour/+1 damage)",
            "Research: For exploration, survey, and analysis. (laboratory, medbay)",
            "Industrial: For mining, construction, salvaging, etc. (various tools)",
            "Merchant: For transporting goods and resources. (huge cargo bay)",
            "Liner: For transporting many individuals at once. (many cryopods)",
            "Personal: For transporting a few individuals in luxury. (many staterooms)"
            ]
        shipStrengths = [
            "Reinforced hull. +3 HUL.",
            "Large engines. +3 ENG.",
            "Overclocked systems. +3 SYS.",
            "Armour plating. +1 Armour.",
            "Targeting computers. +1 damage.",
            "Strong shields. +4 HP.",
            "Exceptional maneuverability.",
            "Long range, high accuracy sensors.",
            "Difficult to detect and scan.",
            "Has the benefits of another ship type."
            ]
        shipWeaknesses = [
            "Cracked hull. -3 HULL.",
            "Small engines. -3 ENG.",
            "Buggy systems. -3 SYS.",
            "Obvious weak points. HUL damage always causes critical damage.",
            "Undersized weapons. -1 damage.",
            "Weak shields. -4 HP.",
            "Slow turns and acceleration/deceleration.",
            "Inaccurate, obvious sensors.",
            "Adware constantly broadcasts its position.",
            "Lacks the benefits of its ship type."
            ]
        shipAppearance = [
            "Blocky and grey, totally devoid of intentional aesthetic.",
            "Sleek and elegant, pure white with black glass.",
            "Black and angular, as if a stealth ship.",
            "Green and organic-looking – possibly a living ship.",
            "Red and curved, like a retrofuturist rocket ship.",
            "A mechanical cube, sphere, pyramid, or other polyhedron.",
            "Spindly and elegant, golden and shimmering with large glass planes.",
            "A Frankenstein of several other ships welded together.",
            "Dark blue, long and with rounded edges and bright yellow windows.",
            "Ostentatious and religious, like a cathedral turned into a ship.",
            "Bright white plastic with blue and orange extremeties.",
            "A series of bright green spheres connected by pipes.",
            "Insectoid in appearance, with bright, clashing colours.",
            "Cartoonish, covered in stars, constantly shifting between several vibrant colours.",
            "Narrow and angular, like an upsized starfighter.",
            "Round, smooth edges, dull yellow, orange, or brown.",
            "Imposing, blocky, and long, red as blood.",
            "White, sleek exterior half-conceals a pitch black, biomechanical interior.",
            "An asteroid, space station, or even space lifeform's corpse turned into a ship.",
            "Deep purple, with shiny metallic trimming."
            ]
        initDict["shipSize"] = random.choice(shipSize) # 
        initDict["shipType"] = random.choice(shipType) #
        strength = random.choice(shipStrengths)
        initDict["shipStrengths"] = strength
        shipWeaknesses.remove(shipWeaknesses[shipStrengths.index(strength)])
        initDict["shipWeaknesses"] = random.choice(shipWeaknesses) # 
        initDict["shipAppearance"] = random.choice(shipAppearance) #
        # initDict["gimmick"] = random.choice(gimmick)

        return initDict
    def __init__(self, initDict):
        self.initDict = initDict
        self.shipSize = initDict["shipSize"] 
        self.shipType = initDict["shipType"] 
        self.shipStrengths = initDict["shipStrengths"] 
        self.shipWeaknesses = initDict["shipWeaknesses"] 
        self.appearance = initDict["shipAppearance"] 
        # self.gimmick = initDict["gimmick"] 
    def getBlurb(self):
        '''This ship is as large as normal and is a Personal (comes with many staterooms) design, owned by robots, independent or to better serve their owners. 
        It looks like a series of bright green spheres connected by pipes. 
        Its main strength is the fact that it has the benefits of another ship type (roll a D6), while its main weakness is its obvious weak points (HUL damage always causes critical damage). 
        It is a pirate ship, beginning to pursue the party. +1 damage if not a Military ship
        '''
        text="This ship is {} and is a {} ".format(self.shipSize.lower(), self.shipType.lower())
        text+="It looks like {} ".format( self.appearance.lower())
        text+=" Its main strength is the fact that {}, while its main weakness is its {} ".format(self.shipStrengths.lower(), self.shipWeaknesses.lower())
        # Ship Actions in space: text+="Their gimmick is that their {}".format(self.gimmick.lower())
        return text
# =====================================================================
class ZozerSoloTravellerSave():
    location_states = ["In Media Res", "On Planet", "In Space", "Jump Space", "Exploring"]
    days_of_week = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
    def is_time_for_ship_maintenance(self): return self.total_weeks_in_game % 4 == 3
    def __init__(self, name, surname, traveller_names, ship_name, sector_name, hex_coord):
        self.name = name
        self.surname = surname
        self.main_character = None
        self.traveller_names = traveller_names
        self.ship_name = ship_name
        self.sector_name = sector_name
        self.hex_coord = hex_coord
        self.previous_hex_coord = None
        self.jump_target_hex_coord = None
        self.in_system_location_name = None

        self.previous_location_state = None
        self.location_state = "In Media Res"

        self.in_system_location = None
        
        self.total_weeks_in_game = 0
        self.hours = 8
        self.days = 1
        self.weeks = 1
        self.months = 1
        self.years = 1
        self.jobs = []
        self.log_entries = []
        self.weeks_stay=0

        # vvv This is reset each load in case edits happen outside save file.
        self.travellers = []
        self.ship = None
        self.sector = None
        for t in self.traveller_names:
            print(t)
            fname = t.split("-")[0]
            lname = t.split("-")[1]
            traveller=None
            filename = "{}-{}.pickle".format(name, surname)
            if os.path.exists(filename):
                file = open(filename, 'rb')
                traveller = Traveller.load(name, surname)
                file.close()
            if traveller:
                self.travellers.append(traveller)
            else:
                print("!No Traveller Loaded from {}!".format(filename))
        print(self.ship_name)
        filename = self.ship_name+".pickle"
        if os.path.exists(filename):
            file = open(filename, 'rb')
            self.ship = Ship.load(self.ship_name)
            file.close()
        else: print("!No Ship Loaded! from {}!".format(filename))
        filename = self.sector_name+"-Sector.pickle"
        if os.path.exists(filename):
            file = open(filename, 'rb')
            self.sector = Sector.load(self.sector_name)
            file.close()
        else: print("!No Sector Loaded! from {}!".format(filename))
    def save(self):
        for t in self.travellers:
            self.ship.remove_passanger_from_stateroom(t)
            t.save()
        self.ship
        self.ship.save()
        self.sector.save()
        self.travellers = []
        self.main_character = None
        self.ship = None
        self.sector = None
        file = open("{}-{}-{}.pickle".format("zozer", self.name, self.surname), 'wb')
        pickle.dump(self, file)
        file.close()
    @staticmethod
    def load(fname, lname, verbose=False):
        save_file=None
        filename = "{}-{}-{}.pickle".format("zozer", fname, lname)
        if verbose: print(filename)
        if os.path.exists(filename):
            file = open(filename, 'rb')
            save_file = pickle.load(file)
            file.close()
            save_file.travellers = []
            for t in save_file.traveller_names:
                f = t.split("-")[0]
                l = t.split("-")[1]
                traveller=None
                filename = "{}-{}.pickle".format(f, l)
                if verbose: print(filename)
                if os.path.exists(filename):
                    file = open(filename, 'rb')
                    traveller = Traveller.load(f, l)
                    if verbose: print("Traveller" + str(traveller))
                    if (traveller.name.lower() == fname.lower() and traveller.surname.lower() == lname.lower()):
                        save_file.main_character = traveller
                        if verbose: print("Setting Main character: {} {}".format(save_file.main_character.name, save_file.main_character.surname))
                    file.close()
                if traveller:
                    save_file.travellers.append(traveller)
            filename = save_file.ship_name+".pickle"
            if verbose: print(filename)
            if os.path.exists(filename):
                file = open(filename, 'rb')
                save_file.ship = Ship.load(save_file.ship_name)
                file.close()
                if save_file.ship is not None:
                    for traveller in save_file.travellers:
                        if traveller not in save_file.ship.standard_passangers:
                            save_file.ship.standard_passangers = [traveller] + save_file.ship.standard_passangers
            filename = save_file.sector_name+"-Sector.pickle"
            if verbose: print(filename)
            if os.path.exists(filename):
                file = open(filename, 'rb')
                save_file.sector = Sector.load(save_file.sector_name)
                file.close()
        return save_file
    def get_traveller_summary_cards(self):
        cards = []
        for traveller in self.travellers:
            card_text = "| {} {}  {} Age {}, {} term   {}cr on hand |".format(
                traveller.name, traveller.surname, traveller.get_upp_plus_6(), 
                traveller.age, len(traveller.term_history), traveller.cash,
                traveller.get_skills_as_string(),
                )
            cards.append(card_text)
        return cards
    def get_last_logs(self):
        self.log_entries.reverse() 
        if len(self.log_entries) > 4: logs = self.log_entries[:4]
        else: logs = list(self.log_entries)
        self.log_entries.reverse()
        return logs
    def add_time(self, hours=0, days=0, weeks=0):
        self.hours += hours
        if self.hours >= 24: 
            self.hours -= 24
            self.days += 1
        if days > 0 or weeks > 0: self.hours = 7
        self.days += days
        if self.days >= 7: 
            self.days -= 7
            self.weeks += 1
            if self.weeks_stay > 0:
                self.weeks_stay -= 1
        self.weeks += weeks
        if self.weeks >= 4.5: 
            self.weeks -= 4
            self.months += 1
        if self.months >= 12:
            self.months -= 12
            self.years += 1
# =====================================================================
class Npc(Character):
    def __init__(self, initDict):
        self.initDict = initDict
        super().__init__(initDict)
        self.reaction = initDict.get("reaction", "neutral")
        self.upp = initDict.get("upp") #  6BA854
        self.career = initDict.get("career") #  Scientist
        self.terms = initDict.get("terms") #  6
        self.apparent_gender = initDict.get("apparent gender", "Same as sex") #  Male/Female/Non-binary
        self.hair = initDict.get("hair")
        self.origin = initDict.get("origin") #  Neighbouring Sector
        self.disposition = initDict.get("disposition") #  Businesslike
        self.motivation1 = initDict.get("motivation1") #  Lust-4
        self.motivation2 = initDict.get("motivation2") #  Knowledge-6
        self.quirk1 = initDict.get("quirk1") # Evangelical religious
        self.quirk2 = initDict.get("quirk2") # Evangelical religious
        self.combatSkills = initDict.get("combatSkills") # 
        self.businessSkills = initDict.get("businessSkills") # 
        self.hexLocation = initDict.get("hex location", None) # 
        self.systemLocation = initDict.get("system location", None) # 
        self.localLocation = initDict.get("local location", None) # 
        self.mutations = initDict.get("mutations", []) # 
    def get_characteristics_from_upp(self, characteristic):
        if characteristic in [Traveller.STR]: index = 0
        elif characteristic in [Traveller.DEX]: index = 1
        elif characteristic in [Traveller.END]: index = 2
        elif characteristic in [Traveller.INT]: index = 3
        elif characteristic in [Traveller.EDU]: index = 4
        elif characteristic in [Traveller.SOC]: index = 5
        elif characteristic in [Traveller.MOR]: index = 6
        elif characteristic in [Traveller.LCK]: index = 7
        elif characteristic in [Traveller.SAN]: index = 8
        elif characteristic in [Traveller.CHM]: index = 9
        elif characteristic in [Traveller.PSI]: index = 10
        else:
            index = 11
        if(len(self.upp) > index):
            self.upp[index]
        else:
            return 6
    def asDict(self, initDict = {}):
        initDict["name"] = self.name
        initDict["surname"] = self.name
        initDict["upp"] = self.upp  #  6BA854
        initDict["age"] = self.age  #  58 yrs
        initDict["career"] = self.career  #  58 yrs
        initDict["terms"] = self.terms #  58 yrs
        initDict["apparent gender"] = self.apparent_gender #  Male
        initDict["fitness"] = self.fitness  # (for race)  Average
        initDict["height"] = self.height  # (for race)  Average
        initDict["weight"] = self.weight  # (for race)  Overweight
        initDict["species"] = self.species  #  Human
        initDict["subspecies"] = self.subspecies  #  Vilani
        initDict["hair"] = self.hair 
        initDict["origin"] = self.origin  #  Neighbouring Sector
        initDict["disposition"] = self.disposition  #  Businesslike
        initDict["motivation1"] = self.motivation1  #  Lust-4
        initDict["motivation2"] = self.motivation2  #  Knowledge-6
        initDict["quirk1"] = self.quirk1  # Evangelical religious
        initDict["quirk2"] = self.quirk2  # Evangelical religious
        initDict["combatSkills"] = self.combatSkills  # 
        initDict["businessSkills"] = self.businessSkills # 
        initDict["hex location"] = self.hexLocation
        initDict["system location"] = self.systemLocation
        initDict["local location"] = self.localLocation
        return initDict
    def getSkill(self, skill):
        if(skill in self.combatSkills.keys()):
            return self.combatSkills.get(skill)
        elif(skill in self.businessSkills.keys()):
            return self.businessSkills.get(skill)
        return 0 # defaults to 0 for skill
    def __str__(self): 
        return "{} {} ({}yo {}/{} {} {})".format(
            self.name, 
            self.surname, 
            self.age,
            self.sex, 
            self.apparent_gender, 
            self.subspecies,
            self.species,
            )
    def get_description(self):
        hair = "{} {} {}".format(self.hair["length"], self.hair["color"], self.hair["style"])
        if self.hair["length"].lower() == "bald":
            hair = "{} {}".format(self.hair["length"], self.hair["color"], self.hair["style"])
        if "Same" in self.apparent_gender and self.sex in ["Male"]:
            if self.hair.get("facial"):
                hair += " {}".format(self.hair.get("facial"))
        
        return "[{} {}] {} {} [{}] ({}yo {}/{} {} {}) {} [{} {}] {}. {}, {}. {}, {}, {}.".format(
            self.hexLocation,
            self.systemLocation, 
            self.name, 
            self.surname, 
            self.reaction,
            self.age,
            self.sex[0], 
            self.apparent_gender[0],  
            self.subspecies,
            self.species,
            self.upp,
            self.career,
            self.terms, 
            hair,
            self.motivation1, self.motivation2,
            self.disposition,
            self.quirk1, self.quirk2
            )
    @staticmethod
    def generate(
            name, surname, 
            age="random-adult", terms="random",
            sex="random", apparent_gender="random",
            species="random", subspecies="random", 
            height="random", weight="random", fitness="random",
            upp="random", career="random",
            hair={"length":None, "style":None, "color":None, "beard":None},
            origin="random", disposition="random", 
            motivation1="random", motivation1_value="random", 
            motivation2="random", motivation2_value="random", 
            quirk1="random", quirk2="random",
            hex_location="random",
            system_location="random",
            local_location="random",
            reaction="random"
            ):
        print("GENERATE NPC DICTIONARY")
        initDict = {}
        #
        apparent_genders = ["Same as sex", "Opposite of sex", "Non-binary"]
        careers = ["Civilian", "Bureaucrat", "Merchant", "Scientist", "Entertainer", 
            "Free Trader", "Explorer","Hunter", "Scout","Army", "Wet Navy", "Flyer", 
            "Space Navy", "Marine"]
        hairLengths = ["Bald", "Buzz-cut", "Short", "Average","Long"]
        hairColors = ["Grey/White", "Blonde", "Brown","Black","Colored"]
        hairStyles = ["Fanned", "Tiered", "Straight","Curly","Asymmetric"]
        beardChoices = ["Goatee", "Big scraggy beard", 
            "Neat beard","Mustache",
            "Handlebar Mustache"]
        origins = ["Local Area", "Local Area", "Region", "Continent", "World", "Inner System", 
            "Belt", "Outer System", "Neighboring System", "Subsector", "Sector", "Neighboring Sector", 
            "Long way away!"]
        dispositions = ["Happy", "Sad", "Angry", "Nervous", 
            "Cool", "Sinister", "Frightened", "Annoyed", "Businesslike", 
            "Very friendly","Amorous/Flirtatious"]
        motivations = ["Fame","Career","Respect","Love & Romance", "Wealth & Money",
            "Helping Others", "Helping Self", "Helping Family/Nepotism","Greed", "Pain & Suffering",
            "Control", "Safety & Security", "Protecting Family","Honor/Loyalty","Discovering","Knowledge",
            "Health","Power","Creating/Creativity","Contributing","Approval/Acceptance","Curiosity","Idealism",
            "Justice","Independence","Equality","Order","Lust","Social Interaction","Status","Tranquility",
            "Vengeance", "Violence", "Stubbornness", "Leadership", "Generosity", "Cowardice", "Fellowship", 
            "Wisdom","Honesty", "Pomposity/Arrogance", "Ruthless", "Liar", "Harmless Eccentric", "Insane"]
        combatSkills = ["Unarmed","Blade","Pistol","Rifle"]
        businessSkills = [
            "Negotiation","Carousing","Computer","Streetwise","Liaison",
            "Leader","Broker/Trader", "Profession (Other)"]
        quirks = ["Facial tick", "Artificial arm", "Cyber-eye", "Cyber-visor", 
            "Unpleasant odor", "Cough", "Sneezing", "Boils/warts", "Burns", "Scars", 
            "Bandaged arm", "Limp", "Leg Brace", "Very smart", "Very unkempt", 
            "Too many clothes", "Too few clothes", "Open weapon", "Drunk", "Dark glasses", 
            "Breathing mask", "Large bag", "Notable headgear", "Notable gloves", 
            "Notable clothes", "Pet/Familiar", "Personal bot","Obsessive note-taking", 
            "Wants to come along","Hums","Whistles", "Accomplice","Strong accent",
            "Long fingernails", "Notable hair","Very formal language","Poor Language",
            "Psionic","Wears a Psionic Helmet","Constantly on phone","Constantly on net", 
            "Eschews technology","Has baby with them", "Bare feet", "Notable footwear", 
            "Swears constantly", "Uses long words/old-fashioned speech", "Pious religious", 
            "Evangelical religious", "Constantly eating","Darting eyes"]
        if upp == "random":
            upp=""
            for i in range(6):
                upp += Character.uppValues[random.randint(2, 12)]
        initDict["upp"] = upp # 6BA854
        if species == "random":
            species = random.choice(list(DescriptionGenerator.species.keys()))
        if species in DescriptionGenerator.species.keys() and subspecies.lower() in [None, "random"]:
            subspecies = random.choice(list(DescriptionGenerator.species.get(species)))
        initDict["species"] = species
        initDict["subspecies"] = subspecies

        if terms == "random":
            terms = random.randint(1, 6)
        elif terms == "random-longlife":
            terms = random.randint(1, 20)
        terms = int(terms)
        initDict["terms"] = terms
        if age == "random-adult":
            initDict["age"] = 18 + (terms*4) + random.randint(0, 3) #  58 yrs
        elif age == "random-older":
            initDict["age"] = 18 + (terms*4) + random.randint(3, 6) #  58+ yrs
        elif age == "random-longlife":
            initDict["age"] = 38 + (terms*4) + random.randint(0, 3) #  150+ yrs
        elif age == "random-kid":
            initDict["age"] = random.randint(13, 18) #  18 yrs
        elif age == "random-longlife-kid":
            initDict["age"] = random.randint(18, 38) #  38 yrs
        else:
            initDict["age"] = int(age)
        #
        if sex == "random" and len(DescriptionGenerator.species_sexes[species]) > 1:
            sex = random.choice(DescriptionGenerator.species_sexes[species])
        elif sex == "random" and len(DescriptionGenerator.species_sexes[species]) < 2:
            sex = DescriptionGenerator.species_sexes[species][0]
        if apparent_gender == "random":
            roll = random.randint(1,8)
            if roll in [1, 2, 3, 4, 5, 6]:
                apparent_gender = "Save as sex"
            elif roll in [7]:
                apparent_gender = "Opposite as sex"
            elif roll in [8]:
                apparent_gender = "Non-binary"
        initDict["sex"] = sex
        initDict["apparent gender"] = apparent_gender
        print(initDict["sex"])
        print(initDict["apparent gender"])

        if name.lower() =="random":
            if sex.lower() in ["female"]:
                name = NameGenerator.normalize_name(NameGenerator.get_random_female_name())
            elif sex.lower() in ["male"]:
                name = NameGenerator.normalize_name(NameGenerator.get_random_male_name())
            else:
                name = NameGenerator.normalize_name(NameGenerator.get_random_name())
        if surname.lower() =="random":  
            surname = NameGenerator.normalize_name(NameGenerator.get_random_surname())

        initDict["name"] = name
        initDict["surname"] = surname
        #
        initDict["fitness"] = fitness
        if height == "random":
            roll = random.randint(1, 6)
            height = 48 + ((roll-3) * 6) + random.randint(-5, 5)
        initDict["height"] = float(height) # (for race)  Average

        if weight == "random":
            weight = 1.5*height + height-20 + (random.randint(0, 10))
        initDict["weight"] = float(weight) # (for race)  Overweight
        #
        if career == "random":
            career = random.choice(careers)
        initDict["career"] = career
        initDict["careerRank"] = min(max(1, int(terms)), 6) 
        #
        if hair is not None:
            length = hair.get("length")
            style = hair.get("style")
            color = hair.get("color")
            beard = hair.get("beard")
            if length is not None and length == "random" and initDict["species"].lower() not in ["devaronian"] and initDict["sex"].lower() not in ["male"]:
                length = random.choice(hairLengths)
            elif length is not None and length == "random" and initDict["species"].lower() in ["devaronian"] and initDict["sex"].lower() in ["male"]:
                length = hairLengths[0]

            if style is not None and style == "random" and initDict["species"].lower() not in ["devaronian"] and initDict["sex"].lower() not in ["male"]:
                style = random.choice(hairStyles)
            elif style is not None and style == "random" and initDict["species"].lower() in ["devaronian"] and initDict["sex"].lower() in ["male"]:
                style = hairLengths[0]


            if color is not None and color == "random" and initDict["species"].lower() not in ["devaronian"] and initDict["sex"].lower() not in ["male"]:
                color = random.choice(hairColors)
            if beard is not None and beard == "random" and initDict["sex"].lower() not in ["female"]:
                beard = random.choice(hairColors)
        initDict["hair"] = {}
        initDict["hair"]["length"] = random.choice(hairLengths)
        if initDict["hair"]["length"].lower() in ["bald"] and sex.lower() in ["female"]:
            initDict["hair"]["length"] = random.choice(hairLengths[2:])
        initDict["hair"]["style"] = random.choice(hairStyles)
        initDict["hair"]["color"] = random.choice(hairColors)
        if initDict["apparent gender"] in ["Female", "Other", "Special"]:
            initDict["hair"]["facial"] = None
        else:
            initDict["hair"]["facial"] = beard
        #
        if origin == "random":
            origin = random.choice(origins)
        if origin is None:
            origin = TerminalUtils.selectMenuItem(options=origins, prompt="Select an option. $>")
        initDict["origin"] = origin
        #
        if disposition == "random":
            disposition = random.choice(dispositions)
        initDict["disposition"] = disposition
        #
        if motivation1 == "random":
            motivation1 = random.choice(motivations)
        if motivation1_value == "random":
            motivation1_value = random.randint(3,10)
        initDict["motivation1"] = "{}-{}".format(motivation1, motivation1_value)

        motivations_list_for_2 = list(motivations)
        motivations_list_for_2.remove(motivation1)
        if motivation2 == "random":
            motivation2 = random.choice(motivations_list_for_2)
        if motivation2_value == "random":
            motivation2_value = random.randint(3,10)
        initDict["motivation2"] = "{}-{}".format(motivation2, motivation2_value)
        #
        if quirk1 == "random":
            quirk1 = random.choice(quirks)
        initDict["quirk1"] = quirk1
        quirks_list_2 = list(quirks)
        quirks_list_2.remove(quirk1)
        if quirk2 == "random":
            quirk2 = random.choice(quirks_list_2)
        initDict["quirk2"] = quirk2

        initDict["combatSkills"] = {} # 
        if (initDict["career"] in ["Hunter", "Scout","Army", "Wet Navy", "Flyer", "Space Navy", "Marine"]):
            for i in range(terms):
                selection = random.choice(combatSkills)
                if (selection in initDict["combatSkills"].keys()):
                    initDict["combatSkills"][selection] += 1
                else:
                    initDict["combatSkills"][selection] = 1
        else:
            if (random.randint(1, 6) in [4, 5, 6]):
                for i in range(terms//2):
                    selection = random.choice(combatSkills)
                    if (selection in initDict["combatSkills"].keys()):
                        initDict["combatSkills"][selection] += 1
                    else:
                        initDict["combatSkills"][selection] = 1
        #
        initDict["businessSkills"] = {"Profession ({})".format(career): terms, }# 
        if (initDict["career"] in ["Civilian", "Bureaucrat", "Merchant", "Scientist","Entertainer", "Free Trader"]):
            for i in range(terms):
                selection = random.choice(businessSkills)
                if (selection in initDict["businessSkills"].keys()):
                    initDict["businessSkills"][selection] += 1
                else:
                    initDict["businessSkills"][selection] = 1
        else:
            if (random.randint(1, 6) in [4, 5, 6]):
                for i in range(terms//2):
                    selection = random.choice(businessSkills)
                    if (selection in initDict["businessSkills"].keys()):
                        initDict["businessSkills"][selection] += 1
                    else:
                        initDict["businessSkills"][selection] = 1
        #
        if hex_location == "random":
            hex_location = None
        if system_location == "random":
            system_location = None
        if local_location == "random":
            local_location = None
        initDict["hex location"] = hex_location
        initDict["system location"] = system_location
        initDict["local location"] = local_location

        if reaction.lower() == "random":
            roll = random.randint(2, 12)
            if roll in [2, 3]: reaction = "Hostile"
            elif roll in [4, 5]: reaction = "Guarded"
            elif roll in [9, 10]: reaction = "Friendly"
            elif roll in [11, 12]: reaction = "Allied"
            else: reaction = "Neutral"
        initDict["reaction"] = reaction
        initDict["mutations"] = []
        return initDict
# =====================================================================
# =====================================================================
# =====================================================================
# =====================================================================
if __name__ == "__main__":
    import os, sys
    os.system('cls' if os.name == 'nt' else 'clear')
