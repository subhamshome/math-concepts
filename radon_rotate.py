# Radno Transform and its Rotation property

import numpy as np
import matplotlib.pyplot as plt
from skimage.data import shepp_logan_phantom
from skimage.transform import radon, rotate, resize

# Generate the Shepp-Logan phantom and resize it
phantom = shepp_logan_phantom()

# Resize phantom, beacause original phantom renders a very narrow sinogram
ph_size = phantom.shape
phantom = resize(phantom, (ph_size[0] / 2, ph_size[1] / 2))

# Parameters
num_projections = 200
angles = 180
theta = np.linspace(0, angles, num_projections, endpoint=False)
rotation_angle = 45

# Rotate the phantom
rotated_phantom = rotate(phantom, rotation_angle)

# Perform radon transforms
sinogram = radon(phantom, theta)
rotated_sinogram = radon(rotated_phantom, theta)

# Display the original and rotated sinograms
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
fig.suptitle("Radon Transform and its Rotation Property")

im1 = axes[0, 0].imshow(phantom, cmap=plt.cm.Greys_r)
axes[0, 0].set_title("Original Shepp-Logan Phantom")

im2 = axes[0, 1].imshow(sinogram, cmap=plt.cm.Greys_r)
axes[0, 1].set_title("Original Sinogram")
axes[0, 1].set_xlabel("Angle")
axes[0, 1].set_ylabel("Projection Position")

im3 = axes[1, 0].imshow(rotated_phantom, cmap=plt.cm.Greys_r)
axes[1, 0].set_title("Rotated Shepp-Logan Phantom")

im4 = axes[1, 1].imshow(rotated_sinogram, cmap=plt.cm.Greys_r)
axes[1, 1].set_title("Rotated Sinogram")
axes[0, 1].set_xlabel("Angle")
axes[0, 1].set_ylabel("Projection Position")

# Add colorbars for all images
for i, ax in enumerate(axes.flat):
    cbar = plt.colorbar(eval(f"im{i+1}"), ax=ax)
    cbar.set_label("Intensity")

plt.show()
