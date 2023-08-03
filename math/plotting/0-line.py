#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# Plotting y as a solid red line
plt.plot(y, color='red')

# Setting x-axis range from 0 to 10
plt.xlim(0, 10)

# Display the plot
plt.show()
