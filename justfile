pdf:
    pandoc -t beamer --template=custom --data-dir=. slide.md -s --pdf-engine=lualatex -o slide.pdf
latex:
    pandoc -t beamer --template=custom --data-dir=. slide.md -s -o slide.tex
show:
    zathura slide.pdf
