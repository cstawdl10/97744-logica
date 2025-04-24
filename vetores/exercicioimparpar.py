import os 
os.system("clear")

lista_numeros = []

def pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
             impares += 1
    return pares, impares


for i in range(6):
    numeros = int(input("Digite seu número: "))
    lista_numeros.append(numeros)
    
        
pares, impares = pares_impares(lista_numeros)
print("\n=Lista de Números=")
for i, numeros in enumerate(lista_numeros,start=1):
    print(f"{i}º Número:{numeros}")
    
print(f"Número pares:{pares}")
print(f"Número impares:{impares}")


