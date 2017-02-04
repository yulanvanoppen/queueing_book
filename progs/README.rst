I make the figures with the following tools:

* .. _python: http://www.python.org
* , and its libraries scipy, numpy, matplotlib, matplotlibtikz,
* pweave  
* latex.



The python scripts contain the python code to make tikz code for a
figure and save it to a file. Then I input the file in
``testing_ground.tex`` and test the tikz code with

  pdflatex testing_ground.tex


Once I am happy about the figure I include it in the book. In the book
I typically mention the script that I used to make the figure.

As an example:

  python3 reflected_random_walk.py && pdflatex testing_ground.tex
