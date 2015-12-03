import json
import matplotlib.pyplot as plt


with open('/home/imani/mp4/exps.out-3.json') as file:
    data = json.load(file)

y = []
num = [20, 40, 60, 80, 100]
x = range(5, 101)

for j in num:
    for i in range(5, 101):
        y.append(data[str(j)][str(i)]['utilization']*100)
    plt.plot(x,y) 
    y = []
    x = range(5, 101)

plt.title("Channel Utilization for an Number of Nodes with Varying Packet Size")
plt.ylabel('Channel Utilization (in percentage)')
plt.xlabel('Number of Nodes')
plt.legend(['L = 20', 'L = 40', 'L = 60', 'L = 80', 'L = 100'], loc='lower right')
plt.show()
