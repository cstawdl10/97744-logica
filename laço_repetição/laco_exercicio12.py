import os
os.system("clear")
soma = 0
contador = 0
while True:
    nota = float(input("Digite sua nota: "))
    soma += nota
    contador += 1
    mais_notas = input("Deseja adicionar mais uma nota ?\nUse 'S' or 'N' para responder: ").lower()
    if mais_notas == "n":
        break 

media = soma / contador

print(f"Sua média: {media:.1f}")
print(f"Quantidade de notas informadas: {contador}")