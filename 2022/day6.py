def rolling_check(s, N):
  for i in range(len(s)-N):
    if len(set(s[i:i+N])) == len(s[i:i+N]):
      return i + N

print(rolling_check(open('day6.txt','r').read(), 4))
print(rolling_check(open('day6.txt','r').read(), 14))