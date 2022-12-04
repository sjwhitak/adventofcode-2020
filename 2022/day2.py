x = [x.strip().split(' ') for x in open('day2.txt','r').readlines()]

their_count = 0
your_count = 0

# Part 1
for draw in x:
  # Draws
  if draw[0] == 'A' and draw[1] == 'X':
    their_count  += 1 + 3
    your_count += 1 + 3
  elif draw[0] == 'B' and draw[1] == 'Y':
    their_count  += 2 + 3
    your_count += 2 + 3
  elif draw[0] == 'C' and draw[1] == 'Z':
    their_count  += 3 + 3
    your_count += 3 + 3
    
  # Wins
  if draw[0] == 'A' and draw[1] == 'Z':
    their_count  += 1 + 6
    your_count += 3 + 0
  elif draw[0] == 'B' and draw[1] == 'X':
    their_count  += 2 + 6
    your_count += 1 + 0
  elif draw[0] == 'C' and draw[1] == 'Y':
    their_count  += 3 + 6
    your_count += 2 + 0
      
  # Losses
  if draw[0] == 'A' and draw[1] == 'Y':
    their_count  += 1 + 0
    your_count += 2 + 6
  elif draw[0] == 'B' and draw[1] == 'Z':
    their_count  += 2 + 0
    your_count += 3 + 6
  elif draw[0] == 'C' and draw[1] == 'X':
    their_count  += 3 + 0
    your_count += 1 + 6
    
print(your_count)


# Part 2
their_count = 0
your_count = 0
for draw in x:
  
  # Draws
  if draw[0] == 'A' and draw[1] == 'X': 
    their_count  += 1 + 6
    your_count += 3 + 0
  elif draw[0] == 'B' and draw[1] == 'Y':
    their_count  += 2 + 3
    your_count += 2 + 3
  elif draw[0] == 'C' and draw[1] == 'Z':
    their_count  += 3 + 0
    your_count += 1 + 6
    
  # Wins
  if draw[0] == 'A' and draw[1] == 'Z':
    their_count  += 1 + 0
    your_count += 2 + 6
  elif draw[0] == 'B' and draw[1] == 'X':
    their_count  += 2 + 6
    your_count += 1 + 0
  elif draw[0] == 'C' and draw[1] == 'Y':
    their_count  += 3 + 3
    your_count += 3 + 3
      
  # Losses
  if draw[0] == 'A' and draw[1] == 'Y':
    their_count  += 1 + 3
    your_count += 1 + 3
  elif draw[0] == 'B' and draw[1] == 'Z':
    their_count  += 2 + 0
    your_count += 3 + 6
  elif draw[0] == 'C' and draw[1] == 'X':
    their_count  += 3 + 6
    your_count += 2 + 0
  
print(your_count)