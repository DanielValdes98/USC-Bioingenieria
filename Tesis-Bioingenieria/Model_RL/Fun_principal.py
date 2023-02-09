def LV():
    pass
    # #cargar librerias necesarias
    # import numpy as np
    # import matplotlib.pyplot as plt
    # from numpy.linalg.linalg import multi_dot
    # from sklearn.linear_model import LinearRegression
    # from sklearn import metrics
    # from sklearn.metrics import mean_squared_error
    # from sklearn.model_selection import train_test_split
    # from sklearn.preprocessing import StandardScaler
    # from sklearn.linear_model import SGDRegressor
    # from joblib import dump, load
    # from numpy.linalg import norm 
    # import pandas as pd

    # from Jf import Jf
    # from Y_exact_upload import Y_exact_upload
    # from Fun_S import Fun_S

    # YE50,YE25,YEDW,YExact_Comsol,DTE_Comsol = Y_exact_upload()

    # # import random
    # # mu, sigma, e = 0, 0.05, 0.1 # mean, standard deviation and error
    # # Y = np.random.normal(YE25, sigma*e)
    # # Y = Y.reshape(-1,1)

    # # EXPORTAR LA Y CON ERROR:
    # # df = pd.DataFrame(Y)
    # # df.to_excel('Y.xlsx')

    # #  Cargar Y con error:
    # Y = np.loadtxt('Y.txt',delimiter=',')
    # Y = Y.reshape(-1,1)

    # #RL_model = load('model_RL_27-06-2021.joblib') ---> MEJOR MODELO ENTRENADO HASTA AHORA
    # RL_model = load('model_RL_07-09-2021.joblib') # Se carga el último modelo entrenado

    # # Parametros fijos:
    # cp = 4184.1 
    # k = 0.6034 

    # # Parametros a estimar:
    # nwp = 1098.02 # = 998.20 + 998.20*0.1 
    # nmi_h2o = 15.092 # = 13.72 + 13.72*0.1 --> 0.025%
    # nmi_h2o1 = 49.588 # = 45.08 + 45.08*0.1  --> 0.050%
    # nmi_h2o2 = 2.156 # = 1.96 + 1.96*0.1  --> Distilled Water

    # # P estimado
    # P_est = [nwp,nmi_h2o]
    # P_est = np.array(P_est)
    # P_est = P_est.reshape(-1,1) #IMPORTANTE

    # # Vector de entrada:
    # P = [cp, P_est[0,0], k, P_est[1,0]]
    # P = np.array(P)

    # #Parametros iniciales sin ninún cambio:
    # P_prueba = [cp, P_est[0,0], k, P_est[1,0]]
    # P_prueba = np.array(P_prueba)

    # Taux = RL_model.predict(P.reshape(1,-1))
    # J = Jf(P)
    # omega = np.diag(np.diag((J.T).dot(J))) # MATLAB ---> omega = diag(diag(J'*J)) // Matriz 2x2

    # T= Taux.T
    # mi = 0.001

    # i=1
    # j=1
    # while (norm(P_est - (P_est + np.linalg.inv(J.T.dot(J) + mi*omega).dot(J.T).dot(Y-T))) > 10e-5):
    #     Taux = RL_model.predict(P.reshape(1,-1))
    #     T= Taux.T
    #     J = Jf(P)
    #     omega = np.diag(np.diag(J.T.dot(J))) # MATLAB ---> omega = diag(diag(J'*J)) // Matriz 2x2    
    #     Paux = P_est + np.linalg.inv(J.T.dot(J) + mi*omega).dot(J.T).dot(Y-T)
    #     nP = [cp,Paux[0,0],k,Paux[1,0]]
    #     nP = np.array(nP)

    #     if (Fun_S(P,Y) < Fun_S(nP,Y)):
    #         mi = 10*mi
    #         j = j + 1

    #     else:
    #         P_est = Paux
    #         P = nP
    #         mi = 0.1*mi

    #         # VnP = []
    #         # VnP = np.array(VnP)
    #         # VnP[i] = P_est
    #         i = i + 1
    #         # print(nP)
    # res = P

    # # print(VnP)

    # T_LM = RL_model.predict(res.reshape(1,-1))
    # T_LM = T_LM.T

    # T_ti = RL_model.predict(P_prueba.reshape(1,-1))
    # T_ti = T_ti.T

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
    # # print(P_est + np.linalg.inv(J.T.dot(J) + mi*omega).dot(J.T).dot(Y1-T)) #FUNCIONA BIEN

    # # import pandas as pd
    # # from openpyxl import Workbook

from numpy.matrixlib.defmatrix import matrix
from Gauss_New import Gauss
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Lever_Marq import Lever_Marq
from Lever_Marq1 import Lever_Marq1
from Lever_Marq2 import Lever_Marq2
from Gauss_New import Gauss
from Y_exact_upload import Y_exact_upload
import time

YE50,YE25,YEDW,YExact_Comsol,DTE_Comsol = Y_exact_upload()

# import random
# mu, sigma, e = 0, 0.05, 0.1 # mean, standard deviation and error

