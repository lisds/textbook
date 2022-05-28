BUILD_DIR=_build/html

html: bibliography
	# Check for ipynb files in source (should all be .Rmd).
	if compgen -G "*/*.ipynb" 2> /dev/null; then (echo "ipynb files" && exit 1); fi
	jupyter-book build -W .
	python _scripts/make_redirects.py

github: html
	ghp-import -n _build/html -p -f

clean:
	rm -rf _build

rm-ipynb:
	rm -rf */*.ipynb

BIBLIOGRAPHIES= bib/data-science-bib/data_science.bib \
				bib/course_refs.bib

bibliography: $(BIBLIOGRAPHIES)
	cat $(BIBLIOGRAPHIES) > _references.bib
