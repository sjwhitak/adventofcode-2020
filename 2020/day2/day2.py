import numpy as np

with open('day2', 'r') as fd: # read file
    out = fd.readlines()      # str

# Part 1
strings = [x.split(" ") for x in out]

counter = 0
for string in strings:
    ranges = string[0].split("-")
    minimum = int(ranges[0])
    maximum = int(ranges[1])
    
    letter = string[1][:-1]
    password = string[2]
    
    count = password.count(letter)
    
    if count >= minimum and count <= maximum:
        counter+=1
    
    
#%% Part 2
strings = [x.split(" ") for x in out]

counter2 = 0
for string in strings:
    ranges = string[0].split("-")
    first = int(ranges[0])
    second = int(ranges[1])
    
    letter = string[1][:-1]
    password = string[2]
    
    if (password[first-1] == letter and password[second-1] != letter) or \
       (password[first-1] != letter and password[second-1] == letter):
        counter2 += 1
    