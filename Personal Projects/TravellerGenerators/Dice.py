import random
import os, sys, getopt
class Dice:
    def __init__(self, range=[0,1], min=1):
        self.base = min
        self.min_range=range[0]
        self.max_range=range[1]
    def __str__(self):
        return "{0}-{1}".format(self.base+self.min_range, self.base+self.max_range)
    def roll(self):
        if (self.min_range < self.max_range):
            return random.randint(self.min_range,self.max_range)+self.base
        return self.base
    def set_from_str(self,dice_str="0-2"):
        dice_str_arr=dice_str.split("-")
        try:
            #print(dice_str_arr[0])
            #print(dice_str_arr[1])
            self.base = int(dice_str_arr[0])
            self.min_range=int(dice_str_arr[0])-self.base
            self.max_range=int(dice_str_arr[1])-self.base
        except:
            pass
    @staticmethod
    def total_up(dice_list=[]):
        dice = Dice()
        dice.base = 0
        dice.min_range=0
        dice.max_range=0
        if(len(dice_list) > 0):
            for d in dice_list:
                if d is not None:
                    dice.base+=d.base
                    dice.min_range+=d.min_range
                    dice.max_range+=d.max_range
        return dice

class Card(object):
    # https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
    NAME_TO_SYMBOL = {
        'Spades':   '♠',
        'Diamonds': '♦',
        'Hearts':   '♥',
        'Clubs':    '♣',
        'Joker':    'J',
    }
    CARD_VALUES = {
        'Ace': 11,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
        'Joker': 0
    }
    CARD = ("┌─────────┐"
            "│{rank: <2}       │"
            "│         │"
            "│         │"
            "│    {suit: <2}   │"
            "│         │"
            "│         │"
            "│       {rank: >2}│"
            "└─────────┘")
    HIDDEN_CARD = ( "┌─────────┐"
                    "│░░░░░░░░░│"
                    "│░░░░░░░░░│"
                    "│░░░░░░░░░│"
                    "│░░░░░░░░░│"
                    "│░░░░░░░░░│"
                    "│░░░░░░░░░│"
                    "│░░░░░░░░░│"
                    "└─────────┘")
    def __init__(self, suit, rank, flipped=False):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.CARD_VALUES[rank]
        self.flipped=flipped
        self.card_face = ["┌─────┐",
        f"│{self.rank:<5}│",
        f"│  {Card.NAME_TO_SYMBOL[self.suit]}  │",
        f"│{self.rank:>5}│",
        "└─────┘"]
        self.card_back = ["┌──────┐",
            "│░░░░░░│",
            "│░░░░░░│",
            "│░░░░░░│",
            "└──────┘"]
    def code(self):
        rank = "T" if (self.rank=='10') else str(self.rank)[0]
        return f"{rank}{str(self.suit)[0]}"
    def get_card_face_as_string(self):
        text = ""
        if self.flipped:
            for line in self.card_back:
                text += line+"\n"
        else:
            for line in self.card_face:
                text += line+"\n"
        return text
    def __str__(self): return f"{self.rank} of {self.suit}"
    @staticmethod
    def get_standard_playing_list(include_jokers=False):
        suits=["Diamonds","Spades","Clubs","Hearts"]
        numbers=['Ace', '2',  '3', '4', '5',  '6', '7',  '8',  '9', '10', 'Jack', 'Queen', 'King']
        cards=[]
        for suit in suits:
            for number in numbers:
                cards.append(Card(suit, number))
        if include_jokers:
            cards.append(Card("Joker","Joker"))
            cards.append(Card("Joker","Joker"))
        return cards

def dice_test():
    dice = Dice()
    dice.set_from_str("2-4")
    print(dice)
    print("roll: "+str(dice.roll()))
    print("roll: "+str(dice.roll()))
    print("roll: "+str(dice.roll()))
    dice.set_from_str("0-2")
    print(dice)
    print("roll: "+str(dice.roll()))
    print("roll: "+str(dice.roll()))
    print("roll: "+str(dice.roll()))
    dice.set_from_str("1-8")
    print(dice)
    print("roll: "+str(dice.roll()))
    print("roll: "+str(dice.roll()))
    print("roll: "+str(dice.roll()))
def main_dice_roller(argv):
    #
    #   python Dice.py -d 2d6 -r 2
    #   python Dice.py -d 1d100 -r 3
    #   python Dice.py -d 1d100 -r 9
    #print ("argv: "+str(argv))
    dice_code=None
    rerolls=1
    card_draws = 0
    include_jokers = False
    try:
        opts, args = getopt.getopt(argv,
            "hjd:r:c:",
            ["dice=", "cards="]
            )
        #print ("Opts done")
    except getopt.GetoptError:
        #print ("Bad arguments.")
        usage()
        sys.exit(2)
    #print("Check opts")
    #
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            exit(0)
        elif opt in ("-d", "--dice"):
            dice_code = arg
            if(dice_code[0]=="d"):
                dice_code = "1"+dice_code
        elif opt in ("-c", "--cards"):
            card_draws = int(arg)
        elif opt in ("-r", "--rerolls"):
            rerolls = int(arg)
        elif opt in ("-j", "--joker"):
            include_jokers = True
        else:
            print("cannot find --opt <arg>")
            usage()
            exit(1)
    if dice_code:
        dice_code_split = dice_code.split("d")
        amount = int(dice_code_split[0])
        varience = int(dice_code_split[1])
        dice = Dice()
        dice.set_from_str("{}-{}".format(1,varience))

        for r in range(rerolls):
            total = 0
            results = ""
            for i in range(amount):
                roll = dice.roll()
                total += roll
                results += f", {roll}"
            results = results[2:]

            print(f"Dice Code: {dice_code}. Total: {total}. Rolls: {results}.")
    if card_draws > 0:
        cards = Card.get_standard_playing_list(include_jokers=include_jokers)
        random.shuffle(cards)
        random.shuffle(cards)
        for c in range(card_draws):
            card = cards.pop()
            print(str(card))
            print(card.get_card_face_as_string())


    
    #print ("End of Line...")
def usage():
    print("Help:")
    print("""Arguments:
        -h --help <HELP!>
        -h --help <HELP!>
        -h --help <HELP!>
        -h --help <HELP!>
        -h --help <HELP!>
        -h --help <HELP!>
        """)
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main_dice_roller(sys.argv[1:])