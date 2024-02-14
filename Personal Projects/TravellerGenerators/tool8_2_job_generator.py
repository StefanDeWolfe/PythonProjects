# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
# 
import random, os, sys, re
import getopt
"""
This is a random Job Generator. 
To be used for Solo play or as a GM tool.
"""
class Node(object):
    def __init__(self, name):
        self.next = []
        self.previous = []
        self.name = name
        self.description = description
class Container(object):
    def __init__(self, name, description):
        self.listOfNodes = []
        self.name = name
        self.description = description
        self.startingNode = None
        self.endingNode = None
class Job(object):
    secondQuirkChance = 0.9
    facialHairChange = 0.2
    chanceextracbtskill = 0.5
    chanceextrabusskill = 0.4
    @staticmethod
    def generate(systemStance, patron=None):
        initDict = {}

        patrons = ["Individual","Hunter","Reporter/Media", "Explorer","Scientist",
            "Industrialist","Local Police/Spy", "Local Corporate","Large Corporate",
            "Intelligence","Military","Shady Organization","MegaCorporation","Noble"]

        missiontype = ["Explore","Courier","Investigate","Penetrate","Protect",
            "Liberate","Rescue","Seize","Kidnap","Destroy","Military"]

        target=["Person", "Team", "Organization", "Gadget/Equipment", "Installation"]

        opposition = ["Nil","Elements","Opposing Person","Police/Spy","Opposing Organization",
            "Organization Crime","Pirates","Military"]

        supports = ["Nil","Supplies","Tech","Weapons","QRF","Spaceship"]

        legality = ["Legal","Marginal","Dubious","Illegal","Totally Illegal"]

        spaceDistances = ["Current System", "Jump-1",  "Jump-2", "Jump-3", "Jump-5",
            "Other side of subsector", "Neighboring Subsector", "Neighboring Sector"]

        systemLocations = ["Current world", "Inner System", "Belt", "Mid-System", 
            "Outer System"]

        worldDistances = ["Local", "Continent", "Planet", "Moon", "Other World"]

        difficulty = ["Milk Run", "Easy", "Easy", "Average","Average", "Average", "Difficult","Difficult","Formidable","Impossible"]

        if systemStance.lower() in ["backwater"]: 
            pass
        elif "peace" in systemStance.lower(): 
            pass
        elif systemStance.lower() in ["distant threat"]: 
            pass
        elif systemStance.lower() in ["piracy"]: 
            pass
        elif systemStance.lower() in ["terrorism"]: 
            pass
        elif systemStance.lower() in ["insurgency"]: 
            pass
        elif systemStance.lower() in ["war"]: 
            pass
        else:
            pass
        if patron:
            initDict["patron"] = patron
            initDict["patron career"] = patron.career
        else:
            initDict["patron"] = None
            initDict["patron career"] = random.choice(patrons)
        initDict["missionType"] = random.choice(missiontype) # 
        initDict["missionTarget"] = random.choice(target) # 
        initDict["opposition"] = random.choice(opposition)  # 
        initDict["support"] = random.choice(supports)  # 
        initDict["legality"] = random.choice(legality) # Legal
        radialDirection = random.randint(1,12)
        initDict["spaceDistance"] = "{} (Radial Direction: {})".format(random.choice(spaceDistances), radialDirection) 
        initDict["systemLocation"] = "{}".format(random.choice(worldDistances))
        initDict["difficulty"] = random.choice(difficulty) 

        reward = 10000
        if (initDict["difficulty"] == "Milk Run"):
            reward = 1000
        elif (initDict["difficulty"] == "Easy"):
            reward = 10000
        elif (initDict["difficulty"] == "Average"):
            reward = 100000
        elif (initDict["difficulty"] == "Difficult"):
            reward = 1000000
        elif (initDict["difficulty"] == "Formidable"):
            reward = 10000000
        elif (initDict["difficulty"] == "Impossible"):
            reward = 100000000
        else:
            reward = 100000000

        initDict["relativeReward"] = random.randint(0,1000)/10
        initDict["rewardCredits"] = int((initDict["relativeReward"]/100) * reward) # 0% (875)

        return initDict
    def __init__(self, initDict):
        self.initDict = initDict
        self.patron = initDict.get("patron") # Scientist
        self.patronCareer = initDict.get("patron career") # Scientist
        self.missionType = initDict.get("missionType") # Protect
        self.missionTarget = initDict.get("missionTarget") # Team
        self.opposition = initDict.get("opposition") # Elements
        self.support = initDict.get("support") # Spaceship
        self.legality = initDict.get("legality") # Legal
        self.spaceDistance = initDict.get("spaceDistance") # Neighboring Subsector (Radial Direction: 2)
        self.systemLocation = initDict.get("systemLocation") # Outer System
        self.relativeReward = initDict.get("relativeReward") # 0%
        self.rewardCredits = initDict.get("rewardCredits") # (875)
        self.difficulty = initDict.get("difficulty") # Difficult
