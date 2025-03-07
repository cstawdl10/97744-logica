import os

os.system("clear")

nome = input("Digite o seu nome: ")
sexo = input("Digite o seu sexo: ")
estado_civil = input("Digite o seu estado civil: ").lower()
resultado = int


if estado_civil == "casada" or "casado":
  resultado = input("Quantos anos tem de casado(a) ?:  ")


print()
print(f"Nome: {nome}")
print(f"Sexo: {sexo}") 
print(f"Estado civil:{estado_civil}")
print(f"Tempo de casado(a):{resultado}")