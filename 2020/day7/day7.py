# -*- coding: utf-8 -*-

import re

with open('day7', 'r') as fd: # read file
    bags = fd.read().splitlines()      # str
    
test = bags[0]

bag_color = test.split(' bags contain ', 1)