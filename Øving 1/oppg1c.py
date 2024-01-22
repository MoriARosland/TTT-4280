import numpy as np

res = 20.485 + 2.093*0.1089*np.sqrt(1+1/20)
res2 = 20.485 - 2.093*0.1089*np.sqrt(1+1/20)

print(round(res, 3))
print(round(res2, 3))
