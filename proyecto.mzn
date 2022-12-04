include "data.dzn";
int: n;
int: m;
array[1..n, 1..m] of int: c;
array[1..m] of int: p;
array[1..n,1..m] of int : h;
array[1..n, 1..m] of var 0..1: x;
var int: ct;

constraint ct = sum(i in 1..n, j in 1..m) (x[i,j]*h[i,j]);

constraint forall (i in 1..n)
              (sum(j in 1..m) (x[i,j]) <= 5);
             
constraint forall (j in 1..m)
              (sum(i in 1..n) (x[i,j]) <= 5);
            
constraint forall (j in 1..m)
              (sum(i in 1..n) (x[i,j]*c[i,j]) = p[j]);

constraint forall (i in 1..n)
              (sum(j in 1..m) (x[i,j]*h[i,j]) <= 45);
             
solve minimize ct;