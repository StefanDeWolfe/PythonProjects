
import heapq
import os
import sys
import math
import time
import typing
from typing import List
'''
you are given a string and an array acting as a dictionary. Return true if the string contains valid words and return false if not.
'catbat' -> ['cat', 'bat'] TRUE
'ctabta' , ['cat', 'bat'] FALSE
'''
class Solution:
    def _rec_word_in_brute(self, current_word: str, dictionary: List[str]):
        for w in dictionary:
            if w.lower() in current_word.lower():
                current_word.replace(w,"")
                return w, current_word

    def word_in_brute(self, word: str, dictionary: List[str]) -> bool:
        '''
        For each word in the dictionary
            compare lowercase word to the string

        :param word:
        :param dictionary:
        :return:
        '''
        words_found = []
        current_word = str(word)
        while current_word != "":
            w, current_word = self._rec_word_in_brute(current_word, dictionary)
            words_found.append(w)


        return len(words_found) > 1, words_found

class Solution2:
    def get_lowerest_positive_int(self, array):
        lowerest_positive_int = 1
        while lowerest_positive_int in array:
            lowerest_positive_int += 1
        return lowerest_positive_int

def main():
    solution = Solution()
    words = ['catbat', 'ctabta']
    dictionary = []
    with open("words.txt") as file:
        dictionary = [line.rstrip() for line in file]
    expected = [True, False]
    for word in words:
        result, wordlist = solution.word_in_brute(word, dictionary)
        print(f"word {word} result {result} Successful?: {result == expected[words.index(word)]}")
        print(wordlist)

def main2():
    solution = Solution2()
    arrays = [ [3, -1, 1], [], [2, 1, 4], [3,4,5], [0,-1,50],  ]
    expected = [ 2, 1, 3, 1, 1, ]
    for array in arrays:
        result = solution.get_lowerest_positive_int(array)
        print(f"array {array} result {result} Successful?: {result == expected[arrays.index(array)]}")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
    main2()