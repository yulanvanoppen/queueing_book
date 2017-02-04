# queueing_book
A book on the analysis of queueing systems with sample paths and simulation. 

To make the book:

> python3 pweaveAll.py
> pdflatex book

``pweaveAll.py`` weaves  the tex file and writes the results to 
``chunks/*.tx``.  ``book.tex`` includes the ``*.tx`` files.

When writing/testing a certain file I uncomment the related ``input``
in booktest.tex and include the file to be weaved in ``pweaveAll.py``.

``makeClean`` does what its name says it does: delete ``*.aux`` and the like. 

