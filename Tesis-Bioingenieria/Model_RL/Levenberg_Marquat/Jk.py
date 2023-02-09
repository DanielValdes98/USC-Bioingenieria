from modelo2 import modelo2

def Jf(P):
    import numpy as np
    # p_mais = evalin('base','p_mais');
    # p_menos = evalin('base','p_menos');

    Fmais = param4*p_mais
    Fmenos = param4*p_menos
    Taux = modelo2(Fmais,P)
    Taux = modelo2(Fmenos,P)
    r = (((Taux[P,:]) - (Taux[P,:]))/(Fmais-Fmenos))
    # r = (((Taux(P,:)) - (Taux2(P,:)))/(Fmais-Fmenos));

    # Qué hace la función evalin()?
    # De dónde salen las variables param4, p_mais,p_menos?
    return r