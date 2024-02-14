# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
# 
import random, os, sys
import getopt
# 

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
        self.patron = initDict["patron"] # Scientist
        self.patronCareer = initDict["patron career"] # Scientist
        self.missionType = initDict["missionType"] # Protect
        self.missionTarget = initDict["missionTarget"] # Team
        self.opposition = initDict["opposition"] # Elements
        self.support = initDict["support"] # Spaceship
        self.legality = initDict["legality"] # Legal
        self.spaceDistance = initDict["spaceDistance"] # Neighboring Subsector (Radial Direction: 2)
        self.systemLocation = initDict["systemLocation"] # Outer System
        self.relativeReward = initDict["relativeReward"] # 0%
        self.rewardCredits = initDict["rewardCredits"] # (875)
        self.difficulty = initDict["difficulty"] # Difficult
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
        self.career = initDict.get("career") #  58 yrs
        self.terms = initDict.get("terms") #  58 yrs
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
    def __str__(self): return "Patron: {} ({}yo {} {})".format(self.name, self.age, self.apparentGender, self.race)
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
    patron = Patron(Patron.generate("Patron"))
    debugPatron(patron)
    return patron
def testJob():
    job = Job(Job.generate("Peace"))
    debugJob(job)
    return job
def testJob2(patron):
    job = Job(Job.generate("Peace", patron))
    debugJob(job)
    return job
