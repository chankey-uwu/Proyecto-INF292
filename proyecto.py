from random import randint
import time

f = open("data.dzn","w")
N = int(input("Valor de N: "))
M = int(input("Valor de M: "))
start_time = time.time()

f.write("n = {};\n".format(N))
f.write("m = {};\n".format(M))

f.write("p = [")
for j in range(M):
    if j != M - 1:
        f.write("{}, ".format(randint(500,1000)))
    else:
        f.write(str(randint(500,1000)))
f.write("];\n\n")

f.write("c =\n")
f.write("[| ")
for i in range(N):
    if i != 0:
        f.write(" | ")
    for j in range(M):
        if (i != N - 1) or (j != M - 1):
            f.write("{}, ".format(randint(1,10)))
        else:
            f.write("{}".format(randint(1,10))) 
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
            f.write("{}, ".format(randint(1,30)))
        else:
            f.write("{}".format(randint(1,30))) 
    f.write("\n")
    if i == N - 1:
        f.write(" |];\n\n")


f.write("h_p = [")
for j in range(M):
    if j != M - 1:
        f.write("{}, ".format(randint(1,45)))
    else:
        f.write(str(randint(1,45)))
f.write("];\n\n")


f.close()
print("--- %s seconds ---" % (time.time() - start_time))