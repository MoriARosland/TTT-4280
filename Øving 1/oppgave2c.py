import numpy as np

t_p = 2.262

intervall1 = np.array([20.6, 20.4, 20.4, 20.6, 20.4,
                      20.8, 20.5, 20.5, 20.5, 20.4])

intervall2 = np.array([20.4, 20.4, 20.4, 20.2, 20.4,
                      20.3, 20.4, 20.5, 20.4, 20.4,])


mean_intervall1 = round(np.sum(intervall1)/len(intervall1), 3)
mean_intervall2 = round(np.sum(intervall2)/len(intervall2), 3)

var1 = round(1/(len(intervall1))*np.sum((intervall1-mean_intervall1)**2), 3)
var2 = round(1/(len(intervall2))*np.sum((intervall2-mean_intervall2)**2), 3)

phi1 = np.sqrt(var1)
phi2 = np.sqrt(var2)


def confidence_intervall(s_x, mean, len):

    conf_high = round(mean + t_p * (s_x/np.sqrt(len)), 3)
    conf_low = round(mean - t_p * (s_x/np.sqrt(len)), 3)
    conf = [conf_low, conf_high]

    return conf


print(confidence_intervall(phi1, mean_intervall1, len(intervall1)))
print(confidence_intervall(phi2, mean_intervall2, len(intervall2)))