class Patron(object):
    @staticmethod
    def generate(name):
        uppValues = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        #
        initDict = {}

        races = ["Human", "Human", "Human", "Minor Human Race", "Other Major Race", 
            "Non-Human Minor Race",]
        careers = ["Civilian", "Bureaucrat", "Merchant", "Scientist","Entertainer", 
            "Free Trader", "Explorer","Hunter", "Scout","Army", "Wet Navy", "Flyer", 
            "Space Navy", "Marine"]
        subraces = ["White Skin", "Black Skin", "Olive Skin", "Brown Skin", 
            "Short, with crumpled face", "Almond eyed"]
        mass = ["Gaunt", "Skinny", "Average","Overweight","Obese"]
        height = ["Very Short", "Short", "Average","Tall","Very Tall"]
        hairLengths = ["Buzz-cut", "Short", "Average","Long","Bald"]
        hairColors = ["Grey/White", "Blonde", "Brown","Black","Colored"]
        hairStyles = ["Fanned", "Tiered", "Straight","Curly","Asymmetric"]
        beardChoices = ["Goatee", "Big scraggy beard", "Neat beard","Mustache",
            "Handlebar Mustache"]
        origin = ["Local Area", "Local Area", "Region", "Continent", "World", "Inner System", 
            "Belt", "Outer System", "Neighboring System", "Subsector", "Sector", "Neighboring Sector", 
            "Long way away!"]
        dispositions = ["Happy", "Sad", "Angry", "Nervous", "Cool", "Sinister", 
            "Frightened", "Annoyed", "Businesslike", "Businesslike", "Very friendly","Amorous/Flirtatious"]
        motivations = ["Fame","Career","Respect","Love & Romance","Wealth & Money",
            "Helping Others", "Helping Self", "Helping Family/Nepotism","Greed", "Pain & Suffering",
            "Control", "Safety & Security", "Protecting Family","Honour/Loyalty","Discovering","Knowledge",
            "Health","Power","Creating/Creativity","Contributing","Approval/Acceptance","Curiosity","Idealism",
            "Justice","Independence","Equality","Order","Lust","Social Interaction","Status","Tranquility",
            "Vengeance", "Violence", "Stubborness", "Leadership", "Generousity", "Cowardice", "Fellowship", 
            "Wisdom","Honesty", "Pomposity/Arrogance", "Ruthless", "Liar", "Harmless Eccentric", "Insane"]
        combatSkills = ["Unarmed","Blade","Pistol","Rifle"]

        businessSkills = ["Negotiation","Carousing","Computer","Streetwise","Liaison",
            "Leader","Broker/Trader"]

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


        upp = ""
        for i in range(6):
            upp += uppValues[random.randint(2, 12)]
        initDict["name"] = name
        initDict["upp"] = upp # 6BA854
        #
        terms = random.randint(1, 6)
        initDict["terms"] = terms
        initDict["age"] = 18 + terms*4 + random.randint(0, 3) #  58 yrs
        initDict["apparentGender"] = random.choice([
        "Male", "Male", "Male", "Male", "Female", "Female", 
        "Female", "Female", "Neuter", "Other", "Special"]) #  Male
        #
        initDict["height"] = random.choice(height) # (for race)  Average
        initDict["mass"] = random.choice(mass) # (for race)  Overweight
        #
        
        initDict["race"] = random.choice(races)
        initDict["subrace"] = None
        if (initDict["race"].lower() in ["human"]):
            subraces = ["White Skinned", "Brown Skinned", "Black Skinned", 
            "Almond eyed", "Short, with crumpled face", "Olive Skin"]
            initDict["subrace"] = random.choice(subraces)  
        #
 
        initDict["career"] = random.choice(careers)
        initDict["careerRank"] = terms 
        #
        initDict["hairLength"] = random.choice(hairLengths)
        initDict["hairStyle"] = random.choice(hairStyles)
        initDict["hairColour"] = random.choice(hairColors)

        if initDict["apparentGender"] in ["Female", "Other", "Special"]:
            initDict["facialHair"] = "None"
        else:
            initDict["facialHair"] = random.choice(beardChoices)
        #
        initDict["origin"] = random.choice(origin)
        #
        initDict["disposition"] = random.choice(dispositions)
        #
        motivation = random.choice(motivations)
        initDict["motivation1"] = "{}-{}".format(motivation, random.randint(1,10))
        motivations2 = list(motivations)
        motivations2.remove(motivation)
        initDict["motivation2"] = "{}-{}".format(random.choice(motivations2), random.randint(1,10))
        #
        quirk = random.choice(quirks)
        initDict["quirk1"] = quirk
        quirks2 = list(quirks)
        quirks2.remove(quirk)
        initDict["quirk2"] = random.choice(quirks2) 

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
        initDict["businessSkills"] = {}# 
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
        return initDict
    @staticmethod
    def generateDirected(name, archetype):
        uppValues = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        #
        initDict = {}

        races = ["Human", "Human", "Human", "Minor Human Race", "Other Major Race", 
            "Non-Human Minor Race",]
        careers = ["Civilian", "Bureaucrat", "Merchant", "Scientist","Entertainer", 
            "Free Trader", "Explorer","Hunter", "Scout","Army", "Wet Navy", "Flyer", 
            "Space Navy", "Marine"]
        subraces = ["White Skin", "Black Skin", "Olive Skin", "Brown Skin", 
            "Short, with crumpled face", "Almond eyed"]
        mass = ["Gaunt", "Skinny", "Average","Overweight","Obese"]
        height = ["Very Short", "Short", "Average","Tall","Very Tall"]
        hairLengths = ["Buzz-cut", "Short", "Average","Long","Bald"]
        hairColors = ["Grey/White", "Blonde", "Brown","Black","Colored"]
        hairStyles = ["Fanned", "Tiered", "Straight","Curly","Asymmetric"]
        beardChoices = ["Goatee", "Big scraggy beard", "Neat beard","Mustache",
            "Handlebar Mustache"]
        origin = ["Local", "Local", "Region", "Continent", "World", "Inner System", 
            "Belt", "Outer System", "Neighboring System", "Subsector", "Sector", "Neighboring Sector", 
            "Long way away!"]
        dispositions = ["Happy", "Sad", "Angry", "Nervous", "Cool", "Sinister", 
            "Frightened", "Annoyed", "Businesslike", "Businesslike", "Very friendly","Amorous/Flirtatious"]
        motivations = ["Fame","Career","Respect","Love & Romance","Wealth & Money",
            "Helping Others", "Helping Self", "Helping Family/Nepotism","Greed", "Pain & Suffering",
            "Control", "Safety & Security", "Protecting Family","Honour/Loyalty","Discovering","Knowledge",
            "Health","Power","Creating/Creativity","Contributing","Approval/Acceptance","Curiosity","Idealism",
            "Justice","Independence","Equality","Order","Lust","Social Interaction","Status","Tranquility",
            "Vengeance", "Violence", "Stubborness", "Leadership", "Generousity", "Cowardice", "Fellowship", 
            "Wisdom","Honesty", "Pomposity/Arrogance", "Ruthless", "Liar", "Harmless Eccentric", "Insane"]
        combatSkills = ["Unarmed","Blade","Pistol","Rifle"]

        businessSkills = ["Negotiation","Carousing","Computer","Streetwise","Liaison",
            "Leader","Broker/Trader"]

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


        upp = ""
        for i in range(6):
            upp += uppValues[random.randint(2, 12)]
        initDict["name"] = name
        initDict["upp"] = upp # 6BA854
        #
        terms = random.randint(1, 6)
        initDict["terms"] = terms
        initDict["age"] = 18 + terms*4 + random.randint(0, 3) #  58 yrs
        initDict["apparentGender"] = random.choice([
        "Male", "Male", "Male", "Male", "Female", "Female", 
        "Female", "Female", "Neuter", "Other", "Special"]) #  Male
        #
        initDict["height"] = random.choice(height) # (for race)  Average
        initDict["mass"] = random.choice(mass) # (for race)  Overweight
        #
        
        initDict["race"] = random.choice(races)
        initDict["subrace"] = None
        if (initDict["race"].lower() in ["human"]):
            subraces = ["White Skinned", "Brown Skinned", "Black Skinned", 
            "Almond eyed", "Short, with crumpled face", "Olive Skin"]
            initDict["subrace"] = random.choice(subraces)  
        #
 
        initDict["career"] = random.choice(careers)
        initDict["careerRank"] = terms 
        #
        initDict["hairLength"] = random.choice(hairLengths)
        initDict["hairStyle"] = random.choice(hairStyles)
        initDict["hairColour"] = random.choice(hairColors)

        if initDict["apparentGender"] in ["Female", "Other", "Special"]:
            initDict["facialHair"] = "None"
        else:
            initDict["facialHair"] = random.choice(beardChoices)
        #
        initDict["origin"] = random.choice(origin)
        #
        initDict["disposition"] = random.choice(dispositions)
        #
        motivation = random.choice(motivations)
        initDict["motivation1"] = "{}-{}".format(motivation, random.randint(1,10))
        motivations2 = list(motivations)
        motivations2.remove(motivation)
        initDict["motivation2"] = "{}-{}".format(random.choice(motivations2), random.randint(1,10))
        #
        quirk = random.choice(quirks)
        initDict["quirk1"] = quirk
        quirks2 = list(quirks)
        quirks2.remove(quirk)
        initDict["quirk2"] = random.choice(quirks2) 

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
        initDict["businessSkills"] = {}# 
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
        return initDict
    def __init__(self, initDict):
        self.initDict = initDict
        self.name = initDict.get("name") #  6BA854
        self.upp = initDict.get("upp") #  6BA854
        self.age = initDict.get("age") #  58 yrs
        self.career = initDict.get("career") #  Scientist yrs
        self.terms = initDict.get("terms") #  6
        self.apparentGender = initDict.get("apparentGender") #  Male
        self.height = initDict.get("height") # (for race)  Average
        self.mass = initDict.get("mass") # (for race)  Overweight
        self.race = initDict.get("race") #  Vilani
        self.subrace = initDict.get("subrace") #  Vilani
        self.hairLength = initDict.get("hairLength") #  Buzz-cut
        self.hairStyle = initDict.get("hairStyle") #  Tiered
        self.hairColour = initDict.get("hairColour") #  Brown
        self.facialHair = initDict.get("facialHair") #  Neat beard
        self.origin = initDict.get("origin") #  Neighbouring Sector
        self.disposition = initDict.get("disposition") #  Businesslike
        self.motivation1 = initDict.get("motivation1") #  Lust-4
        self.motivation2 = initDict.get("motivation2") #  Knowledge-6
        self.quirk1 = initDict.get("quirk1") # Evangelical religious
        self.quirk2 = initDict.get("quirk2") # Evangelical religious
        self.combatSkills = initDict.get("combatSkills") # 
        self.businessSkills = initDict.get("businessSkills") # 
    def asDict(self):
        initDict = {}
        initDict["name"] = self.name #  6BA854
        initDict["upp"] = self.upp  #  6BA854
        initDict["age"] = self.age  #  58 yrs
        initDict["career"] = self.career  #  58 yrs
        initDict["terms"] = self.terms #  58 yrs
        initDict["apparentGender"] = self.apparentGender #  Male
        initDict["height"] = self.height  # (for race)  Average
        initDict["mass"] = self.mass  # (for race)  Overweight
        initDict["race"] = self.race  #  Vilani
        initDict["subrace"] = self.subrace  #  Vilani
        initDict["hairLength"] = self.hairLength  #  Buzz-cut
        initDict["hairStyle"] = self.hairStyle  #  Tiered
        initDict["hairColour"] = self.hairColour  #  Brown
        initDict["facialHair"] = self.facialHair  #  Neat beard
        initDict["origin"] = self.origin  #  Neighbouring Sector
        initDict["disposition"] = self.disposition  #  Businesslike
        initDict["motivation1"] = self.motivation1  #  Lust-4
        initDict["motivation2"] = self.motivation2  #  Knowledge-6
        initDict["quirk1"] = self.quirk1  # Evangelical religious
        initDict["quirk2"] = self.quirk2  # Evangelical religious
        initDict["combatSkills"] = self.combatSkills  # 
        initDict["businessSkills"] = self.businessSkills # 
    def getSkill(self, skill):
        if(skill in self.combatSkills.keys()):
            return self.combatSkills.get(skill)
        elif(skill in self.businessSkills.keys()):
            return self.businessSkills.get(skill)
        return 0 # defaults to 0 for skill
    def __str__(self): return "{} ({}yo {} {})".format(self.name, self.age, self.apparentGender, self.race)
