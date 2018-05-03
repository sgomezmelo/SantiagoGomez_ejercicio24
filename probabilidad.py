import numpy as np
import matplotlib.pyplot as plt
n = 1000
lamb = np.linspace(1.0,100.0,n)
P = np.zeros(n)

for i in range(n):
    l = lamb[i]
    Norm = (np.exp(-1.0/l)-np.exp(-20.0/l))
    px_1 = (1/l)*np.exp(-1.2/l)/Norm
    px_2 = (1/l)*np.exp(-2.5/l)/Norm
    px_3 = (1/l)*np.exp(-2.8/l)/Norm
    px_4 = (1/l)*np.exp(-5.0/l)/Norm
    P[i] = (1.0/99.0)*px_1*px_2*px_3*px_4

h = (100.0-1.0)/n
I = 0.0
for i in range(1,n):
    I += (lamb[i] - lamb[i-1])*(P[i])

plt.figure()
plt.semilogx(lamb,P/I)
plt.savefig('Probabilidad.pdf')

    
    
