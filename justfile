pdf:
    pandoc -t beamer --template=custom --data-dir=. slide.md -s --pdf-engine=lualatex -o slide.pdf
latex:
    pandoc -t beamer --template=custom --data-dir=. slide.md -s -o slide.tex
show:
    zathura slide.pdf
py313:
    docker run --rm -it -v .:/app -w /app python:3.13
py312:
    docker run --rm -it -v .:/app -w /app python:3.12
py311:
    docker run --rm -it -v .:/app -w /app python:3.11
py310:
    docker run --rm -it -v .:/app -w /app python:3.10
py39:
    docker run --rm -it -v .:/app -w /app python:3.9
py38:
    docker run --rm -it -v .:/app -w /app python:3.8
py37:
    docker run --rm -it -v .:/app -w /app python:3.7
py36:
    docker run --rm -it -v .:/app -w /app python:3.6
py35:
    docker run --rm -it -v .:/app -w /app python:3.5
