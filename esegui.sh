echo "Eseguo il programma"
python calcolo_sviluppo_cariche_puntiformi.py
echo "Compilo il file .tex"
pdflatex sviluppo.tex
echo "Visualizzo il file"
gnome-open sviluppo.pdf

