import os 
os.system("clear")

media = 0
while True:
    notaa = float(input("Digite sua primeira nota: "))
    
    if notaa < 0 or notaa > 10:
        print("Nota inválida, tente novamente.\n")
    else:
            break

while True:
    nota = float(input("Digite sua segunda nota: "))
    if nota < 0 or nota > 10:
        print("Nota inválida, tente novamente.\n")
    else:
            break
media = (notaa + nota) / 2

print(f"Sua primeira nota: {notaa} ")
print(f"Sua segunda nota: {nota} ")
print(f"Sua média: {media} ")

