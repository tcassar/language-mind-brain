LATEXCC=latexmk
LATEX_FLAGS=-pdf
TAGRET=main.tex

interactive:
	$(LATEXCC) $(LATEX_FLAGS) -pvc $(TAGRET)

static:
	$(LATEXCC) $(LATEX_FLAGS) $(TAGRET)

clean:
	$(LATEXCC) -C
	
