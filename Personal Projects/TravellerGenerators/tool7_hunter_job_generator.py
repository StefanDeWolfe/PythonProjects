# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
import random, os, sys
"""
This is a simple bounty hunter generator from some place online. 
I'll look for the site and cite it when I find it.
"""
class HuntingJob(object):
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
class Hunter(object):
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
class HunterSpaceShip(object):
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
def testJob():
    job = HuntingJob(HuntingJob.generate())
    debugJob(job)
def debugJob(huntingJob):
    print("Hunter Job:")
    print("  Target Description: {}".format(huntingJob.targetDescription))
    print("  Wanted For: {}".format(huntingJob.wantedFor))
    print("  Reward: {}".format(huntingJob.rewardCredits))
    print("")
def testHunter():
    hunter = Hunter(Hunter.generate())
    debugHunter(hunter)
def debugHunter(hunter):
    print("Hunter:")
    print("  Demeanour: {}".format(hunter.demeanour))
    print("  Weapon Preference: {}".format(hunter.weaponPreference))
    print("  Specialist Gear: {}".format(hunter.specialistGear))
    print("  Description: {}".format(hunter.description))
    print("  Species: {}".format(hunter.species))
    print("  Gimmick: {}".format(hunter.gimmick))
    print("")
    JobGenerator.pprint(hunter.getBlurb())
    print("")
def testHunterSpaceShip():
    hunterSpaceShip = HunterSpaceShip(HunterSpaceShip.generate())
    debugHunterSpaceShip(hunterSpaceShip)
def debugHunterSpaceShip(hunterSpaceShip):
    print("Hunter Ship:")
    print("  Ship Size: {}".format(hunterSpaceShip.shipSize))
    print("  Ship Type: {}".format(hunterSpaceShip.shipType))
    print("  Strength: {}".format(hunterSpaceShip.shipStrengths))
    print("  Weakness: {}".format(hunterSpaceShip.shipWeaknesses))
    print("  Species: {}".format(hunterSpaceShip.appearance))
    # print("Gimmick: {}".format(hunterSpaceShip.gimmick))
    print("")
    JobGenerator.pprint(hunterSpaceShip.getBlurb())
    print("")
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    testJob()
    testHunter()
    testHunterSpaceShip()
    #
#