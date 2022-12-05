def move_stack(boxes, start, end, move):
  for i in range(move):
    boxes[end-1].append(boxes[start-1][-1])
    boxes[start-1].pop()
  return boxes


def move_stack_group(boxes, start, end, move):
  boxes[end-1].extend(boxes[start-1][-move:])
  for i in range(move):
    boxes[start-1].pop()
  return boxes


L=[]
L.append(['Q', 'S', 'W', 'C', 'Z', 'V', 'F', 'T'])
L.append(['Q', 'R', 'B'])
L.append(['B', 'Z', 'T', 'Q', 'P', 'M', 'S'])
L.append(['D', 'V', 'F', 'R', 'Q', 'H'])
L.append(['J', 'G', 'L', 'D', 'B', 'S', 'T', 'P'])
L.append(['W', 'R', 'T', 'Z'])
L.append(['H', 'Q', 'M', 'N', 'S', 'F', 'R', 'J'])
L.append(['R', 'N', 'F', 'H', 'W'])
L.append(['J', 'Z', 'T', 'Q', 'P', 'R', 'B'])

lines = open('day5.txt', 'r').readlines()
lines = [line.strip() for line in lines]
moves = []
starts = []
ends = []
for line in lines:
  words = line.split(' ')
  L = move_stack(L, int(words[3]), int(words[5]), int(words[1]))
  
[print(l[-1], end='') for l in L]
print('')  
  
L=[]
L.append(['Q', 'S', 'W', 'C', 'Z', 'V', 'F', 'T'])
L.append(['Q', 'R', 'B'])
L.append(['B', 'Z', 'T', 'Q', 'P', 'M', 'S'])
L.append(['D', 'V', 'F', 'R', 'Q', 'H'])
L.append(['J', 'G', 'L', 'D', 'B', 'S', 'T', 'P'])
L.append(['W', 'R', 'T', 'Z'])
L.append(['H', 'Q', 'M', 'N', 'S', 'F', 'R', 'J'])
L.append(['R', 'N', 'F', 'H', 'W'])
L.append(['J', 'Z', 'T', 'Q', 'P', 'R', 'B'])

lines = open('day5.txt', 'r').readlines()
lines = [line.strip() for line in lines]
moves = []
starts = []
ends = []
for line in lines:
  words = line.split(' ')
  L = move_stack_group(L, int(words[3]), int(words[5]), int(words[1]))
  
[print(l[-1], end='') for l in L]
print('')