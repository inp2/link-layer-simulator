import json
import matplotlib.pyplot as plt

y = []

with open('/home/imani/mp4/exps.out.json') as file:
    data = json.load(file)

for i in range(5, 101):
    y.append(data[str(i)]['utilization']*100)

x = range(5, 101)

plt.plot(x, y)
plt.title('Channel Utilization for an Increasing Number of Nodes')
plt.ylabel('Channel Utilization (in percentage)')
plt.xlabel('Number of Nodes')
plt.show()
