import json
import matplotlib.pyplot as plt

y = []

with open('/home/imani/mp4/exps.out.json') as file:
    data = json.load(file)

for i in range(5, 101):
    y.append(data[str(i)]['col_count'])

x = range(5, 101)

ax = plt.subplots()
plt.title("Total Numer of Collision for an Increasing Number of Nodes")
plt.plot(x, y)
plt.ylabel('Total Number of Collisions')
plt.xlabel('Number of Nodes')
plt.show()
