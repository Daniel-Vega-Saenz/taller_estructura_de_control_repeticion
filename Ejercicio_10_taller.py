num_e=int(input("ingrese el numero de estudiantes: "))
altura_mayor=0
for i in range(1, num_e+1):
    altura=float(input("digite su altura: "))
    if(altura_mayor<=altura):
        altura_mayor=altura
print(f"la altura mayor es de: {altura_mayor} m")