# Y1 = np.random.normal(YEDW, sigma*e)
# Y1 = Y1.reshape(-1,1)

# Y2 = np.random.normal(YE25, sigma*e)
# Y2 = Y2.reshape(-1,1)

# Y3 = np.random.normal(YE50, sigma*e)
# Y3 = Y3.reshape(-1,1)

# #EXPORTAR LA Y CON ERROR:
# df1 = pd.DataFrame(Y1)
# df1.to_excel('Y1.xlsx')

# df2 = pd.DataFrame(Y2)
# df2.to_excel('Y2.xlsx')

# df3 = pd.DataFrame(Y3)
# df3.to_excel('Y3.xlsx')

#  Cargar Y con error gaussiano:
# Y1 = np.loadtxt('Y1.txt',delimiter=',')
# Y1 = Y1.reshape(-1,1)

# Y2 = np.loadtxt('Y2.txt',delimiter=',')
# Y2 = Y2.reshape(-1,1)

# Y3 = np.loadtxt('Y3.txt',delimiter=',')
# Y3 = Y3.reshape(-1,1)

#RESULTADOS EXPERIMENTALES PARA CADA CONCENTRACIÓN:
Y3 = np.loadtxt('Exp_Data_Kel_50.txt',delimiter=',')
Y3 = Y3.reshape(-1,1) #50

Y2 = np.loadtxt('Exp_Data_Kel_25.txt',delimiter=',')
Y2 = Y2.reshape(-1,1) #25

Y1 = np.loadtxt('Exp_Data_Kel_DW.txt',delimiter=',')
Y1 = Y1.reshape(-1,1) #DW

#Y1 SIMULADADA:
Sim_LM_50 = np.loadtxt('Datasets\BBDD_data_LevMarq_wt_Nanofluid_50.txt',delimiter=',')
# Y1_Sim = Y1_Sim.reshape(-1,1) #50

Sim_LM_25 = np.loadtxt('Datasets\BBDD_data_LevMarq_wt_Nanofluid_25.txt',delimiter=',')
# Y2_Sim = Y2_Sim.reshape(-1,1) #50

Sim_LM_DW = np.loadtxt('Datasets\BBDD_data_LevMarq_wt_Nanofluid_DW.txt',delimiter=',')
# Y3_Sim = Y3_Sim.reshape(-1,1) #50

# Variables de entrada:
X1_Sim = Sim_LM_50[:4]
X2_Sim = Sim_LM_25[:4]
X3_Sim = Sim_LM_DW[:4]

# Variables de salida:
Y1_Sim = Sim_LM_50[4:101]
Y2_Sim = Sim_LM_25[4:101]
Y3_Sim = Sim_LM_DW[4:101]

# Parametros a estimar:
nwp = 998.20 + 998.20*0.01 
nmi_h2oDW = 1.96 + 1.96*0.1 # --> Distilled Water
nmi_h2o25 = 13.72 + 13.72*0.1 #--> 0.025%
nmi_h2o50 = 45.08 + 45.08*0.1 # --> 0.050%
nk = 0.6034 + 0.6034*0.05

cpE = 4184.1 
pE = 998.20 
kE = 0.6034
mi_h2oEDW = 1.96
mi_h2oE25 = 13.72
mi_h2oE50 = 45.08


# ESTIMANDO RHO Y MI_H2O
# T_LM_DW, T_ti_DW, resDW, P_prueba_DW,i1,j1 = Lever_Marq(nwp, nmi_h2oDW, Y1)
# T_LM_25, T_ti_25, res25, P_prueba_25,i2,j2 = Lever_Marq(nwp, nmi_h2o25, Y2)
# T_LM_50, T_ti_50, res50, P_prueba_50,i3,j3 = Lever_Marq(nwp, nmi_h2o50, Y3)

# ESTIMANDO K Y MI_H2O
start = time.time() # Iniciar medida del tiempo
T_LM_DW, T_ti_DW, resDW, P_prueba_DW,i1,j1 = Lever_Marq1(nk, nmi_h2oDW, Y1)
T_LM_25, T_ti_25, res25, P_prueba_25,i2,j2 = Lever_Marq1(nk, nmi_h2o25, Y2)
T_LM_50, T_ti_50, res50, P_prueba_50,i3,j3 = Lever_Marq1(nk, nmi_h2o50, Y3)
end = time.time() # Tomar el tiempo final
total = end - start
# print('Tiempo total Levenberg - Marquadt: ' + str(total) + ' segundos')

# ESTIMANDO RHO, K Y MI_H2O
# T_LM_DW, T_ti_DW, resDW, P_prueba_DW,i1,j1,J1,omega1,Paux1 = Lever_Marq2(nwp,nk, nmi_h2oDW, Y1)
# T_LM_25, T_ti_25, res25, P_prueba_25,i2,j2,J2,omega2,Paux2 = Lever_Marq2(nwp,nk, nmi_h2o25, Y2)
# T_LM_50, T_ti_50, res50, P_prueba_50,i3,j3,J3,omega3,Paux3 = Lever_Marq2(nwp,nk, nmi_h2o50, Y3)

