
TEXFILES := $(wildcard *.tex)
BASENAMES := $(basename $(TEXFILES))

.PHONY: all clean $(BASENAMES) watch $(addprefix watch-, $(BASENAMES))

all: $(BASENAMES)

$(BASENAMES): %: %.tex
	latexmk -pdf $<

$(addprefix watch-, $(BASENAMES)):
	@BASENAME=$(@:watch-%=%); \
	latexmk -pdf -pvc $$BASENAME.tex


$(addprefix count-, $(BASENAMES)):
	@BASENAME=$(@:count-%=%); \ 
	@texcount $$BASENAME.tex

clean:
	latexmk -C

