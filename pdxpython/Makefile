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

slides:
	xelatex $(TEX)
	xelatex $(TEX)
	make clean
	open $(PDF)

ipython:
	ipython notebook $(IPY)

play:
	open -a "QuickTime Player" $(MP3)