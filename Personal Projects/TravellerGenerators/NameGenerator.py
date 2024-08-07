# Author: Stefan DeWolfe
# Date: 6/2024
#
import os, getopt, sys
import random


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
    consonants_random_list = consonants+consonant_combos
    vowels_random_list = vowels+vowel_combos
    name_types = [
        "cv", "vc",
        "cvc", "vcv", "cvc", "vcv",
        "cVc", "vCv",
        "cvcv", "vcvc", "cvcv", "vcvc",
        "cVcv", "vCvc",
        "cvCv", "vcVc",
        "cvcvc", "vcvcv", "cvcvc", "vcvcv",
        "cvCvc", "vcVcv",
        "cVcvc", "vcvCv",
        "cvcvcv", "vcvcvc"
        # "",
    ]
    @staticmethod
    def normalize_name(name="NAME"): return name[0].upper() + name[1:].lower()
    @staticmethod
    def get_random_male_name(file="MaleFirstNames.txt"):
        pass
        return NameGenerator.get_random_name_from_file(file=file)
    @staticmethod
    def get_random_female_name(file="FemaleFirstNames.txt"):
        pass
        return NameGenerator.get_random_name_from_file(file=file)
    @staticmethod
    def get_random_surname(file="Surnames.txt"):
        pass
        return NameGenerator.get_random_name_from_file(file=file)
    @staticmethod
    def get_random_town_name(file1='TownPrefixes.txt', file2='TownSuffixes.txt'):
        pass
        return f"{NameGenerator.get_random_name_from_file(file=file1)} {NameGenerator.get_random_name_from_file(file=file2)}"
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
    def get_random_name(name_kind=""):
        original_selected_type=name_kind
        name=""
        first = True

        if(name_kind==""):
            name_kind = NameGenerator.name_types[random.randint(0, len(NameGenerator.name_types)-1)]
        for i in name_kind:
            if(i in ["v", "V"]):
                name += random.choice(NameGenerator.vowels_random_list)
            elif(i in ["c", "C"]):
                name += random.choice(NameGenerator.consonants_random_list)
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
        return NameGenerator.normalize_name(part1 + part2)     
class StarWarsPlanetNameGenerator():
    @staticmethod
    def getName():
        planet_name_preffixes = ["Ord ","Ord "]
        planet_name_suffixes = ["ir", "aan", "ooine", "afar", "ifar", "ant", "osis", "ofis", "oo"]
        roll_name_type = random.randint(1,10)
        name = ""
        if roll_name_type in [1,2,3,4]:
            name = NameGenerator.normalize_name(NameGenerator.get_random_name(name_kind=random.choice([
            "cv","vc",
            "cvc","cvc","cvc","cvc","cvc","cvc",
            "vc", "vc",
            "cVc","vC",
            "cvC", "VC",
            "cvc", "Vc",
            "cVc", "vC",
            "Cvc","vcvc", "cVC","vcvc",
            "cVc","vCvc",
            "cvC","vcVc",
            "Cvc","vcvc",
            "cvC","vcVc",
            "cVc","vcvC",])) + random.choice(planet_name_suffixes))
        elif roll_name_type in [5, 6]:
            name = random.choice(planet_name_preffixes) + NameGenerator.normalize_name(
                NameGenerator.get_random_name(
                    name_kind=random.choice(NameGenerator.name_types)
                ))
        else:
            name = NameGenerator.normalize_name(NameGenerator.get_random_name(name_kind=random.choice([
                "cvcv cv","cvcv vc",
                "cVcv cv","cVcv vc",
                "cVCv cv","cVCv vc",
                "cvc","vcv", "cvc","vcv",
                "cVc","vCv",
                "cvcv","vcvc", "cvcv","vcvc",
                "cVcv","vCvc",
                "cvCv","vcVc",
                "cvcvc","vcvcv", "cvcvc","vcvcv",
                "cvCvc","vcVcv",
                "cVcvc","vcvCv",
                "cvcvcv","vcvcvc",

                "cvcv cV","cvcv vC","cvcv CV","cvcv VC",
                "cVcv cV","cVcv vC","cVcv CV","cVcv VC",
                "cVCv cV","cVCv vC","cVCv CV","cVCv VC",
                "cvcv cvC","cvcv vcv", "cvcv cvC","cvcv vcv",
                "cvcv cVC","cvcv vCV",
                "cVcv cvC","cVcv vcv", "cVcv cvC","cVcv vcv",
                "cVcv cVC","cVcv vCV",
                "cVCv cvC","cVCv vcv", "cVCv cvC","cVCv vcv",
                "cVCv cVC","cVCv vCV",
                "cvcv","vcvc", "cvcv","vcvc",
                "cVcV","vCvC",
                "cvCV","vcVC",
                "cvcvC","vcvcV", "CvcvC","vcvcV",
                "cvCvC","vcVcV",
                "cVcvC","vcvCV",
                "cvcvcV","vcvcvC",
                #"",
                ])))
            names = name.split(' ')
            name = ""
            for n in names:
                name += f"{NameGenerator.normalize_name(n)} "
        return name.strip()

