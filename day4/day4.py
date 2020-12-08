# Day 4
import string

with open('day4', 'r') as fd: # read file
    out = fd.read().splitlines()      # str
    
def get_passport(file):
    
    # Get first line for each passport
    passport = ''
    passports = []
    for line in out:
        passport += ' ' + line
        
        if line == '': # If the whole line is empty, then it's a new passport
            passports.append(passport[1:-1])
            passport = ''
    passports.append(passport[1:]) # add the last one in, too
    return passports

def fill_out_fields(data):
    field_values = data.split(" ")
    content = dict({'byr':[], 'iyr':[], 'eyr':[], 'hgt':[], 'ecl':[], 'pid':[], 'cid':[]})
    for field in fields:
        for passport_field in field_values:
            if field in passport_field:
                content[field] = passport_field[4:]    
    return content

passports = get_passport(out)

# Part 1    
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
valid_count = 0
for passport in passports:
    valid = True
    for field in fields:
        if field not in passport:
            if field != 'cid':
                valid = False
    if valid:
        valid_count += 1






# Part 2
passports = get_passport(out)
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
valid_count = 0
i = 0
valid_passport_fields = [True] * len(passports)
for passport in passports:
    valid = True
    for field in fields:
        if field not in passport:
            if field != 'cid':
                valid = False

    if valid:
        valid_count += 1
    valid_passport_fields[i] = valid
    i += 1

passport_list = [y for x,y in zip(valid_passport_fields, passports) if x]
valid_passport_list_fields = [False] * len(passport_list)

valid_passports = 0
i = 0
for passport in passport_list:
    
    data = fill_out_fields(passport)
    valid_fields = 0
    if int(data['byr']) >= 1920 and int(data['byr']) <= 2002:
        valid_fields += 1
    if int(data['iyr']) >= 2010 and int(data['iyr']) <= 2020:
        valid_fields += 1
    if int(data['eyr']) >= 2020 and int(data['eyr']) <= 2030:
        valid_fields += 1
        
    # Check height, cm: [150, 193].. in: [59, 76]
    if data['hgt'][-2:] == 'cm':
        if int(data['hgt'][:-2]) >= 150 and int(data['hgt'][:-2]) <= 193:
            valid_fields += 1
    elif data['hgt'][-2:] == 'in':
        if int(data['hgt'][:-2]) >= 59 and int(data['hgt'][:-2]) <= 76:
            valid_fields += 1    
    
    # Check hair color
    hcl = data['hcl']
    if hcl[0] == '#':
        clr = hcl[1:]
        if len(clr) == 6:
            if set(clr).issubset(string.hexdigits):
                valid_fields += 1
    
    # Check eye color
    if data['ecl'] == 'amb' or data['ecl'] == 'blu' or data['ecl'] == 'brn' or data['ecl'] == 'gry' \
        or data['ecl'] == 'grn' or data['ecl'] == 'hzl' or data['ecl'] == 'oth':
            valid_fields += 1
            
    if len(data['pid']) == 9:
        try: 
            int(data['pid'])
            valid_fields += 1
        except:
            pass
        # valid_fields += 1
    
    if valid_fields >= 7:
        valid_passports += 1
        valid_passport_list_fields[i] = True
    i += 1
valid_passport_list = [y for x,y in zip(valid_passport_list_fields, passport_list) if x]
