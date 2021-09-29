#=========================================================================
# Builders and flags:

BIBTEX = bibtex
PDFLATEX = pdflatex
EPSTOPDF = epstopdf
INKSCAPE = inkscape --without-gui

RM = rm -f
MV = mv


#=========================================================================
# Files:

SRCS = schema

LOGFILES = $(addsuffix .log, $(SRCS)) $(addsuffix .blg, $(SRCS)) \
	   $(addsuffix .out, $(SRCS)) $(addsuffix .snm, $(SRCS))
AUXFILES = $(addsuffix .aux, $(SRCS)) $(addsuffix .bbl, $(SRCS)) \
	   $(addsuffix .vrb, $(SRCS)) $(addsuffix .toc, $(SRCS)) \
	   $(addsuffix .nav, $(SRCS))
RESFILES = $(addsuffix .pdf, $(SRCS))

BIBFILES = schema.bib

#=========================================================================
# Maintargets:

# default target
all: $(RESFILES)

# clean: Remove temporary files
clean:
	$(RM) $(LOGFILES)

# realclean: Remove all intermediate files
realclean:
	$(RM) $(AUXFILES) $(LOGFILES)

# distclean: Remove all automatically created files
distclean:
	$(RM) $(RESFILES) $(AUXFILES) $(LOGFILES) $(PDFIMGS)

# Tell make, that the main targets are not actually files, that should
# considered to be build:
.PHONY: all clean realclean distclean


#=========================================================================
# Implicit rules:

.SUFFIXES:
.SUFFIXES: .tex .pdf .eps .svg .dot

%.bbl: %.tex
	$(PDFLATEX) $*
	$(BIBTEX) $*

%.pdf: %.tex
	while true; do \
	  $(PDFLATEX) $*; \
	  grep -s 'Rerun to get .* right' $*.log || break; \
	done

%.pdf: %.eps
	$(EPSTOPDF) $<

%.eps: %.svg
	$(INKSCAPE) --export-eps=$@ $<

%.svg: %.gv
	dot -Tsvg -o $@ $<


#=========================================================================
# Dependencies:
schema.bbl: schema.tex $(BIBFILES)
schema.pdf: schema.bbl schema.tex
