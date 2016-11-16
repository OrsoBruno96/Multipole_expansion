import funzioni_utili
from funzioni_utili import *


### per aggiungere simboli nuovi puoi usare la sintassi
### y = symbols('nome_y', real=True)



#############  QUI I DATI DA INSERIRE ############

esempio_1 = numpy.array([[a,0,0,q],[a,sympy.pi,0,q], [a,sympy.pi/2, 0, q], [a,sympy.pi/2, sympy.pi/2, q], [a,sympy.pi/2, sympy.pi, q], [a,sympy.pi/2, 3*sympy.pi/2, q], [0,0,0,-6*q] ]) #6 cariche sugli assi cartesiani a distanza a dal centro e una in mezzo -6q
esempio_2 = numpy.array([[a,0,0,q],[a,sympy.pi,0,-q]]) #classico dipolo elettrico
esempio_3 = numpy.array([[a,0,0,q],[a,sympy.pi,0,q], [0,0,0,-2*q]]) #quadrupolo classico




vettore_cariche = esempio_3 #in questo caso il vettore è [r,theta,phi, q]
rho = q/(4*sympy.pi/3*a**3)*Heaviside(a-R)



file_out = 'sviluppo.tex'       # su quale file .tex vuoi scrivere
ordine = 2                     #ordine a cui fermare lo sviluppo




########## FINE DATI DA INSERIRE ###########

##########################################
#####   QUESTO E' IL PROGRAMMA ###########
##########################################
    

espr = calcolo_sviluppo_puntif(ordine, vettore_cariche)# + calcolo_sviluppo_rho(ordine, rho)
output_latex(espr, file_out, ordine)

