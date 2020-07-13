from time import time
import matplotlib.pyplot as plt

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

def addtask(space):
    temp = ['OPD Reminder', '0', '2020/07/12', '02:16:12', '2020/07/13', '14:00:00', '1', '0', '']
    space.append(temp)

elapse = []
for i in range(20):
    start_time = time()
    addtask(space)
    print(space)
    end_time = time()
    total = end_time - start_time
    elapse.append(total)
print(elapse)
print('The average time elapsed for Add Task function is', sum(elapse)/len(elapse))
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
iterations = ['Run1', 'Run2', 'Run3', 'Run4', 'Run5', 'Run6', 'Run7', 'Run8', 'Run9', 'Run10', 'Run11', 'Run12', 'Run13', 'Run14', 'Run15', 'Run16', 'Run17', 'Run18', 'Run19', 'Run20']
durations = elapse
ax.bar(iterations, durations)
plt.show()
