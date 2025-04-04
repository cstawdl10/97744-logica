import os 
os.system("clear")
par = 0
impar = 0
def pares(par):
    numeros =""
    if numeros % 2 == 0:
       par = 0
       par += 1
    return pares
def impares(impar):
    numeros = ""
    if numeros % 2 == 1:
        impar = 0
        impar += 1
    return impares

pares(par)
impares(impar)

n = int(input("Digite seu primeiro número: "))
n = int(input("Digite seu segundo número: "))
n = int(input("Digite seu terceiro número: "))
n = int(input("Digite seu quarto número: "))
n = int(input("Digite seu quinto número: "))
n = int(input("Digite seu sexto número: "))

print(f"Pares: {par}")
print(f"Impares: {impar}")
