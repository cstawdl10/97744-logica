import os
os.system("clear")
soma = 0
contador = 0
while True:
        nota = int(input("Digite sua nota: "))
        if nota > 0:
            soma += nota
            contador += 1
        else:
              break
            
            
 

media = soma / contador

print(f"Sua média: {media:.1f}")
print(f"Quantidade de notas informadas: {contador}")