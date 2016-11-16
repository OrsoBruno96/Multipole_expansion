import funzioni_utili
from funzioni_utili import *



file_armoniche = 'armoniche.tex'
ordine = 2


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


scrivi_armoniche(ordine)











