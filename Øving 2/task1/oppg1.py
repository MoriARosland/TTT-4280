import numpy as np
import matplotlib.pyplot as plt

numberOfSamples = 900
plotRange = 200
delta_t = 0.2e-3  # Seconds

F = 100  # Hz

time = np.arange(0, numberOfSamples*delta_t, delta_t)
x_t = np.sin(2*np.pi*F*time)

plt.stem(x_t[:plotRange])

plt.xlabel('Time [s]')
plt.ylabel('Voltage [V]')
plt.show()
