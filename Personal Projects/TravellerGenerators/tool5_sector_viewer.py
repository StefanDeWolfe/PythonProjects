# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
import random, sys, os
import pickle
import getopt
from os.path import exists
from TravellerLibrary import *
from TravellerUtilsLibrary import *
'''
This tool views and edits parts of the sector created with the tool4_sector_generator.py file.

'''
# =====================================================================

# =====================================================================
def usage():
    print("USAGE:")
    print("python tool5_sector_viewer.py -f --file <filename> -s --system <system name or hex coord> [-e --edit]")
    print('python tool5_sector_viewer.py -f "New_Sector-Sector.pickle" -s 1614')
    print('python tool5_sector_viewer.py -f "New_Sector-Sector.pickle" -s 1614 -e')
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvs:f:en:t:", ["help", "system=", "file=", "transform="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    viewHexCoord = False
    hexCoord = None
    fileName = None
    uwp = None
    performEdit=False
    new_name = None
    rename = False
    planet_to_be_changed = None
    has_made_changes = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-s", "--system"):
            viewHexCoord = True
            hexCoord = a
        elif o in ("-f", "--file"):
            fileName = a
        elif o in ("-n", "--name"):
            new_name = a
            rename = True
        elif o in ("-e", "--edit"):
            performEdit = True
        elif o in ("-t", "--transform"):
            planet_to_be_changed = a
        else:
            assert False, "unhandled option"
    if(fileName is not None and exists(fileName)):
        if(".pickle" in fileName):
            sector = pickle.load( open( fileName, "rb" ) )
            viewer = SectorViewer(sector)
            if(viewHexCoord and hexCoord is not None):
                system = viewer.getSystemByHex( hexCoord) 
                if (system is  None):
                    system = viewer.getSystemByName( hexCoord)
                if (system is not None):
                    if planet_to_be_changed is not None:
                        SectorEditor.transformPrimaryInSystemToPreset(planet_to_be_changed, sector, system, viewer)
                        has_made_changes = True
                    if(rename):
                        SectorEditor.performSystemRename(new_name, sector, system, viewer)
                        has_made_changes = True
                    for body in system.systemLineup:
                        if isinstance(body, GasGiant): 
                            for moon in body.moons:
                                if isinstance(moon, AsteroidBelt) and not body.rings:
                                    body.rings = True
                                    has_made_changes = True
                        if body is not None and not isinstance(body, Star):
                            index = system.systemLineup.index(body)
                            current_body = body
                            while current_body.parent is not None:
                                print("{} has a parent not on the lineup!".format(current_body))
                                current_body = current_body.parent
                                print("New: {}".format(current_body))
                                has_made_changes = True
                            system.systemLineup[index] = current_body
                    viewer.displaySystemStats(system)
                    if(performEdit):
                        has_made_changes = SectorEditor.performSystemEdit(sector, system, viewer)
                    if has_made_changes:
                        print("Saving changes")
                        SubsectorGenerator.writeSectorTextFile(sector)
                        SubsectorGenerator.writeSectorXmlFile(sector)
                        SubsectorGenerator.writeSectorToFile(sector)
                    
                else:
                    print("\"{}\" is not a valid system.".format(hexCoord))
            else:
                print("Empty Hex at "+str(hexCoord)+". try another one.")
        else:
            print("\".pickle\" is not in the filename")
    else:
        print("\".pickle\" file is needed to use this app. (File is none or DNE)")
    #
    
    #
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
