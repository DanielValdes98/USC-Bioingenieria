def Lever_Marq(P2,P4,Y):
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

    # YE50,YE25,YEDW,YExact_Comsol,DTE_Comsol = Y_exact_upload()

    # import random
    # mu, sigma, e = 0, 0.05, 0.1 # mean, standard deviation and error
    # Y = np.random.normal(YE25, sigma*e)
    # Y = Y.reshape(-1,1)

    # EXPORTAR LA Y CON ERROR:
    # df = pd.DataFrame(Y)
    # df.to_excel('Y.xlsx')

    #  Cargar Y con error:
    # Y = np.loadtxt('Y.txt',delimiter=',')
    # Y = Y.reshape(-1,1)

    #RL_model = load('model_RL_27-06-2021.joblib') ---> MEJOR MODELO ENTRENADO HASTA AHORA
    RL_model = load('model_RL_07-09-2021.joblib') # Se carga el último modelo entrenado

    # Parametros fijos:
    cp = 4184.1 
    k = 0.6034 

    # Parametros a estimar:
    nwp = P2 # = 998.20 + 998.20*0.1 
    nmi_h2o = P4 # = 13.72 + 13.72*0.1 --> 0.025%

    # P estimado
    P_est = [nwp,nmi_h2o]
    P_est = np.array(P_est)
    P_est = P_est.reshape(-1,1) #IMPORTANTE

    # Vector de entrada:
    P = [cp, P_est[0,0], k, P_est[1,0]]
    P = np.array(P)

    #Parametros iniciales sin ningún cambio:
    P_prueba = [cp, P_est[0,0], k, P_est[1,0]]
    P_prueba = np.array(P_prueba)

    Taux = RL_model.predict(P.reshape(1,-1))
    J = Jf(P)
    omega = np.diag(np.diag((J.T).dot(J))) # MATLAB ---> omega = diag(diag(J'*J)) // Matriz 2x2

    T= Taux.T
    mi = 0.001

    i=1
    j=1
    while (norm(P_est - (P_est + np.linalg.inv(J.T.dot(J) + mi*omega).dot(J.T).dot(Y-T))) > 10e-12):
        Taux = RL_model.predict(P.reshape(1,-1))
        T= Taux.T
        J = Jf(P)
        omega = np.diag(np.diag(J.T.dot(J))) # MATLAB ---> omega = diag(diag(J'*J)) // Matriz 2x2    
        Paux = P_est + np.linalg.inv(J.T.dot(J) + mi*omega).dot(J.T).dot(Y-T)
        nP = [cp,Paux[0,0],k,Paux[1,0]]
        nP = np.array(nP)

        if (Fun_S(P,Y) < Fun_S(nP,Y)):
            mi = 10*mi
            j = j + 1

        else:
            P_est = Paux
            P = nP
            mi = 0.1*mi

            # VnP = []
            # VnP = np.array(VnP)
            # VnP[i] = P_est
            i = i + 1
            # print(nP)
            
        res = P

    # print(VnP)

    T_LM = RL_model.predict(res.reshape(1,-1))
    T_LM = T_LM.T

    T_ti = RL_model.predict(P_prueba.reshape(1,-1))
    T_ti = T_ti.T

    return T_LM, T_ti, res, P_prueba,i,j

    # print('rho inicial: ',nwp)
    # print('rho nuevo: ',res[1])

    # print('mi_h2o inicial: ',nmi_h2o)
    # print('mi_h2o nuevo: ',res[3])

    # print(res)
    # print(P_prueba)

    # print('i (else): ',i)
    # print('j (if): ',j)

    # plt.figure(figsize=(20, 10))
    # plt.plot(T_LM)
    # plt.plot(YE25,'--r')
    # plt.plot(T_ti,'.k')
    # plt.plot(Y,'g')
    # plt.show()



    # """ EXTRA """
    # print(P_est + np.linalg.inv(J.T.dot(J) + mi*omega).dot(J.T).dot(Y1-T)) #FUNCIONA BIEN

    # import pandas as pd
    # from openpyxl import Workbook