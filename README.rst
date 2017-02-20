Analysis of queueing systems with sample paths and simulation. 
===================

This book supports my course on queueing theory. Comments are more
than welcome of course: `n.d.van.foreest@rug.nl`.

* ``tex_files/``: source files for the text
* ``progs/``:  programs, mainly python, to make the graphs and the simulations
* ``figures/``: the figures read by the latex files
* ``chunks/``: weaved files, will be overwritten by ``pweaveAll.py``. Do not edit if you intend to run   ``pweaveAll.py``.
  

Quite a few of the source tex files contain python code. These files
should be weaved with `pweave <http://mpastell.com/pweave/>`_. The
weaved files are sent to the ``chunks/`` directory with extension
``.tx``. These ``.tx`` files are read by ``book.tex``. Thus, if you
edit the ``.tx`` files, they will be overwritten when you weave the
``.tex`` files. However, if you don't run ``pweaveAll.py`` this will
not happen.

To make the book from the weaved files, run:

  pdflatex book

To make the book from scratch, run

  python3 pweaveAll.py

  pdflatex book


When writing/testing a certain file I typically uncomment the related
file as an ``input`` command in ``booktest.tex`` and modify 
``pweaveAll.py`` such only this file is weaved. 

``makeClean`` does what its name says it does: delete ``*.aux`` and
the like.

Here are the tools that I use to make the text and the figures:

* `Python <http://www.python.org/>`_
* `Scipy <http://www.scipy.org/>`_
* `numpy <http://www.numpy.org/>`_
* `matplotlib <http://matplotlib.org/>`_
* `matplotlib2tikz <https://github.com/nschloe/matplotlib2tikz>`_
* `pweave <http://mpastell.com/pweave/>`_
* `latex <https://www.latex-project.org/>`_
* `tikz <http://www.texample.net/tikz/>`_
    

