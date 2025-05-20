from streamfun import streamfun  # Import the function that computes the stream function
import matplotlib.pyplot as plt  # Import matplotlib for plotting

# --- Case (i): n = 5 ---
# Compute stream function psi and the corresponding x and y coordinates for n = 5
x, y, psi = streamfun(5)

# Plot contour lines of the stream function
C = plt.contour(x, y, psi)

# Add labels to the contour lines
plt.clabel(C)

# Ensure equal scaling on both axes
plt.axis("equal")

# Add axis labels
plt.xlabel("x")
plt.ylabel("y")

# Show a color bar to represent the values of psi
plt.colorbar()

# Add a plot title
plt.title("Case (i): n = 5")

# Display the plot
plt.show()

# --- Case (ii): n = 30 ---
# Compute stream function for a denser grid (n = 30)
x, y, psi = streamfun(30)

# Plot contour lines of the stream function
C = plt.contour(x, y, psi)

# Add labels to the contour lines
plt.clabel(C)

# Ensure equal scaling on both axes
plt.axis("equal")

# Add axis labels
plt.xlabel("x")
plt.ylabel("y")

# Show a color bar to represent the values of psi
plt.colorbar()

# Add a plot title
plt.title("Case (ii): n = 30")

# Display the plot
plt.show()
