import os 

os.system("clear")


primeira_nota = float(input("Digite sua primeira nota: "))
print()

segunda_nota = float(input("Digite sua segunda nota: "))
print()

terceira_nota = float(input("Digite sua terceira nota: "))
print()

media = float (primeira_nota + segunda_nota + terceira_nota) / 3

print("Sua média é: ", media)    

if media == 7:
    print("APROVADO")
elif media < 7:
    print("Reprovado")
else:
    print("Aprovado")