def testScenario():
    patron = testPatron()
    print("")
    job = testJob2(patron)
    print("")
    sections = 2
    if(job.difficulty == "Milk Run"):
        sections += 1
    elif(job.difficulty == "Easy"):
        sections += 2
    elif(job.difficulty == "Average"):
        sections += 3
    elif(job.difficulty == "Difficult"):
        sections += 4
    elif(job.difficulty == "Formidable"):
        sections += 6
    elif(job.difficulty == "Impossible"):
        sections += 8
    print("Number of sections: {}".format(sections))
    print("")
    # Introduction Section 0
    '''[    "Individual","Hunter","Reporter/Media", "Explorer","Scientist",
            "Industrialist","Local Police/Spy", "Local Corporate","Large Corporate",
            "Intelligence","Military","Shady Organization","MegaCorporation","Noble"]''' 
    if (job.patron in ["Reporter/Media"]):
        pass
    ''' ["Explore","Courier","Investigate","Penetrate","Protect", 
        "Liberate","Rescue","Seize","Kidnap","Destroy","Military"]'''
    if (job.missionType in []):
        pass
    print("You are approached by a {}".format(job.patron))
    print("The job is this: You need to {} a {}".format(job.missionType, job.missionTarget))
    if job.opposition is not "Nil": print("A {} will oppose the objective.".format(job.opposition))
    if job.support is not "Nil": print("You can call in a {} for support".format(job.support))

    ChaseSkills = ["Drive", "Fly", "Pilot", "Athletics: Dexterity", "Athletics: Strength", "Athletics: Endurance", "Navigation"]
    InfiltrationSkills = ["Carouse", "Gambler", "Investigate", "Persuade", "Deception", "Streetwise", "Recon", "Explosives"]
    FixSkills = ["Mechanic", "Engineering", "Electronics"]
    AdministrationSkills = ["Broker","Advocate","Admin","Diplomat","Profession","Persuade"]
    CombatSkills = ["Melee Combat", "Gun Combat", "Gunnary", "Explosives", "Tactics: Military", "Leadership"]

    # Start Section:
    sectionOptions = 1
    if(job.difficulty in ["Milk Run", "Easy"]):
        sectionOptions += 0
    elif(job.difficulty == "Average", "Difficult"):
        sectionOptions += 1
    elif(job.difficulty == "Formidable"):
        sectionOptions += 2
    elif(job.difficulty == "Impossible"):
        sectionOptions += 3
    ''' ["Explore","Courier","Investigate","Penetrate","Protect", 
        "Liberate","Rescue","Seize","Kidnap","Destroy"]'''
    if (job.missionType in ["Explore"]):
        if (job.missionTarget in ["Person"]):
            print("Explore with a person")

        elif (job.missionTarget in ["Team"]):
            print("Explore with a exploration Team")

        elif (job.missionTarget in ["Organization"]):
            print("Explore with an Organization")

        elif (job.missionTarget in ["Gadget/Equipment"]):
            print("Explore using some Gadget/Equipment")

        elif (job.missionTarget in ["Installation"]):
            print("Explore using abandoned Installation")
        else:
            print("ERROR MISSION TARGET")
    elif (job.missionType in ["Courier"]):
        if (job.missionTarget in ["Person"]):
            print("Take message to Person")

        elif (job.missionTarget in ["Team"]):
            print("Take message to Team")

        elif (job.missionTarget in ["Organization"]):
            print("Take message to Organization")

        elif (job.missionTarget in ["Gadget/Equipment"]):
            print("Take Gadget/Equipment to Location/Person/Team")

        elif (job.missionTarget in ["Installation"]):
            print("Take message to Installation")
        else:
            print("ERROR MISSION TARGET")
    elif (job.missionType in ["Investigate"]):
        if (job.missionTarget in ["Person"]):
            print("Investigate a Person")

        elif (job.missionTarget in ["Team"]):
            print("Investigate a Team")

        elif (job.missionTarget in ["Organization"]):
            print("Investigate Organization")

        elif (job.missionTarget in ["Gadget/Equipment"]):
            print("Investigate Gadget/Equipment")

        elif (job.missionTarget in ["Installation"]):
            print("Investigate Installation")
        else:
            print("ERROR MISSION TARGET")
    elif (job.missionType in ["Penetrate"]):
        if (job.missionTarget in ["Person"]):
            print("Get Person inside Organization/Installation")

        elif (job.missionTarget in ["Team"]):
            print("Get Team inside Organization/Installation")

        elif (job.missionTarget in ["Organization"]):
            print("Infiltrate Organization")

        elif (job.missionTarget in ["Gadget/Equipment"]):
            print("Get Gadget/Equipment inside Organization/Installation")

        elif (job.missionTarget in ["Installation"]):
            print("Infiltrate Installation")
        else:
            print("ERROR MISSION TARGET")
    elif (job.missionType in ["Protect"]):
        if (job.missionTarget in ["Person"]):
            print("Protect Person from opposition.")

        elif (job.missionTarget in ["Team"]):
            print("Protect Team from opposition.")

        elif (job.missionTarget in ["Organization"]):
            print("Protect Organization from opposition.")

        elif (job.missionTarget in ["Gadget/Equipment"]):
            print("Protect Gadget/Equipment from opposition.")

        elif (job.missionTarget in ["Installation"]):
            print("Protect Installation from opposition.")
        else:
            print("ERROR MISSION TARGET")
    elif (job.missionType in ["Liberate"]):
        if (job.missionTarget in ["Person"]):
            print("Liberate Person from opposition.")

        elif (job.missionTarget in ["Team"]):
            print("Liberate Team from opposition.")

        elif (job.missionTarget in ["Organization"]):
            print("Liberate Organization from opposition.")

        elif (job.missionTarget in ["Gadget/Equipment"]):
            print("Liberate Gadget/Equipment from opposition.")

        elif (job.missionTarget in ["Installation"]):
            print("Liberate Installation from opposition.")
        else:
            print("ERROR MISSION TARGET")
    elif (job.missionType in ["Rescue"]):
        if (job.missionTarget in ["Person"]):
            print("Rescue Person from opposition.")

        elif (job.missionTarget in ["Team"]):
            print("Rescue Team from opposition.")

        elif (job.missionTarget in ["Organization"]):
            print("Rescue Organization from opposition.")

        elif (job.missionTarget in ["Gadget/Equipment"]):
            print("Rescue Gadget/Equipment from opposition.")

        elif (job.missionTarget in ["Installation"]):
            print("Rescue Installation from opposition.")
        else:
            print("ERROR MISSION TARGET")
    elif (job.missionType in ["Seize"]):
        if (job.missionTarget in ["Person"]):
            print("Bring Person to patron.")

        elif (job.missionTarget in ["Team"]):
            print("Bring Team to patron.")

        elif (job.missionTarget in ["Organization"]):
            print("Take over Organization to patron.")

        elif (job.missionTarget in ["Gadget/Equipment"]):
            print("Seize Gadget/Equipment to patron.")

        elif (job.missionTarget in ["Installation"]):
            print("Seize Installation for patron.")
        else:
            print("ERROR MISSION TARGET")
    elif (job.missionType in ["Kidnap"]):
        if (job.missionTarget in ["Person"]):
            print("Kidnap Person for patron.")

        elif (job.missionTarget in ["Team"]):
            print("Kidnap Team to patron.")

        elif (job.missionTarget in ["Organization"]):
            print("Kidnap Organization leader to patron.")

        elif (job.missionTarget in ["Gadget/Equipment"]):
            print("Take Gadget/Equipment For patron.")

        elif (job.missionTarget in ["Installation"]):
            print("Kidnap Installation leader to patron.")
        else:
            print("ERROR MISSION TARGET")
    elif (job.missionType in ["Destroy"]):
        if (job.missionTarget in ["Person"]):
            print("Kill Person for patron.")

        elif (job.missionTarget in ["Team"]):
            print("Kill Team for patron.")

        elif (job.missionTarget in ["Organization"]):
            print("Bring Down Organization to patron / Kill Organization leader.")

        elif (job.missionTarget in ["Gadget/Equipment"]):
            print("Destroy Gadget/Equipment for patron.")

        elif (job.missionTarget in ["Installation"]):
            print("Destroy/Disable Installation leader to patron / Kill Installation leader.")
        else:
            print("ERROR MISSION TARGET")
    else:
        print("ERROR MISSION TARGET")
        '''target=["Person", "Team", "Organization", "Gadget/Equipment", "Installation"]

        ''' 
    for i in range(sections-2):
        pass
    # End Section: final boss/challenge
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
def debugJob(job):
    print("Job:")
    if (job.patron):
        print("Patron: {}".format(job.patron.career))
    else:
        print("Patron: {}".format(job.patronCareer))
    print("Mission Type: {}".format(job.missionType))
    print("Mission Target: {}".format(job.missionTarget))
    print("Opposition: {}".format(job.opposition))
    print("Support: {}".format(job.support))
    print("Legality: {}".format(job.legality))
    print("Space Distance: {}".format(job.spaceDistance))
    print("System Location: {}".format(job.systemLocation))
    print("Relative Reward: {}% ({}cr)".format(job.relativeReward, job.rewardCredits))
    print("Difficulty: {}".format(job.difficulty))
    print("")
def testDebug():
    patron = testPatron()
    job = testJob2(patron)
# =====================================================================
def usage():
    print("USAGE:")
    print("python tool8_job_generator.py [ -p --patron <filename>] [-s --system <system name or hex coord>]")
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

