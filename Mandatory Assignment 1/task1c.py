from math import pi
import numpy as np
import matplotlib.pyplot as plt

# Create an array of 200 equally spaced values from 0 to 1
x = np.linspace(0, 1, 200)

# List of launch angles (in radians): π/5, π/4, π/3
theta = [pi/5, pi/4, pi/3]

# Loop over each angle and plot the corresponding curve
for i in theta:
  # Compute y* = -x*(x - 1)*tan(θ) for each x
  plt.plot(x, -x*(x-1)*np.tan(i), label=i)

# Add title and axis labels
plt.title('Baner (x*,y*) for 3 utkastvinkler')
plt.xlabel('x*')
plt.ylabel('y*')

# Add legend and grid
plt.legend()
plt.grid()

# Display the plot
plt.show() 
