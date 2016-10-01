# -*-coding:Latin-1 -*

import os 
from map import map_function

# input reader
# read the input file and store each line in a cell of a list
content = [line.rstrip('\r\n') for line in open('input.txt', 'r')]
print(content)

mapper = map_function(content)
print(mapper)