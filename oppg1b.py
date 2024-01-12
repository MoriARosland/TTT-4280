import numpy as np

avg = 20.485
maalinger = 20
standard_avvik = 0.106  # Fra oppgave 1b
t_p = 2.093  # Fra tosidig student t-fordeling

konfidensintervall_pos = avg + t_p*(standard_avvik/np.sqrt(maalinger))
konfidensintervall_neg = avg - t_p*(standard_avvik/np.sqrt(maalinger))

intervall = [round(konfidensintervall_neg, 3),
             round(konfidensintervall_pos, 3)]


print(intervall)
