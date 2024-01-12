import numpy as np

maalinger = np.array([20.4, 20.4, 20.4, 20.2, 20.4, 20.3, 20.4, 20.5, 20.4,
                      20.4, 20.4, 20.4, 20.1, 20.3, 20.3, 20.2, 20.3, 20.2, 20.3, 20.3])
n = 20

m_x = np.sum(maalinger)/n

varianse = 1/(n-1)*sum((maalinger-m_x)**2)
s_x = np.sqrt(varianse)

konfint_low = round(m_x - 2.093*(s_x/np.sqrt(n)), 4)
konfint_high = round(m_x + 2.093*(s_x/np.sqrt(n)), 4)

intervall = [konfint_low, konfint_high]

print(intervall)
