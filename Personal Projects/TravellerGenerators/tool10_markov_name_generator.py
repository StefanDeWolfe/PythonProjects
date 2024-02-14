# Author: Stefan DeWolfe
# Date: 9 / 2022
# Last Modified: 2 / 14 / 2024
import random
"""
This is a psuedo markov name generator.
"""
class PseudoMarkovNameGenerator():
    @staticmethod
    def readLinesFromFile(filename):
        lines = []
        with open(filename) as file:
            lines = file.readlines()
            lines = [line.lower().rstrip() for line in lines]
        return lines
    @staticmethod
    def getName(lines, verbose=False):
        name1 = lines[random.randint(0,len(lines)-1)]
        name2 = lines[random.randint(0,len(lines)-1)]
        part1 = name1[:len(name1)//2] 
        part2 = name2[len(name2)//2:]
        if (verbose): print("{} - {}".format(part1, part2))
        return part1[0].upper() + part1[1:] + part2
if __name__ == "__main__":
    import os, sys
    os.system('cls' if os.name == 'nt' else 'clear')
    lines = PseudoMarkovNameGenerator.readLinesFromFile("surnames.txt")
    for i in range(10):
        print(PseudoMarkovNameGenerator.getName(lines))