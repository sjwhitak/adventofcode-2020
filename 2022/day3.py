def calc(s, alphabet):
  return alphabet.rfind(s)+1
  
def run_thru_alphabet(str_list, alphabet):
  for i in alphabet:
    checks = [i in s for s in str_list]
    if all(checks):
      return i

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTYVWXYZ'

x = [x.strip() for x in open('day3.txt','r').readlines()]

s = [run_thru_alphabet([i[:len(i)//2], i[len(i)//2:]], alphabet) for i in x]
counts = [calc(i, alphabet) for i in s]
print(sum(counts))

counts = []
for i in range(len(x)//3):
  start = 3*i
  end = 3*(i+1)
  s = run_thru_alphabet(x[start:end], alphabet)
  counts.append(calc(s, alphabet))

print(sum(counts))