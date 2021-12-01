def get_passport(file):
    
    # Get first line for each passport
    passport = []
    passports = []
    for line in out:
        passport.append(line)
        
        if line == '': # If the whole line is empty, then it's a new passport
            passports.append(passport[:-1])
            passport = []
    passports.append(passport) # add the last one in, too
    return passports



with open('day6', 'r') as fd: # read file
    out = fd.read().splitlines()      # str
    
answers = get_passport(out)


answers_list = []
for answer in answers:
    group = []
    for x in answer:
        group.extend(x)
    answers_list.append(group)
    
answers_out = [list(set(x)) for x in answers_list]
count = sum([len(x) for x in answers_out])
print('Part 1: ' + str(count))

for i in range(len(answers)):
    unique_answers = list(set(answers_list[i]))
    for j in range(len(answers[i])):
        individual_answers = answers[i][j]
        for letter in unique_answers:
            if letter not in individual_answers:
                if letter in answers_out[i]:
                    answers_out[i].remove(letter)

count = sum([len(x) for x in answers_out])
print('Part 2: ' + str(count))