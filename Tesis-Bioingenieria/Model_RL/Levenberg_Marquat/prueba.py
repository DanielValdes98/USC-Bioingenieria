# scipy.integrate.ode(f).set_integrator('vode', method='bdf', order=15)
from scipy.integrate import ode
from scipy.integrate import solve_ivp
import  matplotlib as plt

from scipy.integrate import solve_ivp
from scipy.special import gamma, airy

def func(t, y):
    return [t*y[1],y[0]]

t_span = [0,2]
y0 = 1

sol1 = solve_ivp(func, t_span, y0)

plt.plot(sol1,'-o')
