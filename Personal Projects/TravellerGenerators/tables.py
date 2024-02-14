# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
import random, os, getopt, sys
from TravellerUtilsLibrary import Utils, TerminalUtils
"""
This is a library of tables that can be used to generate adventures for Solo players or GMs. 
"""
''' http://www.ianewilliamson.co.uk/rpg/DnD/rules/worldgen/settlement.html
    Official race percentages
    Race                            Isolated    Mixed   Integrated
    Main race (eg human)            97%         79%         37%     37
    Main minority (eg halfling)     2%          9%          20%     57
    Second minority (eg elf)        1%          5%          18%     75
    Third minority (eg dwarf)                   3%          10%     85
    Fourth minority (eg gnome)                  2%          7%      92
    Fifth minority (eg half-elf)                1%          5%      97
    Sixth minority (eg half-orc)                1%          3%      100
    '''
class Tables():
    # ============================================================
    @staticmethod
    def getZozerBadConsequences():
        return {
            2: "Death (Of you or other)", 
            3: "Death (Of you or other)", 
            4: "Death (Of you or other)", 
            5: "Serious Injury",
            6: "Minor injury",
            7: "Trapped, lost or delayed",
            8: "Part of the mission was failed or incriminating evidence left behind",
            9: "Damage to a useful or valuable piece of kit",
            10: "Seriously upset or antagonise an NPC",
            11: "The task takes four times longer than planned",
            12: "The task takes four times longer than planned",
        }
    @staticmethod
    def getZozerGoodConsequences():
        return {
            2: "The task took half the expected time", 
            3: "The task took half the expected time", 
            4: "The task took half the expected time", 
            5: "The task took half the expected time",
            6: "Tracks covered, no evidence left behind",
            7: "Hear a rumor or discover a valuable piece of information",
            8: "Hear a rumor or discover a valuable piece of information",
            9: "Find a useful or valuable piece of kit",
            10: "Find a useful or valuable piece of kit",
            11: "Make a Contact or friend",
            12: "Make a Contact or friend",
        }
    @staticmethod
    def getZozerTravellerInMediaRes():
        return {
            2: "Hijack. The free trader your PCs are travelling on has been hijacked by three of the passengers (possibly with help from a crew-member – it is still unclear). One hijacker has barricaded himself into the engineering section, the others are on the bridge. All the crew-members (including the passengers – the PCs) have been locked inside a single stateroom. The crew have no combat experience and are fearful of being spaced. What do you do?",
            3: "Manslaughter. It was a simple job, provide protection and company for a rich traveller to this backwater world. But he's gotten into a fight that wasn't his fault and accidentally killed someone. Now the heat is on, be it the cops, a local gang or whatever. Get to the starport and off-world – fast.",
            4: "Pirates. The free trader your PCs are travelling on has been intercepted by a scout ship that demands to dock otherwise it will launch a full salvo of missiles. Travelling only between 'safe' systems, the free trader is unarmed. The crew have no combat experience and are about to be boarded in 15 minutes. What do you do?",             
            5: "AWOL. The PCs are being paid to get a military officer to the starport where a ship is waiting to take him off-world. He may be a defector, a spy, a coward or simply be disillusioned. The military of the planet do not intend him to leave, however.",             
            6: "The Package. Paid to carry a small package off-world, the PCs leave the patron's premises just before gunmen arrive to kill him. Now they want the package and will kill anyone who has touched it. Get off world quickly!",
            7: "Stuck. There is an emergency on planet that the PCs are caught up in. Travel is curtailed and if they don't get to the starport in 3 days the last transports will leave and there will be no way off planet for weeks or months.",
            8: "Arrested. One of the PCs has been held by security at the hotel for some (real or imagined) past crime until the police arrive. The hotel security officer has no idea the suspect has friends in the building …",
            9: "Missing. One of the PCs (choose or determine randomly) is missing, despite the group having booked passage on a starliner leaving in three days' time. The reason for the disappearance should be linked to one of the PC's hooks if possible.",
            10: "Low Berth. Low berth pods open automatically and the PCs get out. They are on a ship, but there seems to be no crew onboard. What type of ship is it? Where are they? What happened? The SOLO Player might decide between alien infestation, piracy or hijacking, or some strange jump drive anomaly.",
            11: "Hijack. The free trader your PCs are travelling on has been hijacked by three of the passengers (possibly with help from a crew-member – it is still unclear). One hijacker has barricaded himself into the engineering section, the others are on the bridge. All the crew-members (including the passengers – the PCs) have been locked inside a single stateroom. The crew have no combat experience and are fearful of being spaced. What do you do?",
            12: "Missing. One of the PCs (choose or determine randomly) is missing, despite the group having booked passage on a starliner leaving in three days' time. The reason for the disappearance should be linked to one of the PC's hooks if possible.",
            }
    @staticmethod
    def getZozerTravellerOnboardEventspassengerShip():
        return {
            11: "Hijack or piracy or both",
            12: "There is an incident amongst the crew and they turn to the PC for help.",
            13: "What the problem is will probably revolve one of the PCs skills, status or situation.",
            14: "An accident aboard ship requires repair, may involve an injury or some inconvenience. See Ship Malfunction Table.",
            15: "Fire in the cargo area – an electrical fault in the cargo bed rollers.",
            16: "Demanding passenger is a friend of destination's port manager.",
            21: "Passenger is an inspector for the government who is authorized a tour of the ship.",
            22: "Crewman becomes sullen, uncommunicative and makes mistakes, but will not discuss.",
            23: "Recycling systems require maintenance, it's a messy job.",
            24: "Find out some useful info from a passenger about the destination world, use it to either get half price living costs at the starport, a +1 on any Admin roll, or re-roll a cargo result during a cargo search. Make a Contact.",
            25: "Crewman's or passenger's fresher is broken , the stateroom is flooded!",
            26: "Jump field misaligning, requires spot retuning of the drive, very dangerous.",
            31: "Cargo containers have shifted due to grav compensator malfunction. Need re-setting.",
            32: "There's one obnoxious passenger people try to avoid. This trip will be miserable unless someone deals with him, which skill will work with him/her? (1) Streetwise, (2) Carouse, (3) Admin, (4) Bribery, (5) Leader, 6) Social Standing. Liaison is always appropriate. Make a suitable roll to deal with this person.",
            33: "Sensors are producing false readings. Or are they? If so, why?",
            34: "Cargo container explosion and chemical fire.",
            35: "Two passengers have a blazing and unresolved argument. It needs resolving!",
            36: "A passenger shows too much interest in another, and attempts entry into his/her cabin.",
            41: "Typical trip, with highs and lows.",
            42: "Fuel pump fails – reactor put on stand-by, something ingested during fuel scooping?",
            43: "Power failure – several tripped fuses, shuts down power in parts of engineering.",
            44: "Meet one of your contacts who needs your help. Is it financial, legal, administrative or personal?",
            45: "Passenger declares he has seen a gun in another passenger's stateroom.",
            46: "A passenger falls mysteriously ill.",
            51: "Security patrol ship makes contact in outer system or close to main world. (1) checks registry; moves on; (2) asks for passenger lists, is looking for a fugitive; (3) asks for cargo lists, is checking for customs irregularities; (4-5) will board, spend 1-3 hours conducting a routine search then move on. Roll 5+ for PC to avoid some cargo or personal irregularity which leads to his or her put under scrutiny/fined/delayed or detained; (6) the starship is breaking the law and will be accompanied to the starport where it will be impounded and investigated. Can the PC help with Bribery or Admin or other skills in preventing this?? If not, everyone is detained at the starport for 1-3 weeks, cargoes included. On a second roll of 10+ the panicked starship captain makes a run for it and the patrol ship will be forced to fire on the fugitive vessel.",
            52: "Crewman has an affair with a passenger.",
            53: "Gambling passenger takes everyone's money and causes bother ...",
            54: "Meet a fellow traveller as a potential Contact. Roll on the reaction table to make their acquaintance, roll on Patron table to determine their identity. When met again, roll reaction result or less for assistance, cheap cargo, help in dealing with a problem, etc.",
            55: "Captain runs a crew training session: see Starship Training Table.",
            56: "Theft from a passenger stateroom or luggage area.",
            61: "Captain is incapacitated, roll for a simultaneous event/crisis that needs resolving!",
            62: "Engineering problem requires all crew to help replace a huge component. See Ship Malfunction Table",
            63: "Crewman has a crisis of doubt, failure of duty. He/she shuts down.",
            64: "One of the stewards is: (1) rude, (2) corrupt, (3) missing, (4) exploitative, (5) thieving, (6) under pressure from a passenger.",
            65: "Passenger is extremely reclusive, will not come out of his cabin.",
            66: "Mysterious death of passenger or crew, was it murder?",
            }
    @staticmethod
    def getZozerTravellerOnboardEventsNonpassengerShip():
        return {
            11: "Piracy or hijack.",
            12: "Ship Malfunction. Check table.",
            13: "What the problem is will probably revolve one of the PCs skills, status or situation.",
            14: "An accident aboard ship requires repair, may involve an injury or some inconvenience. See Ship Malfunction Table.",
            15: "Fire in the cargo area – an electrical fault in the cargo bed rollers.",
            16: "Crewman is very ill, but the reason is a little mysterious.",
            21: "Ship Malfunction. Check table.",
            22: "Crewman becomes sullen, uncommunicative and makes mistakes, but will not discuss.",
            23: "Recycling systems require maintenance, it's a messy job.",
            24: "Typical trip, with highs and lows.",
            25: "Crewman's fresher is broken , the stateroom is flooded!",
            26: "Jump field misaligning, requires spot retuning of the drive, very dangerous.",
            31: "Cargo containers have shifted due to grav compensator malfunction. Need re-setting.",
            32: "Typical trip, with highs and lows.",
            33: "Sensors are producing false readings. Or are they? If so, why?",
            34: "Cargo container explosion and chemical fire.",
            35: "Two crewmen have a blazing and unresolved argument. It needs resolving!",
            36: "Typical trip, with highs and lows.",
            41: "Typical trip, with highs and lows.",
            42: "Fuel pump fails – reactor put on stand-by, something ingested during fuel scooping?",
            43: "Power failure – several tripped fuses, shuts down power in parts of engineering.",
            44: "Strange readings on the bridge suggest there might be a stowaway.",
            45: "The ship computer is acting oddly. Why? Is it malfunctioning? Has it been reprogrammed?",
            46: "It appears you have a cargo on-board – that doesn't belong to you …",
            51: "Security patrol ship makes contact in outer system or close to main world. (1) checks registry; moves on; (2) asks for passenger lists, is looking for a fugitive; (3) asks for cargo lists, is checking for customs irregularities; (4-5) will board, spend 1-3 hours conducting a routine search then move on. Roll 5+ for PC to avoid some cargo or personal irregularity which leads to his or her put under scrutiny/fined/delayed or detained; (6) the starship is breaking the law and will be accompanied to the starport where it will be impounded and investigated. Can the PC help with Bribery or Admin or other skills in preventing this?? If not, everyone is detained at the starport for 1-3 weeks, cargoes included. On a second roll of 10+ the panicked starship captain makes a run for it and the patrol ship will be forced to fire on the fugitive vessel.",
            52: "Ship Malfunction. Check table.",
            53: "Shipboard romance.",
            54: "Holiday or commemoration celebration.",
            55: "Captain runs a crew training session: see Starship Training Table.",
            56: "Crew entertainment evening.",
            61: "Captain is incapacitated, roll for a simultaneous event/crisis that needs resolving!",
            62: "Engineering problem requires all crew to help replace a huge component.",
            63: "Crewman has a crisis of doubt, failure of duty. He/she shuts down.",
            64: "The captain shuts him or herself off. It is quite mysterious.",
            65: "Captain runs a crew training session: see Starship Training Table.",
            66: "Ship Malfunction. Check table.",
            }
    @staticmethod
    def getZozerTravellerShipMalfunction():
        return {
            11: "Airlock malfunctions",
            12: "Grav Plates",
            13: "Water Recycling",
            14: "Computer Glitch",
            15: "Turret Mechanisms",
            16: "Flooding",
            21: "Fusion overheat",
            22: "Plasma leak",
            23: "Air Recycling",
            24: "Ship's Boat drive",
            25: "Maneuver drive",
            26: "Jump Drive calibration",
            31: "Security lock-outs",
            32: "Long range sensor ghosting",
            33: "Sensor hardware failure",
            34: "Hull stresses",
            35: "Micrometeoroid strike",
            36: "Heating/Life support problems",
            41: "Jump Drive trigger",
            42: "Jump field generator",
            43: "Fuel pump problem",
            44: "Gas build-up",
            45: "Radiation leak",
            46: "Fusion plant sensor failure",
            51: "Plasma coil replacement",
            52: "Computer core failures",
            53: "Cockpit display glitch",
            54: "Inertial compensators failing",
            55: "Missile targeting errors",
            56: "Missile loader jamming",
            61: "Laser weapon over-heat",
            62: "Bay-door jamming",
            63: "Coolant leak",
            64: "Undercarriage stress weakness",
            65: "Kitchen malfunction",
            66: "Waste disposal problem",
            }
    @staticmethod
    def getZozerTravellerShipboardTraining():
        return {
            2: "Nav Training",
            3: "Fuel-Leak",
            4: "Depressurization",
            5: "Seminar",
            6: "Fire",
            7: "Individual training", 
            8: "Power fluctuation",
            9: "Hijack",
            10: "Computer Malfunction",
            11: "Zero-G Training",
            12: "Combat",
            }
    @staticmethod
    def getZozerTravellerStarportEncounters():
        return{
        11: "Starport Shutdown - 1 week. Issue is a labor dispute, accident, festively/holiday or security problem.",
        12: "Your cargo is in the wrong place and your ship can't wait till whenever for it to be moved. Will Bribery or Admin help here?",
        13: "Your ship or ship's crew are in trouble, perhaps legally, perhaps personally or perhaps mechanically. They may need assistance.",
        14: "Customs - Roll 5+ for the cargo to clear customs. If not, there may be a 1 week delay or a duty to pay (1%). Is there a way around it? An Admin roll, on 10+ will find a loophole.",
        15: "Red Tape - Transfer papers contain irregularities. Bribery or Admin should smooth the way.",
        16: "Security - Security at starports is always high, you and your cargo are searched. The search will throw up some issue to do with your cargo or luggage you were unaware of on a 6 on 1d6. Arrest? Detention? Week-long delay? Set-up by a rival trader or a spurned seller? Roleplay the results.",
        21: "Meet a fellow traveller as a potential Contact. Roll on reaction table to make their acquaintance, roll on Patron table to determine their identity. Record the reaction result. Require a result of 8+ ('interested') for a friendship. When met again, roll reaction result or less for assistance, cheap cargo, help in dealing with a problem, etc.",
        22: "Meet one of your contacts who needs your help. Is it financial, legal, administrative or personal?",
        23: "Your cargo is pilfered or damaged, reduce amount by 10-60%",
        24: "Bunch of asteroid miners in port causing trouble all week for port officials and other travellers.",
        25: "Meet a minor celebrity/dignitary/notable in the company of a couple of aides/guards.",
        26: "Port personnel confuse you with someone else; roll 1d6 and on 1-3 this is good, on 4-6 it is bad. A quick ID check should sort it out – shouldn't it?",
        31: "A ship has limped into port this week with damage and crew casualties.",
        32: "Meet one of your contacts – they are desperate for help.",
        33: "Find a great hang-out/bar/cafe/restaurant at the port. Perfect for hiding away, making deals or wooing someone.",
        34: "Mysterious ship landed at the port, no-one allowed to see it or go near it, though there are plenty of rumors around.",
        35: "Warehouse has cargoes available for auction in order to get rid of them. Determine goods, determine price; player puts in a bid. Roll 8+ to get the cargo at your price., -1 if bidding over half, -2 if bidding half or less than, -4 if bidding a quarter or less than of the price.",
        36: "Free trader crew arrested and their ship seized.",
        41: "Someone needs to get off-world fast ... but it's not as simple as that ....",
        42: "One of your skills is recognized by a port employee ... they have a little problem, could you help them with it?",
        43: "Fire alarm keeps going off – everyone is jumpy and nervous.",
        44: "You are approached to smuggle illegal goods off-planet. If you accept, roll Bribery 8+ to succeed. There may be other complications. If you refuse you may make an enemy of the smuggler.",
        45: "A cargo seized by customs is going cheap. You can pick it up for a bonus (+2 on purchase table). Do the original owners want it back, though?",
        46: "Military ships in port causing a variety of problems for other travellers.",
        51: "Meet a fellow traveller as a potential Contact. Roll on reaction table to make their acquaintance, roll on Patron table to determine their identity. Record the reaction result. Require a result of 8+ ('interested') for a friendship. When met again, roll reaction result or less for assistance, cheap cargo, help in dealing with a problem, etc.",
        52: "Meet a fellow traveller as a potential Contact. Roll on reaction table to make their acquaintance, roll on Patron table to determine their identity. Record the reaction result. Require a result of 8+ ('interested') for a friendship. When met again, roll reaction result or less for assistance, cheap cargo, help in dealing with a problem, etc.",
        53: "Meet a fellow traveller as a potential Contact. Roll on reaction table to make their acquaintance, roll on Patron table to determine their identity. Record the reaction result. Require a result of 8+ ('interested') for a friendship. When met again, roll reaction result or less for assistance, cheap cargo, help in dealing with a problem, etc.",
        54: "Meet one of your contacts.",
        55: "Meet one of your contacts.",
        56: "Meet one of your contacts.",
        66: "Nothing out of the ordinary occurs.",}
    @staticmethod
    def getZozerTravellerWorldEncounterTable():
        return {
            11: "Crime. Roll UNDER law level to avoid a random non-lethal crime costing you Cr200 x 1D6.",
            12: "Renowned restaurant", 
            13: "Sudden weather change may affect travel plans", 
            14: "Trade agents of a large megacorporation are on planet, making normal trade difficult.", 
            15: "Sudden restriction on movement, unless you can find a way to avoid it", 
            16: "Another trader is after your preferred lot of trade goods.", 
            21: "Invited to a posh function", 
            22: "Ruined structure holds your interest", 
            23: "Discover a landed spacecraft. Why is it there?", 
            24: "Interesting or potentially dangerous encounter with some local wildlife.", 
            25: "Local situation and manner of seller make you suspicious and consider rethinking your purchase.", 
            26: "Holiday or festival celebrations slow things down, but become an enjoyable diversion.", 
            31: "Seller involved in legal trouble and you risk getting embroiled", 
            32: "Community is either not what it seems, or very welcoming", 
            33: "Discover a wonderful little-known retreat, a place to relax - or to hide.", 
            34: "Security check. Roll the Law Level or less to avoid a complete check of papers and a search of belongings and vehicle.", 
            35: "Patron offers you a short-term courier job to your next destination.", 
            36: "Transport delays", 
            41: "Hard times on the planet mean few trade goods for purchase", 
            42: "Valuable trade goods are on offer at a great deal. Why?", 
            43: "Harassed by a group of locals", 
            44: "Learn a secret on planet, political, corporate, etc. you can profit from this, if you decide. If so, roll Streetwise to get away with it and gain Cr10-60,000, fail and face being arrested, pursued or shipped off planet.", 
            45: "You need to travel to a restricted area and travel incognito with a forged ID. Goods will be more valuable (gain +1 bonus on the buying roll). If caught you will be sent back to the starport.", 
            46: "You are offered the chance to make extra money at a job lasting one day and paying Cr1000, or a favour.", 
            51: "Find yourself travelling with a group of interesting locals, gain useful information about the world and a tip (+1 to find a dealer) on this, or your next, visit.", 
            52: "Local crisis; bush-fire, earthquake, hurricane, rioting. If you have a cargo of particular use in the crisis you can sell for 3x the rolled price.", 
            53: "Investment opportunity arises on some local planetary business venture; you may gamble a multiple of Cr1,000 up to Cr10,000. Roll Gambler 8+ or Broker 8+ and if you succeed you gain half-again in profit, if you fail you lose your stake. The result occurs by the end of the week.", 
            54: "Goods are on offer direct from the grower/manufacturer. It is top quality stuff that will sell with a +1 bonus.", 
            55: "You are offered the chance to take part in a risky but rewarding adventure or expedition.", 
            56: "Introduced to local entertainments, spending hundreds of credits (Cr100 x 1D6) but gaining a friend and memories of a good time!", 
            61: "Job opportunity comes up that will last up to three days and pay Cr1000 plus 1D6 x Cr100.", 
            62: "You get ill. Roll 1D6, on 1-3 it is some bizarre local disease requiring an expensive local doctor who will cost you Cr600, otherwise you are bedridden each day till you successfully roll End 10+", 
            63: "You are approached to smuggle illegal goods off-planet. If you accept, roll Bribery 8+ to succeed. There may be other complications. If you refuse you may make an enemy of the smuggler.", 
            64: "Boom economy at the moment. This week, every dealer has three cargoes for you to choose from.", 
            65: "Embroiled in legal trouble. A lawyer with Admin 8+ roll will sort out the problem quickly, otherwise you may have to resort to bribery or other methods to get out of the situation.", 
            66: "Another off-worlder befriends you, they are in a spot of bother it soon transpires, would you help? There may be payment, or a favour.", 
        }
    @staticmethod
    def getZozerTravellerPatron():
        return {
            11: "Naval Officer", 41: "Corporate Official",
            12: "Reporter", 42: "Scientist",
            13: "Hunter", 43: "Spy",
            14: "Soldier", 44: "Broker",
            15: "Diplomat", 45: "Technician",
            16: "Army Officer", 46: "Financier",
            21: "Noble", 51: "Government Official",
            22: "Marine Officer", 52: "Scout Pilot",
            23: "Belter", 53: "Doctor",
            24: "Bureaucrat", 54: "Corporate Boss",
            25: "Starport Official", 55: "Local Military Officer",
            26: "Peasant/Farmer", 56: "Pilot",
            31: "Assassin", 61: "Smuggler",
            32: "Avenger", 62: "Researcher",
            33: "Merchant", 63: "Engineer",
            34: "Rogue", 64: "Mercenary",
            35: "Professor", 65: "Police Officer",
            36: "Gangster", 66: "Ship-Owner",
            }
    @staticmethod
    def getZozerTravellerPatronMissions():
        return {
            11: "Explore a moon or asteroid", 41: "Protect someone",
            12: "Explore ruins", 42: "Assist someone",
            13: "Salvage", 43: "Rescue someone",
            14: "Survey area", 44: "Join Expedition",
            15: "Capture animal", 45: "Infiltrate Group",
            16: "Hijack vehicle or ship", 46: "Find Missing Ship",
            21: "Assassination", 51: "Find Missing Goods",
            22: "Theft", 52: "Join Expedition",
            23: "Blackmail", 53: "Provide Protection on a Journey",
            24: "Burglary", 54: "Trick Someone",
            25: "Blackmail", 55: "Bribe",
            26: "Discredit", 56: "Sabotage",
            31: "Investigate Theft", 61: "Find Missing Person",
            32: "Investigate Murder", 62: "Transport Special Item",
            33: "Investigate Mystery", 63: "Transport Illegal Goods",
            34: "Investigate Accident", 64: "Transport Data",
            35: "Research a target", 65: "Transport Dangerous Cargo",
            36: "Spy on a Location", 66: "Transport Person",
            }
    @staticmethod
    def getZozerTravellerMissionTargets():
        return {
        11: "Yacht", 41: "Remote Base",
        12: "Free Trader", 42: "Orbital Station",
        13: "Security Ship", 43: "Starport",
        14: "Naval Craft", 44: "City Building",
        15: "Cargo Ship", 45: "Underground Vault or Bunker",
        16: "Orbital Station", 46: "Nightclub",
        21: "Artwork", 51: "Crime Gang",
        22: "Chemical Canister", 52: "Corporation",
        23: "Data Chip", 53: "Intelligence Agency",
        24: "Money or Bonds", 54: "Media Corporation",
        25: "Prototype", 55: "Planetary Government",
        26: "Weapon", 56: "Local Police",
        31: "Illegal Cargo",
        32: "Illegal Cargo",
        33: "Illegal Cargo",
        34: "Cargo",
        35: "Cargo",
        36: "Cargo",
        61: "Roll on Patron Table (S1)",
        62: "Roll on Patron Table (S1)",
        63: "Roll on Patron Table (S1)",
        64: "Roll on Patron Table (S1)",
        65: "Roll on Patron Table (S1)",
        66: "Roll on Patron Table (S1)",
        }
    @staticmethod
    def getZozerTravellerColorfulLocals():
        return {
            11: "Adventurers", 41: "Political Dissident",
            12: "Alien Starship Crew", 42: "Potential Patron",
            13: "Ambushing Brigands", 43: "Public Demonstration",
            14: "Bandits", 44: "Religious Pilgrims",
            15: "Beggars", 45: "Reporters",
            16: "Belters", 46: "Researchers",
            21: "Drunken Crew", 51: "Riotous Mob",
            22: "Fugitives", 52: "Security Troops",
            23: "Government Officials", 53: "Servant Robots",
            24: "Guards", 54: "Soldiers on Patrol",
            25: "Hunters and Guides", 55: "Street Vendors",
            26: "Law Enforcers on Patrol", 56: "Technicians",
            31: "Local Performers", 61: "Thugs",
            32: "Maintenance Crew", 62: "Tourists",
            33: "Merchants", 63: "Traders",
            34: "Military Personnel on Leave", 64: "Vigilantes",
            35: "Noble with Retinue", 65: "Workers",
            36: "Peasants", 66: "Player's Choice",
        }
    @staticmethod
    def getZozerRelationshipTable():
        return {11: "Bickers", 41: "Sexual partner",
        12: "Secretly in love", 42: "Sexual partner",
        13: "Secretly hates", 43:" Married couple",
        14: "Competitive rival", 44: "Divorced due to past incident",
        15: "Blames for a past event", 45: "Divorced over differences",
        16: "Blames for a past event", 46: "Related (and on good terms)",
        21: "Knows a dark secret", 51: "Related (but feuding or cold)",
        22: "Ignores or ridicules", 52: "Life-long friend",
        23: "Good friends", 53: "Secretly related (only one knows)",
        24: "Good friends", 54: "Loner",
        25: "Life-long friend", 55: "Competitive rival",
        26: "Hatred and constant arguing", 56: "Inseparable buddies",
        31: "Admires", 61: "Secretly in love",
        32: "Secretly jealous", 62: "Friendship through guilt",
        33: "Openly jealous", 63: "Hatred and constant arguing",
        34: "Dependent on another PC's support", 64: "Knows a dark secret",
        35: "Old (and these days, ex-) friends", 65: "Enemy – waiting for chance to strike",
        36: "Share a secret past incident", 66: "Roll again, but it's all an act. Why?",}
    @staticmethod
    def getZozerNpcReaction():
        return {
        2: "Hostile NPC will actively work against the PCs.",
        3: "Hostile NPC will actively work against the PCs.",
        4: "Guarded NPC does not trust the PCs. Will show no favours.",
        5: "Guarded NPC does not trust the PCs. Will show no favours.",
        6: "Neutral Treats PCs like everyone else. Unconcerned.",
        7: "Neutral Treats PCs like everyone else. Unconcerned.",
        8: "Neutral Treats PCs like everyone else. Unconcerned.",
        9: "Friendly There is some point of connection or common interest. They may show some favour to the PCs.",
        10: "Friendly There is some point of connection or common interest. They may show some favour to the PCs.",
        11: "Allied NPC finds a common cause with the Cs and show favour, assist or help further the cause of the group.",
        12: "Allied NPC finds a common cause with the Cs and show favour, assist or help further the cause of the group.",
        }
    #
    @staticmethod
    def getZozerShipEncounterMajorRoute():
        return {
        2: "Nothing",
        3: "Nothing",
        4: "Nothing",
        5: "Roll on Scout Ship Encounter Table",
        6: "Roll on Special Ship Encounter Table",
        7: "Roll on Small Transport Ship Encounter Table",
        8: "Roll on Large Transport Ship Encounter Table",
        9: "Roll on Industrial Ship Encounter Table",
        10: "Roll on Military Ship Encounter Table",
        11: "Roll on Large Transport Ship Encounter Table",
        12: "Roll on Military Ship Encounter Table",
        13: "Roll on Large Transport Ship Encounter Table",
        14: "Roll on Special Ship Encounter Table",
        }
    @staticmethod
    def getZozerShipEncounterMinorRoute():
        return {
        2: "Nothing",
        3: "Nothing",
        4: "Nothing",
        5: "Nothing",
        6: "Nothing",
        7: "Nothing",
        8: "Nothing",
        9: "Roll on Frontier Ship Encounter Table",
        10: "Roll on Small Transport Ship Encounter Table",
        11: "Roll on Military Ship Encounter Table",
        12: "Roll on Industrial Ship Encounter Table",
        13: "Roll on Large Transport Ship Encounter Table",
        }
    @staticmethod
    def getZozerIndustrialShipEncounter():
        return {
        2: "Ore Carrier 1000 Enterprise: Beijing, Leedan, Mephistopholes, Glisen Enterprise",
        3: "Ore Carrier 1000 Enterprise: Beijing, Leedan, Mephistopholes, Glisen Enterprise",
        4: "Ore Carrier 1000 Enterprise: Beijing, Leedan, Mephistopholes, Glisen Enterprise",
        5: "Mining Derrick 600 Oregon: New Horizon, Poseidon, Voyager",
        6: "Tanker Tender 1000 Syndic: Deep Blue, Cleopatra, Yeoman Bridge",
        7: "Mining Cutter 50 YY",
        8: "Prospecting Ship 100 Seeker: Chancer, Hero of the People, Snake Eyes, Vara's Den, Saturn 5",
        9: "Lab Ship 400 Artemis: Sophocles, Aristotle",
        10: "Salvage Cruiser 2000 Garshiirarmu: Opportunity",
        11: "Salvage Cruiser 2000 Garshiirarmu: Opportunity",
        12: "Mobile Teaching Hospital 200 Orbis",
        }
    @staticmethod
    def getZozerMilitaryShipEncounter():
        return {
        2: "Mercenary Cruiser 800 Broadsword: Sabre, Claymore, Lucifer, Jacob's Ladder",
        3: "Mercenary Cruiser 800 Broadsword: Sabre, Claymore, Lucifer, Jacob's Ladder",
        4: "Mercenary Cruiser 800 Broadsword: Sabre, Claymore, Lucifer, Jacob's Ladder",
        5: "Light Patrol Craft 200 Vorenus: Rapax, Venator, Gladius, Invictus, Novus, Hellas, Felix",
        6: "Close Escort 400 Punisher, Arbitrator, Justicar, Tormentor, Vindicator",
        7: "Patrol Cruiser 400 Arrogant, Audacious, Illustrious, Zealous, Vanguard, Trident, Vigilant, Intrepid, Glorious, Warspite , Monarch, Fortitude, Ardent, Defiance, Swiftsure",
        8: "Fleet Courier 400 Astra, Horizon, Zenith, Perigee, Zodiac, Nadir",
        9: "Battlecruiser 1250 Victory Class: Alemann",
        10: "Destroyer Escort 1000 DE Argus Class: Arethusa, Aurora, Galatea, Penelope, Phaeton, Royalist",
        11: "SDB 400 Avenger: no names",
        12: "Fleet Squadron in Transit",
        }
    @staticmethod
    def getZozerSpecialShipEncounter():
        return {
        2: "Fat Corsair 400 Challenger Ghost:",
        3: "Emergency Response Boat 100 Kineshii: Sanctuary, Mercy II, Hope, Relief, Haven, Refuge, Tranquility",
        4: "Personal Transport 100 Steed: Iruushigak, Niffleheim, My Lucy, Isengard",
        5: "Express Courier 200 Sprinter: Ben Morgan, Julian, Ambrose, Certainty",
        6: "Merchant Courier 100 Eucles: Nautilus, Herod, Deneb",
        7: "Yacht 150 Wind: Harmony, Destiny, Symphony",
        8: "Small Craft (Private) various",
        9: "Small Craft (Private) various",
        10: "Lab Ship 400 Artemis: Sophocles, Aristotle",
        11: "Safari Ship 200 Animal: Ocelot, Leopard",
        12: "Safari Ship 200 Animal: Ocelot, Leopard",
        }
    @staticmethod
    def getZozerSmallTransportShipEncounter():
        return {
        3: "Merchant 200 Manta: Arcturus, Nebula, Crimson Flag",
        4: "Subsidized Merchant 400 Stellar: Vector, Transtar, Courier, Reliant, Clear Horizon, Starfall, Certainty, Axis, Los Alamos, Mainstay, Challenger, Glory of Vega",
        5: "Subsidized Merchant 400 Stellar: Vector, Transtar, Courier, Reliant, Clear Horizon, Starfall, Certainty, Axis, Los Alamos, Mainstay, Challenger, Glory of Vega",
        6: "Frontier Trader 400 Boudicca: Venturer, Adventure, Expedition, Explorer",
        7: "Merchant 300 Goose: Cartagena, Turin, Orb's Luck, Just Cause,",
        8: "Small Craft (SPA)",
        9: "Small Craft (Corporate)", 
        10: "Modular Starship 300 Deneb: Aldebaran, Sirius, Procyon, Barnard, Castor",
        11: "Far Trader 200 Emperor Class: Marchant, Alexander, Nicolai, Ferdinand, Nero",
        12: "Small Craft (Industrial/Science)",
        13: "Subsidized Merchant 400 Challenger Class: Kraken, Ocean, Yarbond, Hammerhead, Hero, Equity, Concord, Iteration, Globus, Napoli",
        14: "Free Trader 200 Hero Class: Ambassador, Centennial, Gainful, Beowulf, Vash, Jabberwock, Weyland",
        15: "Small Craft (Personal)",
        16: "Light Transport 200 Nighthawk: Jumpmonkey, Aquinas, Valerian, Optimus",
        17: "Far Trader 200 Kyuseita: Rift Jumper, Phantom, Nephillim, Saint Helena, Netrix",
        18: "Merchant 300 Relationship: Accord, Agreement, Lentari Queen",
        }
    @staticmethod
    def getZozerScoutShipEncounter():
        return {
        2: "Surveyor 400 Dartilla Class: Nicomandia, Kish",
        3: "Surveyor 400 Dartilla Class: Nicomandia, Kish",
        4: "Surveyor 400 Dartilla Class: Nicomandia, Kish",
        5: "Scout 100 Golf Ball: Maynard, King Louis, Vernier, Citadel",
        6: "Fast Scout 100 Adder, Cobra, Rattlesnake",
        7: "Scout 100 Type S: Eagle's Claw, Lightspeed, Kiruul, Grim Reaper, Nightfleet, Thunderchild, Excalibur, Odyssey",
        8: "Scout 100 Type S: Eagle's Claw, Lightspeed, Kiruul, Grim Reaper, Nightfleet, Thunderchild, Excalibur, Odyssey",
        9: "Modular Scout 125 Eagle: Copenhagen, Vega Star, Spectra",
        10: "Scout 100 Type S: Eagle's Claw, Lightspeed, Kiruul, Grim Reaper, Nightfleet, Thunderchild, Excalibur, Odyssey",
        11: "Scout 100 Type S: Eagle's Claw, Lightspeed, Kiruul, Grim Reaper, Nightfleet, Thunderchild, Excalibur, Odyssey",
        12: "Extended Fast Scout 150 Hispaniola, Braveheart",
        13: "X-Boat Tender",
        14: "X-Boat Tender",
        15: "X-Boat awaiting pickup",
        16: "X-Boat awaiting pickup",
        17: "X-Boat awaiting pickup",
        18: "X-Boat awaiting pickup",
        }
    @staticmethod
    def getZozerLargeTransportShipEncounter():
        return {
        2: "Long Liner 1000 Pride of Vega, Deneb Express, Spirit of Arcturus",
        3: "Long Liner 1000 Pride of Vega, Deneb Express, Spirit of Arcturus",
        4: "Long Liner 1000 Pride of Vega, Deneb Express, Spirit of Arcturus",
        5: "Freighter 3000 Golden Harvest, Safety First, Star Liner, First Option",
        6: "Bulk Cargo Hauler 5000 Hercules class: Titan, Atlas, Mammoth, Samson, Endurance, Constitution, Goliath",
        7: "Subsidised Liner 600 Stellar Class: Spinward Star, Majestic Star, Golden Star, Sun Star, Island Star, Star Venture, Evening Star, Winward Star, Dawn Star",
        8: "Merchant Transport 500 Reliant: Armstrong, Kelvin, Nautilus, Saratoga",
        9: "Cargo Carrier 1000 OB101, OB167, OB230",
        10: "Frontier Transport 2000 Britannia, Sharshahan, Panther, Hernandez, Cortez",
        11: "Ore Carrier 1000 Beijing Enterprise, Leedan, Mephistopholes, Glisen Enterprise",
        12: "Ore Carrier 1000 Beijing Enterprise, Leedan, Mephistopholes, Glisen Enterprise",
        }
    @staticmethod
    def getZozerFrontierShipEncounter():
        return {
        3: "Cargo pod/escape ball",
        4: "Derelict vessel",
        5: "Mining Derrick 600 Oregon: New Horizon, Poseidon, Voyager",
        6: "Scout 100 Golf Ball: Maynard, King Louis, Vernier, Citadel",
        7: "Fat Corsair 400 Challenger Ghost:",
        8: "Surveyor 400 Dartilla Class: Nicomandia, Kish",
        9: "Far Trader 200 Emperor Class: Marchant, Alexander, Nicolai, Ferdinand, Nero",
        10: "Patrol Cruiser 400 Arrogant, Audacious, Illustrious, Zealous, Vanguard",
        11: "Frontier Trader 400 Boudicca: Venturer, Adventure, Expedition, Explorer",
        12: "Prospecting Ship 100 Seeker: Chancer, Hero of the People, Snake Eyes, Vara's Den, Saturn 5",
        13: "Scout 100 Type S: Eagle's Claw, Lightspeed, Kiruul, Grim Reaper, Nightfleet, Thunderchild, Excalibur, Odyssey",
        14: "Safari Ship 200 Animal: Ocelot, Leopard",
        15: "Close Escort 400 Punisher, Arbitrator, Justicar, Tormentor, Vindicator",
        16: "Pirate squadron!",
        17: "Fast Scout 100 Adder, Cobra, Rattlesnake",
        18: "Asteroid Hermit",
        }
    @staticmethod
    def getZozerFrontierShipReaction():
        return {
        3: "Fugitives from imperial law, they need a new ship…",
        4: "Fugitives from imperial law, they need a new ship…",
        5: "Fugitives from imperial law, they need a new ship…",
        6: "Debris and wreckage from the rolled ship",
        7: "Debris and wreckage from the rolled ship",
        8: "Radio silence, they fear pirates",
        9: "Radio silence, they fear pirates",
        10: "Ignore you, but polite",
        11: "Asks for info on world you've just left",
        12: "Asks for info on world you've just left",
        13: "Asks for help with a repair",
        14: "Crew are hostile and suspicious, warning you away",
        15: "Crew are hostile and suspicious, warning you away",
        16: "Medical emergency, they have no doctor or supplies",
        17: "Medical emergency, they have no doctor or supplies",
        18: "Medical emergency, they have no doctor or supplies",
        }
    @staticmethod
    def getZozerIndustrialShipReaction():
        return {
        3: "Thinks you are a pirate, based on rumour",
        4: "Thinks you are a pirate, based on rumour",
        5: "Thinks you are a pirate, based on rumour",
        6: "Thinks you are from rival company, warns you away",
        7: "Thinks you are from rival company, warns you away",
        8: "Comms are out, radio silence",
        9: "Medical emergency, their doctor is ill!",
        10: "Ignore you, but polite",
        11: "Ignore you, but polite",
        12: "Asks for info on world you've just left",
        13: "Requires help with repair, please!",
        14: "Require assistance with violent crewman",
        15: "Require assistance with violent crewman",
        16: "Refined ore in space from that ship. But no ship.",
        17: "Hijacked vessel, unusual trajectory/call signs",
        18: "Hijacked vessel, unusual trajectory/call signs",
        }
    @staticmethod
    def getZozerTransportSpecialShipReaction():
        return {
        3: "Thinks you are a pirate, based on rumour",
        4: "Thinks you are a pirate, based on rumour",
        5: "Thinks you are a pirate, based on rumour",
        6: "Transport matches a ship that went missing last year",
        7: "Transport matches a ship that went missing last year",
        8: "Comms are out, radio silence",
        9: "Medical emergency, their doctor is ill!",
        10: "Ignore you, but polite",
        11: "Ignore you, but polite",
        12: "Asks for info on world you've just left",
        13: "Requires help with repair, please!",
        14: "Require assistance with violent passenger/crewman",
        15: "Require assistance with violent passenger/crewman",
        16: "Cargo in space from that ship. But no ship.",
        17: "Hijacked vessel, unusual trajectory/call signs",
        18: "Hijacked vessel, unusual trajectory/call signs",
        }
    @staticmethod
    def getZozerScoutShipReaction():
        return {
        3: "Scout in distress; it has returned from a failed mission",
        4: "Scout in distress; it has returned from a failed mission",
        5: "Scout in distress; it has returned from a failed mission",
        6: "Warn you away from a gravitational disturbance",
        7: "Warn you away from a gravitational disturbance",
        8: "On way to map a moon",
        9: "Mapping gravitation anomalies",
        10: "Launching a nav beacon",
        11: "Launching a nav beacon",
        12: "Friendly hail, ask about world you have come from",
        13: "Ignore you, but are polite",
        14: "Ask for you sensor logs",
        15: "Mapping jump wakes, stay clear",
        16: "Need a civilian spare part",
        17: "Looking for a missing X-Boat",
        18: "Looking for a missing X-Boat",
        }
    @staticmethod
    def getZozerMilitaryShipReaction():
        return {
        3: "Warn you of an unidentified ship in this system",
        4: "Warn you of an unidentified ship in this system",
        5: "Warn you of an unidentified ship in this system",
        6: "Warn you of an unidentified ship in this system",
        7: "Need some civilian spare parts from your ship",
        8: "Asking for info on world just left",
        9: "Ignore you, will not answer comms",
        10: "Ignore you, but are polite",
        11: "Ignore you, but are polite",
        12: "Asking for sensor logs",
        13: "Security Checks",
        14: "Boarding",
        15: "Warn you of piracy in this system",
        16: "Warn you of piracy in this system",
        17: "One of your crew is wanted, see security checks",
        18: "One of your crew is wanted, see security checks",
        }
    # ============================================================
    @staticmethod
    def getBountyHunterGuideWarrentType():
        return {
            2: "Local Security",
            3: "Local Security",
            4: "Local Security",
            5: "Local Security",
            6: "Local Warrant",
            7: "Local Warrant",
            8: "Local Warrant",
            9: "Interstellar Warrant",
            10: "Interstellar Warrant",
            11: "Corporate Warrant",
            12: "Polity Warrant"
        }
    @staticmethod
    def getBountyHunterGuideTargetWanted():
        return {
            2: "Dead (bounty value x 0.2)",
            3: "Dead (bounty value x 0.2)",
            4: "Alive / Escort the target",
            5: "Alive / Escort the target",
            6: "Alive / Escort the target",
            7: "Alive / Escort the target",
            8: "Alive / Escort the target",
            9: "Delivered in cryostasis",
            10: "Recover Ship",
            11: "Recover Ship",
            12: "Recover Artifact"
        }
    @staticmethod
    def getBountyHunterGuideDistanceToTarget():
        return {
            0: "Within the current city",
            1: "Within the current city",
            2: "Within the current city",
            3: "Within the current city",
            4: "Within the current city",
            5: "Within the local region",
            6: "Within the local region",
            7: "Within the local region",
            8: "On the same world",
            9: "On the same world",
            10: "Within the star system",
            11: "Within the star system",
            12: "Up to 1D6+1 parsecs away"
        }
    # ============================================================
    @staticmethod
    def getTravellerSupp9RandomEventRoadsideEvents():
        return {
            11: "The Player Characters hit a small alien, killing it on the spot. After a short time, a roar is heard from a distance and a similar, only much larger, creature charges toward them.",
            12: "A police squad is stopping and searching all passing vehicles for illegal contraband, drugs or weapons due to a terror alert. Their search is cursory, however, and reveals only poorly hidden objects.", 
            13: "A young woman escaping an assailant carelessly runs in front of the Player Characters' car. Roll Drive 8+. If the driver fails, he hits the woman, dealing her 5d6 of damage. If the woman is hit, the assailant runs away, otherwise he continues in hot pursuit.", 
            14: "Five gangsters speeding on a stolen sports vehicle match speeds with the Player Characters and start verbally abusing them. They are high, armed and in a belligerent mood. Roll Streetwise 8+. If you fail, they attack.", 
            15: "Four criminals dressed as policemen stop the Player Characters for a 'routine search'. As soon as the Player Characters step out of their vehicle, the criminals attempt to rob them at gunpoint.", 
            16: "The Player Characters have a flat tire or a motor malfunction. The nearest garage is 1d6 X 10 km away.", 
            21: "The Player Characters come upon a junction not marked on their map. The road signs in the area are vandalised.",
            22: "Major traffic jam due to an accident involving a truck carrying highly toxic chemicals. Unless the Player Characters find an alternative route, they will spend at least six hours stuck in traffic.", 
            23: "Local aristocrats offer the Player Characters to race to the nearest town for 1,000 Credits.", 
            24: "Terrible weather (see page 74 in the Traveller Core Rulebook) forces the Player Characters to stop and wait for 1d6 hours. The weather could be related to a global event (see page 13) or just a spell of bad luck.", 
            25: "The Player Characters are ambushed by local commando soldiers in a tragic case of mistaken identity. Because a lawsuit from the Player Characters could spell long prison terms for all involved, the soldiers will try to kill the Player Characters even if they realise their mistake.", 
            26: "The Player Characters have a flat tire or a motor malfunction. The nearest garage is 1d6 X 10 km away.", 
            31: "Several bullet-riddled cars are parked by the side of the road. A dozen corpses of armed men are scattered around them. A strange suitcase lies in the centre of this massacre. The suitcase contains a treasure or a discovery (see page 12). If the Player Characters pick it up, they soon find out that several very powerful organisations are after it.",
            32: "A bridge over a wide canyon has collapsed. The repair crew says it will be at least a week until traffic can resume. However, the repairmen are rather strangely equipped and keep nervously glancing towards the horizon. Roll 1d6.\n 1–5: They are just unqualified or unmotivated.\n 6: They are hijackers planning to attack a passing military convoy.", 
            33: "A large group of irate and heavily armed aristocrats is pursing an eloping couple. The latter promise to pay the Player Characters a significant amount of money if the Player Characters hide them from their parents.", 
            34: "A sleazy looking motel that serves as the front for a human trafficking operation.", 
            35: "An abomination (see page 86) that slept under the road for centuries wakes up just as the Player Characters pass on top of it and attacks all cars in sight.", 
            36: "The Player Characters have a flat tire or a motor malfunction. The nearest garage is 1d6 X 10 km away.", 
            41: "The Player Characters spot a child driving a vehicle very poorly. It is only a question of time until this ends tragically.",
            42: "There is a colossal advertising board. Roll on the 'What's on TV?' table (page 137) to see what it is showing.", 
            43: "A small town completely devoid of citizens. Investigation will reveal everyone is dead from a mysterious disease. If the Player Characters drive further on, they soon reach a roadblock informing them that they are in a quarantined area and cannot leave until the incident has been investigated. Roll 1d6.\n 1–5: Each player should roll Endurance 6+. If failed, he contracts the disease.\n 6: After several hours, the 'corpses' rise and start attacking everything that moves.", 
            44: "The Player Characters hear a round of gunfire or an explosion from the wilderness surrounding the road. If they choose to investigate, roll on the Wilderness Events Table (see page 25).", 
            45: "A messenger loses control of his vehicle and suffers a serious accident. He is unconscious and in critical condition. Even a cursory examination of the papers scattered in the scene of the accident will reveal he was carrying a Discovery (see page 134).", 
            46: "The Player Characters have a flat tire or a motor malfunction. The nearest garage is 1d6 X 10 km away.", 
            51: "A strange spacecraft lands a few kilometres away from the road. Roll 1d6.\n 1–4: This is a smuggler ship. They will not attack the Player Characters unless harassed.\n 5: This is an ancient drone.\n 6: This is the beginning of an invasion (see page 14).",
            52: "The road is blocked by a group of 6d6 human and vargr protestors demanding equality for all species. The police have not arrived yet and both the stuck motorists and demonstrators are highly agitated. The sight of meat or leather could easily lead to blows.", 
            53: "The Player Characters are ambushed by 1d6+1 bandits who pretend to be distressed motorists.", 
            54: "A mysterious truck keeps trying to push the Player Character off the road. Roll 1d6.\n 1–2: The driver is a serial killer.\n 3–4: The driver is fleeing from an illegal lab and is under the effect of drugs or undergoing a mutation (see page 164).\n 5–6: The driver was hired by an Enemy of one of the Player Characters.", 
            55: "The Player Characters spot a broken vehicle by the side of the road. Roll 1d6.\n 1–3: A hapless couple whose vehicle is broken beyond repair.\n 4: A dangerous psychopath and a hostage pretending to be the former.\n 5: A fugitive from the law (see page 51 for fugitives).\n 6: A NPC known to one or more of the Player Characters.", 
            56: "The Player Characters have a flat tire or a motor malfunction. The nearest garage is 1d6 X 10 km away.", 
            61: "A pack of vicious and monstrously quick aliens charge out of the wilderness and attack the Player Characters and otherpassing vehicles. There are hundreds of them. Roll 1d6.\n 1–4: The creatures eat flash.\n 5–6: The creatures eat metal and will not attack biological organisms unless attacked by them first.",
            62: "As for previous, only the attackers are not aliens but failed experiments. After the Player Characters have dealt with the monsters they will have to deal with a cover-up team consisting of elite mercenaries and corrupt policemen.", 
            63: "The Player Characters suddenly hear punching and crying from the trunk of their vehicle. Roll 1d6.\n 1–3: It is a prank played by an acquaintance. There is nothing but an audio device inside the trunk.\n 4–5: The aforementioned acquaintance wanted to prank the Player Characters but accidentally locked himself inside the trunk, knocking himself out in the process.\n 6: A random NPC locked himself in the truck to hide from assassins who were chasing him the day before.", 
            64: "The Player Characters witness a hit-and-run accident. The victim lies mortally wounded while the young and hysterical driver is fleeing the scene of the accident.", 
            65: "There is a hitchhiker by the side of the road. Just about any NPC in this, or any other book, can be introduced this way.", 
            66: "The Player Characters witness one of the events in this table happening to a faraway vehicle.", 
            }
    @staticmethod
    def getTravellerSupp9RandomEventHealthEvents():
        return {
            11: "Too much time in the pilot seat or the business table and too little exercise take their toll. Gain 10 kilograms.",
            12: "The life of the traveller is hard and this year was exceptionally harsh. Lose 10 kilograms.", 
            13: "You suffer a major cardiac arrest. You recover but the experience weakens your heart. Suffer –1 to Endurance.", 
            14: "You contract cancer. If not treated it kills you within a year.", 
            15: "You spent a great deal of time this year working out and navigating difficult terrain. Gain +1 in any one physical ability.", 
            16: "Your professional duties have caused you to abandon your physical training, leaving you somewhat out of shape. Suffer –1 to any one physical ability.", 
            21: "You gain a drug addiction.",
            22: "You slip and break a bone. Suffer –1 to Dexterity or Strength. Until the injury is healed, you move at half speed.", 
            23: "You have a brain tumour. Roll 1d6.\n 1–3: The tumour is successfully removed and you suffer no ill effects.\n 4–5: The operation weakens your senses, imposing –1 DM on all recon checks.\n 6: The operation damages your brain. Suffer –1 to Intelligence or Education.", 
            24: "A head injury causes a major personality shift.", 
            25: "You spent a great deal of time this year working out and navigating difficult terrain. Gain +1 in any one physical ability.", 
            26: "Your professional duties have caused you to abandon your physical training, leaving you somewhat out of shape. Suffer –1 to any one physical ability.", 
            31: "Years of eating tasteless health food and avoiding alcohol and smoking finally pay of. Gain +1 Endurance.",
            32: "Womb having characters only, re-roll for non-womb havers. You discover that you are pregnant.", 
            33: "Pregnant characters only, re-roll if not pregnant. You suffer a miscarriage.", 
            34: "You start hearing voices. Roll 1d6 for the cause.\n 1–4: Schizophrenia.\n 5: You have uncultivated psionic talents.\n 6: A colossal space alien is trying to contact you (see page 35).", 
            35: "You spent a great deal of time this year working out and navigating difficult terrain. Gain +1 in any one physical ability.", 
            36: "Your professional duties have caused you to abandon your physical training, leaving you somewhat out of shape. Suffer –1 to any one physical ability.", 
            41: "A minor injury gets infected for lack of proper treatment. Roll Endurance 8+. If failed, the infection becomes gangrenous and a random limb has to be amputated. If the effect was –6 or lower, two limbs have to be amputated.",
            42: "The Player Character develops an allergy. Roll 1d6.\n 1–2: Minor allergy to common substance (fur, peanuts).\n 3–4: Major allergy to uncommon substance (aslan fur, exotic food)\n 5: Deadly allergy to very rare substance (alloy used only by the ancients, asteroid dust).\n 6: Deadly allergy to very common substance (water, sun).", 
            43: "The Player Character suffers retrograde amnesia due to exposure to alien radiation. The Player Character loses 1d6 years of memories as well as any skills acquired in this period.", 
            44: "A digestion problem causes the Player Character to develop a most severe and persistent flatulence problem. With a few rare exceptions, it imposes –1 DM to most social checks.", 
            45: "You spent a great deal of time this year working out and navigating difficult terrain. Gain +1 in any one physical ability.", 
            46: "Your professional duties have caused you to abandon your physical training, leaving you somewhat out of shape. Suffer –1 to any one physical ability.", 
            51: "Alien parasites start controlling the Player Character's body.",
            52: "Spending too much time in shoddy spacecraft exposes the Player Character to 3d6 X 10 rads. See page 141 in the Traveller Core Rulebook for more information on radiation.", 
            53: "Hypersomnia. The Player Character must sleep 18 hours per day or fall unconscious after 1d6 hours. Regardless of how much he sleeps, the character is fatigued all the time.", 
            54: "Exposure to alien radiation causes a radical change in the Player Character's cellular structure. Roll 1d6.\n 1: The character gains 200 radiation resistance.\n 2–3: The Player Character becomes resistant to high or low temperature.\n 4–6: The Player Character changes colour.", 
            55: "You spent a great deal of time this year working out and navigating difficult terrain. Gain +1 in any one physical ability.", 
            56: "Your professional duties have caused you to abandon your physical training, leaving you somewhat out of shape. Suffer –1 to any one physical ability.", 
            61: "A disruption of the digestive process causes the Player Character to gain the fast metabolism trait (see page 41 in the Traveller Core Rulebook).",
            62: "The Player Character contracts a sexually transmitted disease.", 
            63: "The Player Character is infected with an alien disease. Imperial medicine can battle the symptoms but not the cause of the disease.", 
            64: "Too much time in the pilot seat or the business table and too little exercise take their toll. Gain 10 kilograms.", 
            65: "The life of the traveller is hard and this year was exceptionally harsh. Lose 10 kilograms.", 
            66: "Some things even the high science of the Space Age cannot explain. Roll 1d6.\n 1: The Player Character's mood affects weather in a 20 km radius.\n 2: The Player Character does not have to sleep.\n 3: The Player Character gains complete resistance to all poisons and diseases.\n 4: The Player Character develops a random mutation (see page 164).\n 5: The Player Characters suffer –1d6 to a random attribute and an equal increase in another attribute.\n 6: The Player Character stops aging completely.", 
            }
    @staticmethod
    def getTravellerSupp9RandomEventBattlefieldEvents():
        return {
            11: "The group is hit by a laser beam shot from orbit. Each character must succeed on a 6+ Athletics (Co-ordination) check or take 6d6 of damage. If the Player Characters are inside a structure, roll 1d6.\n 1–3: Part of the structure collapses, leaving them exposed.\n 4–5: A fire erupts inside the building.\n 6: A single character is hit by debris, taking 2d6 of damage and getting buried under them.",
            12: "The group encounters animals fleeing from the city zoo.", 
            13: "The area is bombed from the air. Every exposed character takes 3d6 of damage and is deafened for an hour. Characters who were behind cover suffer –2 DM to all checks for 10 minutes.", 
            14: "The group comes under sniper fire. The sniper is hiding in a tall building and will continue firing at the Player Characters until he is disabled or the Player Characters leave his area of sight. He will aim at the highest ranking character, unless another character poses a direct threat to him.", 
            15: "Marauders looting the bodies of slain soldiers. They will not attack the Player Characters unless attacked first and would prefer flight to fight.", 
            16: "A military unit on the march (page 122).", 
            21: "A war reporter and her cameraman are looking for soldiers to interview. She is incredibly pesky and seems to be oblivious to the terrible danger she is in.",
            22: "A lynch mob consisting of 6d6 citizens is looking for minorities to brutalise. One in six has firearms. The mob will not hesitate to attack Player Characters who seem to be affiliated with the minority they are after.", 
            23: "An experimental battle robot whose computer was damaged by an electromagnetic discharge. The behemoth attacks everything and everyone in sight while shouting patriotic slogans and occasionally singing the national anthem.", 
            24: "A secret laboratory is bombed. See page 11 for more information on scientific mishaps.", 
            25: "Hundreds of civilian corpses lying in a ditch, all cut down by a single laser beam. A young and very polite boy is walking along the ditch repeating, 'excuse me, have you seen my sister? No? Maybe you saw her?'", 
            26: "A military unit on the march (page 122).", 
            31: "A dazed soldier wandering the battlefield, dragging his rifle like a broom and profusely bleeding from the side of his head.",
            32: "A huge rocket falls on the Player Characters but does not explode. If they are driving a vehicle, then the vehicle takes one double hit and they are trapped inside. If they are walking, then one Player Character takes 4d6+3 damage and is pinned under the rocket. Careless motions might set off the explosives, inflicting 6d6+3 damage in a 10 metre radius.", 
            33: "A swarm of hunter-killer robotic spiders on the prowl. They attack anyone without their side's military insignia.", 
            34: "D66 soldiers with dogs (or an alien equivalent of dogs) going house to house and arresting anyone hiding weapons or enemy combatants. Roll 1d6.\n 1–4: Non-allied combatants are taken to questioning.\n 5–6: Non-allied combatants are summarily executed.", 
            35: "A military aircraft carrying dozens of soldiers crashes about 100 metres from the Player Characters. Most of the soldiers are dead or heavily wounded. Roll 1d6:\n 1–3: No one arrives to rescue the survivors.\n 4: A civilian lynch mob shows up to kill and loot.\n 5: An enemy unit approaches to capture or kill any survivors.\n 6: An allied unit approaches to rescue survivors.", 
            36: "A powerful EMP hits the city, destroying all non-protected electronic devices and erasing all digital records. Characters with cybernetic augmentations may be injured as a result of the pulse.", 
            41: "A young woman with a baby is running to safety. Roll 1d6:\n 1–4: She is a normal woman. \n 5: She is a suicide bomber. \n 6: She is a killer robot disguised as a woman and programmed to take out enemies from close range. Being armed and not in uniform, the Player Characters qualify as enemies.",
            42: "An aircraft passes over the city, releasing poison gas into the air.", 
            43: "D66 peace activists are protesting the war. If the Player Characters are wearing uniform, they will be assaulted by the peace activists, who are armed with stones, clubs and knives. One death is enough to drive them away but this has a chance to be followed by a major media scandal and an Imperial investigation.", 
            44: "A group of half-naked civilians is crammed to an unmarked truck by soldiers in battle dresses but no rank insignia. Roll 1d6 to determine the soldier's commander:\n 1–2: A crazy scientist in search of test subjects.\n 3–4: A slaver and organ harvester exploiting the chaos of war.\n 5–6: A bigoted officer conducting a private massacre.", 
            45: "The group is attacked by a preteen boy armed with a plasma rifle. The boy will continue firing at the group until hurt or a more interesting target presents itself.", 
            46: "A military unit on the march (page 122).", 
            51: "A rocket hits a jewellery store a few hundred metres from the Player Characters, destroying the storefront and deactivating the alarm. Surprisingly, no one arrives to loot the store. Roll 1d6.\n 1–5: The store and the area are truly abandoned.\n 6: There is a defence drone inside the store.",
            52: "A man in an expensive but tattered business suit approaches the Player Characters and offers to pay them 25,000 Credits to help him get out of the city.", 
            53: "A nice old lady offers the Player Characters shelter in her home. If the Player Characters accept her invitation, they are ambushed inside by her son, a partisan commander who suspects they are working for the enemy.", 
            54: "News of the fighting reached the Imperial Court and the Emperor is not pleased. The sky grows crimson as hundreds of spacecraft carrying Imperial Star Marines land in the war torn city. The marines shoot everyone carrying arms.", 
            55: "The sky suddenly fills with purple and yellow fish that eat houses. At the same time, highly opinionated rats rise from the cellars and discuss the role of whiskers in modern society. Every Player Character sees something different. In an attempt to bring a bloodless end to the conflict, one of the sides has released hallucinogenic gasses into the air.", 
            56: "A military unit on the march (page 122).", 
            61: "A strange probe hovers over the Player Characters. It is amazingly durable and dexterous but does not seem to be aggressive. This is an automated news reporter. It is following the Player Characters because of their unusual behaviour, hoping to get a scoop.",
            62: "A long line of refugees is escorted out of the city by neutral peacekeeping forces. The Player Characters can join the group to leave the city. If they do, roll 1d6. On a roll of 6 the group is bombed (event 13) or lasered (event 11) from orbit.", 
            63: "A large scale shootout between two military units. Roll 1d6:\n 1–4: The Player Characters notice it from considerable distance.\n 5–6: The Player Characters walk right into the centre of the engagement.", 
            64: "The Player Characters see from a distance hundreds of soldiers from both sides as well as civilians stumbling about pointlessly, mumbling nonsense or playing stupid games. They were hit by a weapon that temporarily disrupts brain activity. A new pulse will affect the area in 1d6 minutes.", 
            65: "The massive fighting awakens an abomination (page 86) that lay dormant for centuries.", 
            66: "A nuclear bomb is dropped on the city from orbit.", 
            }
    @staticmethod
    def getTravellerSupp9MilitaryUnit():
        return {
            2: "Elite heavy infantry. These are the best-equipped, best-trained and most loyal soldiers in the service of any aristocrat or major corporation. They are equipped with battle dresses and advanced plasma and slug weaponry.",
            3: "Irregulars. Non-military people doing their part to aid the war effort, they are equipped with primitive weapons, wear no armor and fight without discipline. Use statistics for non combatants.",
            4: "Air Cavalry. Relatively slow-moving flying vehicles that can provide air support and transportation.",
            5: "Supplies. A non-combat unit moving supplies. A supplies unit is almost always escorted by a combat unit. Vital supply units can be escorted by several units.",
            6: "Automated soldiers. Roll 1d6. 1–5: drones, 6: robots.",
            7: "Mechanised infantry. Regular soldiers transported in armored personnel carriers.",
            8: "Field Artillery. Powerful but soft war machines capable of immense destruction. Usually equipped with massive rockets or plasma weapons.",
            9: "Combat engineers. Experts in sabotage, demolition, mining, de-mining and so forth.",
            10: "armored Cavalry. Heavy war machines that provide fire support. Not as powerful as the artillery but more manoeuvrable and defended.",
            11: "Air Force. Fast moving and high flying aircraft that provide intelligence and massive fire support. A single air raid could devastate a continent, although such drastic measures are rarely used.",
            12: "Mobile hospital. Just like the supply unit, the hospital is almost never found without an escorting combat unit."
            }
    @staticmethod
    def getTravellerSupp9RandomEventUrbanEvents():
        return {
            2:"Local Urban Event",
            3:"Local Urban Event",
            4:"Local Urban Event",
            5:"Local Urban Event",
            6:"Local Urban Event",
            7:"Local Urban Event",
            8:"Local Urban Event",
            9:"Local Urban Event",
            10:"Local Urban Event",
            11:"Local Urban Event",
            12:"Global Urban Event",
            }
    @staticmethod
    def getTravellerSupp9RandomEventLocalUrbanEvents():
        return {
            2:"Civil Unrest (page 9)",
            3:"Hostage Situation (page 10)",
            4:"Crime Spree (page 9)",
            5:"Scientific Mishap (page 11)",
            6:"Industrial Mishap (page 10)",
            7:"Surprising Discovery (page 12)",
            8:"Alien Visitors (page 9)",
            9:"Tournament (page 13)",
            10:"Festival (page 10)",
            11:"Accident (page 9)",
            12:"Chance Encounter (page 9)",
            }
    @staticmethod
    def getTravellerSupp9RandomEventLocalUrbanCivilUnrest():
        return {
            1: "Event 1 A gang of 2–12 angry demonstrators (use petty thug, Traveller Core Rulebook page 84) attacks the Player Characters with stones and sticks.",
            2: "The Player Characters are taken in for questioning by a group of 1–6 fully armed and armored riot policemen (use security officer 1, Traveller Core Rulebook page 84).",
            3: "A gang of 2D6 angry demonstrators (use petty thug, Traveller Core Rulebook page 84) attack the Player Characters with stones and sticks.",
            4: "The Player Characters are taken in for questioning by a group of 1–6 fully armed and armored riot policemen (use security officer 1, Traveller Core Rulebook page 84).",
            5: "A lone demonstrator is brutally beaten by a 4–9 policemen.",
            6: "A member of the group targeted by the demonstration is about to be lynched by an angry mob.",
            }
    @staticmethod
    def getTravellerSupp9RandomEventLocalUrbanAccidents():
        return {
            1:"A ferocious beast escapes from the zoo and runs about in the streets tearing to ribbons anyone who stands in its way. Rules for generating creatures are presented in page 69 of the Traveller Core Rulebook. Additionally, some ready-to-use monsters can be found on page 30.",
            2: "A defense turret suffers a software error and starts firing in all directions in the middle of a crowded street. Some people are stranded behind flimsy covers that will soon crumble under the deadly barrage of fire.",
            3: "A truck moving toxic waste overturns, spilling its load into the streets. A survivor climbed the roof of his car to escape the deadly flow but unless he is removed from there very soon, he will succumb to the deadly fumes. See pages 72–24 in the Traveller Core Rulebook for potential effects.",
            4: "Two cars collide and catch on fire. It seems that survivors, if any, will burn to death before help arrives. The Player Characters must act quickly and pull as many survivors as possible out the wreckage before it explodes.",
            5: "The lower levels of a skyscraper the Player Characters are visiting catch on fire. The fire rapidly moves up towards them, forcing them to think of some quick way to leave the burning building or perish in the flames.",
            6: "A boat collides with some debris and begins to sink with some survivors still inside.\n 1–4: The water is very cold but otherwise harmless. \n5: The water is highly toxic due to years of pollution.\n 6: Dangerous beasts live under water and attack passengers and rescuers.",
            }
    @staticmethod
    def getTravellerSupp9RandomEventLocalUrbanSurvivors():
        return {
            1: "The pregnant wife of an influential and grateful businessman.",
            2: "A Rival now turned Ally.",
            3: "As for previous only the Rival is not honest about his change of heart.",
            4: "A very humble man who insists on giving the Player Characters a significant monetary award that is likely to bankrupt him.",
            5: "A fugitive from the law (page 51).",
            6: "A man on a quest of personal vengeance or cosmic importance who succumbs to his wounds seconds after asking the Player Characters to finish his great mission.",
            }
    @staticmethod
    def getTravellerSupp9RandomEventLocalUrbanAlienVisitors():
        return {
            1: "The aliens are missionaries spreading an absolutely absurd religion no one even wants to hear about, which is a pity because their sacred texts contain many hints on the locations of priceless artefacts and ancient technology",
            2: "Under the guise of anthropologists in need of local guides (possibly the Player Characters), the aliens gather sensitive information about the city prior to a full-scale invasion. Player Characters that expose the aliens' true motives might very well save the city from annihilation by intimidating or giving false information to the aliens.",
            3: "The aliens are scions of a powerful family from a world the Imperium wishes to establish trade contacts with. They have diplomatic immunity which they abuse to its fullest, including wanton destruction, rape and murder. The Player Characters are hired by a grieving father to see that justice is done to his victimised daughter. Killing those disgusting brutes is likely to trigger an extensive manhunt after the Player Characters, as well as leading to diplomatic tension and possibly even war.",
            4: "The aliens came in search of warriors brave enough to participate in a series of death matches, the victor of which will become the aliens' king for the next 10 years.",
            5: "A small and incredibly advanced spacecraft crashes in the center of the city, killing all passengers on the spot. Within a few hours, a fleet of similarly advanced warships is spotted heading toward the city. Convinced their ambassador was murdered, the aliens came to avenge his death.",
            6: "An alien probe lands in the center of town and a public debate starts as to how to react to its arrival. Since the Player Characters are known to be experienced travellers, City Hall hires them as consultants.",
            }
    @staticmethod
    def getTravellerSupp9RandomEventAbsentPlayerActions():
        return {
            11: "Life Event (page 67). Re-roll in case of a hook.",
            12: "You get hit by a speeding vehicle while crossing the street, taking 5d6+3 damage. The number flees the scene of the incident. Roll 1d6.\n 1–3: You lie wounded by the side of the road until the party finds you.\n 4–5: A kindly but eccentric family takes you in and helps as much as it can. Gain them as Contacts and suffer –1 to any one physical attribute.\n 6: All the equipment you carry on your person is stolen.", 
            13: "You got food poisoning from something you ate on the street. Treat the poisoning as regina flu (page 73 in the Traveller Core Rulebook).", 
            14: "You spent all this time watching television and eating junk food. Gain 1d6 kilograms.", 
            15: "You ignored a red light and ran over a boy who was crossing the road. The boy was killed on the spot. The accident was witnessed by the boy's preteen sister. What did you do?", 
            16: "Urban Event (page 7).", 
            21: "Life Event (page 67). Re-roll in case of a hook.",
            22: "You went for a walk in the woods and stepped in a primitive trap. See page 166 for traps.", 
            23: "You were tricked into enlisting in the Imperial Navy. The ship leaves tomorrow. Deserters will be shot.", 
            24: "You fell into a deep and narrow hole in an alley no one ever visits. There is no reception in this hole. Youfear that as soon as you fall asleep the rats will eat you.", 
            25: "An enemy has decided to use the fact that you are finally alone to make his move. Roll Gun Combat 8+. If you fail, take 4d6 of damage and wake up in a hospital. Police are very curious why was someone shooting at you.", 
            26: "Urban Event (page 7).", 
            31: "Life Event (page 67). Re-roll in case of a hook.",
            32: "You were kidnapped by a local gang. It demands a 50,000 Credits ransom for your release. The group has one week to come up with this money or you will be murdered.", 
            33: "You fell for a clever scam and lost 1d6 X 1,000 Credits.", 
            34: "You had an online argument with a stranger who turned out to be incredibly vindictive and mentally unbalanced. Gain an Enemy.", 
            35: "You had a hot date that ended in bed. Roll 1d6: 1–2: The date steals 1d6 X 100 Credits or a random item. 3–4: The date is the child of a local gangster known for his conservative family values and harsh enforcement of aforementioned values. 5–6: The date is murdered the next morning and you are arrested for the murder.", 
            36: "Urban Event (page 7).", 
            41: "Life Event (page 67). Re-roll in case of a hook.",
            42: "You wake up naked a few miles outside the city. You are hugging a large dog and have 'killer' written on your forehead with lipstick. You have no recollections of what happened in the last few days.", 
            43: "You have an Unusual Event (page 34 in Core Rulebook).", 
            44: "You beat up a bunch of rich kids who assaulted a young woman returning alone from work late at night. The next day, you hear on the news that the police is looking for a thug who attacked the Duke's son and his friends.", 
            45: "You were invited to a fancy party at the duke's palace. Roll Carouse 8+. If you succeed, gain 1d3 Contacts. If you fail, you are challenged to a duel by an Aslan diplomat.", 
            46: "Urban Event (page 7).", 
            51: "Life Event (page 67). Re-roll in case of a hook.",
            52: "You accidentally broke a taboo while strolling in an Aslan neighborhood and must now flee an angry mob. Roll Stealth, Streetwise or Persuade 8+. If you fail, reduce any one Physical Characteristic by one. You may no longer safely enter this neighbourhood.", 
            53: "You had a fight with an old friend and ended up deeply hurting his feelings. Despite your attempts to make amends, he has no desire to ever talk with you again. Lose an Ally. If you do not have an Ally, gain a Rival.", 
            54: "You got into a bar fight and were arrested for disorderly conduct. The other Player Characters can bail you out for 1d6 X 100 Credits. If not bailed out, you spend about a week in jail. In any case, you are fined 500 Credits.", 
            55: "You find an ancient artifact in a trash bin in the street. As soon as you touch it, it fuses with your brain. From now on, every time you see a person of a certain type known only to the device, you lose control over your body and attack them. Removing the artefact would require a very expensive and dangerous neurosurgical procedure.", 
            56: "Urban Event (page 7).", 
            61: "Life Event (page 67). Re-roll in case of a hook.",
            62: "You found an injured kitten and spent a week nursing it back to health. Roll 1d6. 1–4: The kitten has made a full recovery, gain a cat. 5–6: The kitten died despite your best efforts.", 
            63: "During routine maintenance, you managed to ruin a weapon, armor or vehicle.", 
            64: "Alone and bored, you experimented with drugs of questionable origins. Roll 1d6. 1–3: You had a good time. 4–5: You gained a drug addiction. 6: The drug damaged your brain; suffer –1 to any one mental attribute.", 
            65: "You find yourself walking in the woods, both your hands smeared in blood and some unidentified chemical. You do not remember what happened but every night for the following six months you wake up screaming and sobbing.", 
            66: "You wake up on a planet many parsecs away. The last thing you remember is a strange man in a pub asking you if you would like to see a magic trick.", 

        }
    @staticmethod
    def getTravellerSupp9FootChase():
        return {
            11: "Freakishly bad weather appropriate for the environment.",
            12: "A peddler drags his cart right in front of the Player Characters. They must either run around it, losing precious time, or attempt to jump over it with a Difficult Athletics (Co-ordination) check.", 
            13: "The area is crowded with alien tourists. Movement is slowed down by three quarters and both Player Characters and target gain +2 DM to Stealth checks.", 
            14: "Electrical work is being done in the area. Each character passing through must make Athletics (Coordination) check or be hit by an electrical grid (see page 168).", 
            15: "The escapee runs into a dead-end alley with high walls. He cannot escape.", 
            16: "A long vehicle such as a train or a tram passes between the chaser and the escapee, giving the escapee a chance to gain a considerable distance over his chasers.", 
            21: "A mentally unbalanced man pulls out a knife and starts chasing the character.",
            22: "A mentally unbalanced man pulls out a firearm and starts chasing the character.", 
            23: "Chaser and escapee get mixed up in an Aslan funeral procession. The mourners are drunk, angry and armed. One wrong move and there will be another funeral today.", 
            24: "A natural disaster (15) occurs in the middle of the chase.", 
            25: "The escapee runs into a dead-end alley with high walls. He cannot escape.", 
            26: "A long vehicle such as a train or a tram passes between the chaser and the escapee, giving the escapee a chance to gain a considerable distance over his pursuer.", 
            31: "You step on the foot of a very large and hot-headed Vargr/Alien thug.",
            32: "You run into a peaceful demonstration protesting the increase in spaceflight fares. There are tens of thousands of civilians and hundreds of armed policemen in the square. Spotting the escapee is a Difficult task.", 
            33: "A kindly old lady accidentally drops a vase from a high window. The vase lands on someone's head, inflicting 1d6 damage and dazing the victim for one round.", 
            34: "A few dozen street animals join the chase. Their intentions are unclear. 1–4: They are just running for fun. 5: They will attack the chasers. 6: They will attack the escapee.", 
            35: "The escapee runs into a dead-end alley with high walls. He cannot escape.", 
            36: "A long vehicle such as a train or a tram passes between the chaser and the escapee, giving the escapee a chance to gain a considerable distance over his chasers.", 
            41: "A sign saying 'careful, slippery floor'. For the next 50 metres, running for a round without tripping becomes a Routine Athletics (Co-ordination) task.",
            42: "Six policemen are drinking coffee in the street. Wild running or driving will cause them to call backup and join the pursuit.", 
            43: "Escapee suddenly grows wings and flies into the sky. Re-roll if the Player Characters are the escapees.", 
            44: "An old friend of the Player Characters walks out of a building just as the Player Characters pass by.", 
            45: "The escapee runs into a dead-end alley with high walls. He cannot escape.", 
            46: "A long vehicle such as a train or a tram passes between the chaser and the escapee, giving the escapee a chance to gain a considerable distance over his chasers.", 
            51: "The weather suddenly takes a turn for the worst. All Recon and Athletics checks suffer a –2 DM.",
            52: "A police vehicle joins the pursuit.", 
            53: "The escapee runs into one or more allies.", 
            54: "An important device such as a vehicle or a weapon malfunctions. Roll 1d6. 1–3: The device belongs to the chasers. 4–6: The device belongs to the escapees.", 
            55: "The escapee runs into a dead-end alley with high walls. He cannot escape.", 
            56: "A long vehicle such as a train or a tram passes between the chaser and the escapee, giving the escapee a chance to gain a considerable distance over his chasers.", 
            61: "The escapee runs into a dead-end alley with high walls. It appears he cannot escape but in the last moment he pulls a jetpack from a trash canister and flies away. Re-roll if the Player Characters are the escapees.",
            62: "A teenager notices the chase and takes pictures of all involved.", 
            63: "The pavement was scraped off and workers are currently at work laying a new pavement, make the ground highly uneven. Each character running in the area must succeed on a Routine Athletics (Co-ordination) check or sprain an ankle, reducing their speed to 1 for a minute.", 
            64: "The escapee runs into a dead-end alley with high walls. He cannot escape.", 
            65: "A long vehicle such as a train or a tram passes between the chaser and the escapee, giving the escapee a chance to gain a considerable distance over his chasers.", 
            66: "A passer-by is knocked off a bridge or down a shaft, dying on the spot. Roll 1d6. 1–2: The event was recorded on camera, 3–5: The event was witnessed by passers-by. 6: No one saw this.", 
            }
    @staticmethod
    def getTravellerSupp9AncientArtifacts():
        return {
            11: "A fully functional time machine that enables precise time travel both into the past and the future.",
            12: "A fully functional time machine that enables precise time travel only into the future.", 
            13: "A fully functional time machine that enables precise time travel only into the past.", 
            14: "A malfunctioning time machine that hurls the user into a random point in time and space.", 
            15: "A time machine that affects its occupants. For example, traveling five years into the future causes the user to age five years.", 
            16: "Black globe generator.", 
            21: "An acceleration chair that protects travellers from gravity changes created by high acceleration.",
            22: "Black hole generator. Can destroy entire planets from orbit.", 
            23: "A sarcophagus-like device that can cure any injury or disease in a matter of seconds.", 
            24: "As for previous, only patients gain a random mutation (see page 158) each time they use the device.", 
            25: "A toothpick.* (While no more advanced than its earth counterpart, this device can be sold for millions of Credits to collectors or museums.)", 
            26: "Black globe generator.", 
            31: "A device which safely enables moving planets across the galaxy.",
            32: "An artificial planet with complete gravity, weather and rotation control.", 
            33: "As for previous, only the artifact is a star system and not a single planet.", 
            34: "A door frame*. (While no more advanced than its earth counterpart, this device can be sold for millions of Credits to collectors or museums.)", 
            35: "A door mat. The inscription on it reads, 'wipe all feet'.* (While no more advanced than its earth counterpart, this device can be sold for millions of Credits to collectors or museums.)", 
            36: "Black globe generator.", 
            41: "A hyperspace communication device.",
            42: "An antimatter drive which can power a large ship indefinitely. It cannot be reverse-engineered but it can be converted to an antimatter bomb.", 
            43: "A dormant killer machine. Roll 1d6. 1–3: The machine turns on as soon as it is powered. 4–5: The machine turns on if given a command in its language. 6: The machine turns on as soon as it comes in contact with biological matter.", 
            44: "A sculpture of a strange, tentacled humanoid.* (While no more advanced than its earth counterpart, this device can be sold for millions of Credits to collectors or museums.)", 
            45: "A small portable wormhole generator. See page 43 for more information on wormholes.", 
            46: "Black globe generator.", 
            51: "A device which can detect brain waves and play tunes suitable for the general atmosphere in the room.",
            52: "A normal stove.* (While no more advanced than its earth counterpart, this device can be sold for millions of Credits to collectors or museums.)", 
            53: "A robotic pet. The creature is clearly mechanical and highly adaptable; it learns the Player Characters' language in a matter of days and serves as a faithful, although terribly obsolete adviser.", 
            54: "A robotic pet the 'creature' is clearly mechanical and highly adaptable; it learns the Player Characters' language in a matter of days and serves as a faithful, although terribly obsolete adviser., only the pet has a sinister ulterior agenda, such as leading the Player Characters to an ancient dormant killing machine.", 
            55: "A city that can walk across the planet on thousands of powerful robotic legs. Unless given a new command, it will move between two set seasonal positions.", 
            56: "Black globe generator.", 
            61: "A memory device containing the recorded personalities of Ancient. Roll 1d6. 1: Politicians. 2: Criminals. 3–4: Normal people. 6: Slain heroes.",
            62: "Window cleaning nanobot. Roll 1d6. 1–5: The bots need a power source to work. 6: The bots begin working as soon as they identify a window.", 
            63: "A ceremonial sword.* (While no more advanced than its earth counterpart, this device can be sold for millions of Credits to collectors or museums.)", 
            64: "Personal teleportation device. Roll 1d6. 1–2: The device induces a random mutation or disease due to being unfamiliar with non-ancient anatomy. 3–4: The device tends to miss its target by a 6d6 metres in a random direction. 5: The device functions perfectly. 6: The device has a set location hundreds of parsecs away.", 
            65: "Universal lie detecting probe. Whenever a person says something he does not believe in, including making a sarcastic or ironic remark, he is zapped for 1d3 damage.", 
            66: "Black globe generator.", 
            }
    @staticmethod
    def getSupplement16DramaticSituations():
        return {
            11: "A Cry for Help - You need: Three characters – one who needs aid, one who can provide it (perhaps one of the players), and one threatening the first. Example: Peasants ask the players to protect them against the annual visit of a corsair group.",
            12: "Deliverance - You need: Two characters – a victim and a rescuer – and a threat (which might be a third character, natural disaster, etc.). Example: One of the group’s Non-Player Character followersm is condemned to death for breaking a petty local law; the players must rescue him and flee offworld.", 
            13: "Revenge for a Crime - You need: Two characters – a perceived criminal and an avenger. Example: Travellers abducted and murdered a local nobleman’s daughter years ago, and he now revenges himself by harassing any travellers (perhaps the players) entering his domain.", 
            14: "Revenge for a Relative’s Death - You need: Three living characters – the guilty party, the avenger, and someone who is a relative of both – and information about the dead person. Example: The patron’s mother died in an air/raft accident some months ago; he blames his estranged father for her death, and hires the players to embarrass or kill his father. However, during their investigations they encounter the patron’s uncle, who has proof that the death was accidental.", 
            15: "Pursuit - You need: A fugitive character, and a punishment he is trying to escape. Example: The patron is a fugitive who stows away on the players’ ship to avoid execution for murder. If the players help him, he has information or skills of value to them, but they will be pursued by local police unless they can prove his innocence.", 
            16: "Disaster - You need: Two characters – the victim/loser, and either a victor or a messenger. Example: The patron’s children are missing after their air/ raft crashed in dense jungle. The players must heroically overcome savage wildlife or natives, and rescue the children.", 
            21: "Cruelty or Misfortune - You need: An unfortunate victim, and either a misfortune or a cruel opponent. Example: The players stumble upon an attempted murder, and rescue a naive young noble. Investigation will reveal that the noble is threatened by intrigue within his family, as an evil aunt is trying to kill him so that her own son may inherit the family estate.",
            22: "Revolt - You need: Two characters – a tyrant and a conspirator against the tyrant. Example: The players are recruited by freedom fighters seeking to overthrow a local warlord.", 
            23: "Daring Enterprise - You need: A goal, and two characters – a leader and an adversary. Example: The players are a mercenary commando unit hired to destroy the surface sensors for a deep meson gun site, thus allowing their patron’s fleet to attack the planet safely. Their adversaries are the installation’s guards.", 
            24: "Abduction - You need: Three characters – a kidnapper, a victim, and a guard. Example: The band are employed as bodyguards for an heiress. Brigands attempt to kidnap her for ransom.", 
            25: "Enigma - You need: A puzzle; someone to pose it; and someone trying to solve it. Example: Marooned after their vehicle crashes, the players are captured by primitives who will kill them as trespassers unless they can solve a riddle set by the tribal shaman.", 
            26: "Obtaining - You need: A goal, and two or three characters – one trying to attain the goal, his adversary, and (optionally) an arbitrator to decide who wins. Example: Faced with deportation for vagrancy, the players must plead their case before a magistrate against the legal official seeking to deport them. They must trick, bribe or otherwise persuade him to let them stay.", 
            31: "Feud - You need: Two characters, at least one of whom hates the other. Example: The patron hires the players to discredit a hated sibling whom he feels stands to benefit unfairly from their parents’ will; this will cause the family to change the will in the patron’s favour.",
            32: "Rivalry - You need: Two characters, and something or someone they both want. Example: The patron has been jilted by his girlfriend, who prefers a mutual friend. Sure that he can regain her affection if he proves himself a warrior, he hires the players to attack the girl and her lover, humiliate them, and flee when he arrives to defend her.", 
            33: "Murderous Adultery - You need: Two adulterers and a betrayed spouse. Example: The patron has discovered her husband with his mistress, and has killed them both in a fit of passion. Knowing one of the players, she appeals to them to cover up the murder and distract the police from her.", 
            34: "Madness - You need: A madman and their victim. Example: The patron is being stalked by a madman for no apparent reason. The authorities are unwilling to act, as stalking itself is not a crime locally. The patron hires the players to protect her, and find out why she is being stalked.", 
            35: "Imprudence - You need: Someone to be imprudent; someone or something to be lost or destroyed as a result. Example: Wandering into his father’s laboratory, the patron has unleashed a dangerous animal which has killed his father and several neighbours. The band must hunt down this cunning predator and capture or kill it.", 
            36: "Involuntary Crimes of Love - You need: A lover, a beloved, and someone to reveal to them that their love is taboo. Example: A noble wishes to marry, and the players are employed by his parents to investigate his fiancée’s background to ensure that she is not simply marrying him for money. The investigation reveals that she is the noble’s long-lost sister, raised as an orphan by traders who found her on a battlefield.", 
            41: "Involuntary Kinslaying - You need: A killer, and a close relative for him to kill. Example: The party are aboard ship when the cargo bay is holed. To save the passengers, the captain orders it sealed off, but to his horror he learns that his son is still inside. Unable to leave the bridge, or reopen the doors without killing others, he appeals to the party to effect a rescue.",
            42: "Sacrifice for an Ideal -  You need: An ideal, the hero, and (optionally) someone or something for him to sacrifice instead of his own life. Example: The players are in a government office when it is seized by terrorists, who threaten to kill everyone inside unless an official (responsible for the deaths of many of their comrades) surrenders himself to them. To save the innocent bystanders, the government agrees. The players must neutralise the terrorists before they can kill the official.", 
            43: "Sacrifice for Kin - You need: A hero, a kinsman to sacrifice for, and (optionally) someone or something for him to sacrifice instead of his own life. Example: The players are the crew of the last ship taking refugees away from a war zone. A passenger offers to give up his place so that his pregnant sister can have it; the players must either think of a way to carry one more person than their life support is good for, or leave someone behind to face certain death.", 
            44: "Sacrifice for Passion - You need: A lover, the object of desire, and (optionally) someone or something for the lover to sacrifice instead of his own life. Example: The patron is a priest of the local religion, prepared to forfeit position and career for the love of a crew member aboard the players’ ship. He begs to be smuggled offworld. Unfortunately, this carries the death penalty for the priest and all who aid him.", 
            45: "Sacrificing a Loved One - You need: A hero, a beloved victim, and a reason for the sacrifice. Example: Terrorists have seized the children of the local governor, and threaten to kill them unless he releases other terrorists from jail. The players must neutralise this threat as the governor cannot afford to be seen to give in to the terrorists.", 
            46: "Rivalry - You need: Two rivals (of equal or differing power/ability) and something they both want. Example: The patron is one of two brothers whose father has recently died; each thinks he should inherit the family estates. The will favours the patron’s brother, a suspected psionic; the band are hired to prove that he misused his alleged powers to have the will altered in his favour, which would render it void.", 
            51: "Adultery - You need: Two lovers, and a deceived spouse. Example: The patron married for money, but is having an affair with a younger and better-looking partner. The players are hired to provide an alibi for the patron’s absences from home.",
            52: "Forbidden Love - You need: A lover, a beloved, and a reason why this love is forbidden. Example: The patron suspects that her noble daughter is involved with a ‘mere worker’ – going against strict local tradition. She enlists the players to deter the worker from seeing the daughter.", 
            53: "A Loved One Dishonored - You need: A guilty party, and one who discovers their dark secret. Example: The patron is a senior official who suspects that his wife, an offworlder, is a spy who has married him to gain easy access to his homeworld. He hires the band to travel to her homeworld and check her history and parentage.", 
            54: "Obstacles to Love - You need: Two lovers, and an obstacle. Example: An Non-Player Character wants to join the party, hoping to make enough money to marry his sweetheart, whose family insist he be “able to support her properly”.", 
            55: "An Enemy Loved - You need: Two lovers who should be enemies; someone who hates one of them as the enemy. Example: The patron is a police officer who has fallen in love with a member of a terrorist group he is infiltrating. His police superiors are laying a trap which will kill or capture the group. He hires the players to stop his loved one from reaching the rendezvous so that she will escape the trap.", 
            56: "Ambition - You need: An ambitious person; something he wants; an adversary. Example: The patron is a rising executive in a megacorporation; he wants to take over the subsector office, and hires the players to find something he can use to blackmail or discredit the current subsector manager.", 
            61: "Conflict with an Immortal - You need: A mortal and an immortal. Example: The players must make a trade agreement with low-tech natives. On arrival, they find that they cannot do so unless they convince the local priesthood that they are accepted by the local god. This requires the players to succeed in a number of ordeals.",
            62: "Mistaken Jealousy - You need: A jealous person; someone for them to be jealous of (and a reason for it); the cause of the mistake. Example: An arms merchant suggests to each of two neighbouring communities that the other plans an attack, to increase his sales. The merchant hires the players to escort his deliveries but they quickly realise neither community is aggressive.", 
            63: "Mistaken Judgement - You need: A mistaken person, guilty and innocent suspects, and the cause of the mistake. Example: After criminals hide contraband in their luggage, the players are accused of smuggling.", 
            64: "Remorse - You need: A guilty party, a victim or a crime, and an investigator. Example: The patron hires the players to find out what his recently-deceased father did with the missing family fortune. It transpires that the father was consumed with remorse for those he killed while in military service, and donated the money to charities helping the survivors.", 
            65: "Recovery of a Lost One - You need: A seeker, and someone to find. Example: The patron hires the players to find an offworlder with whom she had an affair several years ago; her husband has since died and she is now free to re-marry. She can provide holograms of her lover and his last known location.", 
            66: "Losing Loved Ones - You need: A killer, a victim, and a witness. Example: The players are requested to act as agents for a patron in a business deal with a rich client. The patron was involved in the car accident which killed the client’s daughter and thus dare not reveal his identity to the client.", 
            }
    # ============================================================
    @staticmethod
    def getTravellerCoreTraderSpacecraftQuirks():
        return {
            2: "Black-listed: Trader will be impounded in several systems. DM-1 to all Broker checks.",
            3: "Well maintained: Reduce all maintenance costs by 50%",
            4: "Vessel contains concealed smuggling compartments.", 
            5: "Cargo bay is tainted by chemical spills and leaks. Vulnerable cargoes may be damaged in transit.",
            6: "Damaged sensors: DM-1 to all Electronics (sensors) checks",
            7: "DM-1 to all repair attempts",
            8: "Double maintenance costs",
            9: "Severely Damaged: -10% Hull",
            10: "Damaged thrusters: DM-1 to all Pilot checks",
            11: "Ship is a famous and respected trader, with a good reputation.",
            12: "Upgrade computer to next best type",
        }
    @staticmethod
    def getTravellerCoreMilitarySpacecraftQuirks():
        return {
            2: "Severely Damaged: -1 Hull.",
            3: "Upgrade sensors to next best type.",
            4: "Vessel is equipped with an extra turret, if possible.", 
            5: "Vessel was involved in a notorious battle, and has enemies who wish to destroy it.",
            6: "Damaged sensors: DM-1 to all Electronics (sensors) checks",
            7: "DM-1 to all repair attempts",
            8: "Double maintenance costs",
            9: "Severely Damaged: -10% Hull",
            10: "Damaged thrusters: DM-1 to all Pilot checks",
            11: "Ship served with distinction, and has a good reputation in the navy.",
            12: "Add a weapon costing up to MCr2",
        }
    @staticmethod
    def getTravellerCoreOtherSpacecraftQuirks():
        return {
            2: "Leaky Reactor Core: Roll 2D when the ship jumps. On a 12, all crew suffer 2D x 20 rads.",
            3: "Luxurious starship: DM+1 to all Steward checks",
            4: "Library computer contains erroneous information.", 
            5: "Vessel contains disturbing psionic echoes.",
            6: "Damaged sensors: DM-1 to all Electronics (sensors) checks",
            7: "DM-1 to all repair attempts",
            8: "Double maintenance costs",
            9: "Severely Damaged: -10% Hull",
            10: "Damaged thrusters: DM-1 to all Pilot checks",
            11: "Library computer contains secret or unusual information.",
            12: "Upgrade sensors to next best type",
        }
    # ============================================================
    @staticmethod
    def getLifeEventMasterCampaignGuide():
        return {
        1: "Life Events: Friends, Family and Lovers",
        2: "Life Events: Friends, Family and Lovers",
        3: "Life Events: Innermost Self",
        4: "Life Events: Hooks",
        5: "Life Events: Hooks",
        6: "Life Events: Hooks",
        }
    @staticmethod
    def getLifeEventFriendsFamilyLoversCampaignGuide():
        return {
            11: "A Player Character is confronted by a woman who claims that he is the father of her child.",
            12: "As for previous (A Player Character is confronted by a woman who claims that he is the father of her child.)), only the Player Character has never seen the woman in his life and yet tests show that the child is really his.", 
            13: "A person one of the Player Characters is dating turns out to be controlled by an alien organism. Who is it that the character fell in love with, the person or the alien? What does the alien want? Why was the character chosen of all people?", 
            14: "A Player Character reunites with a long-lost pet, now an uplifted animal actually smarter than his previous owner.", 
            15: "One of the Player Characters' younger brother comes of age and insists on joining a very dangerous expedition. If banned, he sneaks into the ship and hides in a crate until it is too late to turn back.", 
            16: "The Player Character's parents go out of their way to make their son or daughter an interstellar success story, including signing deadly mission contracts in their name and spreading outrageous rumours about his exploits.", 
            21: "The Player Characters are hired to investigate a secret slavers ring only to find out that it is run by one of their favorite uncles.",
            22: "The group protects a relative or spouse of one of the Player Characters from mysterious and powerful assassins who hunt him all over space. Slowly, it turns out that the hunted person has done horrible things on the scale of war crimes or serial killing in his past.", 
            23: "A Player Character's spouse commits suicide while he is away on a mission. There is neither a suicide note, nor a clear cause for this tragic death.", 
            24: "As for previous (A Player Character's spouse commits suicide while he is away on a mission. There is neither a suicide note, nor a clear cause for this tragic death.), only the Player Character's enemies use the opportunity to frame him for the 'murder'.", 
            25: "A Player Character's great-grandfather dies and leaves behind an extremely bizarre testament, bequeathing all his possession to whoever completes a series of strange missions.", 
            26: "As for previous (A Player Character's great-grandfather dies and leaves behind an extremely bizarre testament, bequeathing all his possession to whoever completes a series of strange missions.), only these seemingly random missions are in fact designed to re-activate an ancient death machine the deranged old man believed to be a dead god. This can be deduced from his cryptic diary.", 
            31: "A Player Character's new father-in-law is an eccentric but brilliant engineer who keeps coming up with devices that are as likely to save his life as they are to disintegrate him. He tends to forget mentioning the second half of the deal to Player Characters.",
            32: "A Player Character's spouse or child have become heavily indebted to the sort of people who believe that if one cannot set a good example of paying on time, one should become a horrible warning.", 
            33: "A Player Character's estranged father is a brutal tyrant responsible for heinous war crimes and heading one of the most oppressive regimes in the galaxy. Despite the Player Character having nothing to do with his father's crimes, he may still find himself the target of unwanted media attention or vengeful dissidents.", 
            34: "Memories of an abusive father suddenly begin to disturb a Player Character's dreams. The memories progress nightly, revealing the gentle and loving father is in fact a monstrous deviant.", 
            35: "As for previous (Memories of an abusive father suddenly begin to disturb a Player Character's dreams. The memories progress nightly, revealing the gentle and loving father is in fact a monstrous deviant.), only the memories were planted by the Player Character's enemies.", 
            36: "Two Player Characters find out they are siblings.", 
            41: "The Player Character's twin brother is an infamous womanizer and scoundrel. His ill reputation keeps harming the Player Character's career.",
            42: "When the smoke of a bloody battle with pirates clears, the Player Character finds among the dead his beloved kid brother whom he encouraged to go into space and make something of himself.", 
            43: "One Player Character discovers that another Player Character has killed someone very close to him (such as a parent or a sibling) many years ago.", 
            44: "An old friend from a Player Character's wilder days informs them that a mutual friend was killed by the Aslan mafia. The man is gathering the old gang for retaliation against the Aslans.", 
            45: "A Player Character receives a message from home informing him that a suitable wife has been found for him and that he is to return for the marriage ceremony as soon as possible. Refusal will result in a scandal, loss of family financing and possibly contacts or allies.", 
            46: "A Player Character's wife turns out to be his sibling.", 
            51: "Same as previous (A Player Character's wife turns out to be his sibling.), only the discovery is a plot by the Player Character's enemies.",
            52: "A distant relative dies, living a huge inheritance for a Player Character to collect. While huge, the inheritance is largely useless, basically being a colossal collection of junk. Still, it is possible some interesting items found their way into the massive heap as well.", 
            53: "Same as previous (A distant relative dies, living a huge inheritance for a Player Character to collect. While huge, the inheritance is largely useless, basically being a colossal collection of junk. Still, it is possible some interesting items found their way into the massive heap as well.), only there is no inheritance, this is a plot by the Player Character's enemies to lure him into a trap.", 
            54: "Same as event 52 (A distant relative dies, living a huge inheritance for a Player Character to collect. While huge, the inheritance is largely useless, basically being a colossal collection of junk. Still, it is possible some interesting items found their way into the massive heap as well.), only the relative is not dead, just wants to speak of some important matter. He believes this is the only way to lure in his estranged relative.", 
            55: "Same as event 52 (A distant relative dies, living a huge inheritance for a Player Character to collect. While huge, the inheritance is largely useless, basically being a colossal collection of junk. Still, it is possible some interesting items found their way into the massive heap as well.), only receiving the inheritance requires the completion of a mission... and there is competition from other relatives.", 
            56: "A friend or a relative commits suicide after a personal tragedy. The note only says 'UPGRADE'. Investigation will reveal the man has uploaded his conscience into an android and went about killing the people he considers are responsible for the tragedy.", 
            61: "A childhood friend of a Player Character has received an e-mail from Chatter saying 'big misteak, now i koleckt'. Well aware of the crazed killer's reputation, the friend hysterically calls the Player Characters to come and protect him. This is most probably a hoax and the man is wasting the group's time.",
            62: "Natives have eaten a Player Character's anthropologist sibling. Another sibling, a bookish and harmless person, is obsessed with avenging the anthropologist's death. If left to his own devices, he will not survive a day in the alien wilderness that claimed the anthropologist's life.", 
            63: "Same as previous, only the sibling was not eaten but has gone native and joined the tribe. After many years of separation, combined with the natives' tattoos and body modification rituals, it is likely the Player Character will not be able to recognise his sibling at first sight.", 
            64: "A Player Character accidentally runs into a long-lost sibling or child, a pathetic homeless junkie willing to do anything for his next fix.", 
            65: "The Player Character meets a kid who is suspiciously similar to him. The kid grew in an orphanage and never knew his mother. He can't tell his exact age either.", 
            66: "While exploring an alien wilderness, the Player Character encounters his childhood pet... who has been dead for more than a decade.", 
            }
    @staticmethod
    def getLifeEventInnermostSelfCampaignGuide():
        return {
            11: "Assassins are after the character for damage done to their organization years ago.",
            12: "Same as previous (Assassins are after the character for damage done to their organization years ago.), only this is a case of mistaken identity.", 
            13: "Shadowy monsters the Player Character used to have nightmares about as a child start reappearing. This time they are real, tangible and murderous.", 
            14: "A Player Character wakes up one morning, feeling a body part is no longer his own. After 1d6 days the body part begins to act autonomously and a new body part feels alien. 1–3: This is a psychological condition. 4–6: This is an alien virus.", 
            15: "Records show the Player Character has been dead for more than 13 years.", 
            16: "An arrest warrant is issued for a crime the Player Character has committed more than two decades ago while intoxicated.", 
            21: "The Player Character's ex-wife or ex-girlfriend appears with a court order ordering him to pay her exuberant retroactive alimonies.",
            22: "A combat wound reveals a horrible secret; the Player Character is not a human being but an alien replica. What happened to the original and does the Player Character really want to be replaced by his 'real self'?", 
            23: "As for previous (A combat wound reveals a horrible secret; the Player Character is not a human being but an alien replica. What happened to the original and does the Player Character really want to be replaced by his 'real self'?), only the Player Character is a robot that can be turned off by its operators any minute.", 
            24: "A Player Character begins to slowly transform into a hideous mutant (page 164). Apparently, his mother was not perfectly honest with him about his father's identity.", 
            25: "A Player Character feels compelled to go to a faraway unexplored planet. Once there, he discovers he was injected with alien genes as part of an experiment by the aliens.", 
            26: "Same as previous (A Player Character feels compelled to go to a faraway unexplored planet. Once there, he discovers he was injected with alien genes as part of an experiment by the aliens.), only the aliens are not interested in mere observation or family reunions. They want the character to go back and steal weapons and secrets for them.", 
            31: "A female character discovers she is pregnant. 1–5: The baby is normal. 6: There is something wrong with the baby.",
            32: "The Player Character begins to have vile and perverse urges. Occasionally the urges will become so strong that the character will have no choice but to act according to them. The situation will persist until the Player Character discovers the trauma that caused this condition and deals with it.", 
            33: "Strange events happening to a Player Character begin to shake his confidence in the reality of the world around him. Investigation will reveal the character is an alter-ego created by a powerful psion lying in a coma in a distant hospital.", 
            34: "Chatter (page 159) is after the Player Character. Although the maniac is still many light years away, everyone is already talking about the character in past tense.", 
            35: "A review by an institute the Player Character attended finds out he never graduated and thus is not qualified to use one of his skills.", 
            36: "The Player Character contracts an exotic disease (page 108).", 
            41: "The Player Character begins to experience regular hallucinations. 1–3: He was poisoned. 4–6: An alien being is trying to communicate with him.",
            42: "The Player Character has a sudden urge to swim in space. This urge intensifies to the point of the Player Character having to be restrained. The reason is a colossal alien (page 35) who wants to form a symbiotic bond.", 
            43: "A prestigious news network is shooting an episode about travellers and one of the Player Characters is invited for an interview. Some of the questions asked will touch upon subjects the Player Character would rather have remained hidden.", 
            44: "Player character wakes up in a coffin, buried alive by his enemies. His friends only have a few hours to rescue him before he suffocates to death.", 
            45: "A bump to the head causes the Player Character to experience temporary amnesia.", 
            46: "The Player Character starts receiving ominous messages from a person he killed a few months ago. 1–3: The man had a pirate brother. 4–6: The man uploaded his personality to his computer a few weeks before his death.", 
            51: "While exploring the graveyard of a remote alien village, the Player Character notices a gravestone bearing his name and birth date. The death date is today.",
            52: "The Player Characters have the same continuous dream each night. As time passes, it becomes less and less clear which life is real and which one is dreamed.", 
            53: "The Player Character begins to slowly turn into a cockroach. No one else notices the gruesome transformation. 1–3: This is the result of mental illness. 4–6: A psionist is playing with the Player Character's mind.", 
            54: "Ancient aliens possess the Player Character (page 14).", 
            55: "The Player Character begins to have flashbacks of himself committing horrible crimes. This is especially alarming since the flashbacks seem to take place in a time the character was doing a lot of drugs and was not aware of many of his actions.", 
            56: "An ally and a good friend of the Player Character is accused of crimes the Player Character has committed.", 
            61: "The Player Character discovers his greatest enemy is his biological father.",
            62: "Same as previous (The Player Character discovers his greatest enemy is his biological father.), only this is a baseless rumor.", 
            63: "The Player Character discovers that alien parasites lodged into his brain are responsible for many of his decisions over the years.", 
            64: "The Player Character is diagnosed with a debilitating condition such as multiple sclerosis or chronic fatigue syndrome.", 
            65: "A fortune teller at a festival examines the Player Character's palm, becomes visibly shaken and then runs away screaming 'the end is nigh'!", 
            66: "The Player Character becomes insanely attracted to someone inappropriate. 1–2: A commander or patron. 3–4: An alien with a very different anatomy. 5–6: A hated enemy.", 
            }
    @staticmethod
    def getLifeEventHooksCampaignGuide():
        return {
            11: "The Player Characters wake up naked in a dark cell. Agonized screams ring across the halls and voices obviously not human are heard outside. Development: Illegal research facility.",
            12: "The Player Characters are ambushed by the police as they are walking down the street in their hometown. Someone has framed them for murder and they must act quickly before the entire might of the Imperium lands on their heads. Development: Urban Investigation.", 
            13: "Gangsters have kidnapped someone very close to one or more of the Player Characters and demands the Player Characters complete a very dangerous and illegal mission in return for this person's release. Development: Criminal mission, Espionage mission.", 
            14: "A terrorist attack transforms a building the Player Characters are visiting into a flaming death trap. Without plans of the building or any special equipment they must escape the inferno, battling terrorists and rescuing survivors along the way. Development: Urban disaster.", 
            15: "programming bug causes all robots working in a nearby workshop to go on a murderous rampage. This hook is especially deadly if the Player Characters happen to be visiting the factory at the time of the uprising. Development: Industrial mishap.", 
            16: "A nearly unstoppable robot assassin is dispatched to murder the Player Characters. They have no idea who could have sent it or why. Development: Chatter (page 159), Mistaken Identity", 
            21: "The Player Characters' spacecraft breaks down and is forced to crash land on an uncharted planet. They must improvise some way to escape the planet while dealing with deadly nature, bizarre natives or mysterious ruins. Development: Wilderness events.",
            22: "The Player Characters wake up 1,000 years into the past. What is going on and how do they get back?! Development: Wormhole (page 43), Alien Probe (page 32).", 
            23: "The Player Characters literally fall from the sky into the adventure site. Development: Higher Entity (page 36), Living Planet (page 37).", 
            24: "One or more of the Player Characters has a dream about a peace-loving alien species suffering at hands of ruthless bandits. Investigation will reveal the planet seen in the dream is a real, though unexplored, location. Development: Khudrian (page 152).", 
            25: "One or more of the Player Characters wakes up one morning with the intuitive notion that today something horrible will happen to someone they love. As the day progresses, ever more specific visions begin to assail the Player Characters. Development: Any impending disaster.", 
            26: "A nuclear explosion followed by an alien invasion shakes the city the Player Characters are currently staying in. Even if the Player Characters do not feel like being the heroes and saving the day, they must still somehow escape the ruined city. Development: Invasion (page 14).", 
            31: "The Player Characters are exposed to an alien virus that causes them to rapidly mutate and develop superpowers even as their bodies begin to fail. Fearing mass infection, they are barred from returning home and must find the cure on their own. Development: Mutation (page 164), Mission to the Wilderness (page 105).",
            32: "The Player Characters wake up to find themselves inhabiting the bodies of other people. Where are their bodies, who is responsible and why? Development: Psychopath (page 155).", 
            33: "The child of one of the Player Characters does not want to go to school. With every passing day, his resistance grows stronger, even as his health decreases and strange marks begin to appear on his body. Development: Vampiric aliens run the school.", 
            34: "War has been declared and everyone has been drafted. Deserters will be shot by the military! Heroes will be shot by the enemy! Good luck, trooper! Development: Military mission.", 
            35: "The Player Characters are kidnapped and released into some deadly environment by a powerful alien who announces he will now hunt them for his entertainment. Development: Wilderness events (page 24) and Hunting Party (page 28).", 
            36: "Someone close to the Player Characters dies from a heart attack. Hours before his death he sent them a message – 'come ASAP, you won't believe what I've just discovered!' Development: Corporate Corruption, Secret Military Base (page 27).", 
            41: "An immoral scientist cons the army into infecting a group of elite soldiers with a virus that cause them to give in to their basest urges. Now the city is swarming with raping and murdering madmen. The hotel the Player Characters are staying in has remained an island of sanity in an ocean of madness – but for how long? Development: Zombie Apocalypse (page 16).",
            42: "While flying through space, the Player Characters encounter an extremely xenophobic religious community that claims the Player Characters have broken some religious edict and now must perform a mission to atone. They take hostages. Development: Cultists (page 49).", 
            43: "A decoy distress call draws the Player Characters into an elaborate trap set up by pirates working under the umbrella of corrupt imperial officials. Development: Pirates (page 54), Vargr Raiders (page 58).", 
            44: "Grotesque visages appear in windows as the Player Characters are walking down the street. Horrible faces blink on screens. Strange voices occasionally echo in electronic communication. More and more random acts of violence happen in the neighborhood. Development: Dormant Alien (page 12) about to wake up.", 
            45: "A suicide bombing injures the Player Characters and kills someone close to them. A shadowy political organization offers to assist them in avenging the deaths of their loved ones. Development: Military mission, political mission.", 
            46: "The Player Characters' ship is rocked by a mysterious explosion and is forced to land on a wild, uncharted planet that appears to be devoid of sentient life. Development: Living Planet (page 37) or Wilderness Events (page 24).", 
            51: "An unexplained space phenomenon transports the Player Characters' ship to another galaxy. Soon they encounter bizarre and extremely advanced aliens who could become the Player Characters' saviors or undertakers. Development: Wormhole (page 43).",
            52: "A strange unidentified object is moving at tremendous speed toward the world the players are currently staying on. Since no Imperial ships can reach the system before its arrival, the Player Characters are asked to intercept and investigate it. Development: Asteroid or Alien Probe (page 32).", 
            53: "A radical animal rights group releases all the animals in the city zoo, not realizing that many of them are powerful aliens capable of immense destruction. Development: Animals (69 in Traveller Core Rulebook).", 
            54: "A goblin in a funny hat comes to the Player Character and informs him that he was chosen as the Duke of the Realmunder- Sewage and must now release his kingdom from the evil of the fearsome Kadaiff. Development: Mythological Monsters (page 30) in Tunnels.", 
            55: "The Player Characters pass through a wormhole, finding themselves in a bizarre and deadly sector. Getting back home, either with the help of the demented natives or by navigating a series of wormholes will not be easy... Development: Wormhole (page 43).", 
            56: "A meeting with a potential patron turns out to be a trap. The 'patron' is a slaver who drugged the Player Characters' drinks. They wake on a slave ship headed to a mine on an otherwise uninhabited planet. Development: Slavers (page 28).", 
            61: "The Player Characters hear a shot in an alley. Running to investigate, they find a young man who just shot himself. An SMS appears on his mobile phone. It's for them. Development: Psychopath (page 155), alien conspiracy (page 86)",
            62: "Hiver degenerates kidnap the Player Characters and a score of other sophonts and conjoin them together in a perverse imitation of Siamese twins before dropping them off in the wilderness of an unknown planet. Development: Wilderness Events (page 24).", 
            63: "Someone close to the Player Characters has a huge gambling debt to the mafia. If the situation is not resolved in some way in 72 hours this person will be murdered. Development: Criminal mission.", 
            64: "An infamous serial killer sends a video to the news in which he informs them the Player Characters will become his next victims. Development: Psychopath (page 155) or Chatter (page 159).", 
            65: "A dying woman crawls with her last strength to one of the Player Characters and whispers 'Please! Take care of Verom...' before succumbing to her multiple wounds. The only clue is crumpled note with a hand-written address. Development: Lost child (page 29) and Alien Conspiracy (page 86) or Organized Crime (page 90).", 
            66: "A Player Character receives a panicked call from a family member in need. The message is not clear but it seems the speaker is in great danger. Development: The man has made a surprising discovery (page 12) and is now hunted by religious fanatics.", 
            }
    @staticmethod
    def getCoreStarportEncounters():
        return {
            11: "Maintenance robot at work",
            12: "Trade ship arrives or departs", 
            13: "Captain argues about fuel prices", 
            14: "News report about pirate activity on a starport screen draws a crowd", 
            15: "Bored clerk makes life difficult for the Travellers", 
            16: "Local merchant with cargo to transport seeks a ship", 
            21: "Dissident tries to claim sanctuary from planetary authorities",
            22: "Traders from offworld argue with local brokers", 
            23: "Technician repairing starport computer system", 
            24: "Reporter asks for news from offworld", 
            25: "Bizarre cultural performance", 
            26: "Patron argues with another group of Travellers", 
            31: "Military vessel arrives or departs",
            32: "Demonstration outside starport", 
            33: "Escaped prisoners begs for passage offworld", 
            34: "Impromptu bazaar of bizarre items", 
            35: "Security patrol", 
            36: "Unusual alien", 
            41: "Traders offer spare parts and supplies at cut-price rates",
            42: "Repair yard catches fire", 
            43: "Passenger liner arrives or departs", 
            44: "Servant robot offers to guide Travellers around the spaceport", 
            45: "Trader from a distant system selling strange curios", 
            46: "Old crippled belter asks for spare change and complains about drones taking his job", 
            51: "Patron offers the Travellers a job",
            52: "Passenger looking for a ship", 
            53: "Religious pilgrims try to convert the Travellers", 
            54: "Cargo hauler arrives or departs", 
            55: "Scout ship arrives or departs", 
            56: "Illegal or dangerous goods are impounded", 
            61: "Pickpocket tries to steal from the Travellers",
            62: "Drunken crew pick a fight", 
            63: "Government officials investigate the characters", 
            64: "Random security sweep scans Travellers and their baggage", 
            65: "Starport is temporarily shut down for security reasons", 
            66: "Damaged ship makes emergency docking", 
            }
    @staticmethod
    def getCoreRuralEncounters():
        return {
            11: "Wild Animal",
            12: "Agricultural robots", 
            13: "Crop sprayer drone flies overhead", 
            14: "Damaged agricultural robot being repaired", 
            15: "Small, isolationist community", 
            16: "Noble hunting party", 
            21: "Wild Animal",
            22: "Local landing field", 
            23: "Lost child", 
            24: "Travelling merchant caravan", 
            25: "Cargo convoy", 
            26: "Police chase", 
            31: "Wild Animal",
            32: "Telecommunications black spot", 
            33: "Security patrol", 
            34: "Military facility", 
            35: "Bar or waystation", 
            36: "Grounded spacecraft", 
            41: "Wild Animal",
            42: "Small community – quiet place to live", 
            43: "Small community – on a trade route", 
            44: "Small community – festival in progress", 
            45: "Small community – in danger", 
            46: "Small community – not what it seems", 
            51: "Wild Animal",
            52: "Unusual weather", 
            53: "Difficult terrain", 
            54: "Unusual creature", 
            55: "Isolated homestead - welcoming", 
            56: "Isolated homestead - unfriendly", 
            61: "Wild Animal",
            62: "Private villa", 
            63: "Monastery or retreat", 
            64: "Experimental farm", 
            65: "Ruined structure", 
            66: "Research facility", 
            }
    @staticmethod
    def getCoreUrbanEncounters():
        return {
            11: "Street riot in progress",
            12: "Travellers pass a charming restaurant", 
            13: "Trader in illegal goods", 
            14: "Public argument", 
            15: "Sudden change of weather", 
            16: "Travellers are asked for help", 
            21: "Travellers pass a bar or pub",
            22: "Travellers pass a theatre or other entertainment venue", 
            23: "Curiosity Shop", 
            24: "Street market stall tries to sell the Travellers something", 
            25: "Fire, dome breach or other emergency in progress", 
            26: "Attempted robbery of Travellers", 
            31: "Vehicle accident involving the Travellers",
            32: "Low-flying spacecraft flies overhead", 
            33: "Alien or other offworlder", 
            34: "Random character bumps into a Traveller", 
            35: "Pickpocket", 
            36: "Media team or journalist", 
            41: "Security Patrol",
            42: "Ancient building or archive", 
            43: "Festival", 
            44: "Someone is following the characters", 
            45: "Unusual cultural group or event", 
            46: "Planetary official", 
            51: "Travellers spot someone they recognize",
            52: "Public demonstration", 
            53: "Robot or other servant passes Travellers", 
            54: "Prospective patron", 
            55: "Crime such as robbery or attack in progress", 
            56: "Street preacher rants at the Travellers", 
            61: "News broadcast on public screens",
            62: "Sudden curfew or other restriction on movement", 
            63: "Unusually empty or quiet street", 
            64: "Public announcement", 
            65: "Sports event", 
            66: "Imperial Dignitary", 
            } 
    @staticmethod
    def getCampaignGuideUrbanCharacters():
        return {
        11: "Eccentric Millionaire.",
        12: "Dishonest Journalist.", 
        13: "Serial Killer.", 
        14: "Gang Leader.", 
        15: "Pop Hero.", 
        16: "Writer or Poet.", 
        21: "Simple man covered by the media for no apparent reason.",
        22: "Flamboyant Playboy.", 
        23: "Famous Prostitute.", 
        24: "Haunted Dissident.", 
        25: "Revered Terrorist.", 
        26: "Philanthropist Nobleman.", 
        31: "Retired Interplanetary Hunter.",
        32: "Popular Plastic Surgeon.", 
        33: "Disgraced Alien Politician.", 
        34: "Alien Rights Advocate.", 
        35: "Extreme Nationalist Activist.", 
        36: "Talent-less Sculptor Often Employed by City Hall.", 
        41: "Criminal Turned Honest Politician (or is he?).",
        42: "Hated Corporate Executive.", 
        43: "Daring Robber.", 
        44: "Controversial Scientist.", 
        45: "Revisionist Historian.", 
        46: "Public Attorney.", 
        51: "Campaigning Housewife.",
        52: "Bank Robber.", 
        53: "Sexy Scion.", 
        54: "Street Preacher.", 
        55: "Demented Innovator.", 
        56: "Celebrity ex-convict.", 
        61: "Uplifted Animal – Revolutionary Rat.",
        62: "Uplifted Animal – Philosophical Raven.", 
        63: "Uplifted Animal – A dog working as a tourist guide.", 
        64: "Infamous Graffiti Artist.", 
        65: "A Young Aristocrat Obsessed With Duelling.", 
        66: "A Morbidly Obese Media Mogul.", 
        }
    @staticmethod
    def getCampaignGuideRandomTraits():
        return {
        11: "Heavily Pregnant.",
        12: "Kleptomaniac.", 
        13: "Has very strong political views.", 
        14: "Extremely jealous of his spouse.", 
        15: "Nymphomaniac/Sleazy.", 
        16: "Extreme Pacifist.", 
        21: "Searching for a missing child.",
        22: "Planning to assassinate the Emperor and is very vocal about it.", 
        23: "Looking for the man who has murdered his father.", 
        24: "Investigating corporate corruption.", 
        25: "Believes he is hunted by government agents.", 
        26: "Dangerously Insane.", 
        31: "Mutant (see page 164).",
        32: "Member of a bizarre cult.", 
        33: "Traumatized by his involvement in a catastrophic war.", 
        34: "Fanatically patriotic.", 
        35: "Secretly works for a powerful corporation.", 
        36: "Insanely afraid of avian species (birds).", 
        41: "Bigoted against the species of one or more of the Player Characters.",
        42: "Missing one or more limbs.", 
        43: "Affected by incomplete brain development.", 
        44: "Had a chip with sensitive information installed in head.", 
        45: "Lacks any social skills whatsoever.", 
        46: "Distinctive scar or mutilation.", 
        51: "Flips a coin before any decision.",
        52: "Has a strong stutter.", 
        53: "Tattooed.", 
        54: "Has outrageous fashion sense.", 
        55: "Avid collector.", 
        56: "Brooding and fatalistic.", 
        61: "Dresses and behaves in a manner more fitting the previous century.",
        62: "Obsessed with some alien species and tries to mimic them as closely as possible.", 
        63: "Religious and pious to a fault.", 
        64: "Has an annoying and cheesy catchphrase.", 
        65: "Lacks a sense of humor.", 
        66: "Rude or overbearing.", 
        }
    @staticmethod
    def getCampaignGuideRandomEnchancements():
        return {
        1:"Benign Mutation", 
        2:"Malignant Mutation", 
        3:"Animal and Bird Crossover", 
        4:"Reptile and Fish Crossover", 
        5:"Insect and Plant Crossover", 
        6:"Cybernetic Augmentation"
        }
    @staticmethod
    def getCampaignGuideBenignMutations():
        return {
        2:"Psychic Powers: The character gains Psi 7 or +3 to his current Psi if he is already a psion.",
        3:"Natural SONAR: The character is aware of objects in a 10 meter radius as if able to see them.",
        4:"Additional Eyes*: The character gains +1 DM to Recon checks and has 360 degrees vision.",
        5:"Palm Mouths*: The mouth is extremely sensitive and can recognize most chemicals by taste. It is impossible to be poisoned through palm mouths. Some palm mouths can also speak.",
        6:"Poison Salvia: The character's bite poisons the victim with neurotoxins in addition to causing its normal mechanical damage. The character can also use their saliva to poison melee weapons.",
        7:"Super Digestion: The character can eat almost anything, organic or not, and survive for hours without oxygen.",
        8:"Second head*: +2 DM to Recon checks. Head can have separate personality and stay awake when the original head sleeps.",
        9:"Additional limb*: Can hold an additional item; +2 to STR and END.",
        10:"Tough skin: The character has natural armor of +1 to +3.",
        11:"Ageless cells: The character does not age naturally. Unless killed by injury or disease, he can live forever.",
        12:"Re-roll Twice: NA",
        }
    @staticmethod
    def getCampaignGuideMalignantMutations():
        return {
        2:"Tiny Mouth: It is very difficult to understand what the character says. His bite attacks deal only 1 point of damage.",
        3:"One eye: The character suffers –1 DM to all Recon checks and has 90 degrees vision.",
        4:"Alien Hand: At least once per day, the character's hand acts independently of the character, often against him or his friends.",
        5:"Inhumanity: The character is inhuman in some subtle but disturbing way. This grants +1 DM to intimidation checks and –1 DM to all other social checks.",
        6:"Hermaphrodite: The character has both male and female sexual organs and characteristics.",
        7:"Joined Feet: The character's lower body part resembles that of a snake, only without the snake's grace and dexterity. The character always moves at half speed and suffers –2 Dex.",
        8:"Altered Digestion: The character can eat only one material and even this in a profoundly disgusting way. All social checks made during dinners suffer from a –2 DM.",
        9:"Cancer: The character has cancer.",
        10:"Soft Body: All hits inflict two additional points of damage.",
        11:"Body Part Atrophies: The character is unable to use a body part. 1–2: Leg. 3–4: Hand. 5–6: Tongue.",
        12:"Re-roll Twice: NA",
        }
    @staticmethod
    def getCampaignGuideAnimalBirdMutations():
        return {
        2:"Bat Ears: The character is aware of objects in a 10 meter radius as if able to see them.",
        3:"Leathery Wings: Player Character can fly clumsily.",
        4:"Sabre teeth: The character's bite attack inflicts 2d6 points of damage.",
        5:"Feline Claws: The character's unarmed attacks inflict additional three points of damage.",
        6:"Rhino Hide: The character has natural armor 2.",
        7:"Bull Horns: The character can gore his enemies. This attack is done with –2 DM and inflicts 2d6+3 points of damage.",
        8:"Horse Hooves: –1 DM to Stealth checks.",
        9:"Porcupine Quills: Unarmed attacks against the character inflict three points of damage on the attacker. The character can strike foes with his quills. This inflicts 1d6 points of damage and –2 DM to all attacks due to the pain caused by broken quills lodged in the target's flesh. The negative DMs are not cumulative.",
        10:"Tiger Fur: It is handsome and pleasant to the touch but offers no additional advantages.",
        11:"Sharp Senses: The character gains +1 DM to all Recon checks.",
        12:"Re-roll Twice: This option can be rolled only once. Ignore on further rolls.",
        }
    @staticmethod
    def getCampaignGuideReptileFishMutations():
        return {
        2:"Frog Tongue: The character can move light objects with his tongue.",
        3:"Turtle Shell: armor 5 but speed is halved.",
        4:"Jellyfish tentacles: The tentacles can whip enemies for 1d6+3 points of damage. This attack ignores armor.",
        5:"Snake Bite: The character's bite poisons the victim with neurotoxins in addition to causing its normal mechanical damage. The character can also use his saliva to poison melee weapons.",
        6:"Scales: armor 1.",
        7:"Chameleon Skin: The character's skin changes color and texture to match the surrounding environment. When completely nude, the character enjoys +3 DM to Stealth checks. When nude but equipped the DM is reduced to +1.",
        8:"Blowfish Inflation: The character can inflate into a huge thorny ball. This can be quite scary for unprepared observers. Also, this makes the character float/hover for a limited period of time.",
        9:"Shark Jaws: The character's bite attack inflicts 1d6+3 points of damage.",
        10:"Crocodile Physique: Combines scales, gills and shark jaws.(Scales: armor 1, hark Jaws: The character's bite attack inflicts 1d6+3 points of damage, Gills: The character can freely breathe underwater.)",
        11:"Gills: The character can freely breathe underwater.",
        12:"Re-Roll: Twice NA",
        }
    @staticmethod
    def getCampaignGuideInsectPlantMutations():
        return {
        2:"Grasshopper feet: +4 DM to Athletics (Co-ordination) checks.",
        3:"Barkskin: The character gains armor 4 but becomes highly flammable.",
        4:"Mosquito Style: Attack deals 1d6+3 points of damage. Each round hold is maintained, bloodsucking inflicts 1d6 points of End damage to the victim.",
        5:"Poisonous Spores: Once per day, the character can release poisonous spores into the air. All creatures within a 6 meter radius are affected by the poison (neurotoxin, page 74 of Traveller Core Rulebook).",
        6:"Centipede Body: +2 Stealth, –2 Dex. The character is always considered prone for the purpose of determining combat DMs.",
        7:"Cockroach Stamina: The character gains +2 End. It takes double a radiation dose to damage it (see page 141 in the Traveller Core Rulebook).",
        8:"Flowers: Flowers grow from the Player Character's body. Some consider it pretty.",
        9:"Butterfly Wings: The character can fly clumsily for short periods of time.",
        10:"Barbs: Unarmed attacks against the character inflict 1d6 points of damage to the attacker. Unarmed attacks by character cause 3 more points of damage.",
        11:"Ant Mandibles: Bite inflicts 2d6+3 points of damage",
        12:"Re-Roll Twice: NA",
        }
    @staticmethod
    def getCampaignGuideCyberneticEnhancements():
        return {
            2:"Subdermal armor +1 to +3 to armor. Stacks with other armor.",
            3:"Cybernetic Eyes Infrared vision and +1 to Recon checks.",
            4:"Titanium Bones +2 End.",
            5:"Mechanic Arms +2 Str.",
            6:"Hand Razors When the razors are drawn unarmed attacks deal four additional points of damage.",
            7:"Voice Modulator The character can perfectly mimic the voice of any person he has heard speaking.",
            8:"Artificial Wings The character can fly clumsily.",
            9:"Hydraulic Jaws The character can bite for 1d6+6 points of damage. Attack is made with –2 DM.",
            10:"Self-Destruction The character has a powerful plastic explosive installed within his body and can activate it at will (either his or a faraway operator's).",
            11:"Brain Computer: See page 89 in Traveller Core Rulebook.",
            12:"Finger Laser: The character can shoot laser beams from his finger. This functions in the same way as a standard laser pistol (page 100 in the Traveller Core Rulebook) but due to its small size must be recharged after each shot.",
            }
    @staticmethod
    def getCampaignGuideDistricts():
        return {
            11:"Administrative",
            12:"Alien, Ghetto",
            13:"Alien, Residential",
            14:"Culture",
            15:"Embassy",
            16:"Finance",
            21:"Gladiatorial",
            22:"Government",
            23:"Historic",
            24:"Industrial",
            25:"Marketplace",
            26:"Military",
            31:"Museum",
            32:"Offices, Basic",
            33:"Offices, Corporate",
            34:"Parks",
            35:"Red Light",
            36:"Refugee Camp",
            41:"Residential, Very Poor",
            42:"Residential, Poor",
            43:"Residential, Low",
            44:"Residential, Average",
            45:"Residential, Good",
            46:"Residential, High",
            51:"Residential, Very High",
            52:"Residential, Rich",
            53:"Residential, Very Rich",
            54:"Residential, Ludicrously Rich",
            55:"Ruined",
            56:"Shopping",
            61:"Slave",
            62:"Slums",
            63:"Spaceport",
            64:"University",
            65:"Waterfront",
            66:"Weird",
        }
    @staticmethod
    def getCampaignGuideCityLandmarks():
        return {
        11:"A gigantic ghost figure watching over the city from the heavens.",
        12:"A colossal downed alien warship whose shadow still looms over the city.",
        13:"A sculpture of a hero or a mythological figure visible from orbit.",
        14:"The city is built on a massive mechanised plate and can move across the country.",
        15:"The city is a ring constructed across the planet.",
        16:"An active volcano frozen mid-eruption with ancient technology stands in the centre of the city. Because no one knows how to operate the mysterious device, the citizens simply do not touch it and hope for the best.",
        21:"Huge robots designed to look like different animals patrol the city, protect it from invaders and help move heavy objects around.",
        22:"A yearly parade in the memory of a war in which an ancient enemy was defeated by an alliance of different races. Sophonts of all races are encouraged to participate.",
        23:"The most inclusive zoo in the Imperium. The zoo includes sophonts as well. Possibly even someone the Player Characters know...",
        24:"All official documents and petitions must be written or recited with the appropriate rhyme scheme.",
        25:"Sophont sacrifice is practiced in the city despite widespread condemnation by the intergalactic community and local intelligentsia. The sacrifices are randomly chosen by mysterious priests in crimson battle dresses.",
        26:"A pit many miles deep is located in the centre of the city. The local laws prohibit anyone from going down there. In hard times, sacrificial victims are pushed into the pit to appease 'the one below'.",
        31:"Jobs in the city are randomly distributed by a computer. Every morning, each citizen is given a different role to play for the day. The locals believe this creates equality and understanding among the citizenry.",
        32:"Personalities of deceased citizens are uploaded to a giant computer and continue to live in virtual space.",
        33:"A colossal alien tree with roots spreading all over the city, traditionally believed to be the city's source of life.",
        34:"A historic district entirely carved out of petrified mushrooms.",
        35:"The city is built inside an anthill-like structure created millions of years ago by an extinct species.",
        36:"Duels are legal and extremely common in the city. Foreigners are not exempt and a single wrong phrase is likely to be answered by a challenge for a fight to the death.",
        41:"The city is controlled by the Nudist Party and clothing is strictly forbidden except when worn for protection.",
        42:"Elective surgery is extremely popular in the city. Few of the well-off citizens can be easily recognised as humans. Appearances are changed like costumes and natural looks close many doors.",
        43:"The city is obsessed with death. Life support is illegal, suicide is encouraged and the prevalent architectural philosophy makes the whole area look like one gigantic graveyard.",
        44:"The city is a colossal labyrinth. Without a map, it is practically impossible to navigate its winding streets. The locals believe that living in a labyrinthine city is good for the intellect.",
        45:"The city has absurd modesty rules. Showing even a single inch of skin or hair is strictly forbidden. Everyone must wear the exact same black shawl and blank mask. Visitors are not exempt.",
        46:"A massive cathedral built entirely from the remains of dead sophonts.",
        51:"A huge square full of random objects. Every person passing through the field must leave two objects and pick up one object. He may not throw away this object until he has left the city.",
        52:"A technological landfill that has become self-aware. It is considered to be a prophet of the Gods of Technology by a strange local cult and a major tourist attraction by City Hall. The being itself is friendly and quite wise.",
        53:"A door that teleports anyone who passes through it to a random planet anywhere in the galaxy. It is unknown who constructed this door or why. It is a popular tourist attraction, although few travellers actually dare to step through it.",
        54:"Unusual street animals (examples: dinosaur-like aliens, talking cats and dogs, cockroach-sized sophonts).",
        55:"Some gesture, phrase, clothing article or object is taboo in the city. Their possession or use is strictly illegal and might result in public lynching even before the arrival of the police.",
        56:"Only members of one sex are allowed to enter or live in the city. The city has a twin city, possibly on another planet, where only the other sex is accepted. Once per year the citizens of both cities meet on neutral grounds for a week-long festival.",
        61:"All the houses in the city are intelligent robots capable of defending themselves from intruders and interacting with newcomers and each other. Some houses even have political rights and their own property.",
        62:"Gravity is so low in this city that with a slight push people can jump tens of feet into the air or climb sheer walls. The architecture makes maximum use of this by creating oddly angled houses and doors in the most unpredictable locations.",
        63:"Individual personality must be hidden within the confines of the city. Everyone must wear identical robes and masks that cover the entire body and convert individual voices to identical sounds.",
        64:"The engineers of the city have constructed powerful weather control devices that give City Hall absolute control over the weather. Every evening the weather for the next day is democratically chosen by the citizens.",
        65:"All the buildings in the city are monumental towers thousands of feet tall. A strict social hierarchy describes who is allowed to live on each level.",
        66:"The city has many facilities, institutes, office buildings, factories and hospitals but no residential houses or shops. Citizens sleep and trade in the open, enjoying the mild weather and the lovely sky.",
        }
    # ============================================================
    
    @staticmethod
    def getTable(tableName):
        table = None
        # Core Tables
        # 
        # Zozer Tables
        if tableName.lower() in ["in media res"]: table = Tables.getZozerTravellerInMediaRes()
        elif tableName.lower() in ["passenger ship events"]: table = Tables.getZozerTravellerOnboardEventspassengerShip()
        elif tableName.lower() in ["non-passenger ship events", "non passenger ship events"]: table = Tables.getZozerTravellerOnboardEventsNonpassengerShip()
        elif tableName.lower() in ["ship malfunction", "ship-malfunction"]: table = Tables.getZozerTravellerShipMalfunction()
        elif tableName.lower() in ["shipboard training", "starship training"]: table = Tables.getZozerTravellerShipboardTraining()
        elif tableName.lower() in ["world encounter", "world event", "world encounters", "world events"]: table = Tables.getZozerTravellerWorldEncounterTable()
        elif tableName.lower() in ["patron"]: table = Tables.getZozerTravellerPatron()
        elif tableName.lower() in ["patron missions"]: table = Tables.getZozerTravellerPatronMissions()
        elif tableName.lower() in ["mission targets"]: table = Tables.getZozerTravellerMissionTargets()
        elif tableName.lower() in ["colorful locals"]: table =Tables.getZozerTravellerColorfulLocals()
        elif tableName.lower() in ["relationship table"]: table =Tables.getZozerRelationshipTable()
        #
        elif tableName.lower() in ["ship encounter major route"]: table =Tables.getZozerShipEncounterMajorRoute()
        elif tableName.lower() in ["ship encounter minor route"]: table =Tables.getZozerShipEncounterMinorRoute()
        elif tableName.lower() in ["industrial ship encounter"]: table =Tables.getZozerIndustrialShipEncounter()
        elif tableName.lower() in ["military ship encounter"]: table =Tables.getZozerMilitaryShipEncounter()
        elif tableName.lower() in ["special ship encounter"]: table =Tables.getZozerSpecialShipEncounter()
        elif tableName.lower() in ["small transport ship encounter"]: table =Tables.getZozerSmallTransportShipEncounter()
        elif tableName.lower() in ["scout ship encounter"]: table =Tables.getZozerScoutShipEncounter()
        elif tableName.lower() in ["large transport ship encounter"]: table =Tables.getZozerLargeTransportShipEncounter()
        elif tableName.lower() in ["frontier ship encounter"]: table =Tables.getZozerFrontierShipEncounter()
        elif tableName.lower() in ["frontier ship reaction"]: table =Tables.getZozerFrontierShipReaction()
        elif tableName.lower() in ["industrial ship reaction"]: table =Tables.getZozerIndustrialShipReaction()
        elif tableName.lower() in ["transport ship reaction", "special ship reaction"]: table =Tables.getZozerTransportSpecialShipReaction()
        elif tableName.lower() in ["scout ship reaction"]: table =Tables.getZozerScoutShipReaction()
        elif tableName.lower() in ["military ship reaction"]: table =Tables.getZozerMilitaryShipReaction()
        #
        elif tableName.lower() in ["roadside events"]: table = Tables.getTravellerSupp9RandomEventRoadsideEvents()
        elif tableName.lower() in ["health events"]: table = Tables.getTravellerSupp9RandomEventHealthEvents()
        elif tableName.lower() in ["battlefield events"]: table = Tables.getTravellerSupp9RandomEventBattlefieldEvents()
        elif tableName.lower() in ["military units"]: table = Tables.getTravellerSupp9MilitaryUnit()
        elif tableName.lower() in ["urban events"]: table = Tables.getTravellerSupp9RandomEventUrbanEvents()
        elif tableName.lower() in ["local urban events"]: table = Tables.getTravellerSupp9RandomEventLocalUrbanEvents()
        elif tableName.lower() in ["local urban accidents"]: table = Tables.getTravellerSupp9RandomEventLocalUrbanAccidents()
        elif tableName.lower() in ["local urban survivors"]: table = Tables.getTravellerSupp9RandomEventLocalUrbanSurvivors()
        elif tableName.lower() in ["local urban alien visitors"]: table = Tables.getTravellerSupp9RandomEventLocalUrbanAlienVisitors()
        elif tableName.lower() in ["absent player", "absent player events", "absent player actions"]: table = Tables.getTravellerSupp9RandomEventAbsentPlayerActions()
        # elif tableName.lower() in []: table = Tables.get()
        elif tableName.lower() in ["trader spacecraft quirks"]: table = Tables.getTravellerCoreTraderSpacecraftQuirks()
        elif tableName.lower() in ["military spacecraft quirks"]: table = Tables.getTravellerCoreMilitarySpacecraftQuirks()
        elif tableName.lower() in ["other spacecraft quirks"]: table = Tables.getTravellerCoreOtherSpacecraftQuirks()
        elif tableName.lower() in ["bad consequences"]: table = Tables.getZozerBadConsequences()
        elif tableName.lower() in ["good consequences"]: table = Tables.getZozerGoodConsequences()
        elif tableName.lower() in ["foot chase", "chase-foot"]: table = Tables.getTravellerSupp9FootChase()
        elif tableName.lower() in ["ancient artifacts", "ancient artifacts"]: table = Tables.getTravellerSupp9AncientArtifacts()
        elif tableName.lower() in ["starport events", "starport encounters", "zozer starport events", "zozer starport encounters"]: table = Tables.getZozerTravellerStarportEncounters()
        elif tableName.lower() in ["core starport events", "core starport encounters"]: table = Tables.getCoreStarportEncounters()
        # elif tableName.lower() in []: table = Tables.get()
        elif tableName.lower() in ["life events master"]: table = Tables.getLifeEventMasterCampaignGuide()
        elif tableName.lower() in ["life events friends", "life events family", "life events lovers"]: table = Tables.getLifeEventFriendsFamilyLoversCampaignGuide()
        elif tableName.lower() in ["life events self", "life events innermost", "life events innermost self"]: table = Tables.getLifeEventInnermostSelfCampaignGuide()
        elif tableName.lower() in ["life events hooks"]: table = Tables.getLifeEventHooksCampaignGuide()
        elif tableName.lower() in ["districts", "city districts", "urban districts"]: table = Tables.getCampaignGuideDistricts()
        elif tableName.lower() in ["core urban events", "core urban encounters"]: table = Tables.getCoreUrbanEncounters()
        elif tableName.lower() in ["core rural events", "core rural events"]: table = Tables.getCoreRuralEncounters()
        elif tableName.lower() in ["urban characters"]: table = Tables.getCampaignGuideUrbanCharacters()
        elif tableName.lower() in ["random traits"]: table = Tables.getCampaignGuideRandomTraits()
        elif tableName.lower() in ["random enhancements", "random mutations"]: table = Tables.getCampaignGuideRandomEnchancements()
        elif tableName.lower() in ["good mutations", "benign mutations"]: table = Tables.getCampaignGuideBenignMutations()
        elif tableName.lower() in ["bad mutations", "malignant mutations"]: table = Tables.getCampaignGuideMalignantMutations()
        elif tableName.lower() in ["animal mutations", "bird mutations", "mammal mutations", "avian mutations",
            "animal crossover", "bird crossover", "mammal crossover", "avian crossover"
            ]: table = Tables.getCampaignGuideAnimalBirdMutations()
        elif tableName.lower() in ["reptile mutations", "fish mutations", "reptile crossover", "fish crossover"]: table = Tables.getCampaignGuideReptileFishMutations()
        elif tableName.lower() in ["plant mutations", "insect mutations", "plant crossover", "insect crossover"]: table = Tables.getCampaignGuideInsectPlantMutations()
        elif tableName.lower() in ["cyber augmentations", "cybernetic augmentations", "cyber enhancements", "cybernetic enhancements"]: table = Tables.getCampaignGuideCyberneticEnhancements()
        
        elif tableName.lower() in ["drama sit", "dramatic situation", "dramatic situations"]: tables = Tables.getSupplement16DramaticSituations()
        # elif tableName.lower() in []: table = Tables.get()
        elif tableName.lower() in ["warrant type", "new warrant"]: tables = Tables.getBountyHunterGuideWarrentType()
        elif tableName.lower() in ["warrant target", "target wanted"]: tables = Tables.getBountyHunterGuideTargetWanted()
        elif tableName.lower() in ["warrant distance", "target distance", "distance to target"]: tables = Tables.getBountyHunterGuideDistanceToTarget()
        # elif tableName.lower() in []: table = Tables.get()
        # elif tableName.lower() in []: table = Tables.get()
        # elif tableName.lower() in []: table = Tables.get()
        # elif tableName.lower() in []: table = Tables.get()
        # elif tableName.lower() in []: table = Tables.get()
        # elif tableName.lower() in []: table = Tables.get()
        # elif tableName.lower() in []: table = Tables.get()
        # elif tableName.lower() in []: table = Tables.get()
        # elif tableName.lower() in []: table = Tables.get()
        # elif tableName.lower() in []: table = Tables.get()
        # elif tableName.lower() in []: table = Tables.get()
        # elif tableName.lower() in []: table = Tables.get()
        #
        # Custom Tables
        else: 
            print("Table not present")
        return table
    @staticmethod
    def getTableNameList():
        return [
            "\"in media res\": how to start a space adventure.",
            "\"passenger ship events\": ",
            "\"non-passenger ship events\": ",
            "\"ship malfunction\": ",
            "\"shipboard training\": ",
            "\"world encounter\": ",
            "\"patron\": ",
            "\"patron missions\": ",
            "\"mission targets\": ",
            "\"colorful locals\": ",
            "\"relationship table\": ",
            "\"ship encounter major route\": ",
            "\"ship encounter minor route\": ",
            "\"industrial ship encounter\": ",
            "\"military ship encounter\": ",
            "\"special ship encounter\": ",
            "\"small transport ship encounter\": ",
            "\"scout ship encounter\": ",
            "\"large transport ship encounter\": ",
            "\"frontier ship encounter\": ",
            "\"frontier ship reaction\": ",
            "\"industrial ship reaction\": ",
            "\"transport|special ship reaction\": ",
            "\"scout ship reaction\": ",
            "\"military ship reaction\": ",
            "\"roadside events\": ",
            "\"health events\": ",
            "\"battlefield events\": ",
            "\"military units\": ",
            "\"urban events\": ",
            "\"local urban events\": ",
            "\"local urban accidents\": ",
            "\"local urban survivors\": ",
            "\"local urban alien visitors\": ",
            "\"absent player actions\": ",
            "\"trader spacecraft quirks\": ",
            "\"military spacecraft quirks\": ",
            "\"other spacecraft quirks\": ",
            "\"bad consequences\": ",
            "\"good consequences\": ",
            "\"foot chase\": ",
            "\"ancient artifacts\": ",
            "\"random mutations\": ",
            "\"good mutations\": ",
            "\"bad mutations\": ",
            "\"animal mutations\": ",
            "\"reptile mutations\": ",
            "\"insect mutations\": ",
            "\"cyber augmentations\": ",
            "\"bounty hunter life events\": ",
            "\"warrant type\": ",
            "\"warrant target\": ",
            "\"warrant distance\": ",
            # "\"ship\": ",
            # "\"ship\": ",
            # "\"ship\": ",
            # "\"ship\": ",
            # "\"ship\": ",
            ]
    @staticmethod
    def displayTable(table):
        for row in table:
            if ( isinstance(table[row], list) ):
                text = ""
                for i in table[row]:
                    text += "{}, ".format(i)
                text = text[:-2]
                TerminalUtils.pprint("{0:>2}: {1}".format(str(row), text), indent=4)
            elif ( isinstance(table[row], dict) ):
                print(row)
                TerminalUtils.displayTable(table[row], indent=4)
            else:
                TerminalUtils.pprint("{0:>2}: {1}".format(str(row), str(table[row])), indent=4)
    
    #
