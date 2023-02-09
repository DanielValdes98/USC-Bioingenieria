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


nmi_h2oDW = 1.96
nmi_h2o25 = 13.72
nmi_h2o50 = 45.08
nk = 0.6034 # = 0.6034 + 0.6034*0.1

#Sigmas:
sigma_nk =  nk*0.1
sigma_mi_DW =  nmi_h2oDW*0.1
sigma_mi_25 =  nmi_h2o25*0.1
sigma_mi_50 =  nmi_h2o50*0.1

#Vectores de 50 aleatorios:
Randnk = nk + np.random.randn(50)*sigma_nk
Rand_miDW = nmi_h2oDW + np.random.randn(50)*sigma_mi_DW 
Rand_mi25 = nmi_h2o25 + np.random.randn(50)*sigma_mi_25 
Rand_mi50 = nmi_h2o50 + np.random.randn(50)*sigma_mi_50 

Y3 = np.loadtxt('Exp_Data_Kel_50.txt',delimiter=',')
Y3 = Y3.reshape(-1,1) #50

Y2 = np.loadtxt('Exp_Data_Kel_25.txt',delimiter=',')
Y2 = Y2.reshape(-1,1) #25

Y1 = np.loadtxt('Exp_Data_Kel_DW.txt',delimiter=',')
Y1 = Y1.reshape(-1,1) #DW


#T_LM, T_ti, res, P_prueba,i,j


a = np.zeros((50, 4))   
b = np.zeros((1,97))  
c = np.zeros( (50, 1)) 

resDW,res25,res50 = np.empty_like(a),np.empty_like(a),np.empty_like(a)
T_LM_DW = np.empty_like(b)
T_ti_DW = np.empty_like(b)
P_prueba_DW = np.empty_like(a)
i1=np.empty_like(c)
j1=np.empty_like(c)


for i in range(1,len(Randnk)):
    start = time.time() # Iniciar medida del tiempo

    # resDW[i] = Lever_Marq1(Randnk[i], Rand_miDW[i], Y1)
    # res25[i] = Lever_Marq1(Randnk[i], Rand_mi25[i], Y2)
    # res50[i] = Lever_Marq1(Randnk[i], Rand_mi50[i], Y3)

    # resDW[i] = Gauss(Randnk[i], Rand_miDW[i], Y1)
    # res25[i] = Gauss(Randnk[i], Rand_mi25[i], Y2)
    res50[i] = Gauss(Randnk[i], Rand_mi50[i], Y3)

    end = time.time() # Tomar el tiempo final

total = end - start
# print(Rand_miDW[1])

# print(resDW,'\n') #DW
# print('Promedio DW parametro k (LM): ',np.mean(resDW[:,2]))
# print('Promedio DW parametro mi_h2o (LM): ',np.mean(resDW[:,3]))

# print('STD DW parametro k (LM): ',np.std(resDW[:,2]))
# print('STD DW parametro mi_h2o (LM): ',np.std(resDW[:,3]))

# print(res25,'\n') #25
# print('Promedio 0.025% parametro k (LM): ',np.mean(res25[:,2]))
# print('Promedio 0.025% parametro mi_h2o (LM): ',np.mean(res25[:,3]))

# print('STD 0.025% parametro k (LM): ',np.std(res25[:,2]))
# print('STD 0.025% parametro mi_h2o (LM): ',np.std(res25[:,3]))

print(res50,'\n') #50
print('Promedio 0.050% parametro k (LM): ',np.mean(res50[:,2]))
print('Promedio 0.050% parametro mi_h2o (LM): ',np.mean(res50[:,3]))

print('STD 0.050% parametro k (LM): ',np.std(res50[:,2]))
print('STD 0.050% parametro mi_h2o (LM): ',np.std(res50[:,3]),'\n')

print('Tiempo de ejecucion total: ', total)
print('Tiempo de ejecucion por muestra: ', total/50)







# print(Randnk)
# print(np.std(Randnk))
# print(np.mean(Randnk))
# print(Vnmi_h2oDW)
# print(Vnmi_h2o25)
# print(Vnmi_h2o50)
# print(Vnk)