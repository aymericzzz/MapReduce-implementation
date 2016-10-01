# -*-coding:Latin-1 -*

import os 

# input reader
# read the input file and store each line in a cell of a list
content = [line.rstrip('\r\n') for line in open('input.txt', 'r')]
print(content)

# input reader