# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
# 
import os, getopt, sys
import random
from TravellerLibrary import NameGenerator
def USAGE():
    print("python ./NameGenerator.py [-m --male|-f --female|-r --random] [-s --surname] [-p --pick #]")
    print("python ./NameGenerator.py -r -s -p 5")
    print("python ./NameGenerator.py -m -s -p 5")
    print("python ./NameGenerator.py -d -s -p 5")
    print("python ./NameGenerator.py -r -p 5")
    #  python ./NameGenerator.py -m -f -r -s -p 5
def main_name_gen(argv):
    #print ("argv: "+str(argv))
    # local vars
    gen_male_names=False
    gen_female_names=False
    gen_random_names=False
    gen_surnames=False
    amount_of_names=5
    try:
        opts, args = getopt.getopt(argv,
            "hmfrsp:", 
            [""]
            )
        #print ("Opts done")
    except getopt.GetoptError:
        print ("Bad arguments.")
        USAGE()
        sys.exit(1)
    #print("Check opts")
    #
    for opt, arg in opts:
        #print("opt="+str(opt)+".  arg="+str(arg)+"")
        if opt in ("-h", "--help"):
            USAGE()
            exit(0)
        elif opt in ("-m", "--male"):
            gen_male_names=True
        elif opt in ("-f", "--female"):
            gen_female_names=True
        elif opt in ("-s", "--surname"):
            gen_surnames=True
        elif opt in ("-r", "--random"):
            gen_random_names=True
        elif opt in ("-p", "--pick"):
            amount_of_names = int(arg)
        else:
            print("cannot find --opt <arg>")
            prog_help()
            exit(0)
    if gen_male_names:
        print("Male Names:")
        for _ in range(amount_of_names):
            name = NameGenerator.normalize_name(NameGenerator.get_random_male_name())
            surname = ""
            if gen_surnames:
                surname = NameGenerator.normalize_name(NameGenerator.get_random_surname())
                print("  {} {}".format(name, surname))
    if gen_female_names:
        print("Female Names:")
        for _ in range(amount_of_names):
            name = NameGenerator.normalize_name(NameGenerator.get_random_female_name())
            surname = ""
            if gen_surnames:
                surname = NameGenerator.normalize_name(NameGenerator.get_random_surname())
                print("  {} {}".format(name, surname))
    if gen_random_names:
        print("Random Names:")
        for _ in range(amount_of_names):
            name = NameGenerator.normalize_name(NameGenerator.get_random_name())
            surname = ""
            if gen_surnames:
                surname = NameGenerator.normalize_name(NameGenerator.get_random_name())
                print("  {} {}".format(name, surname))

    #print ("End of Line...")
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main_name_gen(sys.argv[1:])
    NameGenerator.get_random_male_name()
    print("")
