"""Projet renov'eau """

import matplotlib.pyplot as plt 
import numpy as np 


def conso_eau(nb_jour) : 
    normal = np.zeros((nb_jour,1))
    renov = np.zeros((nb_jour,1))
    for k in range (nb_jour) : 
        normal[k, 0] = 96 * k #en Litres en considérant 1 douche par jour 
        renov[k, 0] = 23 * k 
    return normal, renov 

def conso_energie(nb_jour): 
    normal = np.zeros((nb_jour,1))
    renov = np.zeros((nb_jour,1))
    for k in range (nb_jour) : 
        normal[k, 0] = 2.5 * k #en kWh en considérant 1 douche par jour 
        renov[k, 0] = 0.75 * k 
    return normal, renov 

def facture(nb_jour, conso_eau, conso_energie):
    prix_kWh = 0.2026 #eur (prix EDF en mars)
    prix_L_eau = 0.00434 #eur (eaufrance.fr)
    normal = np.zeros((nb_jour, 1))
    renov = np.zeros((nb_jour, 1))
    for k in range(nb_jour): 
        normal[k, 0] = conso_eau(nb_jour)[0][k,0] * prix_L_eau + conso_energie(nb_jour)[0][k,0] * prix_kWh
        renov[k, 0] = conso_eau(nb_jour)[1][k,0] * prix_L_eau + conso_energie(nb_jour)[1][k,0] * prix_kWh
    return normal, renov 

nb_jour = 365
X = np.arange(0, nb_jour).reshape(nb_jour, 1)
Y_normal = facture(nb_jour, conso_eau, conso_energie)[0]
Y_renov =  facture(nb_jour, conso_eau, conso_energie)[1]
Y_economie = Y_normal - Y_renov

# plt.figure()
# plt.plot(X, Y_normal, label = 'Douche standard', color = 'red')
# plt.plot(X, Y_renov, label = 'Douche renov eau', color = 'blue')
# plt.plot(X, Y_economie, label = 'Economies', color ='green')
# plt.xlabel('Temps en jours')
# plt.ylabel('Coût en euros')
# plt.grid()
# plt.legend()
# plt.show()
print ("Argent economisé sur 1 an pour 1 personne : ", Y_economie[-1, 0])






