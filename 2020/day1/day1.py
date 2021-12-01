with open('day1', 'r') as fd: # read file
    out = fd.readlines()      # str
out = [int(x) for x in out]   # str -> int

# Part 1 -- two numbers add up to 2020
for x in out:
    for y in out:
        if x + y == 2020:
            print(x*y)
# Part 2 -- three numbers add up to 2020
for x in out:
    for y in out:
        for z in out:
            if x + y + z == 2020:
                print(x*y*z)