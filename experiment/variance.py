import json
import matplotlib.pyplot as plt

y = []

with open('exps.out.json') as file:
    data = json.load(file)

for i in range(5, 101):
    y.append(data[str(i)]['var'])

x = range(5, 101)

plt.plot(x, y)
plt.ylabel('Variance')
plt.xlabel('Number of Nodes')
plt.show()
