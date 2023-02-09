from typing_extensions import ParamSpec
from Fun_S import Fun_S
from modelo2 import modelo2
from Jk import Jf
from LeverMarq import LeverMarq

# load Medidas_triplicata1_tumor_Doxo

global param
alfa = 3.47
K = 5.8 * 1e3
mu = 6.3 * 1e2
a = 5.2
lamda = 0.006
tempo = [0, 2, 4, 12, 14, 16, 18, 20, 34, 36, 38, 40, 42, 57, 59]

param = [alfa, K, mu, a, lamda] # Modelo2
Nt = len(tempo)
y0[0] = 1e3
y0[1] = 5.4352

# scipy.integrate.ode(f).set_integrator('vode', method='bdf', order=15)
# Qué se hace en la línea de abajo?
# [t,y2] = ode15s('modelo2',tempo,y0);figure;plot(y2(:,1))