# IMPLEMENTANDO GAUSS
startGA = time.time() # Iniciar medida del tiempo
T_GA_DW, T_ti_GA_DW, resGADW, P_prueba_GADW,i_GA1 = Gauss(nk, nmi_h2oDW, Y1)
T_GA_25, T_ti_GA_25, resGA25, P_prueba_GA25,i_GA2 = Gauss(nk, nmi_h2o25, Y2)
T_GA_50, T_ti_GA_50, resGA50, P_prueba_GA50,i_GA3 = Gauss(nk, nmi_h2o50, Y3)
endGA = time.time() # Tomar el tiempo final
totalGA = endGA - startGA
# print('Tiempo total Gauss: ' + str(totalGA) + ' segundos')

#EXPORTAR EL CONJUNTO DE PARAMETROS DE ENTRADA QUE ARROJA LEVENBERG-MARQUADT:
a = np.zeros((3, 4))
conjPM = np.empty_like(a)
conjPM[0] = res50
conjPM[1] = res25
conjPM[2] = resDW
conj_pm = pd.DataFrame(conjPM)
conj_pm.to_excel('Parametros_Leven_Marq.xlsx')

print('Tiempo total Levenberg - Marquadt: ' + str(total) + ' segundos')
print('Tiempo total Gauss: ' + str(totalGA) + ' segundos','\n')

print('i1: ',i1,' ','j1: ',j1)
print('P exacto: ', [cpE,pE,kE,mi_h2oE50])
print('P con LM para 50: ', res50)
print('P con GA para 50: ', resGA50)
print('P inicial para 50: ', P_prueba_50,'\n')

print('i2: ',i2,' ','j2: ',j2)
print('P exacto: ', [cpE,pE,kE,mi_h2oE25])
print('P con LM para 25: ', res25)
print('P con GA para 25: ', resGA25)
print('P inicial para 25: ', P_prueba_25,'\n')

print('i3: ',i3,' ','j3: ',j3)
print('P exacto: ', [cpE,pE,kE,mi_h2oEDW])
print('P con LM para DW: ', resDW)
print('P con GA para GA: ', resGADW)
print('P inicial para DW: ', P_prueba_DW,'\n')


# print(J1.shape)
# print(omega1.shape)
# print(Paux1.shape)
# print((J1.T.dot(J1)).shape)

# print(J1.T.dot(J1))
# det1 = np.linalg.det(J1.T.dot(J1))
# print('Det DW: ', det1,'\n')
# print(Paux1)

# print(J2.T.dot(J2))
# det2 = np.linalg.det(J2.T.dot(J2))
# print('Det 25: ', det2,'\n')
# print(Paux2)

# print(J3.T.dot(J3))
# det3 = np.linalg.det(J3.T.dot(J3))
# print('Det 50: ', det3,'\n')
# print(Paux3)


plt.figure(figsize=(20, 10))

# 0.050% wt Nanofluid
plt.plot(Y3 - 297.95,'k',label = 'Medición experimental para nanofluido al 0.050%')
plt.plot(Y1_Sim - 297.95,'g',label = 'Modelo completo usando Levenberg-Marquadt para nanofluido al 0.050%')
plt.plot(T_LM_50 - 297.95,'b',label = 'Modelo RLM usando Levenberg-Marquadt para nanofluido al 0.050%')
plt.plot(T_GA_50 - 297.95,'r',label = 'Modelo RLM usando método de Gauss para nanofluido al 0.050%')

# 0.025% wt Nanofluid
# plt.plot(YE25 - 297.95,'--r',label = 'Modelo completo para nanofluido al 0.025%')
plt.plot(Y2 - 297.95,'--k',label = 'Medición experimental para nanofluido al 0.025%')
plt.plot(Y2_Sim - 297.95,'--g',label = 'Modelo completo usando Levenberg-Marquadt para nanofluido al 0.025%')
plt.plot(T_LM_25 - 297.95,'--b',label = 'Modelo RLM usando Levenberg-Marquadt para nanofluido al 0.025%')
plt.plot(T_GA_25 - 297.95,'--r',label = 'Modelo RLM usando método de Gauss para nanofluido al 0.025%')

# Distilled Water
# plt.plot(YEDW - 297.95,'.r',label = 'Modelo completo para el agua destilada')
plt.plot(Y1 - 297.95,'.k',label = 'Medición experimental para el agua destilada')
plt.plot(Y3_Sim - 297.95,'.g',label = 'Modelo completo usando Levenberg-Marquadt para el agua destilada')
plt.plot(T_LM_DW - 297.95,'.b',label = 'Modelo RLM usando Levenberg-Marquadt para el agua destilada')
plt.plot(T_GA_DW - 297.95,'.r',label = 'Modelo RLM usando método de Gauss para el agua destilada')

print(conj_pm)

print(X1_Sim)
print(X2_Sim)
print(X3_Sim)

plt.legend(loc = "best")
#plt.title("Modelo de regresión lineal", fontsize=14) 
plt.xlabel("Tiempo(s)", fontsize=12) 
plt.ylabel("∆T(°C)", fontsize=12)
#plt.show()
plt.savefig('T_post_LM.png',bbox_inches='tight')
plt.show()
