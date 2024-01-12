import numpy as np

maalinger = np.array([20.6, 20.4, 20.4, 20.6, 20.4, 20.8, 20.5, 20.5, 20.5,
                      20.4, 20.5, 20.5, 20.5, 20.5, 20.4, 20.4, 20.4, 20.5, 20.3, 20.6])


avg = sum(maalinger)/20

varians = 1/(20-1)*np.sum((maalinger-avg)**2)
standard_avvik = np.sqrt(varians)

print(varians)
print(standard_avvik)
