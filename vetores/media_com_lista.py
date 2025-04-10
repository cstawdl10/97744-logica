import os
os.system("clear")

lista_notas = [] # criando uma lista

for i in range (3):
    nota = float(input("Digite sua nota: "))
    lista_notas.append(nota)

media = sum(lista_notas)/4

os.system("clear")
if media >= 7:
    print("Aprovado")
elif media >= 5: 
    print("Recuperação")
else:
    print("Reprovado")
print()
print()
print(f"Médias: {media:.2f}")

print()
print(f"Primeira nota: {lista_notas[0]} ")
print(f"Segunda nota: {lista_notas[1]} ")
print(f"Terceira nota: {lista_notas[2]} ")
