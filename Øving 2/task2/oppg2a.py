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
frequency = np.fft.fftfreq(N_fft, delta_t)

# plt.subplot(2, 1, 1)
# plt.stem(time[:plotRange], x_t[:plotRange])
# plt.xlabel('Time [s]')
# plt.ylabel('Voltage [V]')
# plt.title('Time Domain')

# plt.subplot(2, 1, 2)
# plt.plot(frequency[:N_fft], np.abs(X_f[:N_fft]))
# plt.xlabel('Frequency [Hz]')
# plt.ylabel('Magnitude')
# plt.title('FFT')

# plt.show()
