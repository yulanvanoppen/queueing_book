I make the figures with

* python, and its libraries scipy, numpy, matplotlib, matplotlibtikz,
* latex.

The python scripts contain the python code to make a tikz figure. I
use ``testing_ground.tex`` to test the tikz code. Once I am happy about
the figure I include it in the book.


To make the output

  > python3 reflected_random_walk.py && pdflatex testing_ground.tex
