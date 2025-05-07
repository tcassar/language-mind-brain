LATEXCC=latexmk
LATEX_FLAGS=-pdf -shell-escape
TAGRET=main.tex

interactive:
	$(LATEXCC) $(LATEX_FLAGS) -pvc $(TAGRET)

static:
	$(LATEXCC) $(LATEX_FLAGS) $(TAGRET)

clean:
	$(LATEXCC) -C
	
