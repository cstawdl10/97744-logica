import os 
os.system("clear")

quantidades_notas = 3
soma = 0
media = 0
for i in range(quantidades_notas):
    while True:
       notas = float(input(f"Digite a {i+1}º nota: "))

       if notas < 0 or notas > 10:
           print("Nota invalida, tente novamente.\n")
       else:
            soma += notas
            break
media = soma / quantidades_notas
if media >= 7:
        resultado = "APROVADO"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"            


print(f"Média: {media:.1f}:")
print(f"resultado: {resultado}")

