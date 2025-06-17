import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parametric equations for a heart shape
theta = np.linspace(0, 2*np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)
x = 16 * np.sin(phi)**3 * np.cos(theta)
y = 13 * np.cos(phi) - 5 * np.cos(2*phi) - 2 * np.cos(3*phi) - np.cos(4*phi)
z = -2.5 * np.sin(4*phi)

# Plot the 3D heart
ax.plot_trisurf(x.flatten(), y.flatten(),
                z.flatten(), color='red', linewidth=0)

# Set aspect ratio to be equal
ax.set_box_aspect([2, 2, 1])

plt.show()
