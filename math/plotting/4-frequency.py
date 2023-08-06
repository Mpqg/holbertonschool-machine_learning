#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Create the histogram
plt.hist(student_grades, bins=np.arange(0, 110, 10), edgecolor='black')

# Add labels and title
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Project A')

# Show the plot
plt.show()
