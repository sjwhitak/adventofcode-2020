import numpy as np
x = [x.split('\n') for x in open('day1.txt','r').read().strip().split('\n\n')]
s = [np.sum(np.array(e).astype(int))for e in x]
s.sort()
print(s[-1])
print(sum(s[-3:]))