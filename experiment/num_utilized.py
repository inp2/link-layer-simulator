import json
import matplotlib.pyplot as plt

y = []

with open('exps.out.json') as file:
    data = json.load(file)

for i in range(5, 101):
    y.append(data[str(i)]['num_utilized'])

x = range(5, 101)

plt.plot(x, y)
plt.ylabel('Number of Nodes Utilized')
plt.xlabel('Number of Nodes')
plt.show()
