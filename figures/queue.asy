// >asy -f pdf queue.asy

settings.outformat = "pdf";
size(5cm);


// build queue path
path[] q = (-0.5,2)--(-0.5,0)--(0.5,0)--(0.5,2);
path[] q = q^^(-0.5,0.4)--(0.5,0.4);
path[] q = q^^(-0.5,0.8)--(0.5,0.8);
path[] q = q^^(-0.5,1.2)--(0.5,1.2);


// middle queue
pair z1 = (0,2);
draw(shift(z1)*q);
draw(z1--(z1.x,0), arrow=ArcArrow(HookHead));

// right queue
pair z2 = (4,2);
draw(shift(z2)*q);
draw((z2.x,7)--(z2.x,4), arrow=ArcArrow(HookHead));
draw(z2--(z2.x,0), arrow=ArcArrow(HookHead));

// baseline
draw((z1.x-0.2,0)--(z2.x+0.2,0));


// make to order server
real midz = (z1.x+z2.x)/2;
draw((midz,0)--(midz,-2), arrow=ArcArrow(HookHead));
pair mid = (midz,-3);
draw(circle(mid,1));
label("$\lambda$",mid);
draw((midz,-4)--(midz,-5.5), arrow=ArcArrow(HookHead));

//make to stock queue and server
draw((z1.x,0)--(z1.x,-2)--(-4,-2)--(-4,0), arrow=ArcArrow(HookHead));
draw(shift((-4,2))*rotate(180.)*q);
draw((-4,2)--(-4,4), arrow=ArcArrow(HookHead));
draw(circle((-4,5),1));
label("$\mu$",(-4,5));
draw((-4,6)--(-4,7)--(z1.x,7)--(z1.x,4), arrow=ArcArrow(HookHead));

