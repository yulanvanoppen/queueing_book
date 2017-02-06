Analysis of queueing systems with sample paths and simulation. 
===================

This book supports my course on queueing theory. Comments are more
than welcome of course: `n.d.van.foreest@rug.nl`

Quite a few of the source tex files contain python code. These files
should be weaved with `pweave <http://mpastell.com/pweave/>`_. The
weaved files are sent to the ``chunks`` directory with extension
``.tx``. These ``.tx`` files are read by ``book.tex``.


To make the book:

  python3 pweaveAll.py && pdflatex book


When writing/testing a certain file I typically uncomment the related
file as an ``input`` command in ``booktest.tex`` and include the file to
be weaved in ``pweaveAll.py``.

``makeClean`` does what its name says it does: delete ``*.aux`` and the like. 

