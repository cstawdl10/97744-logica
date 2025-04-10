import os
os.system("clear")

soma = 0
contador = 0

def calcular(soma):
    return soma / 3

while True: 
    nota = float(input("Digite suas notas: "))    
    soma += nota
    if nota > 0:
        contador + 1
    if nota == 0:
        break
media = calcular(soma)

print(f"Sua média:{media}")