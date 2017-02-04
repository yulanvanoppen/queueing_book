settings.outformat = "pdf";
//size(4cm);
unitsize(1cm);

real radius = 0.55;

path y = (1,-2.5)--(1,3.5);
draw(y);
label("level $n$", (1,-1.8), filltype=Fill(white));

pair center0 = (0,0);
path c0 = circle(center0,radius);
label("$n$", center0);
draw(c0);

pair center1 = (2,0);
path c1 = circle(center1,radius);
draw(c1);
label("$n+1$", center1);

pair center2 = (4,0);
path c2 = circle(center2,radius);
draw(c2);
label("$n+2$", center2);

pair center3 = (6,0);
path c3 = circle(center3,radius);
draw(c3);
label("$n+3$", center3);

path s=center1{down}..{up}center0;
real[] a = intersect(s,c1);
real[] b = intersect(s,c0);
Label l = Label("$\mu$", position=MidPoint, align=(0,0), filltype=Fill(white));
path p = subpath(s,a[0],b[0]);
draw(p, arrow=EndArcArrow(HookHead), L=l);

path s=center0{(1,3)}..{down}center1;
real[] a = intersect(s,c0);
real[] b = intersect(s,c1);
Label l = Label("$\lambda f(1)$", position=MidPoint, align=(0,0), filltype=Fill(white));
path p = subpath(s,a[0],b[0]);
draw(p, arrow=EndArcArrow(HookHead), L=l);

path s=center0{(1,4)}..{(1,-4)}center2;
real[] a = intersect(s,c0);
real[] b = intersect(s,c2);
Label l = Label("$\lambda f(2)$", position=MidPoint, align=(0,0), filltype=Fill(white));
path p = subpath(s,a[0],b[0]);
draw(p, arrow=EndArcArrow(HookHead), L=l);

path s=center0{(1,5)}..{(1,-5)}center3;
real[] a = intersect(s,c0);
real[] b = intersect(s,c3);
Label l = Label("$\lambda f(3)$", position=MidPoint, align=(0,0), filltype=Fill(white));
path p = subpath(s,a[0],b[0]);
draw(p, arrow=EndArcArrow(HookHead), L=l);

path s=center0{(1,7)}..{(1,-7)}(8,0);
real[] a = intersect(s,c0);
Label l = Label("$\lambda f(4)$", position=Relative(0.7), align=(0,0), filltype=Fill(white));
path p = subpath(s,a[0],0.7);
draw(p, arrow=EndArcArrow(HookHead), L=l);
