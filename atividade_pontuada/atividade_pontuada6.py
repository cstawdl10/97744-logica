import os
os.system("clear")


primeira_nota = float(input("Digite sua primeira nota: "))
print()

segunda_nota = float(input("Digite sua segunda nota: "))
print()



media = float (primeira_nota + segunda_nota) / 2

print("Sua média é: ", media)    

if media >= 6:
    print("Aprovado")
elif media >= 4:
    print("Recuperação")
else:
    print("Reprovado")