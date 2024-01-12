import numpy as np

maalinger = [20.6, 20.4, 20.4, 20.6, 20.4, 20.8, 20.5, 20.5, 20.5,
             20.4, 20.5, 20.5, 20.5, 20.5, 20.4, 20.4, 20.4, 20.5, 20.3, 20.6]


avg = sum(maalinger)/20

varians = np.var(maalinger)
standard_avvik = np.sqrt(varians)

print(varians)
print(standard_avvik)