class JobGenerator():
    EncounterTypes = ["Combat", "Skill", "Mixed"]
    EncounterTypesProbabilities = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3]
    @staticmethod
    def generate(numberOfNodes, name):
        jobInitDict = {
            "Patron": None, 
            "Mission Type": None, 
            "Mission Target": None, 
            "Opposition": None, 
            "Support": None, 
            "Legality": None, 
            "Space Distance": None, 
            "System Location": None, 
            "Relative Reward": None, 
            "Difficulty": None,
            }
        job = Job()
        container = Container(name, description)
    @staticmethod
    def pprint(text, width=80):
        if text == None: return None
        p = 0
        skip_space=False
        for i in text:
            p += 1
            if(skip_space and i==" "):
                skip_space=False
                continue
            elif(skip_space and i!=" "):
                skip_space=False
            sys.stdout.write('%s' % i)
            sys.stdout.flush()
            if ((p > width and i == " ") or i == "\n"):
                sys.stdout.write('\n')
                sys.stdout.flush()
                skip_space=True
                p = 0
            #time.sleep(0.01)
        sys.stdout.write('\n')
        sys.stdout.flush()

def testPatron():
    patron = Patron(Patron.generate("<Patron>"))
    debugPatron(patron)
    return patron
def testJob():
    job = Job(Job.generate("Peace"))
    debugJob2(job)
    return job
