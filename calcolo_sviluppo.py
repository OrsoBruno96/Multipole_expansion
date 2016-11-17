import funzioni_utili
from funzioni_utili import *


### per aggiungere simboli nuovi puoi usare la sintassi
### y = symbols('nome_y', real=True)



#############  QUI I DATI DA INSERIRE ############

esempio_1 = numpy.array([[a,0,0,q],[a,sympy.pi,0,q], [a,sympy.pi/2, 0, q], [a,sympy.pi/2, sympy.pi/2, q], [a,sympy.pi/2, sympy.pi, q], [a,sympy.pi/2, 3*sympy.pi/2, q], [0,0,0,-6*q] ]) #6 cariche sugli assi cartesiani a distanza a dal centro e una in mezzo -6q
esempio_2 = numpy.array([[a,0,0,q],[a,sympy.pi,0,-q]]) #classico dipolo elettrico
esempio_3 = numpy.array([[a,0,0,q],[a,sympy.pi,0,q], [0,0,0,-2*q]]) #quadrupolo classico
esempio_4 = numpy.array([[a,sympy.acos(1/sympy.sqrt(3)), 0, q], [a, sympy.acos(1/sympy.sqrt(3)), sympy.pi/2, q], [a, sympy.acos(1/sympy.sqrt(3)), sympy.pi, q], [a, sympy.acos(1/sympy.sqrt(3)), 3*sympy.pi/2, q],[a,sympy.pi-sympy.acos(1/sympy.sqrt(3)), 0, q], [a, sympy.pi-sympy.acos(1/sympy.sqrt(3)), sympy.pi/2, q], [a, sympy.pi-sympy.acos(1/sympy.sqrt(3)), sympy.pi, q], [a, sympy.pi-sympy.acos(1/sympy.sqrt(3)), 3*sympy.pi/2, q] ] ) # cubo di cariche puntiformi




vettore_cariche = esempio_2 #in questo caso il vettore e' [r,theta,phi, q]




file_out = 'sviluppo.tex'       # su quale file .tex vuoi scrivere
ordine = 4                    #ordine a cui fermare lo sviluppo




########## FINE DATI DA INSERIRE ###########

##########################################
#####   QUESTO E' IL PROGRAMMA ###########
##########################################
    

espr = calcolo_sviluppo_puntif(ordine, vettore_cariche)
output_latex(espr, file_out, ordine)

