all: main.pdf

main.pdf: main.tex input/*.tex
	pdflatex --output-directory build main.tex
