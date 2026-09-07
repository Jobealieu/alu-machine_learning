#!/usr/bin/env python3
"""Plots a stacked bar graph of fruit owned by three people."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

people = ['Farrah', 'Fred', 'Felicia']
names = ['apples', 'bananas', 'oranges', 'peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

positions = np.arange(len(people))
bottom = np.zeros(len(people))

for row in range(fruit.shape[0]):
    plt.bar(positions, fruit[row], width=0.5, bottom=bottom,
            color=colors[row], label=names[row])
    bottom += fruit[row]

plt.xticks(positions, people)
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.ylim(0, 80)
plt.yticks(range(0, 81, 10))
plt.legend()
plt.show()
