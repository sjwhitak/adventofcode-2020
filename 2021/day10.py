import numpy as np
data = open('day10','r').readlines()

# When there's an opening bracket, I need to keep adding more opening brackets
# until I find a closing bracket.
# That closing bracket MUST be the most recent opening bracket

requirements = {"[" : "]", "(" : ")", "<" : ">", "{" : "}"}

corrupted_item = list()
for line in data:

    required_list = []
    for item in line.strip():
        try:
            required_list.append(requirements[item])
        except KeyError:
            if item is required_list[-1]:
                required_list.pop(-1)
            else:
                corrupted_item.append(item)
                break

points = corrupted_item.count(")")*3 \
    +corrupted_item.count("]")*57 \
    +corrupted_item.count("}")*1197 \
    +corrupted_item.count(">")*25137
