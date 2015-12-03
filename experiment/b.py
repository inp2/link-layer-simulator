import json
import matplotlib.pyplot as plt

y = []

with open('/home/imani/mp4/exps.out.json') as file:
    data = json.load(file)

for i in range(5, 101):
    y.append((data[str(i)]['idling'])*100)

x = range(5, 101)

plt.plot(x, y)
plt.title('Channel Idle Fraction for an Increasing Number of Nodes')
plt.ylabel('Channel Idle Fraction (in percentage)')
plt.xlabel('Number of Nodes')
plt.show()
