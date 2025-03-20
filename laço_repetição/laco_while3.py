import os 
os.system("clear")
quantidades_notas = 2
soma = 0

for i in range(quantidades_notas):
    while True:
       nota = float(input(f"Digite a {i+1}º nota: "))

       if nota < 0 or nota > 10:
           print("Nota invalida, tente novamente.\n")
       else:
            soma += nota
            break

media = soma / quantidades_notas
print(f"Média: {media}")                   