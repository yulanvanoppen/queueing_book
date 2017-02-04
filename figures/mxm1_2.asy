settings.outformat = "pdf";
//size(4cm);
unitsize(1cm);

real radius = 0.55;

path level = (5,-2.5)--(5,3.5);
draw(level);
label("level $n$", (5,-1.8), filltype=Fill(white));

pair center0 = (0,0);
path c0 = circle(center0,radius);
label("$n-2$", center0);
draw(c0);

pair center1 = (2,0);
path c1 = circle(center1,radius);
draw(c1);
label("$n-1$", center1);

pair center2 = (4,0);
path c2 = circle(center2,radius);
draw(c2);
label("$n$", center2);

pair center3 = (6,0);
path c3 = circle(center3,radius);
draw(c3);
label("$n+1$", center3);

path s=center3{down}..{up}center2;
real[] a = intersect(s,c3);
real[] b = intersect(s,c2);
Label l = Label("$\mu$", position=MidPoint, align=(0,0), filltype=Fill(white));
path p = subpath(s,a[0],b[0]);
draw(p, arrow=EndArcArrow(HookHead), L=l);

pair end = (10,0);
path y = (7,-1)--(7,8);


path s=center0{(1,1)}..{(1,-1)}end;
real[] a = intersect(s,c0);
real[] b = intersect(s,y);
Label l = Label("$\lambda G(2)$", position=MidPoint, align=(0,0), filltype=Fill(white));
path p = subpath(s,a[0], b[0]);
draw(p, arrow=EndArcArrow(HookHead), L=l);

path s=center1{(1,1)}..{(1,-1)}end;
real[] a = intersect(s,c1);
real[] b = intersect(s,y);
Label l = Label("$\lambda G(1)$", position=Relative(0.4), align=(0,0), filltype=Fill(white));
path p = subpath(s,a[0],b[0]);
draw(p, arrow=EndArcArrow(HookHead), L=l);

path s=center2{(1,1.1)}..{(1,-1.1)}end;
real[] a = intersect(s,c2);
real[] b = intersect(s,y);
Label l = Label("$\lambda G(0)$", position=Relative(0.3), align=(0,0), filltype=Fill(white));
path p = subpath(s,a[0],b[0]);
draw(p, arrow=EndArcArrow(HookHead), L=l);

