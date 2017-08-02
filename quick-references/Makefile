all:
	make compile
	make open

compile:
	make compile-abjad
	make compile-bash
	make compile-lilypond
	make compile-python

open:
	make open-abjad
	make open-bash
	make open-lilypond
	make open-python

compile-abjad:
	ajv book -v -g abjadbook.cfg -y stylesheet.ily abjad-quick-reference.tex
	pdflatex -shell-escape abjad-quick-reference.tex
	pdflatex -shell-escape abjad-quick-reference.tex

compile-bash:
	pdflatex -shell-escape bash-quick-reference.tex
	pdflatex -shell-escape bash-quick-reference.tex

compile-lilypond:
	ajv book -v -g abjadbook.cfg -y stylesheet.ily lilypond-quick-reference.tex
	pdflatex -shell-escape lilypond-quick-reference.tex
	pdflatex -shell-escape lilypond-quick-reference.tex

compile-python:
	ajv book -v -g abjadbook.cfg -y stylesheet.ily python-quick-reference.tex
	pdflatex -shell-escape python-quick-reference.tex
	pdflatex -shell-escape python-quick-reference.tex

open-abjad:
	open abjad-quick-reference.pdf

open-bash:
	open bash-quick-reference.pdf

open-lilypond:
	open lilypond-quick-reference.pdf

open-python:
	open python-quick-reference.pdf
