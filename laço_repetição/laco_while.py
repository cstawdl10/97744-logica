import os 
os.system("clear")

while True:
    nota = float(input("Digite uma nota: "))

    if nota < 1 or nota > 10:
        print("Nota inavalida, tente novamente.\n")
    else:
            break
print(f"Nota informada: {nota}")            