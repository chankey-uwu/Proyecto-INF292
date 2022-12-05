include "data.dzn";
int: n;
int: m;
array[1..m] of int: p;
array[1..n, 1..m] of int: c;
array[1..n,1..m] of int : h;
array[1..m] of int: h_p;
array[1..n, 1..m] of var int: x;
array[1..n, 1..m] of var 0..1: y;
var int: ct;

constraint ct =  sum(i in 1..n, j in 1..m) (x[i,j]);

constraint forall (i in 1..n, j in 1..m) 
              (x[i,j] >= (y[i,j]*h[i,j])); %FUNCIONA

constraint forall (i in 1..n)
              (sum(j in 1..m) (y[i,j]) <= 5); %FUNCIONA

constraint forall (j in 1..m)
              (sum(i in 1..n) (y[i,j]) >= 1); %FUNCIONA
             
constraint forall (j in 1..m)
              (sum(i in 1..n) (y[i,j]) <= 5); %FUNCIONA
            
constraint forall (j in 1..m)
              (sum(i in 1..n) (c[i,j]*x[i,j]) <= p[j]); %FUNCIONA

constraint forall (i in 1..n)
              (sum(j in 1..m) (x[i,j]) <= 45); %FUNCIONA

constraint forall (j in 1..m)
              (sum(i in 1..n) (x[i,j]) >= h_p[j]); %FUNCIONA
             
constraint forall (i in 1..n, j in 1..m)
              (x[i,j] >= 0);

solve minimize ct;