def main_name_gen(argv):
    # 
    is_female = False
    is_male = False
    include_surname = False
    random_names = False
    sci_fi_names = False
    name_from_file = False
    try:
        opts, args = getopt.getopt(argv,
            "hfcmsr", 
            ["new=","party=","summary=","weapon=","armor=","equipment=","name=","race=","class="]
            )
        #print ("Opts done")
    except getopt.GetoptError:
        #print ("Bad arguments.")
        prog_help()
        sys.exit(2)
    #print("Check opts")
    #
    for opt, arg in opts:
        #print("opt="+str(opt)+".  arg="+str(arg)+"")
        if opt in ("-h", "--help"):
            prog_help()
            exit(0)
        elif opt in ("-f", "--female"):
            is_female = True
        elif opt in ("-m", "--male"):
            is_male = True
        elif opt in ("-s", "--surname"):
            include_surname = True
        elif opt in ("-c", "--scifi"):
            sci_fi_names = True
        elif opt in ("-r", "--random"):
            random_names = True
        elif opt in ("-n", "--namefromfile"):
            name_from_file = True
            file_name = arg
        else:
            print("cannot find --opt <arg>")
            prog_help()
            exit(0)
    if name_from_file and os.path.exists(name_from_file):
        for i in range(10):
            print(f"{NameGenerator.get_random_name_from_file(file=file_name)}")
    elif is_female and not sci_fi_names:
        for i in range(10):
            print(f"{NameGenerator.get_random_female_name()} {NameGenerator.get_random_surname() if include_surname else '' }")
    elif is_female and sci_fi_names:
        for i in range(10):
            print(f"{NameGenerator.get_random_name_from_file(file='Scifi_FemaleFirstNames.txt')} {NameGenerator.get_random_name_from_file(file='Scifi_Surnames.txt') if include_surname else '' }")
    if is_male and not sci_fi_names:
        for i in range(10):
            print(f"{NameGenerator.get_random_male_name()} {NameGenerator.get_random_surname() if include_surname else ''}")
    elif is_male and sci_fi_names:
        for i in range(10):
            print(f"{NameGenerator.get_random_name_from_file(file='Scifi_MaleFirstNames.txt')} {NameGenerator.get_random_name_from_file(file='Scifi_Surnames.txt') if include_surname else ''}")
    if random_names:
        for i in range(10):
            print(f"{NameGenerator.get_random_name()} {NameGenerator.get_random_surname(file='Surnames.txt') if include_surname else ''}")
    if random_names and sci_fi_names:
        for i in range(10):
            print(f"{NameGenerator.get_random_name()} {NameGenerator.get_random_surname(file='Scifi_Surnames.txt') if include_surname else ''}")
    if include_surname and not is_female and not is_male and not random_names:
        for i in range(10):
            print(f"{NameGenerator.get_random_surname(file='Scifi_Surnames.txt')} | {NameGenerator.get_random_surname(file='Surnames.txt')}")

    #print ("End of Line...")
def prog_help():
    print("Help:")
    print("""Arguments
        -h --help <HELP!>
        """)
if __name__ == "__main__":
    os.system('cls')
    main_name_gen(sys.argv[1:])
    print("")