class CustomTables():
    @staticmethod
    def getBountyHunterInMediaRes():
        return {
            2: "1",
            3: "2",
            4: "3", 
            5: "4",
            6: "5",
            7: "6",
            8: "7",
            9: "8",
            10: "9",
            11: "10",
            12: "11",
        }
    @staticmethod
    def getBiologicalsInMediaRes():
        return {
            2: "1",
            3: "2",
            4: "3", 
            5: "4",
            6: "5",
            7: "6",
            8: "7",
            9: "8",
            10: "9",
            11: "10",
            12: "11",
        }
    @staticmethod
    def getWildWestInMediaRes():
        return {
            2: "Petty Train Robbery: a few Desperados are holding people up on the train planning to point their guns at unarmed folk and take their money. They are hat and bandana wearing gunslingers. Will you Draw on them? will you let them take your possessions?",
            3: "2",
            4: "3", 
            5: "4",
            6: "5",
            7: "6",
            8: "7",
            9: "8",
            10: "9",
            11: "10",
            12: "11",
        }
    @staticmethod
    def getWildWestTownEvents():
        return {
            2: "1",
            3: "2",
            4: "3", 
            5: "4",
            6: "5",
            7: "6",
            8: "7",
            9: "8",
            10: "9",
            11: "10",
            12: "11",
        }
    @staticmethod
    def getWildWestAdventureHooks():
        return { # https://www.tribality.com/2017/09/18/top-8-tips-for-running-a-western-style-game/
            1: "Cattle are disappearing the PCs need to find out what's going on: A. The animals are wandering off through a hole in the owner's fence, they can be found and brought back? B. The animals are getting stolen and rebranded because another brand lines up identically? C. The animals are getting eaten by a wild animal or a mythical creature like the chupacabra? ",
            2: "Natives: A. The Native Americans have intercepted and stolen a shipment of guns. It's up to the PCs to get them back, peacefully, if possible. B. A settlement was destroyed by the Native Americans. The only survivor, a girl, is raised by the tribe that slaughtered her family. It's up to the PCs to save her and teach her the ways of her people. C. The Native Americans have raided the town where the PCs are due to buffalo scarcity and lack of promised governmental assistance. It's up to the PCs to settle them down before things take a more violent turn. D. The PCs are requisitioned to deliver a shipment of supplies to the Native Americans. Little do they know that amidst the shipment is are blankets.",
            3: "A woman and her two daughters are traveling by coach. In each of their possessions they have one piece of a puzzle – a contract for land? a deed for a gold-producing mine?", 
            4: "A crazy old miner comes into the town and goes into the surveyor's office to make a claim. But instead of his claim the surveyor puts in someone else's name. When the man goes back to the location, there's trouble for him. It's up to the PCs to discover the fraud, if they can.", 
            5: "Robberies: A. A bank robber is in the area and according to the pattern of robberies, the town the PCs are in should be the next one struck. It's up to them to stop the robbery before it happens. B. A revival tent comes into town and while much of the town is participating, a series of robberies takes place and those running it are accused of staging it for that purpose. The PCs must prove their innocence",
            6: "There's a strange creature that attacks people and animals at night, it's up to the PCs to figure out what's going on and stop it.",
            7: "There's a strange disease going around. It's up to the PCs to find the source and stop it before it spreads. A. As it turns out, the cause is dirty water that's been contaminated by people dumping waste into an old open well which connects to the underground water supply. B. As it turns out, a seasoning that quite a lot of the town is using was mixed up with a local weed that has unpleasant side effects but tastes amazingly similar.",
            8: "People are suspicious of strange goings on and the superstitious townsfolk accuse orphans of being the troublemakers. They, of course, are innocent of the accusations.",
            9: "A gunslinger comes into town trying to get into gunfights with whoever he can. It's up to the PCs to stop him before he shoots up the entire town.",
            10: "A notorious gambler has hired the PCs to get him out of town with his ill-gotten gains. They need to do so discretely without the town's folk becoming too upset with them for doing so.",
            11: "A group of immigrants from a foreign country are peaceably seeking work. Unfortunately, the townsfolk are not only unwelcoming to them, but consistently cause them trouble. It's up to the PCs to show the town the error of their ways.",
            12: "A natural disaster (fire, flood, stampeding herd) is threatening the town. It's up to the PCs to help rally and organize the town to face the threat.",
            13: "A coach or train having something valuable on board is arriving in town and it's up to the PCs to protect it against notorious thieves.",
        }
    @staticmethod
    def getWildWest36TownsFolk():
        return {
            11: "Trade: Barber",
            12: "Trade: Clothier", 
            13: "Trade: Wood Worker", 
            14: "Trade: Leather Worker", 
            15: "Trade: Smith/Metal Worker", 
            16: "Trade: Entertainer", 
            21: "Merchant: General Store",
            22: "Merchant: Clothier", 
            23: "Trade: Undertaker", 
            24: "Trade: Doctor/Physician", 
            25: "Trade: Civil Engineer/Builder", 
            26: "Merchant: Trader", 
            31: "Trade: Banker",
            32: "Trade: Rancher/Farmer/Fisher", 
            33: "Trade: Miner/Logger", 
            34: "Law: Deputy", 
            35: "Law: Sheriff", 
            36: "Law: Marshal", 
            41: "Company: Broker",
            42: "Company: Human Resources", 
            43: "Company: Technician", 
            44: "Company: Manager", 
            45: "Company: Security/Hired Gun", 
            46: "Politician: Mayor", 
            51: "Politician: Governor",
            52: "Social Worker: Trade Liason", 
            53: "Social Worker: Union Representative", 
            54: "News: Reporter", 
            55: "Doctor", 
            56: "Tourist", 
            61: "Traveller: Merchant/Trader",
            62: "Traveller: Military (Scout, Army, Navy, Marines)", 
            63: "Traveller: Citizen", 
            64: "Traveller: Scientist", 
            65: "Traveller: Law Enforcement/Agent", 
            66: "Traveller: Drifter", 
            }
    @staticmethod
    def getBountyInformation():
        return {
        1: "Residence. The information gives an address or abode for the target.",
        2: "Locale. The information provides a particular location, other than their current residence, that the target frequents on a regular basis.",
        3: "Acquaintances.The information names and locates a relative, friend, or casual acquaintance who may have useful information regarding the target.",
        4: "Gear. The information provides additional details about the target's equipment and tools.",
        5: "Habits. The information provides insights about the routines and preferences of the target.",
        6: "Secrets. The information provides details about a secret associated with the target.",
        }
    @staticmethod
    def getBountyValue():
        return {
            1: "Very weak. 1D6 times 1000 credits. Resources limited to personal. No allies. 1D6-4 Other hunters.", 
            2: "Weak. 1D6 times 2000 credits. Resources: personal + a vehicle. 1 ally. 1D6-3 Other hunters.", 
            3: "Average. 1D6 times 10 thousand credits. Resources (crime ring or family): base, vehicles. 1D3 allies. 1D3-1 Other hunters.", 
            4: "Capable. 1D6 times 20 thousand credits. Resources (crime ring or family): base, vehicles. 1D3+3 allies. 1D3 Other hunters.", 
            5: "Strong. 1D6 times 50 thousand credits. Resources (large crime ring or family): Large base, vehicles. 1D6+6 allies. 1D6 Other hunters.", 
            6: "Powerful. 1D6 times 100 thousand credits. Resources: Organization. Many allies. 1D6+1 Other hunters.", 
            7: "Very Powerful. 1D6 times 200 thousand credits. Resources: Large Organization. Many allies. 1D6+2 Other hunters.", 
            8: "Formidable. 1D6 times 500 thousand credits. Resources: Polity. Many allies within Polity. 1D6+3 Other hunters.", 
        }
    @staticmethod
    def getBountyHunterGenerationsLifeEvents():
        return {
            11: "",
            12: "", 
            13: "", 
            14: "", 
            15: "", 
            16: "", 
            21: "",
            22: "", 
            23: "", 
            24: "", 
            25: "", 
            26: "", 
            31: "",
            32: "", 
            33: "", 
            34: "", 
            35: "", 
            36: "", 
            41: "",
            42: "", 
            43: "", 
            44: "", 
            45: "", 
            46: "", 
            51: "",
            52: "", 
            53: "", 
            54: "", 
            55: "", 
            56: "", 
            61: "",
            62: "", 
            63: "", 
            64: "", 
            65: "", 
            66: "", 
            }
    @staticmethod
    def getRandomSystemLimitedShips():
        return {
            2: "Light Fighter. HP: 4. Armor: 2-4. Thrust 6-8, 1 Fixed Mount, Weapons Pulse/Beam Laser.",
            3: "Gig. HP: 8. Armor: 0-2. Thrust 6-8, 1 single turret, Weapons Pulse/Beam Laser.",
            4: "Launch. HP: 8. Armor: 0-2. Thrust 1-3, 0-2 Fixed Mount, Weapons Pulse/Beam Laser.",
            5: "Pebble. HP: 10. Armor: 0-2. Thrust 2-4, 0-2 Fixed Mount, Weapons Pulse/Beam Laser. Psionic Shielding.",
            6: "Ship's Boat. HP: 12. Armor: 0-2. Thrust 5-8, 0-3 Fixed Mount, Weapons Pulse/Beam Laser.",
            7: "Slow Boat. HP: 12. Armor: 0-2. Thrust 3-5, 0-3 Fixed Mount, Weapons Pulse/Beam Laser.",
            8: "Pinnace. HP: 16. Armor: 0-2. Thrust 5-8, 0-4 Fixed Mount, Weapons Pulse/Beam Laser.",
            9: "Slow Pinnace. HP: 16. Armor: 0-2. Thrust 3-6, 0-4 Fixed Mount, Weapons Pulse/Beam Laser.",
            10: "Modular Cutter. HP: 20. Armor: 0-2. Thrust 4-8, 0-5 Fixed Mount, Weapons Pulse/Beam Laser.",
            11: "Heavy Fighter. HP: 22. Armor: 15?/4. Thrust 9, 2 firm point, Weapons Pulse/Beam Laser / Missile Rack.",
            12: "Shuttle. HP: 38. Armor: 0-2. Thrust 3-6, 0-9 Fixed Mount, Weapons Pulse/Beam Laser, Missile Rack.",

        }
    @staticmethod
    def getRandomInterstellarShips():
        return {
            1: "Scout Courier (Type-S). HP: 40, Armor: 4-8, Thrust 2-4, Jump 2-4, Turrets: 1. Weapons: Pulse/Beam Lasers, Sandcasters, Missile Racks.",
            2: "Seeker Mining Ship (Type-J). HP: 40, Armor: 4-8, Thrust 2-4, Jump 2-4, Turrets: 1. Weapons: Pulse/Beam Lasers, Sandcasters, Missile Racks.",
            3: "Scout (Serpent Class). HP: 40/100, Armor: 4-8, Thrust 2-4, Jump 2-4, Turrets: 1. Weapons: Pulse/Beam Lasers, Sandcasters, Missile Racks.",
            4: "Far Trader (Empress Marava-Class). HP: 80, Armor: 0-4, Thrust 1-3, Jump 2-4, Turrets: 2. Weapons: Pulse/Beam Lasers, Sandcasters, Missile Racks.",
            5: "Far Trader (Type-A2). HP: 80, Armor: 2-6, Thrust 1-3, Jump 2-4, Turrets: 0-2. Weapons: Pulse/Beam Lasers, Sandcasters, Missile Racks.",
            6: "Free Trader (Type-A). HP: 80, Armor: 2-6, Thrust 1-3, Jump 1-3, Turrets: 0-2. Weapons: Pulse/Beam Lasers, Sandcasters, Missile Racks.",
            7: "Safari Ship. HP: 80, Armor: 0-4,Thrust 1-3, Jump 1-3,  Turrets: 0-2. Weapons: Pulse/Beam Lasers, Sandcasters, Missile Racks.",
            8: "Yacht (Type-Y). HP: 80, Armor: 0-4, Thrust 1-3, Jump 1-3, Turrets: 0-2 hidden. Weapons: Pulse/Beam Lasers, Sandcasters, Missile Racks.",
            9: "Asteroid Ship (Rock). HP: 120, Armor: 4-8, Thrust 1-3, Jump 1-3, Turrets: 1-2 hidden. Weapons: Pulse/Beam Lasers, Sandcasters, Missile Racks.",
            10: "Laboratory Ship (Type-L). HP: 160, Armor: 0-4, Thrust 1-3, Jump 1-3, Turrets: 0-4 hidden. Weapons: Pulse/Beam Lasers, Sandcasters, Missile Racks.",
            11: "Patrol Corvette (Type-T). HP: 160, Armor: 4-8, Thrust 4-6, Jump 3-5, Turrets: 2 Triple showing / 0-2 hidden. Weapons: Pulse/Beam Lasers, Sandcasters, Missile Racks.",
            12: "Subsidized Merchant (Type-R). HP: 160, Armor: 0-4, Thrust 1-3, Jump 1-3, Turrets: 0-4 hidden. Weapons: Pulse/Beam Lasers, Sandcasters, Missile Racks.",
            13: "Survey Scout (Donosev-Class). HP: 160, Armor: 0-4, Thrust 2-4, Jump 3-5, Turrets: 0-4 hidden. Weapons: Pulse/Beam Lasers, Sandcasters, Missile Racks. Modular Cutter docked.",
            14: "Mercenary Cruiser (Type-C). HP: 320, Armor: 4-8, Thrust 3-5, Jump 3-5, Turrets: 8 Triple. Weapons: Pulse/Beam Lasers, Sandcasters, Missile Racks. 2x Modular Cutter docked.",
        }
    @staticmethod
    def getRandomCustomMutations():
        return {
        1:"Psychic Powers: The character gains Psi 7 or +3 to his current Psi if he is already a psion.",
        2:"Natural SONAR: The character is aware of objects in a 10 meter radius as if able to see them.",
        # 4:"Additional Eyes*: The character gains +1 DM to Recon checks and has 360 degrees vision.",
        3:"Palm Mouths*: The mouth is extremely sensitive and can recognize most chemicals by taste. It is impossible to be poisoned through palm mouths. Some palm mouths can also speak.",
        # 6:"Poison Salvia: The character's bite poisons the victim with neurotoxins in addition to causing its normal mechanical damage. The character can also use their saliva to poison melee weapons.",
        4:"Super Digestion: The character can eat almost anything, organic or not, and survive for hours without oxygen.",
        # 8:"Second head*: +2 DM to Recon checks. Head can have separate personality and stay awake when the original head sleeps.",
        5:"Additional limb*: Can hold an additional item; +2 to STR and END.",
        6:"Tough skin: The character has natural armor of +1 to +3.",
        7:"Ageless cells: The character does not age naturally. Unless killed by injury or disease, he can live forever.",

        # 2:"Tiny Mouth: It is very difficult to understand what the character says. His bite attacks deal only 1 point of damage.",
        # 3:"One eye: The character suffers –1 DM to all Recon checks and has 90 degrees vision.",
        # 4:"Alien Hand: At least once per day, the character's hand acts independently of the character, often against him or his friends.",
        # 5:"Inhumanity: The character is inhuman in some subtle but disturbing way. This grants +1 DM to intimidation checks and –1 DM to all other social checks.",
        8:"Hermaphrodite: The character has both male and female sexual organs and characteristics.",
        # 7:"Joined Feet: The character's lower body part resembles that of a snake, only without the snake's grace and dexterity. The character always moves at half speed and suffers –2 Dex.",
        # 9:"Cancer: The character has cancer.",
        # 10:"Soft Body: All hits inflict two additional points of damage.",
        # 11:"Body Part Atrophies: The character is unable to use a body part. 1–2: Leg. 3–4: Hand. 5–6: Tongue.",

        # 2:"Bat Ears: The character is aware of objects in a 10 meter radius as if able to see them.",
        # 3:"Leathery Wings: Player Character can fly clumsily.",
        # 4:"Sabre teeth: The character's bite attack inflicts 2d6 points of damage.",
        # 5:"Feline Claws: The character's unarmed attacks inflict additional three points of damage.",
        # 6:"Rhino Hide: The character has natural armor 2.",
        # 7:"Bull Horns: The character can gore his enemies. This attack is done with –2 DM and inflicts 2d6+3 points of damage.",
        # 8:"Horse Hooves: –1 DM to Stealth checks.",
        # 9:"Porcupine Quills: Unarmed attacks against the character inflict three points of damage on the attacker. The character can strike foes with his quills. This inflicts 1d6 points of damage and –2 DM to all attacks due to the pain caused by broken quills lodged in the target's flesh. The negative DMs are not cumulative.",
        # 10:"Tiger Fur: It is handsome and pleasant to the touch but offers no additional advantages.",
        9:"Sharp Senses: The character gains +1 DM to all Recon checks.",
        
        10:"Frog Tongue: The character can move light objects with his tongue.",
        # 4:"Jellyfish tentacles: The tentacles can whip enemies for 1d6+3 points of damage. This attack ignores armor.",
        11:"Chameleon Skin: The character's skin changes color and texture to match the surrounding environment. When completely nude, the character enjoys +3 DM to Stealth checks. When nude but equipped the DM is reduced to +1.",
        # 8:"Blowfish Inflation: The character can inflate into a huge thorny ball. This can be quite scary for unprepared observers. Also, this makes the character float/hover for a limited period of time.",
        12:"Shark Jaws: The character's bite attack inflicts 1d6+3 points of damage.",
        13:"Gills: The character can freely breathe underwater.",

        14:"Cockroach Stamina: The character gains +2 End. It takes double a radiation dose to damage it (see page 141 in the Traveller Core Rulebook).",

        15:"Subdermal armor (Already got, reroll): +1 to +3 to armor. Stacks with other armor.",
        16:"Cybernetic Eyes Infrared vision and +1 to Recon checks.",
        17:"Titanium Bones: +2 End.",
        18:"Mechanic Arms: +2 Str.",
        19:"Voice Modulator: The character can perfectly mimic the voice of any person he has heard speaking.",
        20:"Hydraulic Jaws: The character can bite for 1d6+6 points of damage. Attack is made with –2 DM.",
        # 11:"Brain Computer: See page 89 in Traveller Core Rulebook.",
        21:"Re-roll Twice: This option can be rolled only once. Ignore on further rolls.",
        }
    @staticmethod
    def getRandomCustomMutationsForOffspring():
        return {

        11:"Psychic Powers: The character gains Psi 7 or +3 to his current Psi if he is already a psion.",
        12:"Natural SONAR: The character is aware of objects in a 10 meter radius as if able to see them.",
        13:"Second head*: +2 DM to Recon checks. Head can have separate personality and stay awake when the original head sleeps.",
        14:"Additional limb*: Can hold an additional item; +2 to STR and END.",
        15:"Alien Hand: At least once per day, the character's hand acts independently of the character, often against him or his friends.",
        
        16:"Inhumanity: The character is inhuman in some subtle but disturbing way. This grants +1 DM to intimidation checks and –1 DM to all other social checks.",
        21:"Hermaphrodite: The character has both male and female sexual organs and characteristics.",
        22:"Joined Feet: The character's lower body part resembles that of a snake, only without the snake's grace and dexterity. The character always moves at half speed and suffers –2 Dex.",
        23:"Soft Body: All hits inflict two additional points of damage.",
        24:"Bat Ears: The character is aware of objects in a 10 meter radius as if able to see them.",
        25:"Leathery Wings: Player Character can fly clumsily.",
        26:"Sabre teeth: The character's bite attack inflicts 2d6 points of damage.",
        
        31:"Feline Claws: The character's unarmed attacks inflict additional three points of damage.",
        32:"Rhino Hide: The character has natural armor 2.",
        33:"Bull Horns: The character can gore his enemies. This attack is done with –2 DM and inflicts 2d6+3 points of damage.",
        34:"Horse Hooves: –1 DM to Stealth checks.",
        35:"Porcupine Quills: Unarmed attacks against the character inflict three points of damage on the attacker. The character can strike foes with his quills. This inflicts 1d6 points of damage and –2 DM to all attacks due to the pain caused by broken quills lodged in the target's flesh. The negative DMs are not cumulative.",
        36:"Tiger Fur: It is handsome and pleasant to the touch but offers no additional advantages.",

        41:"Turtle Shell: armor 5 but speed is halved.",
        42:"Jellyfish tentacles: The tentacles can whip enemies for 1d6+3 points of damage. This attack ignores armor.",
        46:"Blowfish Inflation: The character can inflate into a huge thorny ball. This can be quite scary for unprepared observers. Also, this makes the character float/hover for a limited period of time.",
        51:"Shark Jaws: The character's bite attack inflicts 1d6+3 points of damage.",
        52:"Crocodile Physique: Combines scales, gills and shark jaws.(Scales: armor 1, hark Jaws: The character's bite attack inflicts 1d6+3 points of damage, Gills: The character can freely breathe underwater.)",

        53:"Grasshopper feet: +4 DM to Athletics (Co-ordination) checks.",
        54:"Barkskin: The character gains armor 4 but becomes highly flammable.",
        61:"Centipede Body: +2 Stealth, –2 Dex. The character is always considered prone for the purpose of determining combat DMs.",
        65:"Barbs: Unarmed attacks against the character inflict 1d6 points of damage to the attacker. Unarmed attacks by character cause 3 more points of damage.",
        66:"Ant Mandibles: Bite inflicts 2d6+3 points of damage",

         }

    @staticmethod
    def getCustomLifeEventsInSpace():
        return {
            55: "The Player Characters pass through a wormhole, finding themselves in a bizarre and deadly sector. Getting back home, either with the help of the demented natives or by navigating a series of wormholes will not be easy... Development: Wormhole (page 43).", 
        }
    @staticmethod
    def getCustomLifeEventsPlanetside():
        return {

        }
    @staticmethod
    def getCustomLifeEventsAll():
        return {
            # 11: "A Player Character is confronted by a woman who claims that he is the father of her child.",
            # 12: "As for previous (A Player Character is confronted by a woman who claims that he is the father of her child.), only the Player Character has never seen the woman in his life and yet tests show that the child is really his.", 
            # 13: "A person one of the Player Characters is dating turns out to be controlled by an alien organism. Who is it that the character fell in love with, the person or the alien? What does the alien want? Why was the character chosen of all people?", 
            # 14: "A Player Character reunites with a long-lost pet, now an uplifted animal actually smarter than his previous owner.", 
            # 15: "One of the Player Characters' younger brother comes of age and insists on joining a very dangerous expedition. If banned, he sneaks into the ship and hides in a crate until it is too late to turn back.", 
            # 16: "The Player Character's parents go out of their way to make their son or daughter an interstellar success story, including signing deadly mission contracts in their name and spreading outrageous rumours about his exploits.", 
            # 21: "The Player Characters are hired to investigate a secret slavers ring only to find out that it is run by one of their favorite uncles.",
            # 22: "The group protects a relative or spouse of one of the Player Characters from mysterious and powerful assassins who hunt him all over space. Slowly, it turns out that the hunted person has done horrible things on the scale of war crimes or serial killing in his past.", 
            # 23: "A Player Character's spouse commits suicide while he is away on a mission. There is neither a suicide note, nor a clear cause for this tragic death.", 
            # 24: "As for previous (A Player Character's spouse commits suicide while he is away on a mission. There is neither a suicide note, nor a clear cause for this tragic death.), only the Player Character's enemies use the opportunity to frame him for the 'murder'.", 
            # 25: "A Player Character's great-grandfather dies and leaves behind an extremely bizarre testament, bequeathing all his possession to whoever completes a series of strange missions.", 
            # 26: "As for previous (A Player Character's great-grandfather dies and leaves behind an extremely bizarre testament, bequeathing all his possession to whoever completes a series of strange missions.), only these seemingly random missions are in fact designed to re-activate an ancient death machine the deranged old man believed to be a dead god. This can be deduced from his cryptic diary.", 
            # 31: "A Player Character's new father-in-law is an eccentric but brilliant engineer who keeps coming up with devices that are as likely to save his life as they are to disintegrate him. He tends to forget mentioning the second half of the deal to Player Characters.",
            # 32: "A Player Character's spouse or child have become heavily indebted to the sort of people who believe that if one cannot set a good example of paying on time, one should become a horrible warning.", 
            # 33: "A Player Character's estranged father is a brutal tyrant responsible for heinous war crimes and heading one of the most oppressive regimes in the galaxy. Despite the Player Character having nothing to do with his father's crimes, he may still find himself the target of unwanted media attention or vengeful dissidents.", 
            # 34: "Memories of an abusive father suddenly begin to disturb a Player Character's dreams. The memories progress nightly, revealing the gentle and loving father is in fact a monstrous deviant.", 
            # 35: "As for previous (Memories of an abusive father suddenly begin to disturb a Player Character's dreams. The memories progress nightly, revealing the gentle and loving father is in fact a monstrous deviant.), only the memories were planted by the Player Character's enemies.", 
            # 36: "Two Player Characters find out they are siblings.", 
            # 41: "The Player Character's twin brother is an infamous womanizer and scoundrel. His ill reputation keeps harming the Player Character's career.",
            # 42: "When the smoke of a bloody battle with pirates clears, the Player Character finds among the dead his beloved kid brother whom he encouraged to go into space and make something of himself.", 
            # 43: "One Player Character discovers that another Player Character has killed someone very close to him (such as a parent or a sibling) many years ago.", 
            # 44: "An old friend from a Player Character's wilder days informs them that a mutual friend was killed by the Aslan mafia. The man is gathering the old gang for retaliation against the Aslans.", 
            # 45: "A Player Character receives a message from home informing him that a suitable wife has been found for him and that he is to return for the marriage ceremony as soon as possible. Refusal will result in a scandal, loss of family financing and possibly contacts or allies.", 
            # 46: "A Player Character's wife turns out to be his sibling.", 
            # 51: "Same as previous (A Player Character's wife turns out to be his sibling.), only the discovery is a plot by the Player Character's enemies.",
            # 52: "A distant relative dies, living a huge inheritance for a Player Character to collect. While huge, the inheritance is largely useless, basically being a colossal collection of junk. Still, it is possible some interesting items found their way into the massive heap as well.", 
            # 53: "Same as previous (A distant relative dies, living a huge inheritance for a Player Character to collect. While huge, the inheritance is largely useless, basically being a colossal collection of junk. Still, it is possible some interesting items found their way into the massive heap as well.), only there is no inheritance, this is a plot by the Player Character's enemies to lure him into a trap.", 
            # 54: "Same as event 52 (A distant relative dies, living a huge inheritance for a Player Character to collect. While huge, the inheritance is largely useless, basically being a colossal collection of junk. Still, it is possible some interesting items found their way into the massive heap as well.), only the relative is not dead, just wants to speak of some important matter. He believes this is the only way to lure in his estranged relative.", 
            # 55: "Same as event 52 (A distant relative dies, living a huge inheritance for a Player Character to collect. While huge, the inheritance is largely useless, basically being a colossal collection of junk. Still, it is possible some interesting items found their way into the massive heap as well.), only receiving the inheritance requires the completion of a mission... and there is competition from other relatives.", 
            # 56: "A friend or a relative commits suicide after a personal tragedy. The note only says 'UPGRADE'. Investigation will reveal the man has uploaded his conscience into an android and went about killing the people he considers are responsible for the tragedy.", 
            # 61: "A childhood friend of a Player Character has received an e-mail from Chatter saying 'big misteak, now i koleckt'. Well aware of the crazed killer's reputation, the friend hysterically calls the Player Characters to come and protect him. This is most probably a hoax and the man is wasting the group's time.",
            # 62: "Natives have eaten a Player Character's anthropologist sibling. Another sibling, a bookish and harmless person, is obsessed with avenging the anthropologist's death. If left to his own devices, he will not survive a day in the alien wilderness that claimed the anthropologist's life.", 
            # 63: "Same as previous, only the sibling was not eaten but has gone native and joined the tribe. After many years of separation, combined with the natives' tattoos and body modification rituals, it is likely the Player Character will not be able to recognise his sibling at first sight.", 
            # 64: "A Player Character accidentally runs into a long-lost sibling or child, a pathetic homeless junkie willing to do anything for his next fix.", 
            # 65: "The Player Character meets a kid who is suspiciously similar to him. The kid grew in an orphanage and never knew his mother. He can't tell his exact age either.", 
            # 66: "While exploring an alien wilderness, the Player Character encounters his childhood pet... who has been dead for more than a decade.", 

            # 11: "Assassins are after the character for damage done to their organization years ago.",
            # 12: "Same as previous (Assassins are after the character for damage done to their organization years ago.), only this is a case of mistaken identity.", 
            # 13: "Shadowy monsters the Player Character used to have nightmares about as a child start reappearing. This time they are real, tangible and murderous.", 
            # 14: "A Player Character wakes up one morning, feeling a body part is no longer his own. After 1d6 days the body part begins to act autonomously and a new body part feels alien. 1–3: This is a psychological condition. 4–6: This is an alien virus.", 
            # 15: "Records show the Player Character has been dead for more than 13 years.", 
            # 16: "An arrest warrant is issued for a crime the Player Character has committed more than two decades ago while intoxicated.", 
            # 21: "The Player Character's ex-wife or ex-girlfriend appears with a court order ordering him to pay her exuberant retroactive alimonies.",
            # 22: "A combat wound reveals a horrible secret; the Player Character is not a human being but an alien replica. What happened to the original and does the Player Character really want to be replaced by his 'real self'?", 
            # 23: "As for previous (A combat wound reveals a horrible secret; the Player Character is not a human being but an alien replica. What happened to the original and does the Player Character really want to be replaced by his 'real self'?), only the Player Character is a robot that can be turned off by its operators any minute.", 
            # 24: "A Player Character begins to slowly transform into a hideous mutant (page 164). Apparently, his mother was not perfectly honest with him about his father's identity.", 
            # 25: "A Player Character feels compelled to go to a faraway unexplored planet. Once there, he discovers he was injected with alien genes as part of an experiment by the aliens.", 
            # 26: "Same as previous (A Player Character feels compelled to go to a faraway unexplored planet. Once there, he discovers he was injected with alien genes as part of an experiment by the aliens.), only the aliens are not interested in mere observation or family reunions. They want the character to go back and steal weapons and secrets for them.", 
            # 31: "A female character discovers she is pregnant. 1–5: The baby is normal. 6: There is something wrong with the baby.",
            # 32: "The Player Character begins to have vile and perverse urges. Occasionally the urges will become so strong that the character will have no choice but to act according to them. The situation will persist until the Player Character discovers the trauma that caused this condition and deals with it.", 
            # 33: "Strange events happening to a Player Character begin to shake his confidence in the reality of the world around him. Investigation will reveal the character is an alter-ego created by a powerful psion lying in a coma in a distant hospital.", 
            # 34: "Chatter (page 159) is after the Player Character. Although the maniac is still many light years away, everyone is already talking about the character in past tense.", 
            # 35: "A review by an institute the Player Character attended finds out he never graduated and thus is not qualified to use one of his skills.", 
            # 36: "The Player Character contracts an exotic disease (page 108).", 
            # 41: "The Player Character begins to experience regular hallucinations. 1–3: He was poisoned. 4–6: An alien being is trying to communicate with him.",
            # 42: "The Player Character has a sudden urge to swim in space. This urge intensifies to the point of the Player Character having to be restrained. The reason is a colossal alien (page 35) who wants to form a symbiotic bond.", 
            # 43: "A prestigious news network is shooting an episode about travellers and one of the Player Characters is invited for an interview. Some of the questions asked will touch upon subjects the Player Character would rather have remained hidden.", 
            # 44: "Player character wakes up in a coffin, buried alive by his enemies. His friends only have a few hours to rescue him before he suffocates to death.", 
            # 45: "A bump to the head causes the Player Character to experience temporary amnesia.", 
            # 46: "The Player Character starts receiving ominous messages from a person he killed a few months ago. 1–3: The man had a pirate brother. 4–6: The man uploaded his personality to his computer a few weeks before his death.", 
            # 51: "While exploring the graveyard of a remote alien village, the Player Character notices a gravestone bearing his name and birth date. The death date is today.",
            # 52: "The Player Characters have the same continuous dream each night. As time passes, it becomes less and less clear which life is real and which one is dreamed.", 
            # 53: "The Player Character begins to slowly turn into a cockroach. No one else notices the gruesome transformation. 1–3: This is the result of mental illness. 4–6: A psionist is playing with the Player Character's mind.", 
            # 54: "Ancient aliens possess the Player Character (page 14).", 
            # 55: "The Player Character begins to have flashbacks of himself committing horrible crimes. This is especially alarming since the flashbacks seem to take place in a time the character was doing a lot of drugs and was not aware of many of his actions.", 
            # 56: "An ally and a good friend of the Player Character is accused of crimes the Player Character has committed.", 
            # 61: "The Player Character discovers his greatest enemy is his biological father.",
            # 62: "Same as previous (The Player Character discovers his greatest enemy is his biological father.), only this is a baseless rumor.", 
            # 63: "The Player Character discovers that alien parasites lodged into his brain are responsible for many of his decisions over the years.", 
            # 64: "The Player Character is diagnosed with a debilitating condition such as multiple sclerosis or chronic fatigue syndrome.", 
            # 65: "A fortune teller at a festival examines the Player Character's palm, becomes visibly shaken and then runs away screaming 'the end is nigh'!", 
            # 66: "The Player Character becomes insanely attracted to someone inappropriate. 1–2: A commander or patron. 3–4: An alien with a very different anatomy. 5–6: A hated enemy.", 

            11: "The Player Characters wake up naked in a dark cell. Agonized screams ring across the halls and voices obviously not human are heard outside. Development: Illegal research facility.",
            12: "The Player Characters are ambushed by the police as they are walking down the street in their hometown. Someone has framed them for murder and they must act quickly before the entire might of the Imperium lands on their heads. Development: Urban Investigation.", 
            13: "Gangsters have kidnapped someone very close to one or more of the Player Characters and demands the Player Characters complete a very dangerous and illegal mission in return for this person's release. Development: Criminal mission, Espionage mission.", 
            14: "A terrorist attack transforms a building the Player Characters are visiting into a flaming death trap. Without plans of the building or any special equipment they must escape the inferno, battling terrorists and rescuing survivors along the way. Development: Urban disaster.", 
            15: "A programming bug causes all robots working in a nearby workshop to go on a murderous rampage. This hook is especially deadly if the Player Characters happen to be visiting the factory at the time of the uprising. Development: Industrial mishap.", 
            16: "A nearly unstoppable robot assassin is dispatched to murder the Player Characters. They have no idea who could have sent it or why. Development: Chatter (page 159), Mistaken Identity", 
            21: "The Player Characters' spacecraft breaks down and is forced to crash land on an uncharted planet. They must improvise some way to escape the planet while dealing with deadly nature, bizarre natives or mysterious ruins. Development: Wilderness events.",
            # 22: "The Player Characters wake up 1,000 years into the past. What is going on and how do they get back?! Development: Wormhole (page 43), Alien Probe (page 32).", 
            # 23: "The Player Characters literally fall from the sky into the adventure site. Development: Higher Entity (page 36), Living Planet (page 37).", 
            24: "One or more of the Player Characters has a dream about a peace-loving alien species suffering at hands of ruthless bandits. Investigation will reveal the planet seen in the dream is a real, though unexplored, location. Development: Khudrian (page 152).", 
            25: "One or more of the Player Characters wakes up one morning with the intuitive notion that today something horrible will happen to someone they love. As the day progresses, ever more specific visions begin to assail the Player Characters. Development: Any impending disaster.", 
            # 26: "A nuclear explosion followed by an alien invasion shakes the city the Player Characters are currently staying in. Even if the Player Characters do not feel like being the heroes and saving the day, they must still somehow escape the ruined city. Development: Invasion (page 14).", 
            31: "The Player Characters are exposed to an alien virus that causes them to rapidly mutate and develop superpowers even as their bodies begin to fail. Fearing mass infection, they are barred from returning home and must find the cure on their own. Development: Mutation (page 164), Mission to the Wilderness (page 105).",
            # 32: "The Player Characters wake up to find themselves inhabiting the bodies of other people. Where are their bodies, who is responsible and why? Development: Psychopath (page 155).", 
            33: "The child of one of the Player Characters does not want to go to school. With every passing day, his resistance grows stronger, even as his health decreases and strange marks begin to appear on his body. Development: Vampiric aliens run the school.", 
            34: "War has been declared and everyone has been drafted. Deserters will be shot by the military! Heroes will be shot by the enemy! Good luck, trooper! Development: Military mission.", 
            35: "The Player Characters are kidnapped and released into some deadly environment by a powerful alien who announces he will now hunt them for his entertainment. Development: Wilderness events (page 24) and Hunting Party (page 28).", 
            36: "Someone close to the Player Characters dies from a heart attack. Hours before his death he sent them a message – 'come ASAP, you won't believe what I've just discovered!' Development: Corporate Corruption, Secret Military Base (page 27).", 
            41: "An immoral scientist cons the army into infecting a group of elite soldiers with a virus that cause them to give in to their basest urges. Now the city is swarming with raping and murdering madmen. The hotel the Player Characters are staying in has remained an island of sanity in an ocean of madness – but for how long? Development: Zombie Apocalypse (page 16).",
            42: "While flying through space, the Player Characters encounter an extremely xenophobic religious community that claims the Player Characters have broken some religious edict and now must perform a mission to atone. They take hostages. Development: Cultists (page 49).", 
            43: "A decoy distress call draws the Player Characters into an elaborate trap set up by pirates working under the umbrella of corrupt imperial officials. Development: Pirates (page 54), Vargr Raiders (page 58).", 
            44: "Grotesque visages appear in windows as the Player Characters are walking down the street. Horrible faces blink on screens. Strange voices occasionally echo in electronic communication. More and more random acts of violence happen in the neighborhood. Development: Dormant Alien (page 12) about to wake up.", 
            45: "A suicide bombing injures the Player Characters and kills someone close to them. A shadowy political organization offers to assist them in avenging the deaths of their loved ones. Development: Military mission, political mission.", 
            46: "The Player Characters' ship is rocked by a mysterious explosion and is forced to land on a wild, uncharted planet that appears to be devoid of sentient life. Development: Living Planet (page 37) or Wilderness Events (page 24).", 
            51: "An unexplained space phenomenon transports the Player Characters' ship to another galaxy. Soon they encounter bizarre and extremely advanced aliens who could become the Player Characters' saviors or undertakers. Development: Wormhole (page 43).",
            52: "A strange unidentified object is moving at tremendous speed toward the world the players are currently staying on. Since no Imperial ships can reach the system before its arrival, the Player Characters are asked to intercept and investigate it. Development: Asteroid or Alien Probe (page 32).", 
            53: "A radical animal rights group releases all the animals in the city zoo, not realizing that many of them are powerful aliens capable of immense destruction. Development: Animals (69 in Traveller Core Rulebook).", 
            # 54: "A goblin in a funny hat comes to the Player Character and informs him that he was chosen as the Duke of the Realmunder- Sewage and must now release his kingdom from the evil of the fearsome Kadaiff. Development: Mythological Monsters (page 30) in Tunnels.", 
            55: "The Player Characters pass through a wormhole, finding themselves in a bizarre and deadly sector. Getting back home, either with the help of the demented natives or by navigating a series of wormholes will not be easy... Development: Wormhole (page 43).", 
            56: "A meeting with a potential patron turns out to be a trap. The 'patron' is a slaver who drugged the Player Characters' drinks. They wake on a slave ship headed to a mine on an otherwise uninhabited planet. Development: Slavers (page 28).", 
            61: "The Player Characters hear a shot in an alley. Running to investigate, they find a young man who just shot himself. An SMS appears on his mobile phone. It's for them. Development: Psychopath (page 155), alien conspiracy (page 86)",
            62: "Hiver degenerates kidnap the Player Characters and a score of other sophonts and conjoin them together in a perverse imitation of Siamese twins before dropping them off in the wilderness of an unknown planet. Development: Wilderness Events (page 24).", 
            63: "Someone close to the Player Characters has a huge gambling debt to the mafia. If the situation is not resolved in some way in 72 hours this person will be murdered. Development: Criminal mission.", 
            64: "An infamous serial killer sends a video to the news in which he informs them the Player Characters will become his next victims. Development: Psychopath (page 155) or Chatter (page 159).", 
            65: "A dying woman crawls with her last strength to one of the Player Characters and whispers 'Please! Take care of Verom...' before succumbing to her multiple wounds. The only clue is crumpled note with a hand-written address. Development: Lost child (page 29) and Alien Conspiracy (page 86) or Organized Crime (page 90).", 
            66: "A Player Character receives a panicked call from a family member in need. The message is not clear but it seems the speaker is in great danger. Development: The man has made a surprising discovery (page 12) and is now hunted by religious fanatics.", 
            }
    @staticmethod
    def getTable(tableName):
        table = None
        # Custom Tables
        if tableName.lower() in ["in media res bios", "in media res biologicals", "in media res sur", "in media res surrogate"]: 
            table = CustomTables.getBiologicalsInMediaRes()
        elif tableName.lower() in ["in media res hunt"]: 
            table = CustomTables.getBountyHunterInMediaRes()
        elif tableName.lower() in ["in media res wildwest", "in media res wild west"]: 
            table = CustomTables.getWildWestInMediaRes()
        elif tableName.lower() in ["wild west town events", "wildwest town events", "wild west town encounters""wildwest town encounters"]: 
            table = CustomTables.getWildWestTownEvents()
        elif tableName.lower() in ["wild west adventure hooks", "wildwest adventure hooks"]: 
            table = CustomTables.getWildWestAdventureHooks()
        elif tableName.lower() in ["wild west townsfolk", "wildwest townsfolk"]: 
            table = CustomTables.getWildWest36TownsFolk()
        elif tableName.lower() in ["bounty information"]: table = CustomTables.getBountyInformation()
        elif tableName.lower() in ["bounty value"]: table = CustomTables.getBountyValue()
        elif tableName.lower() in ["bounty hunter life events"]: table = Tables.getBountyHunterGenerationsLifeEvents()
        elif tableName.lower() in ["random system ship"]: table = CustomTables.getRandomSystemLimitedShips()
        elif tableName.lower() in ["random interstellar ship", "random ship"]: table = CustomTables.getRandomInterstellarShips()
        elif tableName.lower() in ["custom mutations"]: table = CustomTables.getRandomCustomMutations()
        elif tableName.lower() in ["offspring mutations"]: table = CustomTables.getRandomCustomMutationsForOffspring()
        elif tableName.lower() in ["custom life events"]: table = CustomTables.getCustomLifeEvents()
        # elif tableName.lower() in []: table = CustomTables.get()
        # elif tableName.lower() in []: table = CustomTables.get()
        else: 
            print("Table not present")
        return table
    @staticmethod
    def getTableNameList():
        return [
            "\"in media res bios\": Start a space adventure with Profession: Biologicals.",
            "\"in media res hunt\": Start a space adventure with a Bounty Hunt.",
            "\"in media res wildwest\": Start a space adventure with a Bounty Hunt.",
            "\"wildwest town events\": ",
            "\"wildwest adventure hooks\": ",
            "\"wildwest townsfolk\": ",
            "\"bounty information\": ",
            "\"bounty value\": ",
            "\"bounty ship\": ",
            "\"random system ship\": ",
            "\"random ship\": ",
            "\"custom mutations\": ",
            "\"offspring mutations\": ",
            "\"custom life events\": ",
            # "\"ship\": ",
            # "\"ship\": ",
            # "\"ship\": ",
            ]
    @staticmethod
    def displayTable(table):
        for row in table:
            if ( isinstance(table[row], list) ):
                text = ""
                for i in table[row]:
                    text += "{}, ".format(i)
                text = text[:-2]
                TerminalUtils.pprint("{0:>2}: {1}".format(str(row), text), indent=4)
            elif ( isinstance(table[row], dict) ):
                print(row)
                TerminalUtils.displayTable(table[row], indent=4)
            else:
                TerminalUtils.pprint("{0:>2}: {1}".format(str(row), str(table[row])), indent=4)

