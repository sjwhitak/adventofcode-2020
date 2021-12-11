import numpy as np
data = open('day10','r').readlines()

# When there's an opening bracket, I need to keep adding more opening brackets
# until I find a closing bracket.
# That closing bracket MUST be the most recent opening bracket

requirements = {"[" : "]", "(" : ")", "<" : ">", "{" : "}"}

corrupted_item = list()
incomplete_items = list()
total_count_list = list()
for line in data:
    
    
    corrupted = False
    required_list = []
    for item in line.strip():
        try:
            required_list.append(requirements[item])
        except KeyError:
            if item is required_list[-1]:
                required_list.pop(-1)
            else:
                corrupted_item.append(item)
                corrupted = True
                break
            
    # Part 2 -- print the remaining required values
    if not corrupted:
        incomplete = ''.join(required_list)[::-1]
        incomplete_items.append(incomplete)
        
        total_count = 0
        score = {")":1, "]":2, "}":3, ">":4}
        for char in incomplete:
            total_count = 5*total_count + score[char]
        total_count_list.append(total_count)
            

points = corrupted_item.count(")")*3 \
    +corrupted_item.count("]")*57 \
    +corrupted_item.count("}")*1197 \
    +corrupted_item.count(">")*25137

# Part 2 -- find middle
N = len(total_count_list)
total_count_list = sorted(total_count_list)
print(total_count_list[N//2])