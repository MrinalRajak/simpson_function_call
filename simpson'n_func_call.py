

#simpson'n function call variable step

import numpy as np
from scipy.integrate import simps
import matplotlib.pyplot as plt

n=25
a=float(input("Enter the lower limit: "))
b=float(input("Enter the upper limit: "))
tol=float(input("Enter the tolerance: "))

x,h=np.linspace(a,b,n,retstep=True)
y=(3/(x**2*np.sqrt(2*np.pi)))*np.exp(-9/(2*x**2))

i=(h/3)*(y[0]+y[-1]+4*y[-2])
i1=0
while(abs(i-i1)>tol):
    i1=i
    n=n+2
    x,h=np.linspace(a,b,n,retstep=True)
    y=(3/(x**2*np.sqrt(2*np.pi)))*np.exp(-9/(2*x**2))
    i=(h/3)*(y[0]+y[-1]+4*np.sum(y[1:-1:2])+2*np.sum(y[2:-1:2]))
print("no.of iteration: ",(n-3)/2)
print("Algorithm based comsite simpson's(1/3)rd rule Result: ",i)
print("scipy based integration result: ",simps(y,dx=h))
plt.plot(x,y,c='r',label='Area under the curve')
plt.grid(True)
plt.legend()
plt.show()

# you can use any user defined functions.
    

