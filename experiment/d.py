import json
import matplotlib.pyplot as plt

y = []
num = [1, 2, 4, 8, 16]

with open('/home/imani/mp4/exps.out.json') as file:
    data = json.load(file)

for x in num:
    for i in range(5, 101):
        y.append(data[str(x)][str(i)]['col_count'])

x = range(5, 101)

ax = plt.subplots()
plt.title("Total Number of Collision for an Increasing Number of Nodes with Set R Values")
plt.plot(x, y)
plt.ylabel('Total Number of Collisions')
plt.xlabel('Number of Nodes')
plt.show()