'''
This will have lookup tables. a lot. 
'''

def usage():
    print("python tables.py -t <tableName> [-r [#]] [-p #]")
    print('python tables.py -r -t "world encounter" --pick 3')
    print("Table Names:")
    for table in Tables.getTableNameList():
        print("  {}".format(table))
    for table in CustomTables.getTableNameList():
        print("  {}".format(table))
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvt:rs:xp:n", ["help", "table=", "seed=", "pick="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    seed = None
    tableName = None
    roll_from_table = False
    roll = None
    hideTable = False
    no_repeat = False
    pick_number=1
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-s", "--seed"):
            seed = a
        elif o in ("-t", "--table"):
            tableName = a
        elif o in ("-x", "--hide"):
            hideTable = True
        elif o in ("-r", "--roll"):
            roll_from_table = True
            if a is not None and a != "":
                roll = int(a)
        elif o in ("-p", "--pick"):
            pick_number=int(a)
        elif o in ("-n", "--no-repeat"):
            no_repeat = True
        else:
            assert False, "unhandled option"
    table = Tables.getTable(tableName)
    custom_table = CustomTables.getTable(tableName)
    if table is None and custom_table is not None: 
        table = custom_table
    if not hideTable: 
        Tables.displayTable(table)
        print("")
    if (roll_from_table and table is not None):
        rolled_values = []
        for i in range(pick_number):
            row=None
            while row is None or (row in rolled_values and no_repeat):
                row = random.choice(list(table.keys()))
            if roll is not None and i == 0:
                row = roll
            rolled_values.append(row)
                
            

            TerminalUtils.pprint("Roll: [{}]: {}".format(str(row), str(table[row])), width=100, indent=4)
if __name__ == "__main__":
    main()