def testJob2():
    patron = Patron(Patron.generate("<Patron>"))
    debugJob2(job)
    return job
def debugPatron(patron):
    print("Patron:")
    print("Name:          {}".format(patron.name))
    print("UPP:           {}".format(patron.upp ))
    print("Career:        {}".format(patron.career))
    print("Terms:         {}".format(patron.terms))
    print("Age:           {}".format(patron.age))
    print("Aprt Gender:   {}".format(patron.apparentGender))
    print("Height:        {}".format(patron.height))
    print("Mass:          {}".format(patron.mass))
    print("Race:          {}".format(patron.race))
    if patron.subrace not in [None, "None"]: print("Subrace:      {}".format(patron.subrace))
    print("Hair Length:   {}".format(patron.hairLength))
    print("Hair Style:    {}".format(patron.hairStyle))
    print("Hair Color:    {}".format(patron.hairColour))
    if patron.facialHair not in [None, "None"]: print("Facial Hair:   {}".format(patron.facialHair))
    print("Origin:        {}".format(patron.origin))
    print("Disposition:   {}".format(patron.disposition))
    print("Motivation:    {}".format(patron.motivation1))
    if patron.motivation2 not in [None, "None"]: print("Motivation 2:  {}".format(patron.motivation2))
    print("Quirk:         {}".format(patron.quirk1))
    if patron.quirk2 not in [None, "None"]: print("Quirk 2:       {}".format(patron.quirk2))
    print("Combat Skills:")
    for skill in patron.combatSkills.keys():
        print("- {}-{}".format(skill, patron.combatSkills[skill]))
    print("Business Skills:")
    for skill in patron.businessSkills.keys():
        print("- {}-{}".format(skill, patron.businessSkills[skill]))
