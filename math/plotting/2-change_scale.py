#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# Create the line graph with logarithmic scaling on the y-axis
plt.semilogy(x, y)

# Add labels and title
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title("Exponential Decay of C-14")

# Set x-axis range
plt.xlim(0, 28650)

# Show the plot
plt.show()
