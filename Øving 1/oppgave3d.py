import numpy as np
from numpy.random import default_rng


rng = default_rng()
delta_r = 100  # Recommended value

resistor = 5000
resistor_deviation = 5000 * 0.01

numberOfValues = 10**6


r_values1 = resistor + 2*resistor_deviation * (rng.random(numberOfValues) - 0.5)
r_values2 = resistor + 2*resistor_deviation * (rng.random(numberOfValues) - 0.5)

r_tot = r_values1 + r_values2

relative_std = np.std(r_tot)/np.mean(r_tot)*100

print(relative_std)
