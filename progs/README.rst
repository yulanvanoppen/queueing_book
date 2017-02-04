I make the figures with the following tools:

* `Python <http://www.python.org/>`_
* `Scipy <http://www.scipy.org/>`_
* `numpy <http://www.numpy.org/>`_
* `matplotlib <http://matplotlib.org/>`_
* `matplotlib2tikz <https://github.com/nschloe/matplotlib2tikz>`_
* `pweave <http://mpastell.com/pweave/>`_
* `latex <https://www.latex-project.org/>`_
* `tikz <http://www.texample.net/tikz/>`_
    


The python scripts contain the python code to make tikz code for a
figure and save it to a file. Then I input the file in
``testing_ground.tex`` and test the tikz code with

  pdflatex testing_ground.tex

Once I am happy about the figure I include it in the book. In the book
I typically mention the script that I used to make the figure.

As an example:

  python3 reflected_random_walk.py && pdflatex testing_ground.tex
