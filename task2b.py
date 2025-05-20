import matplotlib.pyplot as plt
import numpy as np

# Create a grid of 50x50 points ranging from -7 to 7 in both x and y directions
k = np.linspace(-7, 7, 50)
[x, y] = np.meshgrid(k, k)

# Define the scalar field f(x, y) = ln(|x|) - y
f = np.log(np.abs(x)) - y

# Plot contour lines (level curves) of the scalar field
plt.contour(x, y, f)

# Create a coarser grid (5x5) for the vector field to avoid clutter
l = np.linspace(-7, 7, 5)
[x, y] = np.meshgrid(l, l)

# Define vector field components: vx = x*y, vy = y
vx = x * y
vy = y

# Plot the vector field using arrows
plt.quiver(x, y, vx, vy)

# Set equal aspect ratio for both axes
plt.axis("equal")

# Show the combined plot
plt.show()
