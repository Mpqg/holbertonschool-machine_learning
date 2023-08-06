#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# Define the fruit names and corresponding colors
fruits = ['Apples', 'Bananas', 'Oranges', 'Peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

# Create the stacked bar graph
person_labels = ['Farrah', 'Fred', 'Felicia']
bar_width = 0.5
bar_positions = np.arange(len(person_labels))

plt.bar(bar_positions, fruit[:, 0], width=bar_width,
        label=fruits[0], color=colors[0])
plt.bar(bar_positions, fruit[:, 1], width=bar_width,
        label=fruits[1], color=colors[1], bottom=fruit[:, 0])
plt.bar(bar_positions, fruit[:, 2], width=bar_width, label=fruits[2],
        color=colors[2], bottom=fruit[:, 0] + fruit[:, 1])
plt.bar(bar_positions, fruit[:, 3], width=bar_width, label=fruits[3],
        color=colors[3], bottom=fruit[:, 0] + fruit[:, 1] + fruit[:, 2])

# Add labels and title
plt.xlabel('Person')
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')

# Set y-axis range and ticks
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))

# Add a legend
plt.legend()

# Set the x-axis ticks and labels
plt.xticks(bar_positions, person_labels)

# Show the plot
plt.show()
