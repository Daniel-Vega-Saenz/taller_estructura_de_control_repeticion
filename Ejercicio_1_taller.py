from ast import While


#Entradas
num=input("")
N,K=num.split(" ")
N=int(N)
K=int(K)
#Caja negra
print(N) 
while(K<N):
    N=N-1
    print(N)
