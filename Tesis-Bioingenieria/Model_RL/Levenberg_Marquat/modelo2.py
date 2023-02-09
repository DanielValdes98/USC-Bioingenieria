global param
def modelo2(t,y,param):
    import numpy as np
    from math import log

    dy = np.zeros((2,1))
    # Modelo de Gompertz
    dy[0] = param[0]*y[0]*np.log(param[1]/y[0]) - (param[2]*y[0]*y[1])/(param[3]+y[0])
    dy[1] = - param[4]*y[1]

    return dy