import os
os.system("clear")

lista_notas = [] # criando uma lista

for i in range (3):
    nota = float(input("Digite sua nota: "))
    lista_notas.append(nota)

media = sum(lista_notas)/3
for nota in lista_notas:
    print(f"Nota: {nota}")

print()
print(f"Somente a primeira nota: {lista_notas[0]} ")