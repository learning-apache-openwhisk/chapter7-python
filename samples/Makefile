help: 
	@echo "Usable targets:";\
	cat Makefile | grep -- '-''test' | sed -e 's/:.*//' -e 's/^/  /'

python.done:
	wsk package update python	
	touch python.done

hello: python.done
	wsk action update python/hello hello.py

hello-test: hello
	wsk action invoke python/hello -p name Mike -r

version: python.done
	wsk action update python/version version.py

version-test: version
	wsk action invoke python/version -r

version3: python.done
	wsk action update python/version3 version.py --kind python:3

version3-test: version3
	wsk action invoke python/version3 -r


requirements: python.done
	wsk action update python/requirements requirements.py --web true

requirements-test: requirements
	curl $$(wsk action get python/requirements --url | tail -1)

requirements3: python.done
	wsk action update python/requirements requirements.py --web true

requirements3-test: requirements3
	curl $$(wsk action get python/requirements --url | tail -1)

environ: python.done
	wsk action update python/environ environ.py

environ-test: environ
	wsk action invoke python/environ -r

zipfile.zip: zipfile/*.py
	cd zipfile ;\
	zip zipfile.zip *.py ;\
	mv zipfile.zip ..

zipfile: python.done zipfile.zip
	wsk action update python/zipfile zipfile.zip --kind python:3
	wsk action update python/zipfile-hello zipfile.zip --kind python:3 --main hello
	wsk action update python/zipfile-hi zipfile.zip --kind python:3 --main hi

zipfile-test: zipfile
	wsk action invoke python/zipfile -r
	wsk action invoke python/zipfile-hello -r
	wsk action invoke python/zipfile-hi -r



