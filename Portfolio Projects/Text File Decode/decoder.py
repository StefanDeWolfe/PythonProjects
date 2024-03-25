import array as arr 
import os
import re
import sys
''' Prompt:
Coding Exercise: Decoding a Message from a Text File
In this exercise, you will develop a function named decode(message_file). This function should read an
encoded message from a .txt file and return its decoded version as a string.
Note that you can write your code using any language and IDE you want (Python is preferred if possible, but
not mandatory).
Your function must be able to process an input file with the following format:

3 love
6 computers
2 dogs
4 cats
1 I
5 you

In this file, each line contains a number followed by a word. The task is to decode a hidden message based on
the arrangement of these numbers into a "pyramid" structure. The numbers are placed into the pyramid in
ascending order, with each line of the pyramid having one more number than the line above it. The smallest
number is 1, and the numbers increase consecutively, like so:

1
2 3
4 5 6

The key to decoding the message is to use the words corresponding to the numbers at the end of each
pyramid line (in this example, 1, 3, and ). You should ignore all the other words. So for the example input file
above, the message words are:

1: I
3: love
6: computers

and your function should return the string "I love computers".
'''

def read_lines_from_file(filename:str):
    lines = []
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def get_pyramid_numbers(value:int): 
    if value < 1:
        return []
    pyramid_depth = 2
    pyramid_indeces = [1]
    while pyramid_indeces[len(pyramid_indeces)-1] < value:
        pyramid_indeces.append((pyramid_depth ** 2 + pyramid_depth)//2)
        pyramid_depth+=1
    return pyramid_indeces

def decode(filename:str):
    lines = read_lines_from_file(filename=filename)
    word_salad = {}
    for line in lines:
        parts = line.split(" ")
        word_salad[int(parts[0])] = parts[1]
    sorted_indexes = sorted(word_salad.keys())
    final_text = ""
    pyramid_indeces = get_pyramid_numbers(value=len(sorted_indexes))
    for index in pyramid_indeces:
        final_text += word_salad.get(index)+ " "
    return final_text.rstrip()


def is_file_valid(filename:str):
    parts = filename.split(".") # ["coding_qual_input", "txt"]
    extension = parts[len(parts)-1]
    if extension in ["txt"]:
        return True
    return False

def usage():
    print("How to use the program:\n"
        "Command: 'python test.py <file.txt>'\n"
        "This program only accepts .txt files, others are invalid and it will not run.\n"
        "Text files MUST be formatted as such:\n"
        "3 love\n6 computer\n2 dogs\n4 cats\n1 I\n5 you\n"
        "No duplicate numbers, a space between a positive integer non-zero and the word.\n"
        "Decode by reading the rightmost word from a sorted pyramid of numbers.\n"
        "  1: I\n 2 3: love\n4 5 6: computers\n"
        "Read as: 1, 3, 6. Final message is: \"I love computers.\""
    )

def main(args:list[str]):
    if len(args) < 1:
        usage()
        exit(1)
    # filename = args[0] # "coding_qual_input.txt"
    if is_file_valid(filename=args[0]):
        print(decode(filename=args[0]))
    else:
        # usage()
        raise ValueError("Expected .txt file in argument got something else instead.")
    

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main(sys.argv[1:])