def Fun_S(P,Y):
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    import time
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import SGDRegressor
    from joblib import dump, load

    RL_model = load('model_RL_07-09-2021.joblib') # Se carga el último modelo entrenado

    Taux = RL_model.predict(P.reshape(1,-1)) # Taux = modelo2(P); %comsol
    T= Taux.T # T = Taux[P,:].T
    # s = np.sum((Y-Taux).T*(Y-Taux)) # N no es T? que sería el vector de temperatura utilizando los parametros en P
    # s = np.sum((Y-T)**2)
    s = np.dot((Y-T).T,(Y-T))
    return s # Dimensión: 97x97

    #T --> (1x97)
    #Y --> (97x1)

    # De dónde salen las variables Y y N?