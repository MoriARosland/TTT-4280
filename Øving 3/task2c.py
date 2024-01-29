import numpy as np
nrand = int(1e4)

c = 300

tauvec = (1 + 2*0.01*(np.random.rand(nrand) - 0.5))
d = 1 + 0.04 * (np.random.rand(nrand) - 0.5)

f = c * tauvec / d
f_baseline = 300  # Assuming all variables equal 1 (d=1, tauvec=1)

f_max = np.max(f)
f_min = np.min(f)

relative_max = np.abs(f_max/f_baseline-1)
relative_min = np.abs(f_min/f_baseline-1)

if (relative_max >= relative_min):
    max_error = round(relative_max, 3)
else:
    max_error = round(relative_min, 3)

print('f_max:', round(np.max(f), 3))
print('f_min:', round(np.min(f), 3))
print('max relative error:', max_error)
