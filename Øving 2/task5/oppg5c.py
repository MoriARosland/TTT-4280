import numpy as np
import matplotlib.pyplot as plt

numberOfSamples = 899

F_s = 5000
N_fft = 4096*2

delta_t = 0.2e-3  # Seconds
delta_f = F_s / N_fft

F = 100  # Hz

time = np.arange(0, numberOfSamples*delta_t, delta_t)
x_t = np.exp(1j*2*np.pi*F*time)

X_f = np.fft.fft(x_t, N_fft)
S_x = 20*np.log10(abs(X_f))  # Power in decibel
S_x_normalized = S_x - np.max(S_x)

frequencies = np.fft.fftshift(np.linspace(-F_s / 2, F_s / 2, N_fft))

plt.plot(frequencies, S_x_normalized)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Relative effect [dB]')
plt.show()
