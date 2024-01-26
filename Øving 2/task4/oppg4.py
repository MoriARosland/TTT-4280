import numpy as np
import matplotlib.pyplot as plt

numberOfSamples = 899
plotRange = 200

maxSampleLength = 4096*2

F_s = 5000
N_fft = 4096*2

delta_t = 0.2e-3  # Seconds
delta_f = F_s / N_fft

A = 1  # Volts
F = 100  # Hz

time = np.arange(0, numberOfSamples*delta_t, delta_t)
x_t = A * np.sin(2*np.pi*F*time)
x_t_windowed = x_t * np.hanning(len(time))

# Add zero-padding to x_t
if len(x_t) < maxSampleLength:
    x_t_padded = np.pad(x_t, (0, maxSampleLength - len(x_t)), 'constant')
    x_t_padded_window = np.pad(x_t_windowed, (0, maxSampleLength - len(x_t_windowed)), 'constant')
else:
    x_t_padded = x_t
    x_t_padded_window = x_t_windowed


X_f = np.fft.fft(x_t, N_fft)
X_f_windowed = np.fft.fft(x_t_windowed, N_fft)

S_x = 20*np.log10(abs(X_f))  # Power in decibel
S_x_normalized = S_x - np.max(S_x)

S_x_windowed = 20*np.log10(abs(X_f_windowed))
S_x_windowed_normalized = S_x_windowed - np.max(S_x_windowed)

frequencies = np.linspace(0, F_s/2, N_fft//2)
index_200Hz = int(np.ceil(201 / delta_f))

plt.plot(frequencies[:index_200Hz], S_x_normalized[:index_200Hz], label='non-windowed')
plt.plot(frequencies[:index_200Hz], S_x_windowed_normalized[:index_200Hz], label='windowed')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Relative effect [db]')
plt.title('N_fft = 8192')
plt.ylim(-70, 5)
plt.legend()
plt.show()
