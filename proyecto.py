from random import randint
import time

f = open("data.dzn","w")
N = int(input("Valor de N: "))
M = int(input("Valor de M: "))
start_time = time.time()

f.write("n = {};\n".format(N))
f.write("m = {};\n".format(M))

p = list()
f.write("p = [")
for j in range(M):
    pres = randint(1,100)
    p.append(pres)
    if j != M - 1:
        f.write("{}, ".format(pres))
    else:
        f.write(str(pres))
f.write("];\n\n")

f.write("c =\n")
f.write("[| ")
for i in range(N):
    if i != 0:
        f.write(" | ")
    for j in range(M):
        if (i != N - 1) or (j != M - 1):
            f.write("{}, ".format(randint(1,int(pres/2))))
        else:
            f.write("{}".format(randint(1,int(pres/2)))) 
    f.write("\n")
    if i == N - 1:
        f.write(" |];\n\n")

f.write("h =\n")
f.write("[| ")
for i in range(N):
    if i != 0:
        f.write(" | ")
    for j in range(M):
        if (i != N - 1) or (j != M - 1):
            f.write("{}, ".format(randint(1,p[j])))
        else:
            f.write("{}".format(randint(1,p[j]))) 
    f.write("\n")
    if i == N - 1:
        f.write(" |];\n\n")




f.close()
print("--- %s seconds ---" % (time.time() - start_time))