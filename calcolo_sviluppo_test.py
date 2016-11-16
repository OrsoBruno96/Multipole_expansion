import mpmath
import sympy
from sympy import symbols
from sympy import *
from sympy import init_printing
from sympy.abc import theta, phi
from sympy import Integral, latex
import numpy

x = symbols('x')
R = symbols('r', real=True)
q = symbols('q', real=True)
a = symbols('a', real=True)
theta = symbols('theta', real=True) 
phi = symbols('phi', real=True)




#############  QUI I DATI DA INSERIRE ############

esempio_1 = numpy.array([[a,0,0,q],[a,sympy.pi,0,q], [a,sympy.pi/2, 0, q], [a,sympy.pi/2, sympy.pi/2, q], [a,sympy.pi/2, sympy.pi, q], [a,sympy.pi/2, 3*sympy.pi/2, q], [0,0,0,-6*q] ]) #6 cariche sugli assi cartesiani a distanza a dal centro e una in mezzo -6q
esempio_2 = numpy.array([[a,0,0,q],[a,sympy.pi,0,-q]]) #classico dipolo elettrico
esempio_3 = numpy.array([[a,0,0,q],[a,sympy.pi,0,q], [0,0,0,-2*q]]) #quadrupolo classico




vettore_cariche = esempio_2 #in questo caso il vettore è [r,theta,phi, q]
rho = 0

file_out = 'sviluppo.tex'       # su quale file .tex vuoi scrivere
ordine = 2                     #ordine a cui fermare lo sviluppo



########## FINE DATI DA INSERIRE ###########

















##########################################
#####   QUESTO E' IL PROGRAMMA ###########
##########################################




def polinomio_Legendre(l):
    if not (isinstance(l, int)): ## controlla se il valore inserito è un intero
        print('Solo valori interi per i polinomi di legendre, pota')
        return
    y = (x**2-1)**l
    for i in range(0,l):
        y = diff(y, x)        
    y = y *Rational(1/ (2**l*factorial(l))) 
    y = factor(y)   
    return y
    
    
def polinomio_Legendre_associato(l,m):
    if not (isinstance(l, int)):
        print('l deve essere intero')
        return
    if not (isinstance(m, int)):
        print('m deve essere intero')
        return
    if abs(m) > l:
        print('m deve essere minore in modulo di l')
        return
        
    if m == 0:
        y =  polinomio_Legendre(l)
        y.subs(x, cos(theta))
        return y
    if m < 0:
        y = polinomio_Legendre_associato(l,-m)
        y = (-1)**m*Rational((factorial(l+m)/factorial(l-m))) * y
        return y
    
    y = polinomio_Legendre(l)
    for i in range(0,m):
        y = diff(y,x)
    
    y = (-1)**m * sympy.sqrt((1-x**2)**(m))*y
    return y

def armonica_sferica(l,m):
    y = polinomio_Legendre_associato(l,m)
    y = sympy.sqrt((2*l+1) * Rational(factorial(l-m)/(4*factorial(l+m))))*y/sympy.sqrt(sympy.pi)
    y = y.subs(x, cos(theta))
    y = trigsimp(y)
    y = simplify(y)
    y = powsimp(y, force = True)
    y = y * sympy.exp(sympy.I * m *phi)
    return y

# 
# def coefficiente_sviluppo_puntif(l,m,r,theta_v,phi_v):
#     z = r**l*armonica_sferica(l,-m)*(-1)**m
#     z = z.subs(theta, theta_v)
#     z = z.subs(phi, phi_v)
#     z = z * 4*sympy.pi/(2*l+1)
#     return z


# def calcolo_sviluppo_puntif(l, punti):
#     print('Sviluppo cariche puntiformi')
#     sviluppo = x
#     sviluppo = sviluppo - x
#     for i in range(0,l+1):
#         print('Faccio l = %d' %(i))
#         for j in range(0,i+1):
#             print('Faccio m = %d' %(j))
#             for h in range(0,len(punti)):
#                 pota = coefficiente_sviluppo_puntif(i,j, punti[h][0], punti[h][1], punti[h][2])
#                 ylm = armonica_sferica(i,j)
#                 if (not j==0):
#                     sviluppo = sviluppo + punti[h][3]*( 2*re(pota*ylm) )/R**(i+1)
#                 else:
#                     sviluppo = sviluppo + punti[h][3]*( pota*ylm ) /R**(i+1)
#                 
#     return sviluppo
#     
def coefficiente_sviluppo(l, m, densita):
    z = armonica_sferica(l,-m)*(-1)**m*sympy.sin(theta)
    z = z * R**l*densita
    print('integrale')
    z = integrate(z,( phi, 0, 2*sympy.pi))
    print('integrale')
    z = integrate(z, (theta, 0, sympy.pi))
    print('integrale')
    z = integrate(z, (R, 0, oo))
    print('integrale finito')
    z = z * (4*sympy.pi)/(2*l+1)
    return z


def calcolo_sviluppo(l, densita):
    print('Sviluppo densita')
    sviluppo = x
    sviluppo = sviluppo - x
    for i in range(0,l+1):
        print('Faccio l = %d' %(i))
        for j in range(-i,i+1):
            print('Faccio m = %d' %(j))
            sviluppo = sviluppo + coefficiente_sviluppo(i,j,densita)*armonica_sferica(i,j)/R**(i+1)
                
    
    return sviluppo



def vec_to_delta(vec):
    return vec[3]*DiracDelta(R-vec[0])*DiracDelta(cos(theta) - sympy.cos(vec[1])) * DiracDelta(phi - vec[2])/R**2






def output_latex(espressione):
    scrittura = open(file_out, 'w')
    scrittura.write('\\documentclass[11pt]{article} \n\\usepackage[T1]{fontenc} \n\\usepackage[utf8]{inputenc} \n')
    scrittura.write('\\usepackage[italian]{babel} \n\\usepackage[a4paper]{geometry} \n\\usepackage[pdftex]{graphicx} \n')
    scrittura.write('\\usepackage{amsmath}')
    scrittura.write('\n\\usepackage{amssymb} \n\\usepackage[T1,OT1]{fontenc}  \n\\title{Espansione in armoniche sferiche fino all\'ordine %d} \n\\begin{document} \n\maketitle \n\n\n' %(ordine))    
    scrittura.write('\[ %s \] \n' %(latex(espressione)))
    scrittura.write('\\end{document} \n ')
    scrittura.close()    



for i in range(0,len(vettore_cariche)):
    rho = rho + vec_to_delta(vettore_cariche[i])
    





    
    

espr = calcolo_sviluppo(ordine, rho)# + calcolo_sviluppo_rho(ordine, rho)
output_latex(espr)

    