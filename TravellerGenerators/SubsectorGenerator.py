import random, sys, os
import pickle
import getopt
# =====================================================================
class DescriptionGenerator(object):
    @staticmethod
    def size_description(value):
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
    def atmosphere_description(value):
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
    def hydrographics_description(value):
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
    def temperature_description(value):
        if(value in ["3","4"]): return "Cold. -51c to 0c. Icy world. Little liquid water, extensive ice caps, few clouds." 
        elif(value in ["5", "6", "7", "8", "9"]): return "Temperate. 0c to 30c. Temperate world. Earth-like. Liquid & vaporized waster are common, moderate ice caps." 
        elif(value in ["A","B"]): return "Hot. 31c to 80c. Hot world. Small or no ice caps, little liquid water.  Most water in the form of clouds."
        elif(value in ["C","D","E","F","16","17","18","19","20"]): return "Boiling. 81c or more. Boiling world. No ice caps, little liquid water."
        elif(value in ["2","1","0","-1","-2","-3","-4","-5","-6"]): return "Frozen. -51c or less. Frozen world. No liquid water, very dry atmosphere."
        else: return "No Data"
    @staticmethod
    def population_description(value):
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
    def population_total(value):
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
    def government_description(value):
        if(value in [1]): return "Company/Corperation.  Ruling functions are assumed by a company managerial elite, and most citizenry are company employees or dependants. (Corporate outpost, asteroid mine, feudal domain.) Contraband [Weapons,Drugs,Travellers]" 
        elif(value in [2]): return "Participating Democracy.  Ruling functinos are reached by the advice and concent of the citizenry directly. (Collective, tribal council, commlinked consensus) Contraband [Drugs]"  
        elif(value in [3]): return "Self-Perpetuating Oligarchy. Ruling functions are performed by a restricted minority, with little or no input from the mass of citizenry. (Plutocracy, hereditary ruling caste) Contraband [Technology, Weapons, Travellers]" 
        elif(value in [4]): return "Representitive Democracy. Ruling functions are performed by elected representitives. (Republic, democracy) [Drugs, Weapons, Psionics]"
        elif(value in [5]): return "Feudal Technocracy. Ruling functions are performed by specific individuals for persons who agree to be ruled by them. Relationship are based on the performance of technical activities which are mutually benefitial. (Technology = Social status) Contraband [Technology, Weapons, Computers]" 
        elif(value in [6]): return "Captive Govenment. Ruling functions are performed by an imposed leadership answerable to an outside group. (A colony or conquered area) Contraband [Weapons, Technology, Travellers]" 
        elif(value in [7]): return "Balkanisation. No central authority exists; rival governments compete for control. Law levels refer to the government nearest starport. (Multiple governments, civil war) Contraband [Varies]" 
        elif(value in [8]): return "Civil Service Bureaucracy. Ruling functions are performed by government agencies employing individuals selected for their expertise. (Techocracy, Communism) Contraband [Drugs, Weapons]" 
        elif(value in [9]): return "Impersonal Bureaucracy. Ruling functions are performed by agencies which have become insulated from the governed citizens. (Entrenched castes of bureaucrats, decaying empire) Contraband [Technology, Weapons, Drugs, Travellers, Psionics]" 
        elif(value in [10]): return "Charismatic Dictator. Ruling functions are performed by agencies directed by a single leader who enjoys the overwhelming confidence of the citizens. (Revolutionary leader, Messiah, emperor) Contraband [None]"
        elif(value in [11]): return "Non-Charismatic Leader. A previous charismatic dictator has been replaced by a leader through normal channels. (Military dictatorship, hereditary kingship) Contraband [Weapons, Technology, Computers]"
        elif(value in [12]): return "Charismatic Oligarchy. Ruling functions are performed by a select group of members of an organisation or class which enjoys the overwhelming confidence of the citizens. (Junta, Revolutionary Council) Contraband [Weapons]"
        elif(value in [13]): return "Religious Dictatorship.  Ruling functions are performed by a religious organisation without regard to the specific individual needs of the citizenry. (Cult, transcendent philosophy, psionic group mind) Contraband [Varies]"
        elif(value in [14]): return "Religious autocracy.  Government by a single religious leader having absolute power over its citizenry. (Messiah) Contraband [Varies]"
        elif(value in [15]): return "Totalitarian Oligarchy. Government by an all-powerful minotiry which maintains absolute control through widespread coercian and oppression. (World Church, Ruthless Corperation) Contraband [Varies]"
        else: return "None.  No government structure.  In most cases, family bons predominate. (Family Clan, Anarchy) Contraband [None]"
    @staticmethod
    def culture_description(value):
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
    def law_level_description(value):
        if(value=="0"): return "No restrictions - Heavy armor and a handy weapon recommended."
        elif(value in [1]): return "Banned Weapons: Poison gas, explosives, undetectable weapons, WMDs.  Max armor permitted: Battle dress." 
        elif(value in [2]): return "Banned Weapons: Portable energy and laser weapons.  Max armor permitted: Combat Armor." 
        elif(value in [3]): return "Banned Weapons: Military grade weapons (automatics).  Max armor permitted: Flak armor." 
        elif(value in [4]): return "Banned Weapons: Light assault automatic weapons, submachine guns.  Max armor permitted: Cloth Armor." 
        elif(value in [5]): return "Banned Weapons: Personal Concealable weapons.  Max armor permitted: Mesh Armor." 
        elif(value in [6]): return "Banned Weapons: All firearms except Shotguns, Stunners; carrying weapons discouraged (by law).  Max armor permitted: Mesh Armor." 
        elif(value in [7]): return "Banned Weapons: Shutguns.  Max armor permitted: Mesh Armor." 
        elif(value in [8]): return "Banned Weapons: All bladed weapons, stunners.  Max armor permitted: All visible armor." 
        else: return "All weapons and armor banned." 
    @staticmethod
    def base_description(value):
        bases = ["S","R","N"]
        if(value=="S"): return "Scout" 
        elif(value=="R"): return "Reserach" 
        elif(value=="N"): return "Naval" 
        elif(value=="T"): return "TAS" 
        else:  return "TAS & " +DescriptionGenerator.base_description(bases[random.randint(0,len(bases)-1)]) + ""
    @staticmethod
    def starport_description(starport):
        if(starport in ["A"]): return "Excellent, cr+"+str(1000*random.randint(1,6))+" Berthing cost.  Refined fuel available. Shipyard (all) Repair facilities. "
        elif(starport in ["B"]): return "Good, cr+"+str(500*random.randint(1,6))+" Berthing cost.  Refined fuel available. Shipyard (spacecraft) Repair facilities. "
        elif(starport in ["C"]): return "Routine, cr+"+str(100*random.randint(1,6))+" Berthing cost.  Unrefined fuel available. Shipyard (small craft) Repair facilities. "
        elif(starport in ["D"]): return "Poor, cr+"+str(10*random.randint(1,6))+" Berthing cost.  Unrefined fuel available. Limited Repair facilities. "
        elif(starport in ["E"]): return "Frontier, No Berthing cost.  No fuel available. No Repair facilities. "
        elif(starport in ["X"]): return "No spaceport. "
    @staticmethod
    def travel_code_description(value):
        if(value=="A"): return "*Amber Travel Zone* Exercise caution, danger exists within this system."
        elif(value=="R"): return "!Restricted Travel Zone! Major Danger within system. Disease or Ongoing War present or Protected space."
        else: return "System is safe for travellers."
    @staticmethod
    def trade_code_description(value):
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
    def tech_level_description(value):
        if(value in [0]): return "TL 0 (Primitive): No technology. TL 0 species have only discovered the simplest tools and principles, and are on a par with Earth’s Stone Age." 
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
    def temperature_description(value):
        if(value <=2 ): return "Frozen world. No liquid water, very dry atmosphere." 
        elif(value in [3, 4]): return "Icy world. Little liquid water, extensive ice caps, few clouds." 
        elif(value in [5, 6, 7, 8, 9]): return "Temperate world. Earth-like. Liquid & vaporised water are common, moderate ice caps." 
        elif(value in [10, 11]): return "Hot world. Small or no ice caps, little liquid water. Most water in the form of clouds." 
        elif(value >= 12): return "Boiling world. No ice caps, little liquid water." 
        else: return "ERROR IN Temperature Description"
