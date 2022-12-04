def merge_interval(times):
  times.sort(key=lambda times: times[0])
  times_out = [times[0]]
  for time in times:
    previous = times_out[-1]
    if time[0] <= previous[1]:
      previous[1] = max(previous[1], time[1])
    else:
      times_out.append(time)
  return times_out

def overlapped_interval(times):
  return times[0][0] <= times[1][0] and times[0][1] >= times[1][1] or \
         times[1][0] <= times[0][0] and times[1][1] >= times[0][1]

x = [x.strip().split(',') for x in open('day4.txt','r').readlines()]
line_out = []
for line in x:
  time_out = []
  for interval in line:
    times = interval.split('-')
    times = [int(times[0]), int(times[1])]
    time_out.append(times)
  line_out.append(time_out)
    
# Part 1
interval = [overlapped_interval(t) for t in line_out]
print(sum(interval))

# Part 2
interval = [len(merge_interval(t)) == 1 for t in line_out]
print(sum(interval))
