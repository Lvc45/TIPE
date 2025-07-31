# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
#Méthode d'Euler
def simu(Lt,wo,lamb):
    q = [-2.5]
    p = [0]
    for i in range(len(Lt)-1):
        dt = Lt[i+1]-Lt[i]
        q.append(p[i]*dt+q[i])
        p.append(p[i]-dt*((wo**2)*q[i]+2*lamb*p[i]))
    return q
#Abscisse 
Lt1 = [.01*i for i in range(120)]
#Départ depuis l'origine
Y = simu(Lt1,11.5,2.5)
Y2=[]
for k in range(len(Y)):
    Y2.append(Y[k]+2.5)
#Affichage de la courbe    
plt.plot(Lt1,Y2)
plt.grid()
plt.xlabel('Temps en seconde')
plt.ylabel('Volt')
plt.show()