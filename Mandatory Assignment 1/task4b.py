from numpy import pi, linspace, meshgrid, cos, sin
import matplotlib.pyplot as plt  # Needed for plotting (you should import this)

# Define a function to generate a velocity field
def velfield(n):
    # Create a 1D array of n points from -π/2 to π/2
    x = linspace(-0.5 * pi, 0.5 * pi, n)
    
    # Generate 2D coordinate grids from the x array
    [X, Y] = meshgrid(x, x)
    
    # Define the velocity components u and v
    u = cos(X) * sin(Y)
    v = -sin(X) * cos(Y)
    
    # Return the coordinate grid and velocity components
    return X, Y, u, v

# Generate the velocity field using n = 8
x, y, u, v = velfield(8)

# Plot the vector field using arrows
plt.quiver(x, y, u, v)

# Show the plot
plt.show()
