# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
import random, sys, os
import pickle
import getopt
from TravellerLibrary import *
from TravellerUtilsLibrary import *
'''
This is a Sector Generator for the Mongoose Traveller RPG V2.

Once this has been run usign the commands below, take the <Sector Name>-Sector.xml txt data and paste it into https://travellermap.com/make/poster to make a visual representation of the Sector.
For additional sector data, also paste in the <Sector Name>-Sector.xml data into the Metadata text window of the same website.

Then you can download it as a PDF, Bitmap, or SVG. 
'''

# =====================================================================
def usage():
    print("USAGE:")
    print("python tool4_sector_generator.py\n[-g]\n[--seed <random seed>]\n[--name <subsector name>]\n[-d --density <standard|dense|very-dense|all|rift|sparce>]")
    print('python tool4_sector_generator.py -g --seed 1234567890 --name "New_Sector" --density "standard"')
    # python tool4_sector_generator.py -g --seed 1234567890 --name "New_Sector" --density "standard"
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvgpes:n:u:x:d:", ["help", "name=", "seed=", "uwp=", "density="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    seed = None
    name = "test System"
    verbose = False
    generateSector=False
    saveToFile=False
    fileName = None
    density = "standard"
    uwp = None
    sprinkle_in_earthlikes = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-s", "--seed"):
            seed = a
        elif o in ("-g", "--generate"):
            generateSector = True
        elif o in ("-p", "--pickle"):
            saveToFile = True
        elif o in ("-n", "--name"):
            name = a
        elif o in ("-u", "--uwp"):
            uwp = a
        elif o in ("-e", "--earthlikes"):
            sprinkle_in_earthlikes = True
        elif o in ("-x", "--xml"):
            fileName = a
        elif o in ("-d", "--density"):
            density = a.lower()
        else:
            assert False, "unhandled option"
    #
    if (uwp is not None):
        SubsectorGenerator.displayUwpStats(uwp)
    elif (fileName is not None):
        sector = pickle.load( open( fileName, "rb" ) )
        systems = SubsectorGenerator.getHumanHabitableSystems(sector, verbose)
        if len(systems) < 1:
            print("Looking at Non-optimal systems")
            systems = SubsectorGenerator.getCloseToHumanHabitableSystems(sector, verbose)
    else:
        if(generateSector):
            print("Creating sector \"{}\" with seed: \"{}\"".format(name, int(seed) ))
            SubsectorGenerator.generateFullSector(int(seed), name, density, sprinkle_in_earthlikes, verbose)
            print("Sector Generation Complete")
        else: 
            SubsectorGenerator.generateSubsector(seed, name)
    #
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
    