settings.outformat = "pdf";
size(8cm);

path[] q = (0,0.25)--(2,0.25)--(2,-0.25)--(0,-0.25);
path[] q = q^^(1.75,0.25)--(1.75,-0.25);
path[] q = q^^(1.5,0.25)--(1.5,-0.25);
path[] q = q^^(1.25,0.25)--(1.25,-0.25);

path[] queue = q;
path[] queueA = shift((5,1))*q;
path[] queueB = shift((5,-1))*q;

label("$\lambda$", (-1,0.25), align=N);
draw((-2,0)--(0, 0), arrow=ArcArrow(TeXHead));
draw(queue);

label("$\lambda_A$", (3.75,0.75), align=N);
draw((2,0)--(5, 1), arrow=ArcArrow(TeXHead));
label("$A$", (6,1.25), align=N);
draw(queueA);
draw((7,1)--(9, 1), arrow=ArcArrow(TeXHead));

label("$\lambda_B$", (3.75,-1.75), align=N);
draw((2,0)--(5, -1), arrow=ArcArrow(TeXHead));
label("$B$", (6,-0.75), align=N);
draw(queueB);
draw((7,-1)--(9, -1), arrow=ArcArrow(TeXHead));





