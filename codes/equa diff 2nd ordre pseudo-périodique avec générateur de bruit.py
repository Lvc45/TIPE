# -*- coding: utf-8 -*-
import random
import math
import matplotlib.pyplot as plt
def aleaGauss(sigma):
    U1 = random.random()
    U2 = random.random()
    return sigma*math.sqrt(-2*math.log(U1))*math.cos(2*math.pi*U2)
def simu(Lt,wo,lamb):
    q = [-2.5]
    p = [0]
    for i in range(len(Lt)-1):
        dt = Lt[i+1]-Lt[i]
        q.append(p[i]*dt+q[i]+aleaGauss(.1))
        p.append(p[i]-dt*((wo**2)*q[i]+2*lamb*p[i]))
    return q
Lt1 = [.01*i for i in range(120)]
Y = simu(Lt1,11.5,2.5)
Y2=[]
for k in range(len(Y)):
    Y2.append(Y[k]+2.5)  
plt.plot(Lt1,Y2)
plt.xlabel('Temps en seconde')
plt.ylabel('Volt')
plt.grid()
plt.show()