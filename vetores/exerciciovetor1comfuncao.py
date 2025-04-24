import os 
os.system("clear")


def maior_menor(lista):
    menor = min(lista_numeros)
    maior = max(lista_numeros)
    return maior,menor

lista_numeros = []

for i in range(5):
    numeros = int(input("Digite seu número: "))
    lista_numeros.append(numeros)
    
        
menor, maior = maior_menor(lista_numeros)
print("\n=Lista de Números=")
for n, numeros in enumerate(lista_numeros,start=1):
    print(f"{n}º Número:{numeros}")
    
print(f"Maior número:{maior}")
print(f"Menor número:{menor}")


