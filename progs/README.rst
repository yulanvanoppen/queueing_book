Programs
======================


The python scripts contain the python code to make tikz code for a
figure and save it to a file. Then I input the file in
``testing_ground.tex`` and test the tikz code with

  pdflatex testing_ground.tex

Once I am happy about the figure I include it in the book. In the book
I typically mention the script that I used to make the figure.

As an example:

  python3 reflected_random_walk.py && pdflatex testing_ground.tex


*  ``mm1.R`` is an R program to simulate the M/M/1 queue
*  ``mm1.py`` is a python program to simulate the M/M/1 queue
*  ``mm1.jl`` is a julia program to simulate the M/M/1 queue
* ``converge_to_exp.py`` shows by simulation that the interarrival
  times of a superposition of arrival processes converge rapidly to
  exponentially distributed interarrival times.
* ``intake_control.py`` analyzes, by simulation, the efficacy of some
  rules to control the intakes of patients by psychiatists. The
  intakes of patients are put into a queue.
* ``random_walk.py`` simulates a random walk.
* ``waiting_time_simulation.py`` shows the converence of the waiting
    time distribution from some intial distribution to the stationary
    distribution, by analytical means and simulation.
  

