# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
import random, sys, os
import getopt
from TravellerLibrary import *
from TravellerUtilLibrary import *
# ==============================================

# ==============================================
# Weapons
# Turret:
# {"mount": "fixed", "tech level":0, "tons": 0, "power": 0, "cost":100000, "weapons": []}
# {"mount": "single", "tech level":7, "tons": 1, "power": 1, "cost":200000, "weapons": []}
# {"mount": "double", "tech level":8, "tons": 1, "power": 1, "cost":500000, "weapons": []}
# {"mount": "triple", "tech level":9, "tons": 1, "power": 1, "cost":1000000,"weapons": [] }
# {"mount": "pop-up", "tech level":10, "tons": 1, "power": 0, "cost":1000000, "weapons": []}
# {"name": "Beam Laser", "tech level":10, "range":"medium", "power": 4, "damage": "1D", "cost":500000, "traits":[]}
# {"name": "Pulse Laser", "tech level":9, "range":"long", "power": 4, "damage": "2D", "cost":1000000, "traits":[]}
# {"name": "Sandcaster", "tech level":9, "range":"special", "power": 0, "damage": "special", "cost":250000, "traits":[]}
# {"name": "Missile Rack", "tech level":7, "range":"special", "power": 0, "damage": "4D", "cost":750000, "traits":["Smart"]}
# {"name": "Missile Barbette", "tech level":7, "range":"special", "power": 0, "damage": "4D", "cost":4000000, "traits":["Smart"]}
# {"name": "Ion Cannon", "tech level":12, "range":"medium", "power": 10, "damage": "2D x 10", "cost":6000000, "traits":["Ion"]}
# {"name": "Torpedo", "tech level":7, "range":"special", "power": 2, "damage": "6D", "cost":3000000, "traits":["Smart"]}
# ==============================================
class ShipGenerator():
    @staticmethod
    def generateRandomTraveller(ship_type="Far Trader Type-A2"):
        ship = None
        if ship_type.lower() in [ "" ]:
            ship_tech_level = 12
            ship_class = ""
            is_standard = True
            ship_name = random.choice([])
            ship_age = random.randint(0,60)
            ship_crew = ["Pilot", "Astrogator", "Engineer", "Medic", "Steward"]
            hull_tons = 1000
            hull_config="standard"
            hull_cost = 25000 * hull_tons

            armor_tons = None
            armor_value = None
            armor_type = None
            armor_cost = 

            description = "1000 ton Ore Carrier. Enterprise-Class"
            ship = Ship({
            "is standard":is_standard,
            "name":ship_name, "age": ship_age,
            "ship-class":ship_class, "tech level":ship_tech_level,
            "description":description,
            "ship-crew": ship_crew,
            "hull":{"tons":hull_tons,"configuation":hull_config, "modifications":[], "cost": hull_cost},
            "armor":{"tons":armor_tons, "type":armor_type, "armor":armor_value, "cost": 1200000},
            "m-drive":{"tons":2, "thrust":1 ,"power":20, "cost": 4000000},
            "j-drive":{"tons":15, "jump":2, "power":40, "cost": 15000000},
            "power-plant":{"tons":6, "type":"Fusion", "power":90, "cost": 6000000},
            "fuel tanks":{"tons":41, "jump-steps":2, "tons-per-jump-step":20, "tons-per-month":1, "cost": 4000000},
            "bridge":{"tons":10, "cost": 1000000, "modifications":["Holographic Controls"]},
            "computer":{"tons":10, "computer-level":5, "modifications":["/bis"], "cost": 30000},
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
                {"type": "Manoeuvre", "value": 0, "cost": 0},
                ],
            "common-areas":{"tons":10, "cost": 1000000, "modifications":["Medical Bay"] },
            "cargo-space":{"tons":57}
            })
        elif ship_type.lower() in [ "mining derrick 600 oregon" ]:
            pass
        elif ship_type.lower() in [ "tanker tender 1000 syndic" ]:
            pass
        elif ship_type.lower() in [ "mining cutter 50 YY" ]:
            pass
        elif ship_type.lower() in [ "prospecting ship 100 seeker" ]:
            pass
        elif ship_type.lower() in [ "lab Ship 400 artemis"]:
            pass
        elif ship_type.lower() in [ "salvage cruiser 2000 garshiirarmu" ]:
            pass
        elif ship_type.lower() in [ "mobile teaching hospital 200 orbis" ]:
            pass
        return ship
    @staticmethod
    def generateIndustrial(ship_type="Ore Carrier 1000 Enterprise"):
        ship = None
        if ship_type.lower() in [ "ore carrier 1000 enterprise" ]:
            ship_tech_level = 12
            ship_class = "Enterprise Ore Carrier"
            is_standard = True
            ship_name = random.choice(["Beijing", "Leedan", "Mephistopholes", "Glisen Enterprise"])
            ship_age = random.randint(3,60)
            ship_crew = ["Captain", "Pilot x3", "Astrogator", "Engineers x8", "Maintenance x2", "Medic", "Workers x20", "Administrator", "Specialists x4"]
            hull_tons = 1000
            hull_config="standard"
            hull_cost = 25000 * hull_tons

            armor_tons = None
            armor_value = None
            armor_type = None
            armor_cost = 

            description = "1000 ton Ore Carrier. Enterprise-Class"
            ship = Ship({
            "is standard":is_standard,
            "name":ship_name, "age": ship_age,
            "ship-class":ship_class, "tech level":ship_tech_level,
            "description":description,
            "ship-crew": ship_crew,
            "hull":{"tons":hull_tons,"configuation":hull_config, "modifications":[], "cost": hull_cost},
            "armor":{"tons":armor_tons, "type":armor_type, "armor":armor_value, "cost": 1200000},
            "m-drive":{"tons":2, "thrust":1 ,"power":20, "cost": 4000000},
            "j-drive":{"tons":15, "jump":2, "power":40, "cost": 15000000},
            "power-plant":{"tons":6, "type":"Fusion", "power":90, "cost": 6000000},
            "fuel tanks":{"tons":41, "jump-steps":2, "tons-per-jump-step":20, "tons-per-month":1, "cost": 4000000},
            "bridge":{"tons":10, "cost": 1000000, "modifications":["Holographic Controls"]},
            "computer":{"tons":10, "computer-level":5, "modifications":["/bis"], "cost": 30000},
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
                {"type": "Manoeuvre", "value": 0, "cost": 0},
                ],
            "common-areas":{"tons":10, "cost": 1000000, "modifications":["Medical Bay"] },
            "cargo-space":{"tons":57}
            })
        elif ship_type.lower() in [ "mining derrick 600 oregon" ]:
            pass
        elif ship_type.lower() in [ "tanker tender 1000 syndic" ]:
            pass
        elif ship_type.lower() in [ "mining cutter 50 YY" ]:
            pass
        elif ship_type.lower() in [ "prospecting ship 100 seeker" ]:
            pass
        elif ship_type.lower() in [ "lab Ship 400 artemis"]:
            pass
        elif ship_type.lower() in [ "salvage cruiser 2000 garshiirarmu" ]:
            pass
        elif ship_type.lower() in [ "mobile teaching hospital 200 orbis" ]:
            pass
        return ship
    @staticmethod
    def generate(ship_type):
        if ship_type.lower() in [
        "ore carrier 1000 enterprise", 
        "mining derrick 600 oregon", 
        "tanker tender 1000 syndic", 
        "mining cutter 50 YY", 
        "prospecting ship 100 seeker",
        "lab Ship 400 artemis",
        "salvage cruiser 2000 garshiirarmu",
        "mobile teaching hospital 200 orbis",
        ]:
            ShipGenerator.generateIndustrial(ship_type)
#
# ==============================================
# =====================================================================
def usage():
    print("python tool1_ship_generator.py -S far-trader-empress-marava-class")

    print("")
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvSCV", ["help", "name=", "upp=", "ship=", "character=", "vehicle=", "pickle="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    seed = None
    saveToFile=False
    ship_class = None
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-p", "--pickle"):
            saveToFile = True
            fileName = a
        elif o in ("-n", "--name"):
            name = a
        elif o in ("-S", "--ship"):
            ship_class = a
        else:
            assert False, "unhandled option"
    #
    shown = False
    ship = FarTraderA3LCalypsoClass()
    if ship_class is not None and ship_class.lower() in ship.ship_class.lower():
        shown = True
    ship = FarTraderEmpressMaravaClass()
    if ship_class is not None and ship_class.lower() in ship.ship_class.lower():
        shown = True
    ship = FreeTraderTypeA()
    if ship_class is not None and ship_class.lower() in ship.ship_class.lower():
        shown = True
    if not shown: 
        ship = Ship({})
    if ship is not None: ship.display_ship_sheet()
        
    #
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
    