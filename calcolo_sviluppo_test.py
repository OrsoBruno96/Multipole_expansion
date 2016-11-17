import funzioni_utili
from funzioni_utili import *



rho = q/(4*sympy.pi*a**3/3)*Heaviside(a - R)

file_out = 'sviluppo.tex'       # su quale file .tex vuoi scrivere
ordine = 2                     #ordine a cui fermare lo sviluppo





    
    

espr = calcolo_sviluppo_rho(ordine, rho)
output_latex(espr, file_out, ordine)

    
