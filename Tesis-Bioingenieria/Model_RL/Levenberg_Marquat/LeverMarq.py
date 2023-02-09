from operator import pos
from Fun_S import Fun_S
from modelo2 import modelo2
from Jk import Jf

def LeverMarq(dy):
    import numpy as np
    from numpy.linalg import norm 

    param4 = 0.1
    P = [param4] #Chute incial
    Taux = modelo2(P)
    J = Jf[P]
    omega = np.diag(np.diag(J.T*J)) #parametros iniciais do Leverberg M.
    mi = 0.001
    i=1
    while (norm(P-(P + np.linalg.inv(J.T*J + mi*omega)*J.T*(Y-N))) > 10e-5):
        Taux = modelo2(P)
        J = Jf(P)
        omega = np.diag(np.diag(J.T*J));
        if (Fun_S[P,pos]<Fun_S(P + np.inv(J.T*J + mi*omega)*J.T*(Y-N),pos)):
            mi = 10*mi
        else:
            P = P + np.inv(J.T * J + mi*omega)*J.T*(Y-N)
            mi = 0.1*mi

        i = i + 1
    res = P


    return res