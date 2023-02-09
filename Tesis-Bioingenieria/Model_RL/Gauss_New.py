def Gauss(P3,P4,Y):
    #cargar librerias necesarias
    import numpy as np
    import matplotlib.pyplot as plt
    from numpy.linalg.linalg import multi_dot
    from sklearn.linear_model import LinearRegression
    from sklearn import metrics
    from sklearn.metrics import mean_squared_error
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import SGDRegressor
    from joblib import dump, load
    from numpy.linalg import norm 
    import pandas as pd

    from Jf import Jf
    from Y_exact_upload import Y_exact_upload
    from Fun_S import Fun_S

    RL_model = load('model_RL_07-09-2021.joblib') # Se carga el último modelo entrenado

    # Parametros fijos:
    cp = 4184.1 
    p = 998.20 

    # Parametros a estimar:
    nk = P3 # = 998.20 + 998.20*0.1 
    nmi_h2o = P4 # = 13.72 + 13.72*0.1 --> 0.025%

    # P estimado
    P_est = [nk,nmi_h2o]
    P_est = np.array(P_est)
    P_est = P_est.reshape(-1,1) #IMPORTANTE

    # Vector de entrada:
    P = [cp, p, P_est[0,0], P_est[1,0]]
    P = np.array(P)

    #Parametros iniciales sin ningún cambio:
    P_prueba = [cp, p, P_est[0,0], P_est[1,0]]
    P_prueba = np.array(P_prueba)

    Taux = RL_model.predict(P.reshape(1,-1))
    J = Jf(P)
    # omega = np.diag(np.diag((J.T).dot(J))) # MATLAB ---> omega = diag(diag(J'*J)) // Matriz 2x2

    T= Taux.T
    # mi = 0.001

    i=1
    # j=1
    while (norm(P_est - (P_est + np.linalg.inv(J.T.dot(J)).dot(J.T).dot(Y-T))) > 10e-12):
        Taux = RL_model.predict(P.reshape(1,-1))
        T= Taux.T
        J = Jf(P)
        # omega = np.diag(np.diag(J.T.dot(J))) # MATLAB ---> omega = diag(diag(J'*J)) // Matriz 2x2    
        P_est = P_est + np.linalg.inv(J.T.dot(J)).dot(J.T).dot(Y-T)
        nP = [cp,p,P_est[0,0],P_est[1,0]]
        nP = np.array(nP)
        P = nP
        res = P
        i = i + 1 

    # print(VnP)

    T_LM = RL_model.predict(res.reshape(1,-1))
    T_LM = T_LM.T

    T_ti = RL_model.predict(P_prueba.reshape(1,-1))
    T_ti = T_ti.T

    return T_LM, T_ti, res, P_prueba,i
    # return res