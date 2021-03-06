import json
import matplotlib.pyplot as plt


with open('/home/imani/mp4/exps.out-2.json') as file:
    data = json.load(file)

y = []
num = [1,2,4,8,16]
x = range(5, 101)

for j in num:
    for i in range(5, 101):
        y.append(data[str(j)][str(i)]['utilization']*100)
    plt.plot(x,y) 
    y = []
    x = range(5, 101)

plt.title("Channel Utilization for an Number of Nodes  with Consecutive Collisions")
plt.ylabel('Channel Utilization (in percentage)')
plt.xlabel('Number of Nodes')
plt.legend(['R = 1', 'R = 2', 'R = 4', 'R = 8', 'R = 16'], loc='lower right')
plt.show()
