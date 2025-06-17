import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parametric equations for a heart shape
t = np.linspace(0, 2*np.pi, 100)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
z = -(x**2 + y**2)**0.5  # Ensure that z is negative to form the heart shape

# Plot the 3D heart and color it red
ax.plot(x, y, z, label='parametric curve', color='red')
# Plot the mirrored image to show from all perspectives
ax.plot(x, y, -z, color='red')
ax.legend()

plt.show()
