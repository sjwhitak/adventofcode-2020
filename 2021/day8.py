import numpy as np


data = open('day8','r').readlines()
part1 = [d.split('|')[1].strip().split(' ') for d in data]


# --- Part 1 ---
# 1 length = 2 segments
# 4 length = 4 segments
# 7 length = 3 segments
# 8 length = 7 segments
lengths = np.array([len(segment) for line in part1 for segment in line])
count = np.sum(np.logical_or(
                 np.logical_or(
                   np.logical_or(lengths == 2, lengths == 4), 
                 lengths == 3),
                lengths == 7))
# --- Part 1 ---
# --- Part 2 ---
seg_display = np.zeros((len(data), 7), dtype=str)

part2 = [d.split('|')[0].strip().split(' ') for d in data]

# Find 1 and 7, this will find "a"
lengths = np.array([len(segment) for line in part2 for segment in line]).reshape((-1, 10))
ones = np.array(part2)[np.array(lengths).reshape((-1, 10)) == 2]
fours = np.array(part2)[np.array(lengths).reshape((-1, 10)) == 4]
sevens = np.array(part2)[np.array(lengths).reshape((-1, 10)) == 3]
eights = np.array(part2)[np.array(lengths).reshape((-1, 10)) == 7]

# First segment found from 1 and 7 compared. This will find 'a'.
for i in range(len(data)):
    for segment in sevens[i]:
        if segment not in ones[i]:
            seg_display[i,0] = segment
            print(''.join(seg_display[i]))
            
# Second segment found with 1 + 7 + 4 mapping a 9
# Must have all of 4, and first segment, then an unknown. This will find 'g'.
for i in range(len(data)):
    for digit in part2[i]:
        
        # Length of 6, narrows down to 0, 6, and 9
        if len(digit) == 6:
            
            # Only 9 will have all segments inside 4
            nine = True
            for segment in fours[i]:
                if segment not in digit:
                    nine = False
                    
            # Find the remaining segment not in 4 nor 'a'.
            # This finds 'g'.
            if nine:
                for segment in digit:
                    if segment not in fours[i]+seg_display[i,0]:
                        seg_display[i,6] = segment
                        print(''.join(seg_display[i]))
            
                        
# Next digit we can find is 0 because we have 'g' and 'a'.
for i in range(len(data)):
    for digit in part2[i]:
        zero = False
        
        # Length of 6, narrows down to 0, 6, and 9
        if len(digit) == 6:
            
            # Only 0 will have all segments inside 'a', 'g', 1, and missing 4.
            zero = True
            
            # Compared 'a', 'g', and 1.
            for segment in ones[i]+seg_display[i,0]+seg_display[i,6]:
                if segment not in digit:
                    zero = False
                    
            # If every segment in 4 is found, then it's not zero.
            count = 0
            for segment in fours[i]:
                if segment in digit:
                    count += 1
            if count == 4:
                zero = False
                    
            if zero:
                # Find the remaining segment not in 4, nor 1, nor 'a' or 'g'.
                # This finds 'e'.
                for segment in digit:
                    if segment not in ones[i]+fours[i]+seg_display[i,0]+seg_display[i,6]:
                        seg_display[i,4] = segment
                        print(''.join(seg_display[i]))
                        
                    # Find the remaining segment in 4, but not in 1.
                    # This finds 'b'.                    
                    if segment in fours[i] and segment not in ones[i]:
                        seg_display[i,1] = segment
                        print(''.join(seg_display[i]))
            

            

# Now, I have 'a', 'b', 'e', and 'g'. We can find all 6's
# This will give us the remaining segments.
for i in range(len(data)):
    for digit in part2[i]:
        
        # Length of 6, narrows down to 0, 6, and 9
        if len(digit) == 6:
            
            # Only 6 will have not have all segments from 1.
            six = False
            for segment in ones[i]:
                if segment not in digit:
                    six = True
                    
            if six:
                # The segment inside 1 and 6 will be 'f'.
                # The segment not in 1 and 6 will be 'c'.
                for segment in digit:
                    # looking for 'c'
                    if segment not in ones[i]+''.join(seg_display[i]):
                        for letter in 'abcdefg':
                            if letter not in digit:
                                seg_display[i,2] = letter
                                print(''.join(seg_display[i]))
                    # looking for 'f'
                    if segment in ones[i]:
                        seg_display[i,5] = segment
                        print(''.join(seg_display[i]))
                        
                # The remaining segment is 'd'
                for segment in digit:
                    if segment not in ''.join(seg_display[i]):
                        seg_display[i,3] = segment
                        print(''.join(seg_display[i]))
                        
# Now, we've found all the digits! Let's write down the list
numbers = np.empty((len(data), 10), dtype=object)
for i in range(len(data)):
    numbers[i,0] = ''.join(seg_display[i,(0,1,2,4,5,6)])
    numbers[i,1] = ''.join(seg_display[i,(2,5)])
    numbers[i,2] = ''.join(seg_display[i,(0,2,3,4,6)])
    numbers[i,3] = ''.join(seg_display[i,(0,2,3,5,6)])
    numbers[i,4] = ''.join(seg_display[i,(1,2,3,5)])
    numbers[i,5] = ''.join(seg_display[i,(0,1,3,5,6)])
    numbers[i,6] = ''.join(seg_display[i,(0,1,3,4,5,6)])
    numbers[i,7] = ''.join(seg_display[i,(0,2,5)])
    numbers[i,8] = ''.join(seg_display[i,(0,1,2,3,4,5,6)])
    numbers[i,9] = ''.join(seg_display[i,(0,1,2,3,5,6)])
    
# Finally we can find the digits of part 1:
# We need to compare number in digit and digit in number.
def same_chars(str1, str2):
    # Note, this will fail on "aaaaaaaabc" and "abc", but this problem
    # does not contain this issue, so fuck you, don't use this function.
    for character in str1:
        if character not in str2:
            return False
    for character in str2:
        if character not in str1:
            return False
    return True

digits = np.zeros((len(data), 4), dtype=int) - 1
answers = np.zeros((len(data), 1), dtype=int) - 1

for i in range(len(data)):
    for d in range(len(part1[i])):
        for num in range(len(numbers[i])):
            if same_chars(part1[i][d], numbers[i,num]):
                digits[i,d] = num
    answers[i] = digits[i,0]*1000+digits[i,1]*100+digits[i,2]*10+digits[i,3]

print(np.sum(answers))