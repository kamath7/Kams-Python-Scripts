run:
	python sample_pkg/main.py

install:
	pip install -r requirements.txt

build:
	python setup.py build bdist_wheel

clean:
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist	
	if exist "./sampleproject.egg-info" rd /s /q sampleproject.egg-info