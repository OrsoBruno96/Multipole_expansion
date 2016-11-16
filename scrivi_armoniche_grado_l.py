import mpmath
import sympy
from sympy import symbols
from sympy import *
from sympy import init_printing
from sympy.abc import theta, phi
from sympy import Integral, latex
import numpy

x = symbols('x')
R = symbols('r')
q = symbols('q')
a = symbols('a')
theta = symbols('theta') 
phi = symbols('phi')

swag = numpy.array([[a,0,0,q],[a,sympy.pi,0,-q]])



file_armoniche = 'pota.tex'



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



def scrivi_armoniche(l):
    scrittura = open(file_armoniche, 'w')
    scrittura.write('\\documentclass[11pt]{article} \n\\usepackage[T1]{fontenc} \n\\usepackage[utf8]{inputenc} \n')
    scrittura.write('\\usepackage[italian]{babel} \n\\usepackage[a4paper]{geometry} \n\\usepackage[pdftex]{graphicx} \n')
    scrittura.write('\\usepackage{amsmath}')
    scrittura.write('\n\\usepackage{amssymb} \n\\usepackage[T1,OT1]{fontenc}  \n\\title{Armoniche sferiche di ordine $l$} \n\\begin{document} \n\maketitle \n\n\n')    
    for m in range(-l,l+1):
        y = armonica_sferica(l,m)
        scrittura.write('\[l = %d, m = %d \qquad ' %(l,m))
        scrittura.write('%s   \] \n \n' %(latex(y)))
    scrittura.write('\\end{document} \n ')
    scrittura.close()

def coefficiente_sviluppo(l,m,r,theta_v,phi_v):
    z = r**l*armonica_sferica(l,-m)*(-1)**m
    z = z.subs(theta, theta_v)
    z = z.subs(phi, phi_v)
    z = z * 4*sympy.pi/(2*l+1)
    return z








def calcolo_sviluppo(l, punti):
    sviluppo = x
    sviluppo = sviluppo - x
    for i in range(0,l+1):
        print('Faccio l = %d' %(i))
        for j in range(-i,i):
            print('Faccio m = %d' %(j))
            for h in range(0,len(punti)):
                sviluppo = sviluppo + punti[h][3]*coefficiente_sviluppo(i,j, punti[h][0], punti[h][1], punti[h][2])*armonica_sferica(i,j)/R**(i+1)
                
    
    return sviluppo
    
print(calcolo_sviluppo(2,swag))
    









