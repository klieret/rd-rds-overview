all: main.pdf

main.pdf: main.tex input/*.tex
	pdflatex main.tex
