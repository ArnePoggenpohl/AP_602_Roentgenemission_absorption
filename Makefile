ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/main.pdf


# hier Python-Skripte:
build/plot_emission.pdf: plot_emission.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plot_emission.py
build/plot_bragg.pdf: plot_bragg.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plot_bragg.py
build/plot_abs_br.pdf: plot_abs_br.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plot_abs_br.py
build/plot_abs_hg.pdf: plot_abs_hg.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plot_abs_hg.py
build/plot_abs_sr.pdf: plot_abs_sr.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plot_abs_sr.py
build/plot_abs_zr.pdf: plot_abs_zr.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plot_abs_zr.py
build/plot_rydberg.pdf: plot_rydberg.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plot_rydberg.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot_emission.pdf build/plot_rydberg.pdf
build/main.pdf: build/plot_bragg.pdf
build/main.pdf: build/plot_abs_br.pdf
build/main.pdf: build/plot_abs_sr.pdf
build/main.pdf: build/plot_abs_hg.pdf
build/main.pdf: build/plot_abs_zr.pdf


build/main.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
