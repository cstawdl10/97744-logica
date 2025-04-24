import os 
os.system("clear")

lista_numero = []

for i in range(5): 
    numero = int(input("Digite seu número: "))
    lista_numero.append(numero)

print("\n=Números Informados=")
for n, numero in enumerate(lista_numero,start=1):
    print(f"{n}° Número:{numero}")
    maior = max(lista_numero)
    menor = min(lista_numero)

print(f"Maior número:{maior}")
print(f"Menor número:{menor} ")
