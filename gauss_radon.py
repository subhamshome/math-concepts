# Radon Transform of a Gaussian Function/Distribution

from skimage.transform import radon
import numpy as np
import matplotlib.pyplot as plt

# Define the Gaussian distribution
x_mean = 1
y_mean = 2
std = 1
size = 100
x = np.linspace(-10, 10, size)
y = np.linspace(-10, 10, size)
X, Y = np.meshgrid(x, y)
gaussian = np.exp(-0.5 * std * (X - x_mean) ** 2 - 0.5 * (Y - y_mean) ** 2)

# Perform the Radon transform
theta = np.linspace(0, 180, 180, endpoint=False)
sinogram = radon(gaussian, theta=theta)

# Plot the Gaussian distribution
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(gaussian, cmap="hot", extent=(-10, 10, -10, 10), aspect="auto")
plt.title("2D Gaussian Distribution")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar()

# Plot the sinogram
plt.subplot(1, 2, 2)
plt.imshow(sinogram, cmap="gray", extent=(0, 180, -10, 10), aspect="auto")
plt.title("Sinogram")
plt.xlabel("Projection Angle (degrees)")
plt.ylabel("Radial Distance")
plt.colorbar()

plt.tight_layout()
plt.show()

# Create a figure and axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

# Plot the Gaussian distribution
ax.plot_surface(X, Y, gaussian, cmap="hot")

# Set labels and title
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("3D Gaussian Distribution")

# Show the plot
plt.show()
