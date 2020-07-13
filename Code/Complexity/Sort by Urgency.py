from time import time
import matplotlib.pyplot as plt
import random

space = [['Going to pool', '1', '2020/07/12', '02:04:27', '2020/07/12', '11:30:00', '0', '0', ''],
        ['Preparing for Presentation', '1', '2020/07/12', '02:05:28', '2020/07/13', '16:00:00', '1', '80', 'Ask Sir Ayaz for the meeting'],
        ['Buying ciggerates', '0', '2020/07/12', '02:06:13', '2020/07/16', '10:00:00', '1', '0', ''],
        ['Hepatitis Research', '1', '2020/07/12', '02:08:00', '2020/07/14', '00:00:00', '1', '10', ''],
        ['Documents Registration', '0', '2020/07/12', '02:09:10', '2020/10/15', '16:00:00', '1', '0', ''],
        ['Marriage Shopping', '0', '2020/07/12', '02:10:10', '2020/12/14', '21:00:00', '1', '0', ''],
        ['Finding Job in UAE', '0', '2020/07/12', '02:10:58', '2021/01/01', '12:00:00', '1', '40', ''],
        ['Waking up in Morning', '1', '2020/07/12', '02:11:45', '2020/07/11', '05:00:00', '1', '0', ''],
        ['Cooking Haleem', '0', '2020/07/12', '02:12:45', '2020/07/13', '14:00:00', '1', '0', ''],
        ['IELTS Preparation', '1', '2020/07/12', '02:15:17', '2020/07/31', '00:00:00', '1', '30', '']]

#Time Complexity for Add Task

def partition(lst, x, y, typeindex):
  i = x - 1
  for j in range(x, y):
    if lst[j][typeindex] <= lst[y][typeindex]:
      i += 1
      lst[i], lst[j] = lst[j], lst[i]
  lst[i+1], lst[y] = lst[y], lst[i+1]
  return i + 1

def sortbyurgency(lst, x, y, typeindex):
  if not x < y:
    return
  z = partition(lst, x, y, typeindex)
  sortbyurgency(lst, x, z - 1, typeindex)
  sortbyurgency(lst, z + 1, y, typeindex)

elapse = []
for i in range(10):
    start_time = time()
    sortbyurgency(space, 0, len(space)-1, 1)
    print(space)
    end_time = time()
    total = end_time - start_time
    elapse.append(total)
    random.shuffle(space)
print(elapse)
print('The average time elapsed for Sort by Urgency function is', sum(elapse)/len(elapse))
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
iterations = ['Run1', 'Run2', 'Run3', 'Run4', 'Run5', 'Run6', 'Run7', 'Run8', 'Run9', 'Run10']
durations = elapse
ax.bar(iterations, durations)
plt.show()