class Sector():
    def __init__(self, name="<Sector>"):
        self.name=name
        self.subsector_dict = {}
class Subsector():
    numberOfGridHexes=80
    def __init__(self, sector="<Sector>", name="<Subsector>"):
        self.name=name
        self.parent_sector=sector
        self.subsector_dict = {}
    def addSystem(self, system_code, system): 
        self.subsector_dict[system_code] = system
    def mapStarSystem(self):
        pass
    def getSystemByIndex(self, index):
        system=None
        if len(list(self.subsector_dict.keys())) > 0:
            l_systems = list(self.subsector_dict.values())
            system = l_systems[random.randint(0,len(l_systems)-1)]
        return system
class StarSystem():
    def __init__(self, name=None):
        self.name = self.generateName(name)
    def generateName(name):
        self.name = name
class Planet():
    def __init__(self, name=None):
        self.name = self.generateName(name)
    def generateName(name):
        self.name = name
#@SUB-SECTOR: Annetti SECTOR: Ryomans
# 
#--------1---------2---------3---------4---------5-------
#PlanetName   Loc. UPP Code   B   Notes         Z  PBG Al
#----------   ---- ---------  - --------------- -  --- --
#Hammontan     1711 C757533-5  S Ag Ni              533 Im
# =====================================================================
class SubsectorGenerator(object):
    """Subsector generator: Generates subsector with a given seed and saves it to pickle file"""
    @staticmethod
    def generateSystem(numberInSubsector, systemChance=None, ): 
        """
        -   systemChance: ranges from 1-5 and is used as a part of a range for world chance in a parsec hex
        """
        planetIsHot = False
        planetIsBoiling = False
        planetHabitableZoneLocation = 0
        systemDictionary = {}
        worldOccurrenceChance = [4,5,6]
        if (systemChance is not None):
            worldOccurrenceChance = range(systemChance,6)
        worldOccurrence = random.randint(1,6)
        if (worldOccurrence not in worldOccurrenceChance): # Finds system?
            print("NO system in ".format((numberInSubsector % 8) + 1, (numberInSubsector / 10) + 1))
            return None
        print("System found in ".format((numberInSubsector % 8) + 1, (numberInSubsector / 10) + 1))
        gasGiantChanceTestDM = 10
        GasGiantTest = random.randint(2,12)
        systemDictionary["system gas giants"] = 0
        if (GasGiantTest > gasGiantChanceTestDM):
            systemDictionary["system gas giants"] = random.randint(1,3)
        # Primary system colonized body
        planetSize = random.randint(2,12)-2
        systemDictionary["primary size"] = planetSize
        planetAtmosphere = random.randint(2,12)-7 + planetSize
        systemDictionary["primary atmosphere"] = planetSize

        HydrographicsDM = 0
        if(planetAtmosphere in [0, 1, 10, 11, 13]):
            HydrographicsDM = -4
        if(planetIsBoiling):
            HydrographicsDM = -6
        elif(planetIsHot):
            HydrographicsDM = -2

        if(planetAtmosphere in [0, 1, 10, 11, 13]):
            HydrographicsDM = -4
        planetHydrographics = random.randint(2,12)-7 + planetAtmosphere + HydrographicsDM
        
        if (planetSize in [0,1]):
            planetHydrographics = 0
        systemDictionary["primary hydrographics"] = planetHydrographics

        planetPopulation = random.randint(2,12)-2
        systemDictionary["primary population"] = planetPopulation

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

         
        planetGovernment = random.randint(2,12)-7 + planetPopulation
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

        culturalDifferences = random.randint(1,6)*10 + random.randint(1,6)
        systemDictionary["primary cultural diff"] = culturalDifferences

        planetLawLevel = random.randint(2,12)-7 + planetGovernment
        if(planetPopulation == 0):
            planetLawLevel = 0
        systemDictionary["primary law level"] = planetLawLevel

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

        systemTradeCodes = []
        if(planetAtmosphere in [4, 5, 6, 7, 8, 9] and planetHydrographics in [4, 5, 6, 7, 8] and planetPopulation in [5, 6, 7]): 
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
        systemDictionary["primary trade codes"] = systemTradeCodes

        # print (systemDictionary)
        return systemDictionary
        #
    @staticmethod
    def generateSubsector(rand_seed, name):
        if rand_seed:
            random.seed(rand_seed)
        subsector = Subsector("<Sector>", name)
        i = 0
        # for i in range(Subsector.numberOfGridHexes):
        system = SubsectorGenerator.generateSystem(i, 1)
        if (system is not None):
            SubsectorGenerator.displayUppCode(system)
        else:
            print("No System of note.")
        # if (system is not None):
        #     subsector.addSystem(system.getSystemCode(), system)
    @staticmethod
    def getStarportClass(starportLevel):
        if(starportLevel in [3, 4]):
            return "E"
        elif(starportLevel in [5, 6]):
            return "D"
        elif(starportLevel in [7, 8]):
            return "C"
        elif(starportLevel in [9, 10]):
            return "B"
        elif(starportLevel >= 11):
            return "A"
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
    @staticmethod
    def displayUppCode(system):
        hexKey=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        print("")
        print("Gas Giant #: {}".format(system["system gas giants"]))
        print("")
        print("Primary Planet")
        print("Primary Size: {} - {}".format(hexKey[system["primary size"]], DescriptionGenerator.size_description(system["primary size"])))
        print("Primary Atmosphere: {} - {}".format(hexKey[system["primary atmosphere"]], DescriptionGenerator.atmosphere_description(system["primary atmosphere"])))
        print("Primary Temp: {} - {}".format(system["primary temperature"], DescriptionGenerator.temperature_description(system["primary temperature"])))
        print("Primary Hydrographics: {} - {}".format(hexKey[system["primary hydrographics"]], DescriptionGenerator.hydrographics_description(system["primary hydrographics"])))
        print("")
        print("Primary Population: {} - {}".format(hexKey[system["primary population"]], DescriptionGenerator.population_description(system["primary population"])))
        print("Primary Government: {} - {}".format(hexKey[system["primary government"]], DescriptionGenerator.government_description(system["primary government"])))
        print("Primary Law Level: {} - {}".format(hexKey[system["primary law level"]], DescriptionGenerator.law_level_description(system["primary law level"])))
        print("Primary Tech Level: {} - {}".format(system["primary tech level"], DescriptionGenerator.tech_level_description(system["primary tech level"])))
        print("")
        print("Primary Starport: {} - {}".format(SubsectorGenerator.getStarportClass(system["primary starport"]), 
            DescriptionGenerator.starport_description(SubsectorGenerator.getStarportClass(system["primary starport"]))))
        print("")
        print("System Trade Codes: ")
        for tradeCode in system["primary trade codes"]:
            print("{} - {}".format(tradeCode, SubsectorGenerator.getGetFullTradeCodes(tradeCode)))
        print("")


# =====================================================================
def usage():
    print("python SubsectorGenerator.py --seed <random seed> --name <subsector name>")
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvs:o:", ["help", "seed=", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    seed = None
    name = "test System"
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-s", "--seed"):
            seed = a
        elif o in ("-n", "--name"):
            name = a
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"
    #
    SubsectorGenerator.generateSubsector(seed, name)
    #
if __name__ == "__main__":
    os.system('cls')
    main()
    