all:
	make book
	make latex

book:
	ajv book \
		-g abjadbook.cfg \
		-y stylesheet.ily \
		demo.tex

latex:
	xelatex demo.tex
	xelatex demo.tex