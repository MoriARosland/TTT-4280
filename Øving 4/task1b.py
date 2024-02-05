import numpy as np

T_med = np.array([3.14, 3.15, 3.92, 3.65, 3.35, 3.89, 3.79, 3.32])
T_uten = np.array([4.28, 4.28, 4.13, 3.76, 4.14, 4.33, 4.10, 4.21])

m_x = np.mean(T_med)
m_y = np.mean(T_uten)

S_x = np.sqrt(1/(len(T_med)-1)*np.sum((T_med-m_x)**2))
S_y = np.sqrt(1/(len(T_uten)-1)*np.sum((T_uten-m_y)**2))

S_a = np.round((24*240*np.log(10))/(10*343.4) *
               np.sqrt(S_x**2*1/m_x**4 + S_y**2*1/m_y**4), 3)

print("Estimated standard deviation:", S_a)
