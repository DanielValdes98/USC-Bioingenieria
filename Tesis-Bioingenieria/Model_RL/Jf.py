def Jf(P):
    # Librerias
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    import time
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import SGDRegressor
    from joblib import dump, load

    a = np.zeros((9, 4))
    x_senb = np.empty_like(a)
    x_senb[0] = P
    x_senb[1] = [P[0]+P[0]*0.1, P[1], P[2], P[3]] #Tcp(+)
    x_senb[2] = [P[0]-P[0]*0.1, P[1], P[2], P[3]] #Tcp(-)
    x_senb[3] = [P[0], P[1]+P[1]*0.1, P[2], P[3]] #Tp(+)
    x_senb[4] = [P[0], P[1]-P[1]*0.1, P[2], P[3]] #Tp(-)
    x_senb[5] = [P[0], P[1], P[2]+P[2]*0.1, P[3]] #Tk(+)
    x_senb[6] = [P[0], P[1], P[2]-P[2]*0.1, P[3]] #Tk(-)
    x_senb[7] = [P[0], P[1], P[2], P[3]+P[3]*0.1] #Tmi_h2o(+)
    x_senb[8] = [P[0], P[1], P[2], P[3]-P[3]*0.1] #Tmi_h2o(-)
    
    # MODELO DE REGRESIÓN LINEAL MÚLTIPLE
    #RL_model = load('model_RL_27-06-2021.joblib') ---> MEJOR MODELO ENTRENADO HASTA AHORA
    RL_model = load('model_RL_07-09-2021.joblib') # Se carga el último modelo entrenado

    #test
    y_predT = RL_model.predict(x_senb)

    Jcp = (y_predT[1] - y_predT[2]) / (2*0.1*P[0]) #97x1
    Jp = (y_predT[3] - y_predT[4]) / (2*0.1*P[1]) #97x1
    Jk = (y_predT[5] - y_predT[6]) / (2*0.1*P[2]) #97x1
    Jmi_h2o = (y_predT[7] - y_predT[8]) / (2*0.1*P[3]) #97x1

    J = np.array((Jk, Jmi_h2o)).T

    return J
