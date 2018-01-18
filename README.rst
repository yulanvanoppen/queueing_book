Analysis of queueing systems with sample paths and simulation. 
===================

The most important file is ''book.pdf'', which contains the notes on my
course on queueing theory. Comments are more
than welcome of course: `n.d.van.foreest@rug.nl`.

* ``tex_files/`` source files for the text
* ``progs/``  programs, mainly python, to make the graphs and the simulations
* ``figures/`` the figures read by the latex files
  

To make the book, run:

  pdflatex book

  pythontex book

  pdflatex book


``makeClean`` does what its name says it does: delete ``*.aux`` and
the like.

Here are the tools I use to make the text and the figures:

* `latex <https://www.latex-project.org/>`_
* `tikz <http://www.texample.net/tikz/>`_
* `pythontex <https://github.com/gpoore/pythontex/>`_
* `Python <http://www.python.org/>`_
* `numpy <http://www.numpy.org/>`_
* `Scipy <http://www.scipy.org/>`_
* `matplotlib <http://matplotlib.org/>`_
* `matplotlib2tikz <https://github.com/nschloe/matplotlib2tikz/>`_
    

