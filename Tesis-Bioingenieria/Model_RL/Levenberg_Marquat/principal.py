from Fun_S import Fun_S
from modelo2 import modelo2
from Jk import Jf
from LeverMarq import LeverMarq

# load Medidas_triplicata1_tumor_Doxo

t = 60
y = 1e3
param = 1
alfa = 3.47
K = 5.8*1e3
mu = 6.3*1e2
a = 5.2
lamda = 0.006
frac = 0.005
p_mais = 1.0 + frac
p_menos = 1.0 - frac
Yt = modelo2(param)
Y = Doxo_mean

# De dónde sale Doxo_mean?
res = LeverMarq(Y) # função Leverber Marquardt