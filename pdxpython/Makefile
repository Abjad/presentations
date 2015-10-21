TEX = abjad.tex
PDF = abjad.pdf
IPY = abjad-ipython-demo.ipynb
MP3 = abjad.mp3

clean:
	find . -name "*.aux" -exec rm -rf {} \;
	find . -name "*.bbl" -exec rm -rf {} \;
	find . -name "*.blg" -exec rm -rf {} \;
	find . -name "*.lof" -exec rm -rf {} \;
	find . -name "*.log" -exec rm -rf {} \;
	find . -name "*.out" -exec rm -rf {} \;
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.toc" -exec rm -rf {} \;

book:
	ajv book \
		-a ./assets \
		-g ./abjadbook.cfg \
		-l . \
		-y ./stylesheet.ily \
		abjad.tex

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
	open $(PDF)

ipython:
	ipython notebook $(IPY)

play:
	open -a "QuickTime Player" $(MP3)