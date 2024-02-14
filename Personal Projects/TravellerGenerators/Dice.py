# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
# 
import random
import os, sys, getopt
class Dice():
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
    dice_code="1d6"
    rerolls=1
    try:
        opts, args = getopt.getopt(argv,
            "hd:r:t:", 
            ["dice="]
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
        elif opt in ("-t", "--timesrolled"):
            print("-t rerolls")
            rerolls = int(arg)
        elif opt in ("-r", "--rerolls"):
            print("-r rerolls")
            rerolls = int(arg)
        else:
            print("cannot find --opt <arg>")
            usage()
            exit(0)
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
            total+=roll
            results +=", {}".format(roll)
        results = results[2:]
        
        print("Dide Code: {}. Total: {}. Rolls: {}.".format(dice_code, total,results))
    
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
    main_dice_roller(sys.argv[1:])
    print("")