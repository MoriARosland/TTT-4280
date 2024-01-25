import numpy as np
import matplotlib.pyplot as plt

numberOfSamples = 900
plotRange = 200

F_s = 5000
N_fft = 1024

delta_t = 0.2e-3  # Seconds
delta_f = F_s / N_fft

A = 1  # Volts
F = 100  # Hz


time = np.arange(0, numberOfSamples*delta_t, delta_t)
x_t = A * np.sin(2*np.pi*F*time)

X_f = np.fft.fft(x_t, N_fft)
S_x = np.abs(X_f)**2

frequencies = np.linspace(0, F_s/2, N_fft//2)

index_200Hz = int(np.ceil(201 / delta_f))

plt.plot(frequencies[:index_200Hz], S_x[:index_200Hz])
plt.xlabel('Frequency [Hz]')
plt.ylabel('Power')
plt.title('PDS')

plt.show()
