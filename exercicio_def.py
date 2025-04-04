import os
os.system("clear")

def medias(n1, n2):
    return (n1 + n2) / 2

n1 = int(input("Digite sua primeira nota: "))
n2 = int(input("Digite sua segunda nota: "))

media = medias(n1,n2)

os.system("clear")
print(f"Primeiro nota informada: {n1} ")
print(f"Sua segunda nota informada: {n2} ")
print(f"Sua média: {media}")
