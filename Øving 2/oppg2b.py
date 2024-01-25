import numpy as np
import matplotlib.pyplot as plt

numberOfSamples = 900
plotRange = 200
delta_t = 0.2e-3  # Seconds

A = 1  # Volts
F = 100  # Hz

N_fft = 1024

time = np.arange(0, numberOfSamples*delta_t, delta_t)
x_t = A * np.sin(2*np.pi*F*time)

X_f = np.fft.fft(x_t, N_fft)

S_x = np.abs(X_f)**2
# S_x = np.fft.fftshift(S_x)

frequency = np.fft.fftfreq(N_fft, delta_t)
# frequency = np.fft.fftshift(np.fft.fftfreq(N_fft, delta_t))

plt.plot(frequency[:N_fft], S_x[:N_fft])
plt.xlabel('Frequency [Hz]')
plt.ylabel('Power')
plt.title('PDS')

plt.show()
