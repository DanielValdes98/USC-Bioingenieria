def Y_exact_upload():
    import numpy as np
    #Se cargan datos de simulacion con los valores exactos en Comsol with Matlab. Mi_H2O = 45.08
    dataSimulacionValExact50 = np.loadtxt('Datasets\BBDD_data_wt_Nanofluid_50.txt',delimiter=',')
    #Se cargan datos de simulacion con los valores exactos en Comsol with Matlab. Mi_H2O = 13.72
    dataSimulacionValExact25 = np.loadtxt('Datasets\BBDD_data_wt_Nanofluid_25.txt',delimiter=',')
    #Se cargan datos de simulacion con los valores exactos en Comsol with Matlab. Mi_H2O = 1.96
    dataSimulacionValExactDW = np.loadtxt('Datasets\BBDD_data_wt_Nanofluid_DW.txt',delimiter=',')

    # Variables de entrada:
    XExact50 = dataSimulacionValExact50[:4]
    XExact25 = dataSimulacionValExact25[:4]
    XExactDW = dataSimulacionValExactDW[:4]

    # Temperatura de salida:
    YExact50 = dataSimulacionValExact50[4:101]
    YExact25 = dataSimulacionValExact25[4:101]
    YExactDW = dataSimulacionValExactDW[4:101]

    Y_Exact_values_Comsol = np.vstack((YExact50,YExact25,YExactDW))

    # Temperatura incial(COMSOL)= 297.95
    DTPE_Exact_Comsol = Y_Exact_values_Comsol - 297.95

    # import random
    # mu, sigma, e = 0, 0.05, 0.1 # mean and standard deviation
    # Y = np.random.normal(YExact25, sigma*e)
    # Y
    return YExact50,YExact25,YExactDW,Y_Exact_values_Comsol,DTPE_Exact_Comsol