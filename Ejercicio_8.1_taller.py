c=0
num=int(input(""))
while(num!=2002):
    c=c+1
    if(c==3):
        print("muchos intentos")
        break
    print("Senha invalida")
    num=int(input(""))
else:
    print("Acesso permitido")