import os
os.system("clear")

notas = 0
media = 0


for i in range (3):
    notas = int(input("Digite suas notas: "))
    media += notas / 3


if media >= 7:
        print("APROVADO")
elif media < 4:
        print("REPROVADO")
else:
    print("RECUPERAÇÃO")       

print(f"Sua média é:{media}")