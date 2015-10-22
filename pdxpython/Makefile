TEX = abjad.tex
PDF = abjad.pdf
IPY = demos/ipython/abjad-ipython-demo.ipynb
MP3 = demos/audio/abjad.mp3

clean:
	find . -name "*.aux" -exec rm -rf {} \;
	find . -name "*.bbl" -exec rm -rf {} \;
	find . -name "*.blg" -exec rm -rf {} \;
	find . -name "*.lof" -exec rm -rf {} \;
	find . -name "*.log" -exec rm -rf {} \;
	find . -name "*.out" -exec rm -rf {} \;
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.toc" -exec rm -rf {} \;
	find . -name "*.nav" -exec rm -rf {} \;
	find . -name "*.snm" -exec rm -rf {} \;
	find . -name "*.vrb" -exec rm -rf {} \;
	rm -Rif _minted-abjad/

book:
	ajv book \
		-a ./assets \
		-g ./abjadbook.cfg \
		-l . \
		-y ./stylesheet.ily \
		abjad.tex source/*.tex

latex:
	xelatex \
		-shell-escape \
		$(TEX)
	xelatex \
		-shell-escape \
		$(TEX)

slides:
	make book
	make latex
	make clean
	make open

open:
	open $(PDF)

ipython:
	ipython notebook $(IPY)

play:
	open -a "QuickTime Player" $(MP3)