def debugJob2(job):
    print("The Patron:")
    if (job.patron):
        ["Male", "Male", "Male", "Male", "Female", "Female", 
        "Female", "Female", "Neuter", "Other", "Special"]
        pronoun = "They"
        pronounPosessive = "Their"
        if job.patron.apparentGender in ["Female"]:
            pronoun = "She"
            pronounPosessive = "Her"
        elif job.patron.apparentGender in ["Male"]:
            pronoun = "He"
            pronounPosessive = "His"
        JobGenerator.pprint("{}, {} {}-{}, {} y/o {} {} {}, {} {}, {} {} {} hair{}.".format(
            job.patron.name, job.patron.upp, job.patron.career.lower(),job.patron.terms, 
            job.patron.age, job.patron.race, job.patron.subrace if job.patron.subrace else "",
            job.patron.apparentGender, 
            job.patron.height.lower() if job.patron.height != "Average" else "average height", 
            job.patron.mass.lower() if job.patron.mass != "Average" else "average weight",
            job.patron.hairLength.lower(), job.patron.hairStyle.lower(), job.patron.hairColour.lower(), 
            " with " + job.patron.facialHair.lower() if job.patron.facialHair is not None and job.patron.facialHair is not "None" else "",

            ))
        print("{} from the {}.".format(
            "{} {}".format(pronoun, "are" if pronoun == "They" else "is"),
            job.patron.origin
            ))
        print("{} {}, motivated by {} and {}. ".format(
            "{} {}".format(pronoun, "are" if pronoun == "They" else "is"),
            job.patron.disposition, job.patron.motivation1, job.patron.motivation2
            ))
        print("{} quirks are {} and {}.".format(
            "{}".format(pronounPosessive),
            job.patron.quirk1, job.patron.quirk2
            ))

        JobGenerator.pprint("{} is skilled in {} {}.".format(
            "{} {}".format(pronoun, "are" if pronoun == "They" else "is"),
            str(job.patron.combatSkills), str(job.patron.businessSkills)
            ))
    print("\nThe Job:")
    print("Lab Location: {} {}".format(job.spaceDistance, job.missionType))
    print("Incubation Subject: {}".format(job.missionTarget))
    print("Opposition: {}".format(job.opposition))
    print("Support: {}".format(job.support))
    print("Legality: {}".format(job.legality))
    print("Relative Reward: {}% ({}cr)".format(job.relativeReward, job.rewardCredits))
    print("Difficulty: {}".format(job.difficulty))
    print("")
    maturationDuration = int(re.search(r'\d+', job.maturation).group())
    months = float(maturationDuration)*0.33
    weeks = int(months*4)
    print("1st Trimester ({} months, {} weeks). ".format(int(months), weeks))
    print("    Return to <Lab> in {} weeks for checkup".format( random.randint(2, weeks//2) ))
    months = float(maturationDuration)*0.67
    weeks = int(months*4)
    print("2nd Trimester ({} months, {} weeks). ".format(int(months), weeks))
    print("    Return to <Lab> in {} weeks for checkup".format( random.randint(weeks//2, weeks-weeks//4) ))
    months = float(maturationDuration)
    weeks = int(months*4)
    print("3rd Trimester ({} months, {} weeks). ".format(int(months), weeks))
    print("    Return to <Lab> in {} weeks for checkup".format( weeks//2+random.randint(weeks//4, weeks-weeks//8) ))


def testDebug():
    job = testJob2()
# =====================================================================
def usage():
    print("USAGE:")
    print("python tool8_2_job_generator.py [ -p --patron <filename>] [-s --system <system name or hex coord>]")
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvs:f:", ["help", "system=", "file="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    viewHexCoord = False
    hexCoord = None
    fileName = None
    uwp = None
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
                    viewer.displaySystemStats(system)
                else:
                    print("\"{}\" is not a valid system.".format(hexCoord))
        else:
            print("\".pickle\" is not in the filename")
    else:
        print("\".pickle\" file is needed to use this app. (File is none or DNE)")
    #
    
    #
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    testDebug()
